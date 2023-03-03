PyObject *
PyObject_GenericGetAttr(PyObject *obj, PyObject *name)
{
    return _PyObject_GenericGetAttrWithDict(obj, name, NULL, 0);
}

PyObject *
_PyObject_GenericGetAttrWithDict(PyObject *obj, PyObject *name,
                                 PyObject *dict, int suppress)
{
    /* Make sure the logic of _PyObject_GetMethod is in sync with
       this method.

       When suppress=1, this function suppress AttributeError.
    */

    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr = NULL;
    PyObject *res = NULL;
    descrgetfunc f;
    Py_ssize_t dictoffset;
    PyObject **dictptr;

    if (!PyUnicode_Check(name)){
        PyErr_Format(PyExc_TypeError,
                     "attribute name must be string, not '%.200s'",
                     name->ob_type->tp_name);
        return NULL;
    }
    Py_INCREF(name);

    if (tp->tp_dict == NULL) {
        if (PyType_Ready(tp) < 0)
            goto done;
    }

    // 在类型字典或父类字典中查找当前属性值
    descr = _PyType_Lookup(tp, name);

    f = NULL;
    // 如果找到找到了一个实现了__get__的描述器，那么就调用__get__
    if (descr != NULL) {
        Py_INCREF(descr);
        f = descr->ob_type->tp_descr_get;
        if (f != NULL && PyDescr_IsData(descr)) {
            res = f(descr, obj, (PyObject *)obj->ob_type);
            if (res == NULL && suppress &&
                    PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_Clear();
            }
            // 执行结束了 不用管下面了
            goto done;
        }
    }
    // 只有没有获取到描述器或者描述器没有__get__才会走到这一步
    // 传入的dict为NULL，因此一定会进这个分支 - 获取实例字典
    if (dict == NULL) {
        /* Inline _PyObject_GetDictPtr */
        // 这个offset是指dict相比于实例结构体偏移量，正则从头算起，负则从尾部算起，0表示没有-例如int没有__dict__
        dictoffset = tp->tp_dictoffset;	
        if (dictoffset != 0) {
            if (dictoffset < 0) {
                Py_ssize_t tsize;
                size_t size;

                tsize = ((PyVarObject *)obj)->ob_size;
                if (tsize < 0)
                    tsize = -tsize;
                size = _PyObject_VAR_SIZE(tp, tsize);
                assert(size <= PY_SSIZE_T_MAX);

                dictoffset += (Py_ssize_t)size;
                assert(dictoffset > 0);
                assert(dictoffset % SIZEOF_VOID_P == 0);
            }
            dictptr = (PyObject **) ((char *)obj + dictoffset);
            dict = *dictptr;
        }
    }
    // 如果实例有__dict__属性，则尝试从实例字典中获取
    if (dict != NULL) {
        Py_INCREF(dict);
        res = PyDict_GetItem(dict, name);
        //  如果实例字典中获取到了就跑路
        if (res != NULL) {
            Py_INCREF(res);
            Py_DECREF(dict);
            goto done;
        }
        Py_DECREF(dict);
    }

    if (f != NULL) {
        res = f(descr, obj, (PyObject *)Py_TYPE(obj));
        if (res == NULL && suppress &&
                PyErr_ExceptionMatches(PyExc_AttributeError)) {
            PyErr_Clear();
        }
        goto done;
    }

    if (descr != NULL) {
        res = descr;
        descr = NULL;
        goto done;
    }

    if (!suppress) {
        PyErr_Format(PyExc_AttributeError,
                     "'%.50s' object has no attribute '%U'",
                     tp->tp_name, name);
    }
  done:
    Py_XDECREF(descr);
    Py_DECREF(name);
    return res;
}

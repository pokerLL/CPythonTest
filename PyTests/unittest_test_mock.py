from unittest.mock import patch

import test

@patch('test.fun')
def test1(x, mock_func):
    test.fun(x)       # Uses patched example.func
    print(mock_func is test.fun)        # True
    mock_func.assert_called_with(x)


test1("1")
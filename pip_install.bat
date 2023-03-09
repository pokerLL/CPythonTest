@echo off
if "%1"=="" (
    echo Please use like ^> pip_install.bat module_name
    goto end
) 

set MIRROR_URL=http://mirrors.aliyun.com/pypi/simple/
set TRUSTED_HOST=mirrors.aliyun.com

pip install %1 -i %MIRROR_URL% --trusted-host=%TRUSTED_HOST%

:end

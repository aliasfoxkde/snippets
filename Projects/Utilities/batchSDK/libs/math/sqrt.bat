@echo off

:: :sqrt
:: 	set sqrt=1 :: Reset variable
:: 	for /F "delims=" %%G IN ('powershell -command "[math]::Sqrt(%1)"') do set /a sqrt=%%G
:: 	echo %sqrt%
:: GOTO :EOF

:sqrt
    SETLOCAL EnableDelayedExpansion
    set root=1
    set /a sqrt=%root%*%root%
    :Loop
    if %sqrt% LSS %1 (
        set /a root=!root!+1
        set /a sqrt=!root!*!root!
        goto Loop
    )
	echo %root%
GOTO :EOF
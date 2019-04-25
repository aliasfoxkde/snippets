@echo off

CALL :pow 2 3    :: 8
CALL :pow 3 3    :: 27
CALL :pow 5 5    :: 3125
CALL :pow 256 3  :: 16777216

set /p=End of Script, press any key to exit...
GOTO :EOF

:: ----- Call Functions -----
:pow
    SET pow=1
    FOR /L %%i IN (1,1,%2) DO SET /A pow*=%1
    ECHO %pow%
GOTO :EOF
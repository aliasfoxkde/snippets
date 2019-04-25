@echo off
:pow
    SET pow=1
    FOR /L %%i IN (1,1,%2) DO SET /A pow*=%1 > NUL 2>&1
    ECHO %pow%
GOTO :EOF
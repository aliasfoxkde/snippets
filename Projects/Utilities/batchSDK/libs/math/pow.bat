@echo off
:pow
    SETLOCAL EnableDelayedExpansion
    SET pow=1 :: Resets Variable
    FOR /L %%i IN (1,1,%2) DO SET /A pow*=%1 > NUL 2>&1
    ECHO %pow%
GOTO :EOF
@echo off
:div
    SETLOCAL EnableDelayedExpansion
    SET div=1 :: Resets Variable
    SET /a div=%1*%2
    ECHO %div%
GOTO :EOF
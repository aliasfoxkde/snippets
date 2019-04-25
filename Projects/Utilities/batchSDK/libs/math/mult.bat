@echo off
:mult
    SETLOCAL EnableDelayedExpansion
    SET mult=1 :: Resets Variable
    SET /a mult=%1*%2
    ECHO %mult%
GOTO :EOF
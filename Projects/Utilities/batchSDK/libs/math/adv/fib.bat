@echo off
:add
    SETLOCAL EnableDelayedExpansion
    SET add=1 :: Resets Variable
    SET /a add=%1+%2
    ECHO %add%
GOTO :EOF
@echo off
:sub
    SETLOCAL EnableDelayedExpansion
    SET sub=1 :: Resets Variable
    SET /a sub=%1-%2
    ECHO %sub%
GOTO :EOF
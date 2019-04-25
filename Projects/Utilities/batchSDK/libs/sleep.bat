@echo off

:sleep
	ping 127.0.0.1 -n %1 > NUL 2>&1
GOTO :EOF
@echo off
setlocal

set /P "=_" < NUL > "Enter password"
findstr /A:07 /V "^$" "Enter password" NUL > CON
del "Enter password"
set /P "password="
cls
color 07
echo The password read is: "%password%"
pause
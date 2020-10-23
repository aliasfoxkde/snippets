@echo off
:: The Goal of this script is to enable automated 
:: incremental commits that can be scheduled.
:: Currently, the script can simi-auto commit
:: by being passed a commit message either
:: from cmmandline or prompt (when no message
:: is provided).

if "%~1"=="" (
	:: Manual Message replaced w/ auto increment
	:: set /p msg=Please provide a commit message... 
	
	git rev-list --all --count > %temp%\cnt.txt
	set /p cnt=<%temp%\cnt.txt
	set "msg=Auto Commit #%cnt%" 
) else (
	:: Commit can take message as passthrough
	set "msg=%1"
)

git add --all && git commit -m "%msg%" && git push

if NOT "%errorlevel%"=="0" (
	:: "Fixes" the Repo if/when out of date
	:: but still needs testing
	git pull
	git add --all && git commit -m %msg% && git push
)

:: Reset Message for Commandline
set "msg="

echo.
TIMEOUT 3

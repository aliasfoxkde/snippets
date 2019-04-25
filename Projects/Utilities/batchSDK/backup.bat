@echo off
@title=Backup Script
:: This is a generic backup script that could work anywhere,
:: just drop it into a folder, run it and all the files get
:: backed up to a ./backup/full-backup_%timestamp%.7z

:: Set Variables
set dateformat=%date:~4,2%-%date:~7,2%-%date:~10,4%

:: Sets the Datestamp with whitespace logic
if "%time:~0,1%" == " " (
	set timeformat=%time:~1,1%%time:~3,2%%time:~6,2%%time:~9,2%
) else (
	set timeformat=%time:~0,2%%time:~3,2%%time:~6,2%%time:~9,2%
)
set timestamp=%dateformat%_%timeformat%

:: Backup using 7za CLI Utility (excludes backup folder)
:: Note: change to .ZIP by just chaging the .7z extension)
tools\7za.exe a backup\full-backup_%timestamp%.7z -x!backup -mx9 -aoa

:: Display Message
echo Backup created [full-backup_%timestamp%.7z] ...
echo.
set /p=Press any key to quit...
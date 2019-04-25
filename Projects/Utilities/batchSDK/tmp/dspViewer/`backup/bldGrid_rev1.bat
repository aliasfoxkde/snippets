@echo off

SETLOCAL EnableDelayedExpansion
echo :: X, Y Grid Display > gridrow.txt
set "lst="


for /L %%c in (0, 1, 9) DO (
	for /L %%a in (0, 1, 3) DO (
		for /L %%b in (0, 1, 9) DO (
			REM echo echo %%D%%a%%b%% >> gridrow.txt
			REM set lst = %lst% + "%%D%%a%%b%%"
			REM set "lst=%lst%%%D%%a%%b%%"
			CALL :buildList %%a %%b
		)

	)
	CALL :outPutMap
)
:: echo %lst% >> gridrow.txt
pause


:buildList
	set "lst=%lst%%%D%1%2%%"
GOTO :EOF

:outPutMap
	echo %lst% >> gridrow.txt
	set "lst="
GOTO :EOF
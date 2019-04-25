@echo off

SETLOCAL EnableDelayedExpansion
echo :: Grid Variables > grid\assignGrid.bat
set "lst="

echo Building the display, please wait...

:: X (Up and Down)
for /L %%x in (0, 1, 0) DO (
	for /L %%y in (0, 1, 9) DO (
		for /L %%z in (0, 1, 9) DO (

			:: Y (Left and Right)
			for /L %%a in (0, 1, 0) DO (
				for /L %%b in (0, 1, 1) DO (
					for /L %%c in (0, 1, 9) DO (
						echo set "D%%x%%y%%z%%a%%b%%c=#" >> grid\assignGrid.bat
					)
				)
			)
		)
	)
)
:: echo %lst% >> gridrow.txt
pause


:buildList
	:: set "lst=%lst%%%D%1%2%3%%"
	set "lst=%lst%%%D%4%5%6%1%2%3%%"
GOTO :EOF

:outPutMap
	echo @echo off >> grid\assignGrid.bat
	echo echo %lst% >> grid\assignGrid.bat
	set "lst="
GOTO :EOF
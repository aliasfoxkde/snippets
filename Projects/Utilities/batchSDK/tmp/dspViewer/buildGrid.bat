@echo off

SETLOCAL EnableDelayedExpansion

:: Build Grid Header
echo @echo off > gridDisplay\assignGrid.bat
echo @echo off > gridDisplay\viewGrid.bat
echo call assignGrid.bat >> gridDisplay\viewGrid.bat
echo :: X, Y Grid Display >> gridDisplay\viewGrid.bat

set "lst="

echo Building the display, please wait...

:: X (Up and Down)
for /L %%x in (0, 1, 0) DO (
	for /L %%y in (0, 1, 1) DO (
		for /L %%z in (0, 1, 9) DO (

			:: Y (Left and Right)
			for /L %%a in (0, 1, 0) DO (
				for /L %%b in (0, 1, 3) DO (
					for /L %%c in (0, 1, 9) DO (
						echo set "D%%x%%y%%z%%a%%b%%c=±" >> gridDisplay\assignGrid.bat
						CALL :buildList %%a %%b %%c %%x %%y %%z
					)
				)
			)
			CALL :outPutMap
		)
	)
)

echo pause >> gridDisplay\viewGrid.bat
pause

:: // ------------ Functions -------------------
:buildList
	:: set "lst=%lst%%%D%1%2%3%%"
	set "lst=%lst%%%D%4%5%6%1%2%3%%"
GOTO :EOF

:outPutMap
	echo echo %lst% >> gridDisplay\viewGrid.bat
	set "lst="
GOTO :EOF

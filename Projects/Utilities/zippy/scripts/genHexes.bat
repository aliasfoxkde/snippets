@echo off
echo. > binOut.txt

:: RANDOM 16 Digit TEST
for /L %%a IN (0,1,1) DO (
	for /L %%b IN (0,1,1) DO (
		for /L %%c IN (0,1,1) DO (
			for /L %%d IN (0,1,1) DO (	
				for /L %%e IN (0,1,1) DO (
					for /L %%f IN (0,1,1) DO (
						for /L %%g IN (0,1,1) DO (
							for /L %%h IN (0,1,1) DO (
								echo %%a%%b%%c%%d%%e%%f%%g%%h >> binOut.txt
							)
						)
					)
				)
			)
		)
	)
)
@echo off
:pow
    SET pow=1
	SET powOf=0
    FOR /L %%i IN (1,1,%2) DO (
		SET /A pow*=%1
		if %pow% GEQ 10000 (
			SET /A pow /= 1000
			SET /A powOf +=3
		)
	)
    ECHO %pow%
GOTO :EOF
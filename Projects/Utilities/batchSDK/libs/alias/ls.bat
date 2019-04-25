@echo off 
if "%1"=="-a" (
    dir
) else (
    if "%1"=="-all" (
        dir
    ) else (
        dir /b
    )
)

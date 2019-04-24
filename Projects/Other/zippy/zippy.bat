@echo off
@title=zippy
::  ####### ,##  ######  ######. ###  ### 
::     ###. ,##  ###  ##,###  ### #####*  
::   ###/   ,##  ####### #######.  (##    
:: .####### ,##  ##(     ###       /##   
::  .......  ..  ..      ...        ..  (TM)  

:: "The Snake Oil Salesman Sales Pitch"
:: 
:: "Zippy" is faster than both 7zip and Zip formats but offers better compression than both!
:: ...but it's a hack so don't expect it to work on "real" data. See if you can figure out
:: the "trick". Good luck.

:: Legal and Disclaimers
:: 
:: This script is provided as is, without warranty of any kind and you
:: the user are allowed full rights to modify, distribute, or otherwise
:: do whatever you damn well please with it. But don't expect support,
:: liability for loss of data, or general damage by using this. 
:: Essentially use freely, but at your own risk.

:: Improvements
:: - Add ability to both compress and decompress files
:: - Add pass-through switches and advanced arguments
:: - Add options for source and destination (otherwise source 
::   directory is assumed to be in the current folder and destination 
::   is the sources name with an extension.

:: Script starts
echo Building archive, please wait...

:: Variables
set "dest=%cd%"

:: Checks if archive files exist
if exist "%dest%\%1.zippy" del /s /q "%dest%\%1.zippy" > null 2>&1
if exist "%temp%\%1.zip" del /s /q "%temp%\%1.zip" > null 2>&1

:: Compression "scheme"
powershell.exe Compress-Archive "%1" "%temp%\%1.zip" > null 2>&1
apps\7z a "%dest%\%1.zippy" "%temp%\%1.zip" > null 2>&1

:: Cleanup
del /s /q "%temp%\*" > null 2>&1

:: End Message
echo Archive complete [%dest%\%1.zippy]
set /p=Press any key to exit script...
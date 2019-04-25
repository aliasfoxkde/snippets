@ECHO off

SET downloadUrl=http://www.africau.edu/images/default/sample.pdf
SET tempFile=%cd%\sample.pdf

:: wget /transfer /download %downloadUrl% %tempFile% >nul
:: wget /transfer /download %downloadUrl% %tempFile%

:: pause

:: BITSADMIN /transfer /download %downloadUrl% %tempFile% >nul
:: TYPE %tempFile%
:: DEL %tempFile%


:: type "http://www.africau.edu/images/default/sample.pdf"

bitsadmin /transfer /download %downloadUrl% %tempFile% >nul
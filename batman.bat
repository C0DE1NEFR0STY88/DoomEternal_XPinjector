@echo off
setlocal

:: === HARD-CODED PATHS ===

set "original_bin=C:\pathtoOG.bin"
set "converter_path=C:\pathtoEXE.exe"
set "inj_path=C:\pathtopy.py"
set "json_path=C:\pathjson.json"
set "newbin=C:newbinHardname.bin"

"%converter_path%" "%original_bin%"
python "%inj_path%"
"%converter_path%" "%json_path%"
move /Y "%newbin%" "%orginal_bin%"

echo Done!
pause

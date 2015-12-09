del output.txt

for /f "tokens=1-3" %%i in (input.txt) do (
	echo. %%~ni, %%j, %%~nk >> output.txt
)


pause
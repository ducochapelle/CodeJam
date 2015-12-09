for /f "tokens=1,3*" %%i in (aceservers.txt) do (
    if %%j=="babel" (
        echo dit %%k >> output.txt
    )
)    
    pause
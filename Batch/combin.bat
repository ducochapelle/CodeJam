for /f "tokens=1*" %%A in (input1.txt) do (
    for /f "tokens=1,2*" %%C in (input2.txt) do (
        if %%A==%%C echo %%B, %%E >> output.txt
    )
)
    
    
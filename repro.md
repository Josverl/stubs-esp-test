Prep 

```
md stubs-esp8266-test
cd stubs-esp8266-test
git init 
echo .venv >> .gitignore
python -m venv .venv

# Activate the virtual environment
.venv/Scripts/Activate.ps1

# install the stubs into the venv
pip install micropython-esp8266-stubs

# Optional : pyright cmdline checker
pip install pyright

# copy in some code to test the stubs
md project
copy ..\micropython-stubs\snippets\esp8266 project
copy ..\micropython-stubs\snippets\validate-stdlib project


code .
```

In vscode run the following command:  
 - [F1]
   - Python: Select interpreter 
     - select the .venv you just created : Python 3.9.13 ('.venv':venv)  
   - Python: Restart Language Server

 - Workspace Settings
   - Python › Analysis: Diagnostic Mode
     - Workspace



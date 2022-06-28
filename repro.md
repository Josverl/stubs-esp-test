Prep 

```
md stubs-esp8266-test
cd stubs-esp8266-test
git init 
echo .venv >> .gitignore
python -m venv .venv

# Activate the virtual environment
.venv/Scripts/Activate.ps1 ( )

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

 - Use Pymaker to connect to a MCU and open it in explorer
   this will cause a multi-root workspace to be created and opened
   
 - Save the workspace as `stubs-esp-test.code-workspace`
 
 to simplify clean testing : quit vscode and reopen it using 
``` 
code .\stubs-esp-test.code-workspace
```

## MEMFS test 

To test with the sample remote / virtual filesystem 

To *get started* you need this:

* install MEMFS from the VSIX file included in this repro : `vscode-memfs-0.0.3.vsix`

* In VSCode , select 'F1 > [MemFS] Setup Workspace' (optionally save the workspace now)

NOTE: that as soon as a virtual filesystem is part of the workspace, Pylance will attempt to scan the **local** rootdrive (`C:\` or '/' ) where the path is relative to the rootpath of the virtual filesystem.

this is shown in the Pylance logs by looking for the tag : `Search paths for \`
``` log 
[Info  - 12:39:18] (26416) Pylance language server 2022.6.30 (pyright 212d1465) starting
[Info  - 12:39:19] (26416) Server root directory: c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist
Notebook support: Legacy
[Info  - 12:39:20] (26416) Background analysis(1) root directory: c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist
[Info  - 12:39:20] (26416) Background analysis(1) started
[Info  - 12:39:20] (26416) Background analysis(3) root directory: c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist
[Info  - 12:39:20] (26416) Background analysis(3) started
[Info  - 12:39:21] (26416) Background analysis(2) root directory: c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist
[Info  - 12:39:21] (26416) Background analysis(2) started
[Info  - 12:39:21] (26416) Background analysis(4) root directory: c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist
[Info  - 12:39:21] (26416) Background analysis(4) started
[Info  - 12:39:21] (26416) No configuration file found.
[Info  - 12:39:22] (26416) No pyproject.toml file found.
[Info  - 12:39:22] (26416) Setting pythonPath for service "MemFS - Sample": "C:\Users\josverl\AppData\Local\Microsoft\WindowsApps\python3.9.exe"
[Warn  - 12:39:23] (26416) stubPath \typings is not a valid directory.
[Info  - 12:39:23] (26416) Assuming Python version 3.9
[Info  - 12:39:23] (26416) Assuming Python platform Windows
[Info  - 12:39:23] (26416) Search paths for \
[Info  - 12:39:24] (26416)   c:\Users\josverl\.vscode\extensions\ms-python.vscode-pylance-2022.6.30\dist\typeshed-fallback\stdlib
[Info  - 12:39:24] (26416)   \
[Info  - 12:39:24] (26416)   \typings
....
[Info  - 12:39:24] (26416) Adding fs watcher for directories:
 \
[Info  - 12:39:24] (26416) Searching for source files
[Info  - 12:39:24] (26416) Auto-excluding \$Recycle.Bin\S-1-12-1-3020494159-1235939459-3438115750-967420959\$REJ16W7.venv
[Info  - 12:39:24] (26416) Auto-excluding \$Recycle.Bin\S-1-12-1-3020494159-1235939459-3438115750-967420959\$RGXEZSB.venv
...
[Warn  - 12:39:24] (26416) Skipping broken link "\$Recycle.Bin\S-1-5-18"
[Warn  - 12:39:24] (26416) Skipping broken link "\PerfLogs"
[Warn  - 12:39:24] (26416) Skipping broken link "\Program Files\WindowsApps"
[Warn  - 12:39:25] (26416) Skipping broken link "\ProgramData\Microsoft\Crypto\PCPKSP\WindowsAIK"
....
```

* select 'F1 > [MemFs] Create Files' and notice how the explorer is now populated
* ... try things out, e.g. IntelliSense in memfs-files, create new files, save them, etc
* select 'F1 > [MemFs] Delete Files' or reload to restart




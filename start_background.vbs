Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "d:\github repos\Sj\ai-incubator"
WshShell.Run """C:\Python314\pythonw.exe"" server.py", 0, False

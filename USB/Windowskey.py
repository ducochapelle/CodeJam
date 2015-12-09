import win32com.client
import time
shell = win32com.client.Dispatch("Wscript.Shell")
time.sleep(10)
shell.SendKeys("{BREAK}")
shell.SendKeys("^{ESC}")
shell.SendKeys("^{ESC}")

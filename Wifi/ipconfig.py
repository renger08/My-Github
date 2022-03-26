import subprocess

modem_info = subprocess.getoutput("ipconfig")

print(modem_info)
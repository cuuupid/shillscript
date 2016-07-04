import os, sys, subprocess

curdir = str(os.path.dirname(os.path.abspath(__file__)))
subprocess.call('start /wait python '+curdir+'\\clinton.py '+sys.argv[1], shell=True)
print("Clinton.py started")
subprocess.call('start /wait python '+curdir+'\\email_server_init.py',shell=True)
print("Email Server online")
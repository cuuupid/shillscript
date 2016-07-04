import os, sys, email_server
from email_server import CustomSMTPServer

print("[+] Starting email server...")
server = CustomSMTPServer(('127.0.0.1',1025), None)
server.initialize()
print("[+] Email server started")
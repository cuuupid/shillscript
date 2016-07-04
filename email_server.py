import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print("Receiving message from "+str(peer))
        print("Message from: "+str(mailfrom))
        print("Message to: "+str(rcpttos))
        print("Message length: "+str(len(data)))
        return
    def initialize(self):
        asyncore.loop()
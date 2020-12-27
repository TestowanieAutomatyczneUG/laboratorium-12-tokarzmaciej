from src.zadanie3.mailServer import MailServer
from src.zadanie3.templateEngine import TemplateEngine


class Messenger:
    def __init__(self):
        self.TemplateEngine = TemplateEngine()
        self.MailServer = MailServer()

    def sendMessage(self, address, message):
        if self.MailServer.sendMessage(address, message):
            return self.TemplateEngine.sendMessage(address, message)
        else:
            raise Exception('Error Server')

    def receiveMessage(self):
        if self.MailServer.receiveMessage():
            return self.TemplateEngine.receiveMessage()
        else:
            raise Exception('Error Server')

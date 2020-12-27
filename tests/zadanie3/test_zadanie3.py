from src.zadanie3.messenger import Messenger
from unittest.mock import *
from unittest import TestCase, main


class testMessenger(TestCase):
    def setUp(self):
        self.temp = Messenger()

    def test_messenger_send(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.sendMessage.return_value = {'address': 'maciek@example.com', 'message': 'Hello'}
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.sendMessage('maciek@example.com', 'Hello')
        self.assertEqual(result, {'address': 'maciek@example.com', 'message': 'Hello'})

    def test_messenger_send_error_server(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = False
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.sendMessage.return_value = {'address': 'maciek@example.com', 'message': 'Hello'}
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, 'Error Server', result, 'maciek@example.com', 'Hello')

    def test_messenger_send_bad_email(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.sendMessage.side_effect = Exception("Bad email")
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, 'Bad email', result, 'maciek_example.com', 'Hello')

    def test_messenger_send_bad_message(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.sendMessage.side_effect = TypeError("Bad type message")
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, "Bad type message", result, 'maciek@example.com', False)

    def test_messenger_receive(self):
        MailServer = Mock()
        MailServer.receiveMessage.return_value = True
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.receiveMessage.return_value = "Hello"
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.receiveMessage()
        self.assertEqual(result, "Hello")

    def test_messenger_receive_error_server(self):
        MailServer = Mock()
        MailServer.receiveMessage.return_value = False
        self.temp.MailServer = MailServer

        TemplateEngine = Mock()
        TemplateEngine.receiveMessage.return_value = "Hello"
        self.temp.TemplateEngine = TemplateEngine

        result = self.temp.receiveMessage
        self.assertRaisesRegex(Exception, 'Error Server', result)


if __name__ == '__main__':
    main()

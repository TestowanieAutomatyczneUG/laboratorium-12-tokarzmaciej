from zadanie2.zadanie2 import Subscriber
from unittest.mock import *
from unittest import TestCase, main


class testSubscriber(TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client_positive(self):
        self.temp.addClient = Mock()
        self.temp.addClient.return_value = [{"name": "Piotr", "email": "piotrnowak@example.com"}]

        result = self.temp.addClient("Piotr", "piotrnowak@example.com")
        self.assertListEqual(result, [{"name": "Piotr", "email": "piotrnowak@example.com"}])

    def test_add_client_this_client_exists(self):
        self.temp.addClient = Mock()
        self.temp.clients = [{"name": "Piotr", "email": "piotrnowak@example.com"}]
        self.temp.addClient.side_effect = Exception("This client exists")

        result = self.temp.addClient
        self.assertRaisesRegex(Exception, "This client exist", result, "Piotr", "piotrnowak@example.com")

    def test_add_client_bad_email(self):
        self.temp.addClient = Mock()
        self.temp.addClient.side_effect = TypeError("Bad type name or/and email")

        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type name or/and email", result, "Piotr", None)

    def test_add_client_bad_name(self):
        self.temp.addClient = Mock()
        self.temp.addClient.side_effect = TypeError("Bad type name or/and email")

        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type name or/and email", result, 123, "piotrnowak@example.com")

    def test_delete_client(self):
        self.temp.deleteClient = Mock()
        self.temp.clients = [{"name": "Krzysztof", "email": "kszysztofnowicki@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.deleteClient.return_value = "Delete person name: Krzysztof, email: kszysztofnowicki@example.com"

        result = self.temp.deleteClient("Krzysztof", "kszysztofnowicki@example.com")
        self.assertEqual(result, "Delete person name: Krzysztof, email: kszysztofnowicki@example.com")

    def test_delete_client_lack_client(self):
        self.temp.deleteClient = Mock()
        self.temp.clients = [{"name": "Krzysztof", "email": "kszysztofnowicki@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.deleteClient.side_effect = Exception("Lack client")

        result = self.temp.deleteClient
        self.assertRaisesRegex(Exception, "Lack client", result, "Filip", "filipostrowski@example.com")

    def test_send_message(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Krzysztof", "email": "kszysztofnowicki@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.return_value = "Send message to kasiapolak@example.com"

        result = self.temp.sendMessage("kasiapolak@example.com", "Hello")
        self.assertEqual(result, "Send message to kasiapolak@example.com")

    def test_send_message_bad_type_message(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Krzysztof", "email": "kszysztofnowicki@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.side_effect = TypeError("Type text message have to be string")

        result = self.temp.sendMessage
        self.assertRaisesRegex(TypeError, "Type text message have to be string", result, "kasiapolak@example.com",
                               False)

    def test_send_message_clients_not_have_this_email(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Krzysztof", "email": "kszysztofnowicki@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.side_effect = Exception("No client has this email")

        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, "No client has this email", result, "bartekkowalslki@example.com", "Hello")


if __name__ == '__main__':
    main()

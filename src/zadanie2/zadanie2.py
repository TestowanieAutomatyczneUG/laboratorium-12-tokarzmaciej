class Subscriber:
    def __init__(self):
        self.clients = []

    def addClient(self, name, email):
        for client in self.clients:
            if client["name"] == name and client["email"] == email:
                raise Exception("This client exists")
        if type(name) == str and type(email) == str:
            self.clients.append({"name": name, "email": email})
            return self.clients
        else:
            raise TypeError("Bad type name or/and email")

    def deleteClient(self, name, email):
        for client in self.clients:
            if client["name"] == name and client["email"] == email:
                self.clients.remove({"name": name, "email": email})
                return "Delete person name: %s, email: %s" % (name, email)

        raise Exception("Lack client")

    def sendMessage(self, email, textMessage):
        for client in self.clients:
            if client["email"] == email:
                if type(textMessage) == str:
                    return "Send message to %s" % email
                else:
                    raise TypeError("Type text message have to be string")
        raise Exception("No client has this email")

import requests


class Api:
    def __init__(self):
        self.api = "https://randomuser.me/api/"

    def getUser(self):
        response = requests.get(self.api)
        return response.json()['results'][0]

    def getUsers(self, amount):
        if type(amount) == int:
            response = requests.get(self.api + "?results=%d" % amount)
            return response.json()['results']
        else:
            raise TypeError("Amount have to be int")

    def getUserName(self):
        response = requests.get(self.api + "?inc=name")
        return response.json()['results'][0]["name"]

    def getUserByNationality(self, nat):
        if type(nat) == str:
            if nat.upper() in ["AU", "BR", "CA", "CH", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "IR", "NL", "NZ", "TR",
                               "US"]:
                response = requests.get(self.api + "?nat=%s" % nat)
                return response.json()['results'][0]["nat"]
            else:
                raise Exception("Bad name nationality")
        else:
            raise TypeError("Nationality have to be string")

    def getUserByGender(self, gender):
        if gender in ["male", "female"]:
            response = requests.get(self.api + "?gender=%s" % gender)
            return response.json()['results'][0]
        else:
            raise Exception("Bad name gender")

    def getUserEmail(self):
        response = requests.get(self.api + "?inc=email")
        return response.json()['results'][0]["email"]



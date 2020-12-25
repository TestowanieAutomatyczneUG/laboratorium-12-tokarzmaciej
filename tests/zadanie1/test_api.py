from unittest import TestCase, main
from zadanie1.zadanie1 import Api


class testApi(TestCase):
    def setUp(self):
        self.temp = Api()

    def test_api_get_user(self):
        self.assertIsInstance(self.temp.getUser(), dict)

    def test_api_get_users(self):
        users = self.temp.getUsers(3)
        self.assertEqual(len(users), 3)

    def test_api_get_users_type_error(self):
        users = self.temp.getUsers
        self.assertRaisesRegex(TypeError, "Amount have to be int", users, "6")

    def test_api_get_user_name(self):
        name = self.temp.getUserName()
        self.assertListEqual(list(name.keys()), ['title', 'first', 'last'])

    def test_api_get_user_by_nationality(self):
        nationality = self.temp.getUserByNationality("fr")
        self.assertEqual(nationality, "FR")

    def test_api_get_user_by_nationality_type_error(self):
        nationality = self.temp.getUserByNationality
        self.assertRaisesRegex(TypeError, "Nationality have to be string", nationality, False)

    def test_api_get_user_by_nationality_bad_name(self):
        nationality = self.temp.getUserByNationality
        self.assertRaisesRegex(Exception, "Bad name nationality", nationality, "abc")

    def test_api_user_by_gender(self):
        gender = self.temp.getUserByGender("female")['gender']
        self.assertEqual(gender, 'female')

    def test_api_user_by_gender_bad_name(self):
        gender = self.temp.getUserByGender
        self.assertRaisesRegex(Exception, "Bad name gender", gender, "fmale")

    def test_api_get_user_email(self):
        email = self.temp.getUserEmail()
        self.assertIn("@", email)


if __name__ == '__main__':
    main()

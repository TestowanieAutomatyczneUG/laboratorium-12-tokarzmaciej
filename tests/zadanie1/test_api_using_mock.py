from zadanie1.zadanie1 import Api
from unittest.mock import *
from unittest import TestCase, main


class testApiUsingMock(TestCase):
    def setUp(self):
        self.temp = Api()

    def test_api_get_user(self):
        self.temp.getUser = Mock()
        self.temp.getUser.return_value = {"gender": "male",
                                          "name": {"title": "Mr", "first": "Wayne", "last": "Patterson"}}

        result = self.temp.getUser()
        self.assertIsInstance(result, dict)

    def test_api_get_users(self):
        self.temp.getUsers = Mock()
        self.temp.getUsers.return_value = [
            {"gender": "female", "name": {"title": "Ms", "first": "Sandra", "last": "Chevalier"}},
            {"gender": "female", "name": {"title": "Miss", "first": "Sara", "last": "Erkkila"}},
            {"gender": "female", "name": {"title": "Miss", "first": "Sheila", "last": "Gardner"}}
        ]

        result = self.temp.getUsers(3)
        self.assertEqual(len(result), 3)

    def test_api_get_users_type_error(self):
        self.temp.getUsers = Mock()
        self.temp.getUsers.side_effect = TypeError("Amount have to be int")

        result = self.temp.getUsers
        self.assertRaisesRegex(TypeError, "Amount have to be int", result, "6")

    def test_api_get_user_name(self):
        self.temp.getUserName = Mock()
        self.temp.getUserName.return_value = {"title": "Mr", "first": "Wayne", "last": "Patterson"}

        result = self.temp.getUserName()
        self.assertListEqual(list(result.keys()), ['title', 'first', 'last'])

    def test_api_get_user_by_nationality(self):
        self.temp.getUserByNationality = Mock()
        self.temp.getUserByNationality.return_value = "FR"

        result = self.temp.getUserByNationality("fr")
        self.assertEqual(result, "FR")

    def test_api_get_user_by_nationality_type_error(self):
        self.temp.getUserByNationality = Mock()
        self.temp.getUserByNationality.side_effect = TypeError("Nationality have to be string")

        result = self.temp.getUserByNationality
        self.assertRaisesRegex(TypeError, "Nationality have to be string", result, False)

    def test_api_get_user_by_nationality_bad_name(self):
        self.temp.getUserByNationality = Mock()
        self.temp.getUserByNationality.side_effect = Exception("Bad name nationality")

        result = self.temp.getUserByNationality
        self.assertRaisesRegex(Exception, "Bad name nationality", result, "abc")

    def test_api_user_by_gender(self):
        self.temp.getUserByGender = Mock()
        self.temp.getUserByGender.return_value = {"gender": "female"}

        result = self.temp.getUserByGender("female")['gender']
        self.assertEqual(result, 'female')

    def test_api_user_by_gender_bad_name(self):
        self.temp.getUserByGender = Mock()
        self.temp.getUserByGender.side_effect = Exception("Bad name gender")

        result = self.temp.getUserByGender
        self.assertRaisesRegex(Exception, "Bad name gender", result, "fmale")

    def test_api_get_user_email(self):
        self.temp.getUserEmail = Mock()
        self.temp.getUserEmail.return_value = "wayne.patterson@example.com"

        result = self.temp.getUserEmail()
        self.assertIn("@", result)


if __name__ == '__main__':
    main()

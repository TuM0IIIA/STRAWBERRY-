from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import *
from main.views import *


def main():  # check database via stored fixture file
    TestDataBase.setUp()
    TestDataBase.test_user_exist()
    TestDataBase.test_user_check_password()
    TestDataBase.test_posts()
    TestDataBase.test_all_data()


class TestDataBase(TestCase):
    """the best solution is to use fixtures to check the data in database
    superuser has to be created before
    all the command u can find in django docs"""
    fixtures = [
        'data.json'
    ]

    def setUp (self):
        self.user = User.objects.get(username="t")
  #      print(self.user)  # double check the output
    def test_user_exist(self):
        users = User.objects.all()
  #      print(users)  # double check the output
        users_number = users.count()
  #      print(users_number)  # double check the output
        user = users.first()
        self.assertEqual(users_number, 1)
        self.assertEqual(user.username, "t")  # name of our superuser
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):  # check the password for superuser we created
        self.assertTrue(self.user.check_password('123'))


    def test_posts(self):
        response = self.client.post(
                '/contact/',
                {'message': 'I like your site'},
            )
        self.assertEqual(response.status_code, 200)  # "The request of HTTP 200 has been done Ok"

    def test_all_data(self):  # check if DB has more than one value for each parameter
        self.assertGreater(Product.objects.all().count(), 0)

if __name__ == "__main__":
    main()

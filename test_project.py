from project import user_prompt,run_tests,run_server,the_check_func
import unittest

"""To run the checking, please  use:  'pytest -s test_project.py' """

def main():
    test_user_prompt ()
    test_run_tests()
    TestMethods.test_the_check_func(self)
    test_run_server()


def test_user_prompt ():
    print("  !!!  Here we check the user input in a row - to pass press '1'")
    assert user_prompt("1") == ('1') #int as an output
    print("  !!!  Here we will check the second options for user input - to pass press '2'")
    assert user_prompt("2") == ('2') #int as an output
    print("  !!!  The third option for user input could be anything, to pass - input 'dog', please ")
    assert user_prompt("dog") == ('dog') #

def test_run_tests():
    print ('     ')
    print(" in this test we wll run the tests checking ")
    print ('     ')
    assert run_tests() == (None) # run the link on tests

class TestMethods(unittest.TestCase):

    def test_the_check_func(self):  # test function
        firstValue = None
        # error message in case if test case got failed
        message = ("Please, follow the recommendations and choose either '1' or '2', Thank you.")
        # assertIsNone() to check that if input value is none
        self.assertIsNone(firstValue, message)


def test_run_server():  # running server CTR+C to close
    print('          ')
    print(" !!! in this test we wll run the server   ")
    print ('          ')
    assert run_server() == (None)
    print('if server is working')


if __name__ == "__main__":
    main()

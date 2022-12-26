from django.core import management
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()


def main():

    variable = user_prompt()
    the_check_func(variable)


def user_prompt(*args):

    user_input = input(
        "Dear CS50 Team, would you like to run the TEST CHECKS (1) or to run the SERVER (2)?  ").strip()
    return (user_input)


def run_tests():
    management.call_command('test')


def run_server():  # if do not use --noreload we have a bug
    # https://code.djangoproject.com/ticket/8085
    management.call_command('runserver', '--noreload')


def the_check_func(user_input):  # due to the requerements
    try:  # Your 3 required custom functions other than main

        if user_input == '1':
            run_tests()

        elif user_input == '2':
            run_server()
        else:
            print("Please, follow the recommendations and choose either '1' or '2', Thank you.")

    except ValueError:
        print(" STOP 😊 ")


if __name__ == "__main__":
    main()

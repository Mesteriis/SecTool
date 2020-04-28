def hack_n_password_for_all_logins(login_generator, password_generator, request, limit=1000):
    """
    Searching passwords with a limit to all logins from the list
    :param login_generator: link to the login generator
    :param password_generator: link to password generator
    :param request: request function reference
    :param limit: search limit
    :return: Prints a couple result
    """
    login_state = None
    while True:
        login, login_state = login_generator(login_state)
        if login is None:
            break
        password_state = None
        for i in range(limit):
            password, password_state = password_generator(password_state)
            if password is None:
                print("Not found :-(")
                break

            if request(login, password):
                print('SUCCESS', login, password)
                break


def hack_n_login_for_all_passwords(login_generator, password_generator, request, limit=100):
    """
    Search n users for all passwords
    :param login_generator: link to the login generator
    :param password_generator: link to password generator
    :param request: request function reference
    :param limit: search limit
    :return: Prints a couple result
    """
    password_state = None
    while True:
        password, password_state = password_generator(password_state)
        if password is None:
            break

        login_state = None
        for i in range(limit):
            login, login_state = login_generator(login_state)
            if login is None:
                print ( "Not found :-(" )
                break

            if request(login, password):
                print('SUCCESS', login, password)
                break


def hack_login_password_random(login_generator, password_generator, request, limit=10000):
    """
    Full random
    :param login_generator: login string
    :param password_generator: link to password generator
    :param request: request function reference
    :param limit: search limit
    :return: Prints a couple result
    """
    login_state = None
    password_state = None
    for attempt in range(limit):
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(password_state)
        if login is None or password is None:
            print ( "Not found :-(" )
            break
        if request(login, password):
            print('SUCCESS', login, password)

def hackKnowUser(login, password_generator, request, limit=10000):
    """
    Password selection for a specific user
    :param login: login string
    :param password_generator: link to password generator
    :param request: request function reference
    :param limit: search limit
    :return: Prints a couple result
    """
    password_state = None
    for attempt in range(limit):
        password, password_state = password_generator(password_state)
        if login is None or password is None:
            print ( "Not found :-(" )
            break
        if request(login, password):
            print('SUCCESS', login, password)
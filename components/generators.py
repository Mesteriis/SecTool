"""
Login and password generators
"""
# WeConnectResources
with open('res/pass.dic') as f_pass:
    content = f_pass.read()
    password_list = content.split('\n')

with open('res/usr.dic') as f_usr:
    content = f_usr.read()
    login_list = content.split('\n')


def generate_popular_passwords(state):
    """
    We get the following password from the popular file
    :param state: item position for response
    :return: couple password and position
    """
    if state is None:
        state = 0
    if state >= len(password_list):
        return None, None
    return password_list[state], state + 1

def generate_logins(state):
    """
    We get the following login from the popular file
    :param state: item position for response
    :return: couple login and position
    """
    if state is None:
        state = 0
    if state >= len(login_list):
        return None, None
    return login_list[state], state + 1

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def generate_passwords_brute_force(state):
    """
    String Based Generation
    :param state: item position for response
    :return:
    """
    if state is None:
        state = [0, 0]
    k, counter = state
    password = ''
    i = counter
    while i > 0:
        r = i % base
        password = alphabet[r] + password
        i = i // base
    password = alphabet[0] * (k - len(password)) + password
    counter += 1
    if password == alphabet[-1] * k:
        k += 1
        counter = 0

    return password, [k, counter]

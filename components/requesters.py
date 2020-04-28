import requests

def request_local_server(login, password):
    """
    Authorization request to the local server
    :param login: Username, string
    :param password: User password, string
    :return: response.status_code
    """
    try:
        response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
        return response.status_code == 200
    except:
        print("Server (http://127.0.0.1:5000/auth) is not available")


def request_local_secure_server(login, password):
    """
    Authorization request to the local sec server
    :param login: Username, string
    :param password: User password, string
    :return: response.status_code
    """
    try:
        response = requests.post('http://127.0.0.1:4000/auth',
                                 json={'login': login, 'password': password})
        return response.status_code == 200
    except:
        print("Server (http://127.0.0.1:4000/auth) is not available")
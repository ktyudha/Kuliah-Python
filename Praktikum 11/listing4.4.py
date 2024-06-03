import requests

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'admin@ent.pens.ac.id'
PASSWORD = 'password'

SIGNUP_URL = 'https://cirt.pens.ac.id/login'


def submit_form():
    """Submit a form"""
    payload = {
    ID_EMAIL : EMAIL,
    ID_PASSWORD : PASSWORD,}
    # make a get request
    resp = requests.get(SIGNUP_URL)
    print ("Response to GET request: %s" %resp.content)
    # send POST request
    resp = requests.post(SIGNUP_URL, payload)
    print ("Headers from a POST request response: %s" %resp.headers)
    print("Success")

if __name__ == '__main__':
    submit_form()
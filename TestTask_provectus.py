import requests
import json
import pytest

# Test on local server
# url = 'http://localhost/login.php'
url = 'http://instatestvx.me/api/auth/login'
data = {'login': 'hello@world.com','password': '12345678'}
headers = {'Content-type': 'application/json'}
r = (requests.post(url, data=json.dumps(data), headers=headers)).json()

def test_checkResponse():
    assert r['success'] == False
    assert r['errors']['email'] == [""]
    assert r['errors']['password'] == [""]
    assert r['errors']['message'] == 'The password and email you entered don\'t match. If you forgot your password,use \"Forgot Password\"'


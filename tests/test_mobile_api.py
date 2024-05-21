import pytest
import requests


@pytest.fixture
def base_url():
    return "https://courses.edx.org/oauth2/access_token"

@pytest.fixture
def body():
    return {"client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "grant_type": "password",
            "username": "xxxxxxxxxx",
            "password": "xxxxxxxxxx",
            "token_type": "JWT",
            "asymmetric_jwt": "1"
            }

def test_post_new_user(base_url, body):

    response = requests.post(f"{base_url}", data=body)
    assert response.status_code == 200
    assert response.json()["token_type"] == "JWT"

    global access_token
    access_token = response.json()["access_token"]

def test_get_user_info():

    user_info_headers = {"X-edx-api-key": "apikey",
                      "Authorization": f"JWT {access_token}",
                      "Content-Type": "application/json"}

    response = requests.get("https://xxxxxxxxxx/api/mobile/v0.5/my_user_info", headers=user_info_headers)

    assert response.status_code == 200
    assert response.json()["id"] == 26093933
    assert response.json()["username"] == "xxxxxxxxxxxxxxx"
    assert response.json()["email"] == "xxxxxxxxxxxxxxx"
    assert response.json()["name"] == "xxxxxxxxxxxxxxx"

def test_user_course_enrollments():

    user_info_headers = {"X-edx-api-key": "apikey",
                      "Authorization": f"JWT {access_token}",
                      "Content-Type": "application/json"}

    response = requests.get("https://xxxxxxxxxxxxxxx/course_enrollments?page=1", headers=user_info_headers)

    assert response.status_code == 200

import requests
from tests.config import API_URL
from auth import hash_password


def test_root():
    response = requests.get(API_URL)
    assert response.status_code == 404


def test_create_user():
    response = requests.post(f'{API_URL}/api_v1/user/create', json={'name': 'example_name',
                             'email': 'example@mail.ru', 'password': hash_password('1245')})
    print(response)
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert 'id' in json_data
    print(json_data)
    assert json_data['name'] == 'example_name'


def test_create_ads():
    response = requests.post(f'{API_URL}/api_v1/create', json={'heading': 'example', 'user_id': 1})
    assert response.status_code == 200
    json_data = response.json()
    assert 'id' in json_data
    assert json_data['heading'] == 'example'


def test_get_ads_by_id(create_ads):
    response = requests.get(f'{API_URL}/api_v1/{create_ads["id"]}/')
    assert create_ads['id'] == response.json()['id']


def test_get_uncreated_ads():
    response = requests.get(f'{API_URL}/api_v1/999/')
    assert response.status_code == 404


def test_patch_ads(create_ads):
    response = requests.patch(f'{API_URL}/api_v1/{create_ads["id"]}', json={'heading': 'new_heading'})
    assert response.status_code == 200


def test_delete_ads(create_ads):
    response = requests.delete(f'{API_URL}/api_v1/{create_ads["id"]}')
    assert response.json()['status'] == 'deleted'


def test_get_user_by_id(create_user):
    response = requests.get(f'{API_URL}/api_v1/user/{create_user["id"]}/')
    assert create_user['id'] == response.json()['id']





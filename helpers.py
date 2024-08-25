from urls import *
from data import *
import requests
import allure
import json


@allure.step('Создаем заказ через апи')
def create_order():

    payload = {
        'email': static_user_login,
        'password': static_user_password
    }

    api_token = requests.post(api_login_url, data=payload).json()["accessToken"]

    headers = {
        'Content-Type': 'application/json',
        'authorization': api_token
    }

    payload = {
        'ingredients': '61c0c5a71d1f82001bdaaa6d'
    }

    response = requests.post(api_orders_url, data=json.dumps(payload), headers=headers)
    return response.json()['order']['number']

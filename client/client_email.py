import time
from typing import Union
import allure
import requests
from utils.generator import random_temporary_email

class ClientEmail:
    def __init__(self):
        self.base_url = 'https://tempmail.plus'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self, method: str, url: str, json=None, headers: str = None):
        response = self.session.request(method=method,
                                        url=self.base_url + url,
                                        headers=headers,
                                        json=json)
        return response


class EmailClient(ClientEmail):

    def __init__(self, temporary_email):
        super().__init__()
        self.base_email = temporary_email

<<<<<<< HEAD
    def get_email(self):
        response = self.request(method='get', url=f'/api/mails?email={self.base_email}')
        return response.json()

    def get_message_by_id(self):
        response = self.get_email()
=======
    def get_email(self, sleep=0):
        time.sleep(sleep)
        response = self.request(method='get', url=f'/api/mails?email={self.base_email}')
        return response.json()

    def get_last_message(self):
        response = self.get_email(sleep=3)
>>>>>>> origin/master
        last_id = response['last_id']
        message_response = self.request(method='get', url=f'/api/mails/{last_id}?email={self.base_email}')
        return message_response.json()

<<<<<<< HEAD
    def get_registration_token(self):
        time.sleep(2)
        return self.get_message_by_id()['html'].split('href="')[1].split('">')[0].split('token=')[1]


random_email = random_temporary_email()
print(random_email)
print(EmailClient('ovAwDLmQtZ@mailto.plus').get_email())
=======
    def get_first_message(self):
        response = self.get_email(sleep=3)
        first_id = response['first_id']
        message_response = self.request(method='get', url=f'/api/mails/{first_id}?email={self.base_email}')
        return message_response.json()

    def get_registration_token(self):
        return self.get_last_message()['html'].split('href="')[1].split('">')[0].split('token=')[1]

    def get_reset_password_link(self):
        return self.get_first_message()['html'].split('href="')[1].split('">')[0]

    def get_change_password_token(self):
        return self.get_first_message()['html'].split('href="')[1].split('">')[0].split('token=')[1]
>>>>>>> origin/master

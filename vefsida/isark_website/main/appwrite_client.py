

from appwrite.client import Client
from appwrite.services.account import Account

def get_appwrite_client():
    client = Client()
    client.set_endpoint('https://cloud.appwrite.io/v1')  
    client.set_project('6752c37e0000b6e66c6a')  
    return client


def get_account():
    client = get_appwrite_client()
    return Account(client)

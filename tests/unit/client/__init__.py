import os

from anna_client.client import Client


client = Client(endpoint='https://api.annahub.se')

if 'ANNA_TOKEN' in os.environ:
	client.inject_token(os.environ['ANNA_TOKEN'])

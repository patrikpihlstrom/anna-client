import os

from anna_client.client import Client


#host = 'https://api.annahub.dev'
#if 'ANNA_HOST' in os.environ:
#	host = os.environ['ANNA_HOST']
host = 'http://localhost:5000/'

client = Client(endpoint=host)

if 'ANNA_TOKEN' in os.environ:
	client.inject_token(os.environ['ANNA_TOKEN'])

from django.test import TestCase
from time import sleep 
from multiprocessing import Process

from datetime import datetime

import requests
from django.views.decorators.csrf import csrf_exempt



import sys

@csrf_exempt
def schedule(wait_for):
	while True:
		sleep(wait_for)
 #this should log in in, i don't have an account there to test.
		data = {'name': 'PROJECT KRON', 'assign': 'Admin', 'status': 'Начало'}
		url = 'http://localhost:8000/admin/main/space/add/'

		r = requests.post(url, data=data) #unless you need to set a user agent or referrer address you may not need the header to be added. 


if __name__ == '__main__':
	Process(target=schedule, args=(2, )).start()

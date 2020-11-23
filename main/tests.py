from django.test import TestCase
from time import sleep 
from multiprocessing import Process

from datetime import datetime

import requests

import sys

class PDF:
    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.pdfObject = fitz.open(pathFile)
    #Поиск ключевого слова в определенной странице, idpage - страница, pattern - ключевое слово 
    def findPage(self, idPage, pattern):
        currentPage = self.pdfObject.loadPage(idPage)
        textCurrentPage = currentPage.getText()
        if re.search(pattern, textCurrentPage):
            return (True, textCurrentPage)
        else:
            return (False, None)

    #Поиск по слову если оно есть во всех страницах пдф, то добовляет в список=[Номер страницы, содиржимое страницы]
    def findAllPage(self, pattern):#pattern - поиск 
        results = []
        for idPage in range(self.pdfObject.pageCount):
            currentPage = self.pdfObject.loadPage(idPage)
            textCurrentPage = currentPage.getText()
            if re.search(pattern, textCurrentPage):
                results.append(('На странице номер', idPage+1, 'нашлость ключевое слово: ',pattern))
        return results


def schedule(wait_for):

	while True:
		sleep(wait_for)
 #this should log in in, i don't have an account there to test.
		data = {
		    "task_name": "TEST",
		    "dead_line": "2020-11-28",
		    "attachments": None,
		    "description": "dwdwd",
		    "created_by": "dwdwedwdd",
		    "lists": 4,
		    "status": 1,
		    "assign": [
		        2
		    ]
		}



		url = 'http://localhost:8000/task_create/'

		r = requests.post(url, json=data, headers = {'Content-Type': 'application/json'}) #unless you need to set a user agent or referrer address you may not need the header to be added. 


if __name__ == '__main__':
	Process(target=schedule, args=(5, )).start()

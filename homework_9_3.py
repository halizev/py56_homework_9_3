import requests
import time


to_date_time = int(time.time())
from_date_time = to_date_time - 172800


class StackOverflow:
    def __init__(self):
        self.questions_list = list()

    def pagination_test(self, to_date_time, from_date_time):
        counter = 0
        url = 'https://api.stackexchange.com/2.3/questions'
        parameters = dict(order='desc', sort='creation', tagged='python', site='stackoverflow', fromdate=from_date_time,
                          todate=to_date_time, pagesize=100)
        r = requests.get(url, params=parameters)
        for question in r.json()['items']:
            self.questions_list.append(question['link'])
            counter += 1
        if counter == 100:
            to_date_time = question['creation_date']
            time.sleep(1)
            self.pagination_test(to_date_time, from_date_time)
        return self.questions_list


print(StackOverflow().pagination_test(to_date_time, from_date_time))
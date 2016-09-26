import json
import time

import requests


class InsightConnection(object):
    def __init__(self, url='', insertKey='', contentType=''):

        self.url = "https://insights-collector.newrelic.com/v1/accounts/1423392/events"
        self.insertKey = "Pr-mRGqjdidm77vQPejXcaj-MsQ4RLqq"
        self.contentType = "application/json"

        print('%s: Insight connection parameters(not the connection) are ready!' % time.ctime())

    def send_metrics(self, metrics):
        print '%s: Prepare to send metrics %s.' % (time.ctime(), metrics)
        metrics_data = json.dumps(metrics)
        headers = {'content-type': self.contentType, 'X-Insert-Key': self.insertKey}
        url = self.url

        r = None
        try:
            r = requests.post(url, data=metrics_data, headers=headers)
            print '%s: send_metrics return code: %d' % (time.ctime(), r.status_code)
        except requests.exceptions.RequestException as e:
            print e
        # should return '200' if succeeds

        return r.status_code

        # http://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

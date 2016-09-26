import threading
import time

from insight_conn import InsightConnection

""" Sender(Consumer) thread
Sender: is a thread that pulls metrics from the Queue, processes them and send them to the New Relic Server.
In this monitoring system, this Sender is the metric Consumer.
"""


class Sender(threading.Thread):
    metrics = []
    insight_conn = InsightConnection()

    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.q = queue

    def run(self):
        print('%s: Basic_metrics_sender started!' % time.ctime())
        while True:
            try:
                # pop metrics from the queue,
                # and merge 20 metrics(or all the left metrics(<10) in the queue) in to a Json object
                while not self.q.empty():
                    if (len(self.metrics) >= 10):
                        break
                    # get(self, block=True, timeout=None) ,1=block_wait,100=timeout secs
                    metric = self.q.get(1, 100)
                    self.metrics.append(metric)

                    print "%s: %s pop queue: %s" % (time.ctime(), self.getName(), metric)
                    time.sleep(1)

                # Call Insight API to send the Json
                while self.insight_conn.send_metrics(self.metrics) is not 200:
                    time.sleep(15)
                    continue
                self.metrics[:] = []

            except:
                print "%s: %s finished!" % (time.ctime(), self.getName())
                # discard metrics because of the exception
                # TODO: should store in the message queue instead
                self.metrics[:] = []
                time.sleep(5)

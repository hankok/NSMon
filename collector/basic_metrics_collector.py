import datetime
import random
import threading
import time

""" Collector(Producer) thread
Collector: is a thread that using NitroAPI to get CPU/MEM/Network/Disk and other data from MaaS and Netscaler, convert
           the data to metrics and push the metrics into a Queue.
In this monitoring system, the metrics are the produce, so the Collector is the metric Producer.
"""


class Collector(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.q = queue

    def run(self):
        """
        while True:
            #get data from MAS/NitroAPI
            metric = NitroOperation.getBasicMetric()

            if metric is not None:
                #push the metrics to the queue
                self.q.put(metric)
            time.sleep(10)
        """
        print('%s: Basic_metrics_collector started!' % time.ctime())
        while True:
            cpu = random.randint(1, 100)
            mem = random.randint(1912321, 2147483648)
            disk = random.randint(1, 100)
            network = random.randint(1, 100)
            host = random.randint(1, 2)
            metric = {"eventType": "SYSTEM_BASIC_METRICS",
                      "clientTime": str(datetime.datetime.now()),
                      "Host": "NetScaler" + str(host),
                      "CPU": cpu,
                      "Mem_used": mem,
                      "Disk_used": disk,
                      "network": network}
            # make sure the queue doesn't eat all the memory
            if self.q.qsize() < 1000:
                self.q.put(metric)
            else:
                print "queue is full!"
            time.sleep(1)

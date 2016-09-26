#!/usr/bin/env python
# coding:utf8
'''
* Copyright (c) 2016 Citrix Systems, Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
'''

from Queue import Queue

from collector import basic_metrics_collector
from sender import basic_metrics_sender

"""
    start all the collectors and senders.
    each pair of (collector, sender) will use a unique Queue (TODO:change to msg queue in later version)
"""


def main():
    queue_basic_metrics = Queue()
    producer = basic_metrics_collector.Collector('BasicMetricsCollector.', queue_basic_metrics)
    consumer = basic_metrics_sender.Sender('BasicMetricsSender', queue_basic_metrics)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print 'All threads started, this script supposed to run eternally on background!'


if __name__ == '__main__':
    main()

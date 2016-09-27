# NSMon
monitoring Netscaler using new relic

Python (3rd party) package requirements:
requests
newrelic
mas-nitro-python


#1. Metric Collector
./collector
Here you can add multiple collectors, each for one type of metrics, e.g. basic_metrics_collector.

./collector/basic_metrics_collector.py

Collector: is a thread that using NitroAPI to get CPU/MEM/Network/Disk and other data from MaaS and Netscaler, convert
           the data to metrics and push the metrics into a Queue.
In this monitoring system, the metrics are the produce, so the Collector is the metric Producer.

./collector/nitro_operation.py
implement all the nitro API operations here for different metric collector types

#2. Metric Sender
./sender
Here you can add multiple Senders, each for one type of metrics, e.g. basic_metrics_sender.

./sender/basic_metrics_sender.py

Sender: is a thread that pop the metrics from a Queue, and uses Insight API to send CPU/MEM/Network/Disk and other data to New Relic.
In this monitoring system, the metrics are the produce, so the Sender is the metric Consumer.

#3. Main methods and Other
./startmon.py
The main method, queue and thread will initilize here.

./common
you know common funcs

./conf
configuration for the project (not used for now)







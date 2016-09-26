class NitroOperation(object):
    # TODO: including all the Operations on Nitro API, e.g. get basic metrics, get other metrics

    def __init__(self, user, password, contentType):
        """
        Get all netscaler IPs, users, passwords correspondingly
        push everything to the list
        ip_list   = ['10.1.1.1', '10.1.1.2']
        user_list = ['user1', 'user2']
        pass_list = ['pass1', 'pass2']

        """
        ip_list = []
        user_list = []
        pass_list = []

        print('Netscaler IP and credentials ready!')

    """
        This will get all the CPU/MEM/Network/Disk data in ONE nitro API call
        This operation will be done periodically
    """

    def getBasicMetric(self):
        # TODO: get all basic metrics from NitroAPI in one call
        # return: a dict, feel free to add all the metrics needed, format like this:
        #        {"eventType": "SYSTEM_BASIC_METRICS", "Host": "NetScaler1", "IP":"10.23.12.2", "CPU": 91, "Mem_used": 2109800, "Disk_used": 82}
        # or return None if failed call
        pass

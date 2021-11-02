# encoding= utf-8
# __author__= gary
import json
import re
import socket
import subprocess
from time import sleep


class DigitIndoor:
    """
    library for digit indoor to answer the call or
    """
    def __init__(self):
        pass

    def start(self, indoor_ip, case_name, case_id, indoor_ip_port=8010):
        """
        the test case need to be started with ip, case_name, and test case id
        """
        msg = json.dumps({"cmd": "AutoTest", "data": {"command": "start", "caseName": case_name,
                                                      "sid": case_id}})
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def end(self, indoor_ip, case_name, case_id, indoor_ip_port=8010):
        """
        the test case need to end with ip, case_name, and test case id
        """
        msg = json.dumps({"cmd": "AutoTest", "data": {"command": "end", "caseName": case_name,
                                                      "sid": case_id}})
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def monitor(self, indoor_ip, outdoor_ip, indoor_ip_port=8010):
        """
        monitoring api for digital indoor monitor the outdoor, the default port is 8010
        """
        msg = json.dumps({"cmd": "AutoTest", "data": {"command": "monitoring", "device_ip": outdoor_ip,
                                                      "device_name": "AutoTest"}})
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def unlock(self, indoor_ip, indoor_ip_port=8010):
        """
        use the api to send unlock command, the default port should be 8010
        """
        msg = '''{"cmd":"AutoTest","data":{"command":"unlock"}} '''
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def _send_message(self, msg, ip_port):
        b_msg = msg.encode()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.sendto(b_msg, ip_port)


if __name__ == '__main__':
    my = DigitIndoor()
    my.start("192.192.255.170", "test_rf", "4")
    my.monitor("192.192.255.170", "192.192.6.6")
    sleep(5)
    my.unlock("192.192.255.170")
    my.end("192.192.255.170", "test_rf", "3")

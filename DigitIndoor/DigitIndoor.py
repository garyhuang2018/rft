# encoding= utf-8
# __author__= gary
import json
import re
import socket
import subprocess


class DigitIndoor:
    def __init__(self):
        pass

    def start(self, indoor_ip, indoor_ip_port, case_name, case_id):
        """
        start the test case
        """
        msg = json.dumps({"cmd": "AutoTest", "data": {"command": "start", "caseName": case_name,
                                                      "sid": case_id}})
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def monitor(self, indoor_ip, indoor_ip_port, outdoor_ip):
        """
        monitoring api for digital indoor monitor the outdoor, the default port should be 8010
        """
        msg = json.dumps({"cmd": "AutoTest", "data": {"command": "monitoring", "device_ip": outdoor_ip,
                                                      "device_name": "AutoTest"}})
        socket_port = (indoor_ip, indoor_ip_port)
        self._send_message(msg, socket_port)

    def unlock(self, indoor_ip, indoor_ip_port):
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
    my.start("192.192.255.170", 8010, "test_rf", "2")
    my.monitor("192.192.255.170", 8010, "192.192.6.6")

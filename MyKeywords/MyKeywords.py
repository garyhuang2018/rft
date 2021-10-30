# encoding= utf-8
# __author__= gary
import re
import subprocess


class MyKeywords:
    def __init__(self):
        pass

    def print_indoor_status(self, response, floor_no, room_no):
        """
        get the status by the floor and room no
        """
        res = response.json()
        for dev in res.get("data"):
            if dev.get('floorNo') == floor_no and dev.get('roomNo') == room_no:
                 if dev.get('status') == 0:
                     print('room', floor_no+room_no, 'is offline')
                 else:
                     print('room', floor_no + room_no, 'is online')

    def print_wall_switch_status(self, dev_addr):
        """
        get the wall switch status
        """
        para = 'adb -s ' + dev_addr + ' shell logcat -d -s wx'
        c_line = subprocess.Popen(para, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        log_results = c_line.decode()
        # search the status of the wall switch
        # (?:.|\n)是指定了一个非捕获组（仅仅用来做匹配，部能通过单独捕获或者编号的组）
        pattern = re.compile(r'status((?:.|\n)*?),')
        status_results = pattern.findall(log_results)
        if len(status_results) > 0:
            if str(status_results[0]).find('off') > 0:
                print('wall switch offline')
            else:
                print('wall switch online')
        else:
            print('wall switch status not change')


if __name__ == '__main__':
    my = MyKeywords()
    my.print_wall_switch_status('M7BBB18A06151861')

# encoding= utf-8
# __author__= gary
import hashlib
import os
import re
import subprocess


class MyKeywords:
    def __init__(self):
        pass

    def print_indoor_status(self, response, floor_no, room_no):
        """
        get the status by the floor and room no, 1 for online, 0 for offline
        """
        res = response.json()
        for dev in res.get("data"):
            if dev.get('floorNo') == floor_no and dev.get('roomNo') == room_no:
                if dev.get('status') == 0:
                    print('room', floor_no + room_no, 'is offline')
                    return 0
                else:
                    print('room', floor_no + room_no, 'is online')
                    return 1

    def print_wall_switch_status(self, dev_addr):
        """
        get the wall switch status
        """
        para = 'adb -s ' + dev_addr + ' shell logcat -d -s wx'
        c_line = subprocess.Popen(para, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        log_results = c_line.decode()
        # search the status of the wall switch
        # (?:.|\n)是指定了一个非捕获组（仅仅用来做匹配，不能通过单独捕获或者编号的组）
        pattern = re.compile(r'status((?:.|\n)*?),')
        status_results = pattern.findall(log_results)
        if len(status_results) > 0:
            if str(status_results[0]).find('off') > 0:
                print('wall switch offline')
                return 0
            else:
                print('wall switch online')
                return 1
        else:
            print('wall switch status not change')

    def get_file_md5(self, file_path) -> str:
        """
        根据文件路径，计算MD5值
        Calculate the md5 value of the file
        """
        if file_path is not None:
            with open(file_path, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            return file_md5
        else:
            return 'None'

    def local_ota_upgrade(self, device_code, file_path):
        """
        根据文件路径进行本地OTA升级
        upgrade the ota file
        e.g.:
        device_code: '192.192.255.237:5555'
        file_path =  r'C:\Users\garyh\Desktop\ota_rk3288_outdoor-P3_20210811.zip'
        """
        para = "adb connect " + device_code
        os.system(para)
        para = 'adb push ' + file_path + ' /sdcard/temp_update.zip'
        os.system(para)
        file_md5 = self.get_file_md5(file_path)
        para = '''adb shell am broadcast -a com.gemvary.ota.local.update --es local_update_path \
        "/sdcard/temp_update.zip" --es tag_md5 ''' + '\"' + file_md5 + '\"'
        print(para)
        os.system(para)


if __name__ == '__main__':
    my = MyKeywords()
    file_p = r'C:\Users\garyh\Desktop\ota_rk3288_outdoor-P3_20210811.zip'
    my.local_ota_upgrade('192.192.255.237:5555', file_p)
   # print(my.print_wall_switch_status('M7BBB18A06151861'))

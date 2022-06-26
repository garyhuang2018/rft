# encoding= utf-8
# __author__= gary
import os
import time
from smb.SMBConnection import SMBConnection
import hashlib


class VersionDetect:
    def get_new_version(self, dir_path, version_date):
        return_dir_path = 'no new version'
        server_ip = "192.192.0.118"  # 共享目录主机IP地址
        username = "gary.huang@gemvary.com"  # 本机用户名
        password = "gemvary1510"  # 本机密码
        my_name = "DESKTOP-OJNEEVN"  # 计算机属性中域名
        remote_name = "abc-infoserver"  # 远端共享文件夹计算机名
        conn = SMBConnection(username, password, my_name, remote_name,
                             is_direct_tcp=True)  # is_direct_tcp=True,默认为当direct_tcp=True时，port需要445。当它是False时，端口应该是139
        assert conn.connect(server_ip, 445)
        shared_file_list = conn.listPath('''提测中转站''', dir_path)
        return_paths = []  # 返回升级文件路径
        for i in shared_file_list:
            if i.filename == version_date:
                return_paths = conn.listPath('''提测中转站''', dir_path + '/' + version_date)
        for s in return_paths:
            if s != '.' or s != '..':
                return_dir_path = str(s.filename)
        return return_dir_path


def get_file_md5(file_path) -> str:
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


def update_app(ip, app_path):
    os.system('adb connect ' + ip)
    os.system('adb install -r ' + full_path.replace('/', '\\'))


if __name__ == '__main__':
    v = VersionDetect()
    dir_path = "/楼宇产品部/门口机/硬编硬解/3288"
    # dir_path = "/智慧社区产品部/室内机/硬编硬解/V2数字机/NX5/DGX"
    # dir_path = "/楼宇产品部/定制项目/千丁定制固件"
    # dir_path = "/智慧社区产品部/定制项目/颐品雅居定制项目"
    print(dir_path)
    now = time.localtime()
    now_time = time.strftime("%Y%m%d", now)
    print(now_time)
    today_version = now_time
    print(dir_path + '/' + today_version + '/' + v.get_new_version(dir_path, today_version))
    full_path = "//192.192.0.118/提测中转站" + dir_path + '/' + today_version + '/' + v.get_new_version(dir_path,
                                                                                                   today_version)
    print(full_path.replace('/', '\\'))
    print(get_file_md5(full_path.replace('/', '\\')))
    path = full_path.replace('/', '\\')
    # 192.192.255.5 is the ip address of main gate outdoor
    update_app('192.192.255.5', path)
#   os.system('adb install -r ' + full_path.replace('/', '\\'))
# print(time.strftime("%Y%m%d", time.localtime(time.time())))

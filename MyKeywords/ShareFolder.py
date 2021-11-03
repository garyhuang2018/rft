# encoding= utf-8
# __author__= gary
import time
from smb.SMBConnection import SMBConnection


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
        sharelist = conn.listPath('''提测中转站''', dir_path)
        return_paths = []  # 返回升级文件路径
        for i in sharelist:
            if i.filename == version_date:
                return_paths = conn.listPath('''提测中转站''', dir_path+'/'+version_date)
        for s in return_paths:
            if s != '.' or s != '..':
                return_dir_path = str(s.filename)
        return return_dir_path


if __name__ == '__main__':
    v = VersionDetect()
    dir_path = "/楼宇产品部/门口机/硬编硬解/3288"
    today_version = '20211019'
    print(dir_path + '/' + today_version + '/' + v.get_new_version(dir_path, today_version))
    #print(time.strftime("%Y%m%d", time.localtime(time.time())))

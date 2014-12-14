#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         deviceinfo.py
#  Description:  获取android手机信息
#
#  Date:         14/11/12 下午7:26
#  Author:       bixiaopeng
#  Tags:        more: http://www.w3cschool.cc/python/python-strings.html
#---------------------------------------------------------------------------
import subprocess
import sys

class AndroidDebugBridgeCommand():

    def __init__(self):
        self.init_command_param()

    #初始化参数
    def init_command_param(self):
        self.command = ['adb'] #默认是adb命令
        self.serial_number = ''
        self.shell_command = None

    def _add_serial_number(self):
        #如果有serial_number需要加上此参数
        if self.serial_number:
            self.command.append('-s %s'%self.serial_number)

    def get_shell_command(self):
        self._add_serial_number()
        #然后获得命令
        if self.shell_command:
            self.command.append('shell %s'%self.shell_command)
        return ' '.join(self.command)

    #adb的非shell命令,只需要传入参数就可以了
    def get_command(self,param):
        self._add_serial_number()
        self.command.append(param)
        return ' '.join(self.command)

class AndroidDebugBridge(object):

    def __init__(self):
        self.adbcmd = AndroidDebugBridgeCommand()


    def get_device_mode(self, serial_num):
        """
        获取手机型号
        [ro.product.model]: [Samsung Galaxy Note 3 - 4.4.2 - API 19 - 1080x1920]
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.product.model")


    def get_device_brand(self, serial_num):
        """
        获取手机的品牌
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.product.brand")

    def get_device_name(self, serial_num):
        """
        手机正式名称
        [ro.product.name]: [vbox86p]
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.product.name")

    def get_device_trace_path(self,serial_num):
        """
        获取trace文件存放路径
        [dalvik.vm.stack-trace-file]: [/data/anr/traces.txt]
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "dalvik.vm.stack-trace-file")

    def get_device_heapssize(self, serial_num):
        """
        单个java虚拟机最大的内存限制,超过会OOM
        [dalvik.vm.heapsize]: [256m]
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "dalvik.vm.heapsize")

    def get_device_heapgrowthlimit(self, serial_num):
        """
        单个应用程序最大内存限制,超过这个值会产生OOM
        [dalvik.vm.heapgrowthlimit]: [96m]
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "dalvik.vm.heapgrowthlimit")

    def get_device_is_root(self,serial_num):
        command = "adb -s %s shell 'ls /system/bin/su' "%serial_num
        result = run_get_result(command).replace('\n','').strip()
        return result == "/system/bin/su"


    def get_devices(self):
        """
        获得设备serial number列表: adb devices
        :return:
        """
        self.adbcmd.init_command_param()
        result=run_get_result(self.adbcmd.get_command("devices"))

        device_line = result.partition('\n')[2].replace('\n', '')

        # logger.info("device list: %s" %device_line)

        #判断是否有设备连接,如果没有就返回空
        if 'device' in device_line and device_line.strip() != "* daemon started successfully *List of devices attached":
            devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')

            return [device for device in devices if len(device) > 1]
        else:
            return []

    def get_device_api_level(self, serial_num):
        """
        获得设备的sdk api level
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.build.version.sdk")

    def get_device_release_version(self, serial_num):
        """
        获取设备的版本号
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.build.version.release")

    def get_device_ip_address(self, serial_num):
        """
        获取设备的ip地址
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "dhcp.wlan0.ipaddress")

    def _getprop(self, serial_num, cmd):
        """
        运行adb shell getprop “”命令
        :param serial_num:
        :param cmd:
        :return:
        """
        return self._shell(serial_num, "getprop %s" % cmd)

    def _shell(self, serial_num, cmd):
        """
        运行adb shell命令
        :param serial_num:
        :param cmd:
        :return:
        """
        command = 'adb -s %s shell %s' % (serial_num, cmd)
        # logger.info("Run command: %s" % command)
        result = run_get_result(command)
        # logger.info("Result: %s" % result)
        return result.replace('\r\n', '')

    def get_device_gsm(self, serial_num):
        """
        获取设备上使用的运营商
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "gsm.operator.alpha")

    def get_device_language(self, serial_num):
        """
        获取设备的语言
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "persist.sys.language")

    def get_device_cpu_brand(self, serial_num):
        """
        获取设备CPU品牌
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "ro.product.cpu.abi2")

    def get_device_timezone(self, serial_num):
        """
        获取设备的时区
        :param serial_num:
        :return:
        """
        return self._getprop(serial_num, "persist.sys.timezone")


#执行shell命令
def run(command, output=None):
    subprocess.call(command, shell=True, stdout=output)


def run_get_result(command):
    try:
        return subprocess.check_output(command, shell=True)
    except Exception, e:
        return ''


def get_device_serial(adb):
    """
    获得一个手机序列号,如果有多个需要选择其中一个
    :param adb:
    :return:
    """

    device_list = adb.get_devices()
    device_len = len(device_list)
    device = None

    # 如果有多台设备,需要先选择
    if device_len > 1:
        print u">>>>>>>>>>> 你的电脑上连接了%s台Android设备,请选择一台进行操作:"% str(device_len)
        seril = 0
        for d in device_list:
            print u"* 设备序号%s: %s"%(seril,d)
            seril += 1

        if sys.platform == 'win32':
            device_num = raw_input(">>>>>>>>>>> 请选择设备序号: ".decode('utf-8').encode('gbk'))
        else:
            device_num = raw_input(">>>>>>>>>>> 请选择设备序号: ")
        device = device_list[int(device_num)]
    elif device_len < 1:
        print u">>>>>>>>>>> 请连接设备"
        exit(0)
    else:
        device = device_list[0]

    return device

def device_info(adb):
    """
    获取手机设备的一些信息
    :param adb:
    :return:
    """
    serial = get_device_serial(adb)
    print u'-----------------------------------测试设备信息---------------------'
    print u"[手机序列号]: %s" % serial
    print u"[手机品牌]: %s" % adb.get_device_brand(serial)
    print u"[手机型号]: %s" % adb.get_device_mode(serial)
    print u"[手机语言]: %s" % adb.get_device_language(serial)
    print u"[Android版本]: %s" % adb.get_device_release_version(serial)
    print u"[AndroidAPI]: %s" % adb.get_device_api_level(serial)
    print u"[时区]: %s" % adb.get_device_timezone(serial)
    print u"[CPU品牌]: %s" % adb.get_device_cpu_brand(serial)
    print u"[IP地址]: %s" % adb.get_device_ip_address(serial)
    print u"[手机网络]: %s" % adb.get_device_gsm(serial)
    print u"[ROOT]: %s" % adb.get_device_is_root(serial)
    print '------------------------------------------------------------------'


if __name__=="__main__":
    device_info(AndroidDebugBridge())

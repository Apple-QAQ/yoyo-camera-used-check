#!/usr/bin/python3
import subprocess
import time
import dbus


is_send = None


def sendLyrics(text):
    bus = dbus.SessionBus()
    lyrics = bus.get_object('com.yoyo.Statusbar', '/Statusbar/PermissionSurveillance')
    iface = dbus.Interface(lyrics, dbus_interface='com.yoyo.Statusbar')
    m = iface.get_dbus_method("sendCameraUser", dbus_interface=None)
    m(text)


def get_app_and_camera():
    try:
        app_lst = []
        shell_return = subprocess.check_output(["bash", "-c", "lsof /dev/video*"]).decode()
        return_lst = shell_return.split("\n")
        del return_lst[0]
        tmp_old = None
        for _i in return_lst:
            __tmp_split = _i.split(" ")
            if __tmp_split[0] == tmp_old:
                ...
            elif __tmp_split[0] != "":
                app_lst.append(__tmp_split[0])
                tmp_old = __tmp_split[0]
        return app_lst
    except subprocess.CalledProcessError:
        return None


while True:
    __tmp_get = get_app_and_camera()
    if is_send == __tmp_get:
        ...
    elif __tmp_get is None:
        ret = "0"
        is_send = __tmp_get
        sendLyrics(ret)
    else:
        is_send = __tmp_get
        ret = "、".join(__tmp_get)
        sendLyrics(ret)
    time.sleep(5)

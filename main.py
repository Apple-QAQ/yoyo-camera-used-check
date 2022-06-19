#!/usr/bin/python3
import os
import time
import dbus


is_send = None


def sendDbusMessage(text):
    bus = dbus.SessionBus()
    lyrics = bus.get_object('com.yoyo.Statusbar', '/Statusbar/PermissionSurveillance')
    iface = dbus.Interface(lyrics, dbus_interface='com.yoyo.Statusbar')
    m = iface.get_dbus_method("sendCameraUser", dbus_interface=None)
    m(text)


def get_app_and_camera():
    app_lst = []
    shell_return = "".join(os.popen("bash -c 'lsof /dev/video*'").readlines())
    if shell_return == "":
        return None
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


while True:
    __tmp_get = get_app_and_camera()
    if is_send == __tmp_get:
        ...
    elif __tmp_get is None:
        ret = "{U-APPLE_QAQ-U}"
        is_send = __tmp_get
        sendDbusMessage(ret)
        # print(ret)
    else:
        is_send = __tmp_get
        ret = "、".join(__tmp_get)
        sendDbusMessage(ret)
        # print(ret)
    time.sleep(5)

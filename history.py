#!/usr/bin/env python
# encoding: utf-8
import os
class save_history(object):
    # 初始化，建立history列表
    def __init__(self):
        self.path=os.path.expandvars('$HOME')
        if os.path.isfile(self.path+ '/.config/mailhistory'):
            self.his_list=[]
            with open(self.path +'/.config/mailhistory', 'r') as b:
                for line in b.readlines():
                    self.his_list.append(line)
                    # 只保存两百条
                if len(self.his_list)>=200:
                    n = len(self.his_list)-200
                    del self.his_list[:n]
        else:
            self.his_list = []
    def add_history(self, number=None):
        if number is not None:
            self.his_list.append(number)
            with open (self.path +'/.config/mailhistory', 'a') as f:
                f.write(self.his_list[-1] + "\n")
    def fetch_history(self):
        self.__init__()
        lenth = len(self.his_list)
        self.his_list.reverse()
        return([self.his_list,lenth])

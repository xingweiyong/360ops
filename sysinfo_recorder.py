#coding:utf-8
import psutil
import re
import time
import os
import json

#get cpu info to dic type var
def get_cpu():
        at_time = time.ctime(time.time())
        cpu = str(psutil.cpu_times())
        item_list = re.findall(re.compile('\((.*?)\)'),cpu)[0].split(' ')
        cpu_info = {}
        result = {}
        for item in item_list:
                cpu_info[item.split('=')[0]] = item.split('=')[1]

        result[at_time] = cpu_info
        return result
#save the result to file
index = 0
def save_res():
        global index
        f = open(os.path.join(os.getcwd(),'file_' + str(index) + '.txt'),'a')

        if os.path.getsize(os.path.join(os.getcwd(),'file_' + str(index) + '.txt')) > 100000:
                #global index
                index += 1
                f = open(os.path.join(os.getcwd(),'file_' + str(index) + '.txt'),'a')
                f.write(json.dumps(get_cpu()))
                f.close()
        else:
                f.write(json.dumps(get_cpu()))
                f.close()

if __name__ == '__main__':
        while True:
                save_res()
                time.sleep(1000)#time interval
                print 'cpu at %s'%time.ctime(time.time())

#coding:utf-8
import subprocess
import os
dic_result = {}
#save the ifconfig result
temp_file = open(os.path.join(os.getcwd(),'if_log'),'w')
subprocess.call(['ifconfig'],stdout=temp_file)

temp_file = open(os.path.join(os.getcwd(),'if_log'),'r')
str_if = temp_file.read()
list_if = str_if.split('\n')
num = len(list_if)
#filter what we want
for i in range((num-1)/9):
        dic_result[list_if[i*9].split(' ')[0]] = list_if[i*9+1].split(':')[1].split(' ')[0]

print dic_result

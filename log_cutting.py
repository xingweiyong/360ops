#coding:utf-8
import time
def log_cut(log_local,targ_local,line_max):
        start_time = time.time()
        index = 0
        line_count = 0
        file = open(targ_local + 'file_' + str(index) + '.txt','a+')
        for line in open(log_local,'r'):
                file.write(line)
                if line_count > line_max:
                        file.close()
                        index += 1
                        file = open(targ_local + 'file_' + str(index) + '.txt','a+')
        file.close()
        end_time = time.time()
        return end_time - start_time
if __name__ == '__main__':
        print log_cut('~/access.log',~/,10000)

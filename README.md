# 360ops
ifconfig_reg
  通过subprocess fork一个执行 ifconfig 的子进程，并通过stdout 属性保存到文件，接着读取该文件，解析出所需的key和value，保存到dic格式变量
log_cutting
  缺点：1.需要单独计算出服务器能够处理的最大文件的行数(line_max)
        2.直接采用readline方式读取，效率可能稍慢，优化的方向可以采用多线程或者迭代器，后续改进。

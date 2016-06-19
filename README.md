# 360ops
password_cache
  要实现远程登录主机不需要重复输入密码的功能，简单的实现方式即是配置ssh信任：
    1.crt远程连上主机
    2.配置hosts文件，vi /etc/hosts
    3.输入ip地址对应
    4.配置ssh 输入ssh-keygen -t rsa 
    5.配置ssh信任 输入 ssh-copy-id 192.168.200.129 回车
  ssh-keygen 生成的 id_rsa及id_rsa.pub文件，id_rsa猜测放在/root/目录下，避免sudo权限的其他人看不到。
ifconfig_reg
  通过subprocess fork一个执行 ifconfig 的子进程，并通过stdout 属性保存到文件，接着读取该文件，解析出所需的key和value，保存到dic格式变量
log_cutting
  缺点：1.需要单独计算出服务器能够处理的最大文件的行数(line_max)
        2.直接采用readline方式读取，效率可能稍慢，优化的方向可以采用多线程或者迭代器，后续改进。

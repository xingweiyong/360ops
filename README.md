# 360ops
ifconfig_reg
  通过subprocess fork一个执行 ifconfig 的子进程，并通过stdout 属性保存到文件，接着读取该文件，解析出所需的key和value，保存到dic格式变量

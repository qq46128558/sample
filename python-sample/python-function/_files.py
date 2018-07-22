#!/usr/bin/env python3

'读写文件操作'
import logging

logging.basicConfig(level=logging.INFO)

# 写文件 model='r'/'w'/'a'/'rb'等
with open('tempfile.txt','w',encoding='utf-8',errors='ignore') as f:
    f.write('让我做你的眼睛，说那样你才看得清\n')
    f.write(r'这首情歌唱给你听，把你当作天上星\n')


# 读文件
with open('tempfile.txt','r',encoding='utf-8',errors='ignore') as f:
    strall=f.read()
    logging.info(strall)
# INFO:root:让我做你的眼睛，说那样你才看得清
# 这首情歌唱给你听，把你当作天上星\n

with open('tempfile.txt','r',encoding='utf-8',errors='ignore') as f:
    for strline in f.readlines():
        logging.info(strline)
# INFO:root:让我做你的眼睛，说那样你才看得清

# INFO:root:这首情歌唱给你听，把你当作天上星\n
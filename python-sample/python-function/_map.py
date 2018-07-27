#!/usr/bin/env python3


'map用法'

import logging
logging.basicConfig(level=logging.INFO)

# 替换list内的指定字符串
mylist=['京口瓜洲一水间,\n钟山只隔数重山\n','春风又绿江南岸,\n明月何时照我还\n']
logging.info(mylist)
# INFO:root:['京口瓜洲一水间,\n钟山只隔数重山\n', '春风又绿江南岸,\n明月何时照我还\n']
mylist=list(map(lambda x:x.replace('\n',''),mylist))
logging.info(mylist)
# INFO:root:['京口瓜洲一水间,钟山只隔数重山', '春风又绿江南岸,明月何时照我还']

# list内的值开方
mylist=[1,3,5,7,9]
logging.info(mylist)
# INFO:root:[1, 3, 5, 7, 9]
mylist=list(map(lambda x:x*x,mylist))
logging.info(mylist)
# INFO:root:[1, 9, 25, 49, 81]

mylist=['京口瓜洲一水间,','钟山只隔数重山,','春风又绿江南岸,','明月何时照我还.']
logging.info("".join(mylist))
# INFO:root:京口瓜洲一水间,钟山只隔数重山,春风又绿江南岸,明月何时照我还.
logging.info(" ".join(map(lambda x:x.replace(',','').replace('.',''),mylist)))
# INFO:root:京口瓜洲一水间 钟山只隔数重山 春风又绿江南岸 明月何时照我还
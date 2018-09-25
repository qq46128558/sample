#!/usr/bin/env python3

'正则表达式'

import logging
import re

logging.basicConfig(level=logging.INFO)

# 精确匹配并提取第一个符合规律的对象(?是非贪婪匹配)
logging.info(re.search(r'(\d+\.?\d*)','130.25平米').group(1))
# INFO:root:130.25

# 正则替换 (\r光标回到0位,\n换行)
s='a\nb\r\nc'
logging.info(s.encode())
# INFO:root:b'a\nb\r\nc'
s=re.sub("\n|\r\n",'',s)
logging.info(s.encode())
# INFO:root:b'abc'
'遗留问题: 暂未知如何只匹配\n而不匹配\r\n'
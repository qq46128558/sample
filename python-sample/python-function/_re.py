#!/usr/bin/env python3

'正则表达式'

import logging
import re

logging.basicConfig(level=logging.INFO)

# 精确匹配并提取第一个符合规律的对象
logging.info(re.search(r'(\d+\.?\d*)','130.25平米').group(1))
# INFO:root:130.25
# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))

sys.path.append(PATH)
# execute(["scrapy","crawl","jobbole"])
# execute(["scrapy","crawl","zhihu"])
# execute(["scrapy","crawl","zhongtu"])
execute(["scrapy","crawl","bilibili"])
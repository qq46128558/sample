
# Scrapy 的每个 Item （条目）对象表示网站上的一个页面。当然，你可以根据需要定义不同的条目（比如 url 、 content 、 header image 等），但是现在我只演示收集每页的 title 字段（field）。

from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

# Module `scrapy.contrib.spiders` is deprecated, use `scrapy.spiders` instead
# from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

# class ArticleSpider(Spider):
class ArticleSpider(CrawlSpider):
    # scrapy crawl article
    name="article"
    allowed_domains=["en.wikipedia.org"]
    # 爬虫先进入 start_urls 里面的两个页面，收集信息，然后停止
    # start_urls=["http://en.wikipedia.org/wiki/Main_Page","http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    start_urls=["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    # 为了让爬虫更加完善，你需要定义一些规则让 Scrapy 可以在每个页面查找 URL 链接：
    rules=[Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item",follow=True)]

    # def parse(self,response):
    #     # Scrapy 用 Item 对象决定要从它浏览的页面中提取哪些信息。
    #     item=Article()
    #     title=response.xpath('//h1/text()')[0].extract()
    #     print("Title is: "+title)
    #     item['title']=title
    #     return item
    
    # 虽然这个爬虫和前面那个爬虫的启动命令一样，但是如果你不用 Ctrl+C 中止程序，它是不会停止的（很长时间也不会停止）
    def parse_item(self,response):
        # ItemMeta’ object does not support item assignment.原来是是在初始化item对象是忘了在类名后加()
        item=Article()
        ''' IndexError: list index out of range 未解决 '''
        title=response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title']=title
        return item

# Scrapy 支持用不同的输出格式来保存这些信息，比如 CSV、JSON 或 XML 文件格式，对应命令如下所示：
# $ scrapy crawl article -o articles.csv -t csv
# $ scrapy crawl article -o articles.json -t json
# $ scrapy crawl article -o articles.xml -t xml
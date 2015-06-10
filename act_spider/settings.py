# Scrapy settings for act_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'remos_spider'

SPIDER_MODULES = ['act_spider.spiders']
NEWSPIDER_MODULE = 'act_spider.spiders'
LOG_LEVEL='ERROR'
ITEM_PIPELINES = ['act_spider.pipelines.MyImagesPipeline','act_spider.pipelines.ActSpiderPipeline']
IMAGES_STORE = './'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'act_spider (+http://www.yourdomain.com)'

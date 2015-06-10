from scrapy.spider import Spider 
from scrapy.selector import Selector
from act_spider.items import ActSpiderItem
from scrapy.http.request import Request
class ActSpider(Spider):
	name="remos_spider"
	allowed_domains=['ligasanmiguel.com']
	start_urls=['http://www.ligasanmiguel.com/clubes/plantilla.php?id=es&c=9#.VXhEwBPtmko']
	BASE="http://www.ligasanmiguel.com/"
	def parse(self, response):
		sel=Selector(response)
		team_name = sel.xpath('//*[@id="col-a"]/div/section/div[1]/header/h2/text()').extract().pop()
		team_logo = sel.xpath('//*[@id="ruta"]/div/img/@src').extract().pop()
		remeros = sel.xpath('//*[@id="col-a"]/div/section/ul[1]/li/span')
		for remero in remeros:
			item=ActSpiderItem()
			item['remo_type'] = remero.xpath('span[1]/span[1]/text()').extract().pop()
			item['image_urls'] = [self.BASE+remero.xpath('span[2]/img/@src').extract().pop(),self.BASE+team_logo]
			item['name'] = remero.xpath('span[3]/span[1]/text()').extract().pop()
			item['surname'] = remero.xpath('span[3]/span[2]/text()').extract().pop()
			item['birth_date'] = remero.xpath('span[3]/span[6]/text()').extract().pop()
			item['team_name'] = team_name
			yield item

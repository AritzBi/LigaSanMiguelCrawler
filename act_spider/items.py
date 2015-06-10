# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ActSpiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    team_name = Field()
    team_logo= Field()
    name = Field()
    surname = Field()
    birth_date = Field()
    remo_type = Field()
    image_urls = Field()
    image_paths= Field()
    pass

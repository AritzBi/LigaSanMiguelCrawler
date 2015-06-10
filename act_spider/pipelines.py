# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http.request import Request
import json
from os.path import isfile
#Proceso que se encarga de obtener el item descargar la imagen y pasar el item a ActSpiderPipeline
class MyImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		item['image_paths'] ="Item contains no images"
		if 'image_urls' in item:
			for image_url in item['image_urls']:
				yield Request(image_url)
	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			item['image_paths'] ="Item contains no images"
		else:
			item['image_paths'] = image_paths
		return item

class ActSpiderPipeline(object):
	#Proceso que obtiene el item y lo mete en el Json
	def process_item(self, item, spider):
		file_name = item['team_name']+'.json'
		if isfile(file_name):
			with open(file_name, 'r') as f:
				data = json.load(f)
		else:
			data = {}
			data['team_name'] = item['team_name']
			data['team_logo'] = item['image_paths'][1]
			data['remeros'] = []
			data['patrones'] = []
		if "Remero" in item['remo_type']:
			remero = {}
			remero['name'] = item['name']
			remero['surname'] = item['surname']
			remero['birthdate'] = item['birth_date']
			remero['image'] = item['image_paths'][0]
			remero['potencia'] = 0
			remero['energia'] = 100
			remero['experiencia'] = 0
			remero['buena_mar'] = 0
			remero['mala_mar'] = 0
			lesionado = False
			data['remeros'].append(remero)
		else :
			patron = {}
			patron['name'] = item['name']
			patron['surname'] = item['surname']
			patron['birthdate'] = item['birth_date']
			patron['image'] = item['image_paths'][0]
			patron['experiencia'] = 0
			patron['buena_mar'] = 0
			patron['mala_mar'] = 0
			patron['liderazgo'] = 0
			patron['lesionado'] = 0
			data['patrones'].append(patron)

		with open(file_name, 'w') as outfile:
			json.dump(data, outfile)
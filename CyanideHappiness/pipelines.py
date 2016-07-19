# -*- coding: utf-8 -*-
from scrapy.contrib.pipeline.images import ImagesPipeline

class CyanideHappinessPipeline(ImagesPipeline):
	def image_key(self, url):
		image_guid = url.split('/')[5].split('?')[0].split('.')[0]		
		print url
		return 'full/%s.jpg' % (image_guid)

    

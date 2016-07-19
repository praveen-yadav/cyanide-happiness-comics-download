# -*- coding: utf-8 -*-

BOT_NAME = 'CyanideHappiness'

SPIDER_MODULES = ['CyanideHappiness.spiders']
NEWSPIDER_MODULE = 'CyanideHappiness.spiders'


FEED_URI = 'logs/%(name)s/%(time)s.csv'
FEED_FORMAT = 'csv'

IMAGES_STORE = 'images/'
#IMAGES_EXPIRES = 90  # 90 days of delay for image expiration


ITEM_PIPELINES = {	
	'CyanideHappiness.pipelines.CyanideHappinessPipeline': 100,
}


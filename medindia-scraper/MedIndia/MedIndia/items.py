# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MedindiaItem(scrapy.Item):
    # define the fields for your item here like:
    drugName = scrapy.Field()
    drugForm = scrapy.Field()
    drugGenericName = scrapy.Field()
    price = scrapy.Field()
    dosage = scrapy.Field()
    basicInfo = scrapy.Field()
    conditions = scrapy.Field()
    sideEffects = scrapy.Field()
    dosageInfo = scrapy.Field()
    howToTake = scrapy.Field()
    contraindications = scrapy.Field()
    warningsAndPrecautions = scrapy.Field()
    otherPrecautions = scrapy.Field()
    StorageConditions = scrapy.Field()



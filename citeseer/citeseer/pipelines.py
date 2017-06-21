# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from citeseer import settings

class WriteToCsv(object):
	@classmethod
	
	def process_item(self, item, spider):
		self.file = open(settings.csv_file_path, 'ab+')
		self.exporter = CsvItemExporter(self.file, include_headers_line=False)
		self.exporter.fields_to_export = settings.csv_export_fields
		self.exporter.export_item(item)
		return item

class CiteseerPipeline(object):
    def process_item(self, item, spider):
        return item

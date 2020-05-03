# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class QotetutorialPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        self.db = self.conn['quotes_db']
        self.collection = self.db['quotes_tb']

    def create_connection_sql(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table_sql(self):
        self.curr.execute("""drop table if exists quotes""")
        self.curr.execute("""create table quotes(
                        title text,
                        author text,
                        tags text
                        )""")

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def store_in_db_sql(self, item):
        self.curr.execute("""insert into quotes values (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.conn.commit()

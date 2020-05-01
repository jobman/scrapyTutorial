# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class QotetutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists quotes""")
        self.curr.execute("""create table quotes(
                        title text,
                        author text,
                        tags text
                        )""")

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.curr.execute("""insert into quotes values (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.conn.commit()

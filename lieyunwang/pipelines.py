# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import xlwt


# 注意在循环外面创建工作簿
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')

# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

row = 0

class LieyunwangPipeline(object):
    # def open_spider(self, spider):
    #     self.f = open("lieyun.json", "w", encoding="utf-8")
    #     pass

    def process_item(self, item, spider):
        # self.f.write(json.dumps(dict(item), ensure_ascii=False) + ",\n")
        # self.f.flush()

        global row

        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(row, 0, label=item['imgsrc'])
        worksheet.write(row, 1, label = item['imgalt'])
        worksheet.write(row, 2, label = item['time'])


        # 保存
        workbook.save('Excel_test.xls')

        row += 1

        return item

    # def close_spider(self, spider):
    #     self.f.close()





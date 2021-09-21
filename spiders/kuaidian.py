# -*- coding: utf-8 -*-
"""
Created on 2021-09-18 01:29:07
---------
@summary:
---------
@author: 86155
"""

import feapder


class Kuaidian(feapder.BatchSpider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    __custom_setting__ = dict(
        REDISDB_IP_PORTS="localhost:6379",
        REDISDB_USER_PASS="",
        REDISDB_DB=0,
        MYSQL_IP="localhost",
        MYSQL_PORT=3306,
        MYSQL_DB="test_db",
        MYSQL_USER_NAME="root",
        MYSQL_USER_PASS="",
    )

    def start_requests(self, task):
        id,url = task
        yield feapder.Request('http://121.5.144.95:8085/?max_cursor=0&user_id=',task_id= id)

    def parse(self, request, response):
        print(response)
        yield self.update_task_batch(request.task_id, 1)

if __name__ == "__main__":
    spider = Kuaidian(
        redis_key="feapder:spider_test",  # redis中存放任务等信息的根key
        task_table="batch_spider_task",  # mysql中的任务表
        task_keys=["id", "url"],  # 需要获取任务表里的字段名，可添加多个
        task_state="state",  # mysql中任务状态字段
        batch_record_table="xxx_batch_record",  # mysql中的批次记录表
        batch_name="快电每小时任务实际服务器接口测试任务",  # 批次名字
        batch_interval=1/24/12,  # 批次周期 天为单位 若为小时 可写 1 / 24
    )

    spider.start_monitor_task() # 下发及监控任务
    spider.start() # 采集

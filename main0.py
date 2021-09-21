from spiders import *
from feapder import ArgumentParser


def crawl_test(args):
    spider = kuaidian.Kuaidian(
        redis_key="feapder:spider_test",  # redis中存放任务等信息的根key
        task_table="batch_spider_task",  # mysql中的任务表
        task_keys=["id", "url"],  # 需要获取任务表里的字段名，可添加多个
        task_state="state",  # mysql中任务状态字段
        batch_record_table="xxx_batch_record",  # mysql中的批次记录表
        batch_name="快电每小时任务实际服务器接口测试任务",  # 批次名字
        batch_interval=1 / 24 ,  # 批次周期 天为单位 若为小时 可写 1 / 24
    )

    if args == 1:
        spider.start_monitor_task()  # 下发及监控任务
    else:
        spider.start()  # 采集

if __name__ == "__main__":

    parser = ArgumentParser(description="批次爬虫测试")

    parser.add_argument(
        "--crawl_test", type=int, nargs=1, help="BatchSpider demo(1|2）", function=crawl_test
    )

    parser.start()
    # python .\main0.py --crawl_test 1

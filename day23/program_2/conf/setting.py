import logging
import os

user_db = 'C:/Users/Administrator/Desktop/PycharmProjects/python_camp/day_23/program_2/db/user_db.pk'


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DB = os.path.join(BASE_DIR, 'db')
BASE_LOG = os.path.join(BASE_DIR, 'log')

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(BASE_LOG):
    os.mkdir(BASE_LOG)

# log文件的全路径
logfile_path = os.path.join(BASE_LOG, 'log.log')

logging.basicConfig(filename=logfile_path,
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)
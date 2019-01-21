import logging
import os

manager_db = 'C:/Users/Administrator/Desktop/python_programming_camp/day18_v2/db/manager_message.pk'
teacher_db = 'C:/Users/Administrator/Desktop/python_programming_camp/day18_v2/db/teacher_message.pk'
student_db = 'C:/Users/Administrator/Desktop/python_programming_camp/day18_v2/db/student_message.pk'
school_message_db = 'C:/Users/Administrator/Desktop/python_programming_camp/day18_v2/db/school_message.pk'


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
# logging.info(user + ' Cash withdrawal ' + str(input_cash))

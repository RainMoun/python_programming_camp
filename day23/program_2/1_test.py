from lib_day23_program_2 import common
from db import db_handler

user_1 = common.User('Kobe', '123456', ('127.0.0.1', 8081), ['James'], {'1': ['James', 'Wade']})
user_2 = common.User('James', '123456', ('127.0.0.1', 8082), ['Kobe'], {'1': ['Kobe', 'Wade']})
user_3 = common.User('Wade', '123456', ('127.0.0.1', 8083), ['Kobe'], {'1': ['Kobe', 'James']})
db_handler.create_user(user_1)
db_handler.create_user(user_2)
db_handler.create_user(user_3)

# 求出即报名python又报名ai课程的学员名字集合
pythons = {'albert', '孙悟空', '周星驰', '朱茵', '林志玲'}
ais = {'猪八戒', '郭德纲', '林忆莲', '周星驰'}
print(pythons & ais)
# 求出所有报名的学生名字集合
print(pythons | ais)
# 求出只报名python课程的学员名字
print(pythons - ais)
# 求出没有同时这两门课程的学员名字集合
print(pythons ^ ais)
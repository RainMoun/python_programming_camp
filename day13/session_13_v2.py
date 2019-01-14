import json
class Student:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def print_all_score(self):
        if self.score:
            for i in self.score:
                print("课程：{}  分数为：{}".format(i, self.score[i]))
        else:
            print("sorry, no score")

    def get_score(self, discipline):
        if discipline in self.score.keys():
            return self.score[discipline]
        else:
            return None


def someone_score(input_name):
    print("Name: {}".format(input_name))
    if input_name in std_lst.keys():
        std_lst[input_name].print_all_score()


def everybody_subject_score(subject):
    for j in std_lst:
        if std_lst[j].get_score(subject):
            print("Name: {}, {} score: {}".format(std_lst[j].name, subject, std_lst[j].get_score(subject)))
        else:
            print("Name: {}, {} score: Not recorded".format(std_lst[j].name, subject))


def total_average_score(subject):
    sum_score = []
    for j in std_lst:
        if std_lst[j].get_score(subject):
            sum_score.append(std_lst[j].get_score(subject))
    print("Subject {} average score: {}".format(subject, sum(sum_score) / len(sum_score)))


def somebody_subject_score(input_name, subject):
    print("Name: {}, subject {} score: {}".format(input_name, subject
                                                  , std_lst[input_name].score[subject]))


def delete_somebody(name):
    std_lst.pop(name)


def performing_operations():
    operate = [-1, "查询学生所有成绩", "查看所有人某科目成绩", "查看所有人某科目平均分", "查看某人某科目成绩",
               "删除某位学生信息", "退出"]
    print("请选择您所要执行的操作编号：")
    for i in range(1, len(operate)):
        print("{}. {}。".format(i, operate[i]))
    input_operate = int(input())
    if input_operate == 6:
        return 0
    else:
        if input_operate == 1:
            input_name = input("请输入查询学生姓名：")
            someone_score(input_name)
        elif input_operate == 2:
            input_subject = input("请输入查询科目名字：")
            everybody_subject_score(input_subject)
        elif input_operate == 3:
            input_subject = input("请输入查询科目名字：")
            total_average_score(input_subject)
        elif input_operate == 4:
            input_name = input("请输入查询学生姓名：")
            input_subject = input("请输入查询科目名字：")
            somebody_subject_score(input_name, input_subject)
        elif input_operate == 5:
            input_name = input("请输入删除学生姓名：")
            delete_somebody(input_name)
        return 1


if __name__ == '__main__':
    # 初始定义部分
    with open('student_score.json') as f:
        std_score = json.load(f)
    std_lst = {}
    for i in std_score:
        std_obj = Student(i)
        std_obj.score = std_score[i]
        std_lst[i] = std_obj
    print("欢迎使用学生成绩管理系统：")
    tag = 1
    while tag:
        tag = performing_operations()
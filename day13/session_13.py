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


if __name__ == '__main__':
    # 初始定义部分
    std1 = Student("Kobe")
    std1.score['shoot'] = 95
    std1.score['no_pass_look'] = 100
    std1.score['pass'] = 50
    std2 = Student("James")
    std2.score['shoot'] = 90
    std2.score['pass'] = 90
    std2.score['rebound'] = 90
    std_lst = {"Kobe": std1, "James": std2}
    # 根据姓名查看所有成绩
    someone_score("Kobe")
    print("###########################################################################")
    # 查看所有人的某学科成绩
    everybody_subject_score("shoot")
    print("###########################################################################")
    # 查看总平均分
    total_average_score("shoot")
    print("###########################################################################")
    # 查看某人学科成绩
    selected_name = "Kobe"
    selected_subject = "no_pass_look"
    print("Name: {}, subject {} score: {}".format(selected_name, selected_subject
                                                  , std_lst[selected_name].score[selected_subject]))
    print("###########################################################################")
    # 根据姓名删除学生
    delete_name = "James"
    std_lst.pop(delete_name)
    for k in std_lst:
        print(k)

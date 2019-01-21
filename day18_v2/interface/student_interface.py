from db import db_handler


def query_score(school, teacher, course, user_data):
    try:
        school_message = db_handler.select('4')
        for i in school_message:
            if i.name == school:
                selected_school = i
        return selected_school.teachers[teacher].courses[course].students[user_data['name']]
    except KeyError:
        print('无对应信息')
        return None
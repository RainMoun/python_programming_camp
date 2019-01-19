# -*- coding: utf-8 -*-
import pickle
import os

from conf import settings


def read_school():
    if os.path.getsize(settings.school_db) > 0:
        with open(settings.school_db, 'rb') as f:
            school_lst = pickle.load(f)
        return school_lst
    else:
        return None


def save_school(school_data):
    with open(settings.school_db, "wb") as f:
        pickle.dump(school_data, f, -1)
        f.close()


def read_class():
    if os.path.getsize(settings.class_db) > 0:
        with open(settings.class_db, 'rb') as f:
            class_lst = pickle.load(f)
        return class_lst
    else:
        return None


def save_class(class_data):
    with open(settings.class_db, "wb") as f:
        pickle.dump(class_data, f, -1)
        f.close()


def read_score():
    if os.path.getsize(settings.score_db) > 0:
        with open(settings.score_db, 'rb') as f:
            score_lst = pickle.load(f)
        return score_lst
    else:
        return None


def save_score(score_data):
    with open(settings.score_db, "wb") as f:
        pickle.dump(score_data, f, -1)
        f.close()




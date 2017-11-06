# populate dummy data by using Faker

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','erm_proj.settings')
# この意味は？？ 下の setup() 用だろうけど

import django
django.setup()

## FAKE POPULATION

import random
from erma_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakerobj = Faker()
#
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]  #よくわからんがタプルの先頭
    t.save()
    return t

    # 理屈から行くと数が少ないと topics がすべて入るわけではない

def populate(Num=10):
    for entry in range(Num):
        cur_topic = add_topic()
        cur_url = fakerobj.url()
        cur_date = fakerobj.date()
        cur_name = fakerobj.company()

        ## ForeignKey のところはオブジェクトを渡す
        webpage_row = Webpage.objects.get_or_create(topic=cur_topic, url=cur_url, name=cur_name)[0]
        ## ForeignKey のところはオブジェクトを渡す
        acc_record_row = AccessRecord.objects.get_or_create(name=webpage_row, date=cur_date)[0]

        # ↓これはいらんのか
        # webpage_row.save()
        # acc_record_row.save()


if __name__ == '__main__':
    print("polulating dummy data")
    populate(30)
    print("polulation completed")

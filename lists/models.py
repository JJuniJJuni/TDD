from django.db import models

# Create your models here.


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default=" ")
    # 새로운 필드(Column)을 생성 할 때 마다 'makemigration' 실행
    # 만약 매개변수로 default 값 안주면, 줄거냐고 커맨드 창에서 물어봄
    list = models.ForeignKey(List, default=None)



import os
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name=models.CharField(max_length=80)

    class Meta:
        abstract=True

    def __str__ (self):
        return self.name

class RoomType(AbstractItem):
    # 데이터베이스에 다른 타입이 들어감
    pass

class Room(core_models.TimeStampedModel):
    """ Room Model Definition """
    
    # 필수 입력 사항 : blank=True, null=True 생략
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price=models.IntegerField()
    address=models.CharField(max_length=140)
    guests=models.IntegerField()
    beds=models.IntegerField()
    bedrooms=models.IntegerField()
    baths=models.IntegerField()
    check_in=models.TimeField() # TimeField = 0시 ~ 24시
    check_out=models.TimeField()
    instant_book=models.BooleanField(default=False)
    host=models.ForeignKey(user_models.User, on_delete=models.CASCADE) # users와 연결
    room_type=models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
    pass
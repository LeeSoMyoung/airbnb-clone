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
    """Room Type Object Definition"""

    class Meta:
        verbose_name="Roome Type"
       # ordering=["-created"]
    pass

class Amenity(AbstractItem):
    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural="Amenities"
    pass

class Facility(AbstractItem):
    """Facility Model Definiton"""

    class Meta:
            verbose_name_plural="Facilities"
    pass

class HouseRule(AbstractItem):
    """House Rule Model Definition"""

    class Meta:
        verbose_name="House Rule"
    pass

class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""
    caption = models.CharField(max_length=80)
    file=models.ImageField()
    room=models.ForeignKey("Room",on_delete=models.CASCADE)
    def __str__(self):
        return self.caption

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
    room_type=models.ForeignKey(RoomType, on_delete=models.SET_NULL,null=True)
    amenities=models.ManyToManyField(Amenity,blank=True)
    facilities=models.ManyToManyField(Facility, blank=True)
    rules=models.ManyToManyField(HouseRule,blank=True)

    def __str__(self):
        return self.name
    pass
from django.db import models


class Music(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=64, verbose_name="곡")
    description = models.CharField(max_length=64, verbose_name="가수")
    banner_image = models.ImageField(
        upload_to="%Y/%m/%d", verbose_name="이미지", blank=True)

    class Meta:
        db_table = 'music'
        verbose_name = '김소정이 좋아하는 음악'
        verbose_name_plural = '김소정이 좋아하는 음악'


class Location(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=64, verbose_name="장소")
    description = models.CharField(max_length=64, verbose_name="위치")
    banner_image = models.ImageField(
        upload_to="%Y/%m/%d", verbose_name="이미지", blank=True)

    class Meta:
        db_table = 'location'
        verbose_name = '김소정이 좋아하는 맛집'
        verbose_name_plural = '김소정이 좋아하는 맛집'


class Hobby(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=64, verbose_name="취미")
    banner_image = models.ImageField(
        upload_to="%Y/%m/%d", verbose_name="이미지", blank=True)

    class Meta:
        db_table = 'hobby'
        verbose_name = '김소정이 좋아하는 취미'
        verbose_name_plural = '김소정이 좋아하는 취미'

class Me(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=64, verbose_name="찍은 장소")
    description = models.CharField(max_length=64, verbose_name="컨셉")
    banner_image = models.ImageField(
        upload_to="%Y/%m/%d", verbose_name="이미지", blank=True)

    class Meta:
        db_table = 'me'
        verbose_name = '김소정이 담겨있는 사진'
        verbose_name_plural = '김소정이 담겨있는 사진'

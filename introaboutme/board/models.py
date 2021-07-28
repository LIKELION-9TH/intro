from django.db import models


class Music(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=64, verbose_name="제목")
    description = models.CharField(max_length=64, verbose_name="설명")
    banner_image = models.ImageField(
        upload_to="%Y/%m/%d", verbose_name="이미지", blank=True)

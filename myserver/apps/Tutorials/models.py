from datetime import datetime

from django.db import models

# Create your models here.


class TutorialsTeacher(models.Model):
    """
    教程老师
    """
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    imageUrl = models.CharField(default="", max_length=300, verbose_name="教师图片", help_text="教师图片")
    desc = models.TextField(default="", verbose_name="教师描述", help_text="教师描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TutorialsVedio(models.Model):
    """
    商品
    """
    teacher = models.ForeignKey(TutorialsTeacher, verbose_name="教程老师")
    name = models.CharField(max_length=100, verbose_name="教程名")
    htmlString = models.TextField(max_length=2000,verbose_name="视频地址的Html")
    click_num = models.IntegerField(default=1000, verbose_name="点击数")
    fav_num = models.IntegerField(default=10, verbose_name="收藏数")
    video_front_image = models.CharField(default="", max_length=300, verbose_name="视频封面", help_text="视频封面")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




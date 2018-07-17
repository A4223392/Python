from django.db import models

from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

member_type = (
    ('管理員', '管理員'),
    ('一般會員', '一般會員'),
    ('贊助商', '贊助商'),
)

class Member(AbstractUser):
    id = models.AutoField(primary_key=True,verbose_name='會員代號')
    account = models.EmailField(unique=True, max_length=50,verbose_name='帳號')
    identifier = models.CharField(max_length=22,verbose_name='會員識別碼')
    membertype = models.CharField(max_length=128, choices=member_type, verbose_name='會員類別', default='')    
    name = models.CharField(max_length=20,verbose_name='姓名')
    nickname = models.CharField(max_length=20, blank=True, null=True,verbose_name='暱稱')
    password = models.CharField(max_length=128,verbose_name='密碼')
    localpicture = models.ImageField(max_length=64, blank=True, null=True,verbose_name='本機照片')
    dbpicture = models.ImageField(max_length=64, blank=True, null=True,verbose_name='資料庫照片')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')

    class Meta(AbstractUser.Meta):
        db_table = 'mbr_member'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = '會員資訊'
        verbose_name_plural=verbose_name

class Membertype(AbstractUser):
    membertype_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10,default='member')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')
    class Meta(AbstractUser.Meta):
        db_table = 'sys_membertype'
        verbose_name = '會員類型'
        verbose_name_plural=verbose_name
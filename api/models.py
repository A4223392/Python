from django.db import models

from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


# Create your models here.

'''
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

'''

class Member(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='會員代號')
    account = models.EmailField(unique=True, max_length=50,verbose_name='帳號',help_text='你的電子信箱')
    identifier = models.CharField(max_length=22,verbose_name='會員識別碼')
    membertype = models.ForeignKey('Membertype',on_delete = models.DO_NOTHING,verbose_name='會員類型代號')
    name = models.CharField(max_length=20,verbose_name='姓名',blank=True)
    nickname = models.CharField(max_length=20, blank=True, null=True,verbose_name='暱稱')
    password = models.CharField(max_length=128,verbose_name='密碼',blank=True)
    localpicture = models.CharField(max_length=64, blank=True, null=True,verbose_name='本機照片')
    dbpicture = models.CharField(max_length=64, blank=True, null=True,verbose_name='資料庫照片')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')

    class Meta:
        db_table = 'mbr_member' 

class Membertype(models.Model):
    membertype_id = models.IntegerField(primary_key=True,verbose_name='會員類型代號')
    name = models.CharField(max_length=10,verbose_name='類型名稱')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')

    class Meta:
        db_table = 'sys_membertype'
        
 

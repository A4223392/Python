from django.db import models

from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class Member(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='會員代號')
    account = models.EmailField(unique=True, max_length=50,verbose_name='帳號',help_text='你的電子信箱')
    identifier = models.CharField(max_length=22,verbose_name='會員識別碼')
    membertype = models.ForeignKey('Membertype',on_delete=models.DO_NOTHING,default=2)    
    name = models.CharField(max_length=20,verbose_name='姓名',blank=True)
    nickname = models.CharField(max_length=20, blank=True, null=True,verbose_name='暱稱')
    password = models.CharField(max_length=128,verbose_name='密碼',blank=True)
    localpicture = models.ImageField(max_length=64, blank=True, null=True,verbose_name='本機照片')
    dbpicture = models.ImageField(max_length=64, blank=True, null=True,verbose_name='資料庫照片')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間') 
    friendship = models.ManyToManyField('self',through='FriendShip',symmetrical=False)     

    class Meta:
        db_table = 'mbr_member' 

class Membertype(models.Model):
    membertype_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10,default='member')
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')

    class Meta:
        db_table = 'sys_membertype'


class FriendShip(models.Model):    
    member_id = models.ForeignKey(Member,db_column='member_id',null=True,on_delete=models.CASCADE,verbose_name='會員代號',related_name='membership_member_id')
    friend_id = models.ForeignKey(Member,db_column='friend_id',null=True,on_delete=models.CASCADE,verbose_name='好友代號',related_name='membership_friend_id')
    nickname = models.CharField(max_length=20,null=True)
    renew_time = models.DateTimeField(default=timezone.now,verbose_name='更新時間')

    class Meta:
        db_table = 'mbr_friendship'
        verbose_name = '好友'      
        unique_together = (('member_id','friend_id'),)  #指定兩個欄位合成一個唯一鍵(類似主鍵))
       
 

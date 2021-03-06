# Generated by Django 2.0.7 on 2018-07-23 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Membertype', verbose_name='會員類型代號'),
        ),
        migrations.AlterField(
            model_name='member',
            name='renew_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新時間'),
        ),
    ]

# Generated by Django 4.2.19 on 2025-03-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, '待启动'), (2, '制作中'), (3, '已完成')], help_text='订单状态', verbose_name='订单状态'),
        ),
    ]

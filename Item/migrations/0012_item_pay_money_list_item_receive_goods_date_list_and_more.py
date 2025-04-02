# Generated by Django 4.2.3 on 2025-04-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0011_item_packing_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pay_money_list',
            field=models.JSONField(default=list, help_text='付款', verbose_name='付款'),
        ),
        migrations.AddField(
            model_name='item',
            name='receive_goods_date_list',
            field=models.JSONField(default=list, help_text='收货日期列表', verbose_name='收货日期列表'),
        ),
        migrations.AddField(
            model_name='item',
            name='send_goods_date_list',
            field=models.JSONField(default=list, help_text='发货日期列表', verbose_name='发货日期列表'),
        ),
    ]

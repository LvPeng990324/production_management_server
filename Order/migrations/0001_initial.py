# Generated by Django 4.2.19 on 2025-02-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(help_text='订单号', max_length=32, verbose_name='订单号')),
                ('order_status', models.IntegerField(choices=[(1, '待处理'), (2, '同意'), (3, '拒绝')], help_text='订单状态', verbose_name='订单状态')),
                ('order_start_time', models.DateTimeField(help_text='订单开始时间', verbose_name='订单开始时间')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
    ]

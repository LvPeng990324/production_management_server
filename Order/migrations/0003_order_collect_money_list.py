# Generated by Django 4.2.3 on 2025-04-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='collect_money_list',
            field=models.JSONField(default=list, help_text='收款列表', verbose_name='收款列表'),
        ),
    ]

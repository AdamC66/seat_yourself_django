# Generated by Django 2.2.3 on 2019-08-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20190203_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='last_res_time',
            field=models.TimeField(null=True),
        ),
    ]

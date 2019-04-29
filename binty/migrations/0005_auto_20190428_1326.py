# Generated by Django 2.0.5 on 2019-04-28 04:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('binty', '0004_auto_20190428_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 26, 4, 922611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 26, 4, 925813, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='director',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 26, 4, 922157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 26, 4, 921638, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.0.5 on 2019-04-20 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('binty', '0002_auto_20190415_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 10, 20, 35, 653023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 10, 20, 35, 653745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='director',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 10, 20, 35, 652697, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 10, 20, 35, 652362, tzinfo=utc)),
        ),
    ]

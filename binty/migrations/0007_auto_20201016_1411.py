# Generated by Django 2.0.5 on 2020-10-16 05:11

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('binty', '0006_auto_20201015_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 5, 11, 54, 687277, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 5, 11, 54, 691089, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='content',
            name='user',
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='director',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 5, 11, 54, 686689, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 5, 11, 54, 686072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 5, 11, 54, 693601, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.0.5 on 2019-04-28 04:25

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('binty', '0003_auto_20190420_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='goods',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='イイね！'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 25, 0, 360378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 25, 0, 363714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='director',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 25, 0, 359973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 4, 25, 0, 359550, tzinfo=utc)),
        ),
    ]

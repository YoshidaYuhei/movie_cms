# Generated by Django 2.0.5 on 2020-10-15 11:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('binty', '0005_auto_20190428_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 58, 48, 475386, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='user',
            name='good',
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cast',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 58, 48, 466854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='awards',
            field=models.CharField(max_length=200, null=True, verbose_name='アワード'),
        ),
        migrations.AlterField(
            model_name='content',
            name='country',
            field=models.CharField(max_length=100, verbose_name='製作国'),
        ),
        migrations.AlterField(
            model_name='content',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='再生時間'),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 58, 48, 472411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='サムネイル'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='director',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 58, 48, 466072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 58, 48, 465344, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='goods',
            name='Content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binty.Content'),
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

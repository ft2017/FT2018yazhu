# Generated by Django 2.0.1 on 2018-01-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180109_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazhu',
            name='work_by',
            field=models.CharField(default='.', max_length=50),
        ),
    ]

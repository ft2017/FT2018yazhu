# Generated by Django 2.0.2 on 2018-03-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20180306_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jitai',
            name='jitai_id',
            field=models.CharField(default='.', max_length=2000),
        ),
    ]

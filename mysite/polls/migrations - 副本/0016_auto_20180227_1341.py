# Generated by Django 2.0.2 on 2018-02-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_jitai_jitai_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jitai',
            name='jitai_id',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 2.0.2 on 2018-02-27 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180227_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jitai',
            name='jitai_id',
        ),
        migrations.AlterField(
            model_name='yazhu',
            name='work_mach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Jitai'),
        ),
    ]

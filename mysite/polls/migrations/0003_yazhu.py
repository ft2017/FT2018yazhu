# Generated by Django 2.0.1 on 2018-01-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='yazhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateTimeField(verbose_name='date published')),
                ('work_prod', models.CharField(default='.', max_length=50)),
                ('work_mach', models.CharField(default='.', max_length=50)),
            ],
        ),
    ]
from django.db import models

# Create your models here.
import datetime
from django.utils import timezone




# class Reject(models.Model):
#     yazhu = models.ForeignKey(Yazhu, on_delete=models.CASCADE)
#     reject_name = models.CharField(max_length=200)
#     reject_qty = models.IntegerField(default=0)
#     def __str__(self):
#         return self.reject_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.CharField(max_length=500, default='.')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Jitai(models.Model):
    jitai_id = models.CharField(max_length=2000, default='.')
    # jitai_description = models.CharField(max_length=500, default='.')
    def __str__(self):
        return self.jitai_id

class Information(models.Model):
    CATEGORY_CHOICES = (
            ('A组',u'A组'),
            ('B组',u'B组'),
            )
    group = models.CharField('组别',max_length=50, choices = CATEGORY_CHOICES)
    empe_id = models.CharField('工号',max_length=2000, default='.')
    empe_name = models.CharField('姓名',max_length=2000, default='.')
    empe_dept = models.CharField('部门',max_length=2000, default='.')
    tel = models.CharField('手机号码',max_length=2000, default='.')
    # jitai_description = models.CharField(max_length=500, default='.')
    def __str__(self):
        return self.group
# class JitaiXX(models.Model):
#     jitaixx_id = models.CharField(max_length=2000, default='.')
#     # jitai_description = models.CharField(max_length=500, default='.')
#     def __str__(self):
#         return self.jitaixx_id


class Yazhu(models.Model):
    # dev_datetime = models.DateTimeField('date published')

    work_date = models.DateField('date published')
    work_prod = models.CharField('产品',max_length=50, default='.')
    # CATEGORY_CHOICES = (
    #         ('50201-000062',u'10T液压切边机2（压二课）'),
    #         )
    # work_mach = models.CharField('机台',max_length=50, choices = CATEGORY_CHOICES)
    work_mach = models.ForeignKey(Jitai, on_delete=models.CASCADE)
    work_by = models.CharField('操作员',max_length=50, default='.')
    work_support = models.CharField('技术员',max_length=50, default='.')
    work_leader = models.CharField('班组长',max_length=50, default='.')
    work_qtyall = models.CharField('数量',max_length=50, default='.')
    work_qtyok = models.CharField('良品数量',max_length=50, default='.')
    work_rej = models.CharField('不良数量',max_length=50, default='.')
    work_rejper = models.CharField('不良率',max_length=50, default='.')
    rej01=models.IntegerField('欠铸',default=0)
    rej02=models.IntegerField('沙孔',default=0)
    rej03=models.IntegerField('气泡',default=0)
    rej04=models.IntegerField('拉伤',default=0)
    rej05=models.IntegerField('冲蚀',default=0)
    rej06=models.IntegerField('表面裂纹',default=0)
    rej07=models.IntegerField('顶针凹/凸',default=0)
    rej08=models.IntegerField('变形',default=0)
    rej09=models.IntegerField('毛刺',default=0)
    rej10=models.IntegerField('尺寸不良',default=0)
    rej11=models.IntegerField('其他',default=0)
    def __str__(self):
        return str(self.work_mach)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

from django.db import models

# Create your models here.
from django.db import models


class Yazhu(models.Model):
    # dev_datetime = models.DateTimeField('date published')
    work_date = models.DateField('date published')
    work_prod = models.CharField('产品',max_length=50, default='.')
    work_mach = models.CharField('机台',max_length=50, default='.')
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
        return self.work_mach

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



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

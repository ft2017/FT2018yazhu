from django.db import models

# Create your models here.
from django.db import models


class Yazhu(models.Model):
    # dev_datetime = models.DateTimeField('date published')

    work_date = models.DateField('date published')
    work_prod = models.CharField('产品',max_length=50, default='.')
    CATEGORY_CHOICES = (
            ('50201-000062',u'10T液压切边机2（压二课）'),
('50201-000045',u'压铸专用双回路油温机（ADDM-18）-3'),
('50201-000063',u'油压切边机QY-10T（压二）'),
('50201-000049',u'10T液压切边机-1'),
('50201-000050',u'10T液压切边机-2'),
('50201-000051',u'10T液压切边机-3'),
('50201-000052',u'10T液压切边机-4'),
('50201-000053',u'10T液压切边机-5'),
('50201-000028',u'钦羽10T液压切边机'),
('50201-000027',u'钦羽10T液压切边机'),
('50201-000033',u'QY15T液压切边机1（压铸）'),
('50201-000034',u'QY15T液压切边机2（压铸）'),
('50201-000037',u'铝制品切销机TM-106K-15T'),
('50201-000038',u'铝制品切销机TM-106K-15T'),
('50201-000039',u'铝制品切销机TM-106K-30T'),
('50201-000054',u'液压切边机（20T）'),
('50201-000064',u'钦羽20T液压切边机'),
('50201-000061',u'钦羽15T液压切边机'),
('50210-000146',u'四柱油压机（DSH-150）'),
('50201-000030',u'S-360立式带锯床'),
('50201-000057',u'立式带锯床(S-360)'),
('50210-000148',u'立式带锯床（S-600）'),
('50210-000147',u'立式带锯床（S-400）'),
('50202-000010',u'REGLOPLAS(切边机）'),
('50201-000018',u'油循环式温控机(OTH-40)'),
('50201-000019',u'油循环式温控机(OTH-40)'),
('50201-000035',u'压铸专用双回路油温机ADDM-18'),
('50201-000036',u'油循环温度控制机AEOT-10'),
('50201-000043',u'压铸专用双回路油温机（ADDM-18）-1'),
('50201-000044',u'压铸专用双回路油温机（ADDM-18）-2'),
('50201-000073',u'Impress系列冷室压铸机DCC400'),
('50201-000079',u'Toyo铝合金冷室压铸机BD-350V5 EX'),
('50201-000031',u'油压冲床QY-6T（压二）'),
('50201-000067',u'Impress系列冷室压铸机DCC400'),
('50201-000041',u'280T冷室压铸机(含控制软件6.1万）'),
('YZ015Y',u'东洋250吨冷室压铸机'),
('50201-000004',u'锌-热式油压自动压铸机(P20)'),
('50201-000005',u'锌-热式油压自动压铸机(P20)'),
('50201-000006',u'锌-热式油压自动压铸机(P20)'),
('50201-000007',u'锌-热式油压自动压铸机(P40)'),
('50201-000008',u'锌-热式油压自动压铸机(P60)'),
('50201-000009',u'锌-热式油压自动压铸机(P60)'),
('50201-000010',u'锌-热式油压自动压铸机(P60)'),
('50201-000011',u'锌-热式油压自动压铸机(P60)'),
('50201-000012',u'锌-热式油压自动压铸机(P100)'),
('50201-000071',u'兴行150吨锌/镁合金热室压铸机'),
('50201-000072',u'兴行150吨锌合金热室压铸机'),
('YZ033Y',u'兴行150吨锌合金热室压铸机'),
('MY004',u'兴行150吨镁合金热室压铸机'),
('50201-000055',u'（特案进口）150T镁合金压铸机-1'),
('50201-000056',u'（特案进口）150T镁合金压铸机-2'),
('50201-000002',u'铝/镁-（免税进口）瑞士铝/镁合金压铸机(340T)'),
('50201-000001',u'镁-（免税进口）瑞士镁合金压铸机660T'),
('50201-000059',u'(免关税进口)Toyo铝合金冷室压铸机BD-125V5'),
('50201-000065',u'Impress系列冷室压铸机DCC160'),
('50201-000066',u'Impress系列冷室压铸机DCC160'),
('50201-000003',u'锌-热式自动压铸机(U-20)'),
('YZ038Y',u'力劲3000吨冷室压铸机'),
('YZ039Y',u'力劲2500吨冷室压铸机'),
('50201-000089',u'伊之密650吨半固态压铸机'),
('FT00385-1',u'活塞检具69#通止规'),
('FT00386-1',u'活塞检具156#通止规'),
('FT00387-1',u'活塞检具146#通止规'),
('FT00388-1',u'活塞检具82#通止规'),
('FT00389-1',u'活塞检具57#通止规'),
('FT00390-1',u'活塞A260#261#模芯检具'),
('FT00391-1',u'活塞A/B158#167#模芯检具'),
('FT00392-1',u'活塞B249#250#模芯检具'),
('FT00347',u'启基3S内盖压铸螺丝孔位检具'),
('FT00348',u'启基3S内盖压铸基准平面检具'),
('FT00445',u'50-300110-01平面度检具'),
('FT00446',u'50-300112-01平面度检具'),
('FT00447',u'50-300111-01平面度检具'),
('FT00464-2',u'3S内盖压铸胀模肉厚检具'),
('FT00167-2',u'1146402导波基板'),
('FT00176',u'枪机17机身检具'),
('FT00177',u'枪机13机身检具'),
('FT00178',u'枪机13机身变形检具'),
('FT00193',u'JG1 94.61通止规'),
('FT00194',u'JG1 178.90通止规'),
('FT00204-3',u'枪机13机身变形检具'),
('FT00208-3',u'枪机17机身尾部检具'),
('FT00223',u'启基3S内盖肉厚通止规检具'),
('FT00225',u'启基3S内盖1.28±0.08通止'),
('FT00246',u'50-300077-01平面度检具'),
('FT00283',u'1222580导波基板孔属检查检具'),
('FT00290',u'JG1/JG1F-GR压铸平面度 检具'),
('FT00299',u'JG1/JG1F-GR散热片卡勾变形检具'),
('FT00312',u'30093支架冲孔检具'),
('FT00443',u'50-300078-01平面度检具'),
('FT00444',u'50-300079-01平面度检具'),
('FT10085',u'数显卡尺'),
('FT00473-1',u'300123/124/129/130方孔厚度检具'),
('FT30129',u'温控仪'),
('FT10086',u'数显卡尺'),
('FT10087',u'数显卡尺'),
('FT13010',u'数显高度规'),
('FT13011',u'数显高度规'),
('FT30014',u'吊磅'),
('FT30086',u'里氏硬度测试仪'),
('FT30105',u'电子称'),
('50201-000046',u'压铸专用双回路油温机（ADDM-18）-4'),
('50201-000047',u'压铸专用双回路油温机（ADDM-18）-5'),
('50201-000048',u'压铸专用双回路油温机（ADDM-18）-6'),
('FT00161-2',u'FD8367V上盖检具'),
('50201-000042',u'400T冷室压铸机（含控制软件7.9万）'),
('50201-000060',u'(免关税进口)Toyo铝合金冷室压铸机BD-350V5'),
('50201-000088',u'伊之密500吨冷室压铸机'),
('50201-000078',u'Toyo铝合金冷室压铸机BD-350V5 EX'),
('YZ016Y',u'东洋200吨冷室压铸机'),
('YZ017Y',u'东洋200吨冷室压铸机'),
('50201-000086',u'压铸专用双回路油温机ADDM-18'),
('50201-000087',u'压铸专用双回路油温机ADDM-18'),
('60401-000005',u'工作台1(2.6*1.2*0.74m)'),
('60401-000006',u'工作台2(2.6*1.2*0.74m)'),
('60401-000007',u'工作台3(2.6*1.2*0.74m)'),
('50201-000092',u'280T镁合金压铸机'),
('50201-000093',u'280T镁合金压铸机'),
('50201-000094',u'400T铝合金压铸机'),
('50201-000091',u'力劲800T冷室压铸机'),
('RJ000001',u'立式锯床'),
('RJ000002',u'立式锯床'),
            )
    work_mach = models.CharField('机台',max_length=50, choices = CATEGORY_CHOICES)
    
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

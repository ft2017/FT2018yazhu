# Generated by Django 2.0.1 on 2018-02-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180112_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazhu',
            name='work_mach',
            field=models.CharField(choices=[('50201-000062', '10T液压切边机2（压二课）'), ('50201-000045', '压铸专用双回路油温机（ADDM-18）-3'), ('50201-000063', '油压切边机QY-10T（压二）'), ('50201-000049', '10T液压切边机-1'), ('50201-000050', '10T液压切边机-2'), ('50201-000051', '10T液压切边机-3'), ('50201-000052', '10T液压切边机-4'), ('50201-000053', '10T液压切边机-5'), ('50201-000028', '钦羽10T液压切边机'), ('50201-000027', '钦羽10T液压切边机'), ('50201-000033', 'QY15T液压切边机1（压铸）'), ('50201-000034', 'QY15T液压切边机2（压铸）'), ('50201-000037', '铝制品切销机TM-106K-15T'), ('50201-000038', '铝制品切销机TM-106K-15T'), ('50201-000039', '铝制品切销机TM-106K-30T'), ('50201-000054', '液压切边机（20T）'), ('50201-000064', '钦羽20T液压切边机'), ('50201-000061', '钦羽15T液压切边机'), ('50210-000146', '四柱油压机（DSH-150）'), ('50201-000030', 'S-360立式带锯床'), ('50201-000057', '立式带锯床(S-360)'), ('50210-000148', '立式带锯床（S-600）'), ('50210-000147', '立式带锯床（S-400）'), ('50202-000010', 'REGLOPLAS(切边机）'), ('50201-000018', '油循环式温控机(OTH-40)'), ('50201-000019', '油循环式温控机(OTH-40)'), ('50201-000035', '压铸专用双回路油温机ADDM-18'), ('50201-000036', '油循环温度控制机AEOT-10'), ('50201-000043', '压铸专用双回路油温机（ADDM-18）-1'), ('50201-000044', '压铸专用双回路油温机（ADDM-18）-2'), ('50201-000073', 'Impress系列冷室压铸机DCC400'), ('50201-000079', 'Toyo铝合金冷室压铸机BD-350V5 EX'), ('50201-000031', '油压冲床QY-6T（压二）'), ('50201-000067', 'Impress系列冷室压铸机DCC400'), ('50201-000041', '280T冷室压铸机(含控制软件6.1万）'), ('YZ015Y', '东洋250吨冷室压铸机'), ('50201-000004', '锌-热式油压自动压铸机(P20)'), ('50201-000005', '锌-热式油压自动压铸机(P20)'), ('50201-000006', '锌-热式油压自动压铸机(P20)'), ('50201-000007', '锌-热式油压自动压铸机(P40)'), ('50201-000008', '锌-热式油压自动压铸机(P60)'), ('50201-000009', '锌-热式油压自动压铸机(P60)'), ('50201-000010', '锌-热式油压自动压铸机(P60)'), ('50201-000011', '锌-热式油压自动压铸机(P60)'), ('50201-000012', '锌-热式油压自动压铸机(P100)'), ('50201-000071', '兴行150吨锌/镁合金热室压铸机'), ('50201-000072', '兴行150吨锌合金热室压铸机'), ('YZ033Y', '兴行150吨锌合金热室压铸机'), ('MY004', '兴行150吨镁合金热室压铸机'), ('50201-000055', '（特案进口）150T镁合金压铸机-1'), ('50201-000056', '（特案进口）150T镁合金压铸机-2'), ('50201-000002', '铝/镁-（免税进口）瑞士铝/镁合金压铸机(340T)'), ('50201-000001', '镁-（免税进口）瑞士镁合金压铸机660T'), ('50201-000059', '(免关税进口)Toyo铝合金冷室压铸机BD-125V5'), ('50201-000065', 'Impress系列冷室压铸机DCC160'), ('50201-000066', 'Impress系列冷室压铸机DCC160'), ('50201-000003', '锌-热式自动压铸机(U-20)'), ('YZ038Y', '力劲3000吨冷室压铸机'), ('YZ039Y', '力劲2500吨冷室压铸机'), ('50201-000089', '伊之密650吨半固态压铸机'), ('FT00385-1', '活塞检具69#通止规'), ('FT00386-1', '活塞检具156#通止规'), ('FT00387-1', '活塞检具146#通止规'), ('FT00388-1', '活塞检具82#通止规'), ('FT00389-1', '活塞检具57#通止规'), ('FT00390-1', '活塞A260#261#模芯检具'), ('FT00391-1', '活塞A/B158#167#模芯检具'), ('FT00392-1', '活塞B249#250#模芯检具'), ('FT00347', '启基3S内盖压铸螺丝孔位检具'), ('FT00348', '启基3S内盖压铸基准平面检具'), ('FT00445', '50-300110-01平面度检具'), ('FT00446', '50-300112-01平面度检具'), ('FT00447', '50-300111-01平面度检具'), ('FT00464-2', '3S内盖压铸胀模肉厚检具'), ('FT00167-2', '1146402导波基板'), ('FT00176', '枪机17机身检具'), ('FT00177', '枪机13机身检具'), ('FT00178', '枪机13机身变形检具'), ('FT00193', 'JG1 94.61通止规'), ('FT00194', 'JG1 178.90通止规'), ('FT00204-3', '枪机13机身变形检具'), ('FT00208-3', '枪机17机身尾部检具'), ('FT00223', '启基3S内盖肉厚通止规检具'), ('FT00225', '启基3S内盖1.28±0.08通止'), ('FT00246', '50-300077-01平面度检具'), ('FT00283', '1222580导波基板孔属检查检具'), ('FT00290', 'JG1/JG1F-GR压铸平面度 检具'), ('FT00299', 'JG1/JG1F-GR散热片卡勾变形检具'), ('FT00312', '30093支架冲孔检具'), ('FT00443', '50-300078-01平面度检具'), ('FT00444', '50-300079-01平面度检具'), ('FT10085', '数显卡尺'), ('FT00473-1', '300123/124/129/130方孔厚度检具'), ('FT30129', '温控仪'), ('FT10086', '数显卡尺'), ('FT10087', '数显卡尺'), ('FT13010', '数显高度规'), ('FT13011', '数显高度规'), ('FT30014', '吊磅'), ('FT30086', '里氏硬度测试仪'), ('FT30105', '电子称'), ('50201-000046', '压铸专用双回路油温机（ADDM-18）-4'), ('50201-000047', '压铸专用双回路油温机（ADDM-18）-5'), ('50201-000048', '压铸专用双回路油温机（ADDM-18）-6'), ('FT00161-2', 'FD8367V上盖检具'), ('50201-000042', '400T冷室压铸机（含控制软件7.9万）'), ('50201-000060', '(免关税进口)Toyo铝合金冷室压铸机BD-350V5'), ('50201-000088', '伊之密500吨冷室压铸机'), ('50201-000078', 'Toyo铝合金冷室压铸机BD-350V5 EX'), ('YZ016Y', '东洋200吨冷室压铸机'), ('YZ017Y', '东洋200吨冷室压铸机'), ('50201-000086', '压铸专用双回路油温机ADDM-18'), ('50201-000087', '压铸专用双回路油温机ADDM-18'), ('60401-000005', '工作台1(2.6*1.2*0.74m)'), ('60401-000006', '工作台2(2.6*1.2*0.74m)'), ('60401-000007', '工作台3(2.6*1.2*0.74m)'), ('50201-000092', '280T镁合金压铸机'), ('50201-000093', '280T镁合金压铸机'), ('50201-000094', '400T铝合金压铸机'), ('50201-000091', '力劲800T冷室压铸机'), ('RJ000001', '立式锯床'), ('RJ000002', '立式锯床')], max_length=50, verbose_name='机台'),
        ),
    ]
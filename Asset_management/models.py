from django.db import models

# Create your models here.
class Zc(models.Model):
    # 资产编号 primary_key=True: 该字段为主键
    ZcId = models.IntegerField('ZcId', primary_key=True)
    # 资产名称 字符串 最大长度255
    ZcName = models.CharField('ZcName', max_length=255)
    # 使用部门 字符串 最大长度255 null=False, 表示该字段不能为空
    UsePart = models.CharField('UsePart', max_length=255, null=False)
    # 使用人 字符串 最大长度255 null=False, 表示该字段不能为空
    UsePeople = models.CharField('UsePeople', max_length=255, null=False)
    # 使用地点 字符串 最大长度255 null=False, 表示该字段不能为空
    UseLocat = models.CharField('UseLocat', max_length=255, null=False)
    # 备注 字符串 最大长度255 null=False, 表示该字段不能为空
    Text = models.TextField('Text', null=True)
    # 图片123
    img1 = models.TextField('img1', blank=True, null=True)
    img2 = models.TextField('img2', blank=True, null=True)
    img3 = models.TextField('img3', blank=True, null=True)
    # 创建时间 auto_now_add：只有在新增的时候才会生效
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改时间 auto_now： 添加和修改都会改变时间
    modifyTime = models.DateTimeField(auto_now=True)
# 指定表名 不指定默认APP名字——类名(app_demo_Student)
    class Meta:
        db_table = 'ZcTable'
from django.db import models


# Create your models here.


class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        如果你想把某些公共信息添加到很多 model 中，抽象基类就显得非常有用。
        你编写完基类之后，在 Meta 内嵌类中设置 abstract=True ，
        该类就不能创建任何数据表。然而如果将它做为其他 model 的基类，那么该类的字段就会被添加到子类中。
        抽象基类和子类如果含有同名字段，就会导致错误(Django 将抛出异常)。
        """
        abstract = True  # 不用创建表可以省区重复写的代码直接继承就可以使用


from django.contrib.auth.models import AbstractUser


class User(Base, AbstractUser):
    """用户表"""
    username = models.CharField(max_length=12, unique=True)  # 账号
    password = models.CharField(max_length=192)  # 密码
    phone = models.CharField(max_length=11)  # 手机号
    grade = models.IntegerField(null=True, blank=True)  # 用户等级
    email = models.EmailField(null=True, blank=True)  # 邮箱
    is_status = {
        (1, '未注销'),
        (2, '注销中'),
        (3, '已注销'),
    }
    status = models.IntegerField(choices=is_status, default=1)

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username


class UserInformation(models.Model):
    """用户信息"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=12, null=True, blank=True, default='')  # 名号
    gender = models.IntegerField(null=True, blank=True, default=0)  # 性别 男 1 ,女 2, 保密 3
    city = models.CharField(max_length=20, null=True, blank=True, default='')  # 城市
    birthday = models.DateField(null=True, blank=True)  # 出生日期
    intro = models.CharField(max_length=254, null=True, blank=True, default='')  # 个人简介

    class Meta:
        db_table = 'UserInformation'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.name


class Image(models.Model):
    """用户头像"""
    image = models.ImageField(upload_to='media')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    md5 = models.CharField(max_length=192)  # 图片md5值

    class Meta:
        db_table = 'image'
        verbose_name_plural = '图片'


# 精准地址
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)  # 加后缀名 省市区
    pid = models.IntegerField()
    sname = models.CharField(max_length=128)  # 不加后缀
    level = models.IntegerField()  # 等级
    citycode = models.CharField(max_length=128, null=True, blank=True)  # 城市区号
    yzcode = models.CharField(max_length=128, null=True, blank=True)  # 城市邮编
    mername = models.CharField(max_length=128)  # 所在地区联名 (中国,北京,北京市)
    Lng = models.FloatField()  # 经度
    Lat = models.FloatField()  # 纬度
    pinyin = models.CharField(max_length=128)

    class Meta:
        db_table = 'region'
        verbose_name = '城市表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Address(models.Model):
    """地址"""
    name = models.CharField(max_length=128)
    province = models.ForeignKey(Region, on_delete=True, related_name='省外键')  # 省外键
    city = models.ForeignKey(Region, on_delete=True, related_name='市外键')  # 市外键
    county = models.ForeignKey(Region, on_delete=True, related_name='县外键')  # 县外键
    detail = models.CharField(max_length=254)  # 详情地址
    phone = models.CharField(max_length=11)  # 手机号
    zip_code = models.CharField(max_length=11)  # 邮政编码
    is_default = {
        (0, '非默认地址'),
        (1, '默认地址'),
    }
    default = models.BooleanField(choices=is_default, default=0)  # 是否为默认地址
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'address'

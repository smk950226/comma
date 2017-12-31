from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(verbose_name = '이름', max_length = 20)
    email = models.EmailField(verbose_name = 'E-mail', unique = True)
    univ = models.CharField(verbose_name = '대학교', help_text = 'Full Name을 적어 주세요. (ex)서울대학교)', max_length = 20)
    major = models.CharField(verbose_name = '전공', help_text = 'Full Name을 적어 주세요. (ex)기계항공공학)', max_length = 20)
    group = models.CharField(verbose_name = '요일조', max_length = 20)
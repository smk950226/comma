from django.db import models

class ActPhoto(models.Model):
    photo = models.ImageField(upload_to='actphoto', verbose_name='활동 사진')
    year = models.CharField(default=2017, verbose_name='활동 년도', max_length=10, choices=(
                                                                                    ('2017','2017년'),
                                                                                    ('2016','2016년'),
                                                                                    ('2015','2015년'),
                                                                                    ('2014','2014년'),
                                                                                    ('2013','2013년 이전'),
    ))
    date = models.CharField(verbose_name='활동 날짜', help_text='0000.00.00과 같이 입력해 주세요.', max_length=20)
    site = models.CharField(verbose_name='활동 장소', max_length=100)
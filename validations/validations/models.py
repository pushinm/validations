import re

from django.db import models
from .validators.validators import validate_even
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, DecimalValidator, MinLengthValidator, MaxLengthValidator
# Create your models here.
class Test(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
    age_child = models.IntegerField(verbose_name='Возраст ребенка',
                                    validators=[MinValueValidator(0),
                                                    MaxValueValidator(18, message='Ребенок должен быть не старше 18 лет')])
    name = models.CharField(
        verbose_name='Имя',
        validators=[RegexValidator(
            regex=r'[^._]',
            message='Нижнее подчеркивание запрещено',
            flags=re.IGNORECASE,
        )],
        max_length=100
    )
    min_length = models.TextField(verbose_name='min_length', validators=[MinLengthValidator(
        limit_value=10,
        message='Минимум 10 символов'
    )])
    max_length = models.TextField(verbose_name='max_length', validators=[MaxLengthValidator(
        limit_value=10,
        message='Максимум 10 символов'
    )])
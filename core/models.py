import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class TelegramUpdate(models.Model):
    """Данные апдейта в JSON-формате"""
    update_JSON = models.JSONField(verbose_name="Данные апдейта")
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время получения апдейта")

    def __str__(self):
        return f"Апдейт от {self.update_date}"

"""Далее классы из обучения https://docs.djangoproject.com/en/5.1/intro/"""
class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question_text} - {self.choice_text} - {self.votes}'

class TakatafoodType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Takatafood(models.Model):
    TakatafoodType = models.ForeignKey(TakatafoodType, on_delete = models.CASCADE)
    TakatafoodName = models.CharField(max_length = 200)
    TakatafoodPrice = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.TakatafoodType} - {self.TakatafoodName} - {self.TakatafoodPrice}'
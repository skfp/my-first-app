from django.db import models
from django.utils import timezone

class Card(models.Model):
    #__tablename__ = 'cards'

    card_id = models.IntegerField(default=0)
    pile_id = models.IntegerField(default=0)
    first_lng = models.CharField(max_length=200, default="NA")
    second_lng = models.CharField(max_length=200, default="NA")
    card_type = models.CharField(max_length=1, default="N")
    last_good_ans = models.DateTimeField(default=timezone.now)
    #N-new, S-short, M-medium, L-long, H-very long, W-wrong

    def publish(self):
        #self.last_good_ans = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_lng)

class Answer(models.Model):
    #__tablename__ = 'answers'
    answer_id = models.IntegerField(default=0)
    card_id_ans = models.IntegerField(default=0)
    pile_id = models.IntegerField(default=0)
    datestamp = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=1, default="X")
    #E-easy, M-medium, H-hard, W-wrong

    def publish(self):
        self.datestamp = timezone.now()
        self.save()

    def __str__(self):
        return self.answer

class User(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=100, default="NA")
    user_login = models.CharField(max_length=100, default="NA")
    user_password = models.CharField(max_length=100, default="NA")
    user_mail = models.CharField(max_length=100, default="NA")
    new_left_today = models.IntegerField(default=0)
    normal_left_today = models.IntegerField(default=0)
    wrong_left_today = models.IntegerField(default=0)
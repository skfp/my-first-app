from django.db import models
from django.utils import timezone

class Card(models.Model):
    #__tablename__ = 'cards'

    card_id = models.IntegerField(default=0)
    pile_id = models.IntegerField(default=0)
    first_lng = models.CharField(max_length=200)
    second_lng = models.CharField(max_length=200)
    card_type = models.CharField(max_length=1)
    last_good_ans = models.DateTimeField(default=timezone.now)
    #N-new, S-short, M-medium, L-long, H-very long, W-wrong

class Answer(models.Model):
    #__tablename__ = 'answers'
    answer_id = models.IntegerField(default=0)
    card_id_ans = models.IntegerField(default=0)
    pile_id = models.IntegerField(default=0)
    datestamp = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=1)  
    #E-easy, M-medium, H-hard, W-wrong



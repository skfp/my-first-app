from django.db import models
from django.utils import timezone

class Card(db.Model):
    #__tablename__ = 'cards'

    card_id = models.Integer()
    pile_id = models.Integer()
    first_lng = models.CharField(max_length=200)
    second_lng = models.CharField(max_length=200)
    card_type = models.CharField(max_length=1)  
    #N-new, S-short, M-medium, L-long, H-very long, W-wrong


class Answer(db.Model):
    #__tablename__ = 'answers'
    answer_id = models.Integer()
    card_id = models.Integer()
    pile_id = models.Integer()
    datestamp = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=1)  
    #E-easy, M-medium, H-hard, W-wrong



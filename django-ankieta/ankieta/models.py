# Create a database schema (CREATE TABLE statements) for this app.
# Create a Python database-access API for accessing Question and Choice objects.

import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Field - rodzaj przechowywanych danych w bazie danych django.db
class Question(models.Model):
    # question_text i pub_date to nazwy kolumn i jednocześnie zmienne.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published") # date published to ludzka nazwa dla maszynowego pub_date
    def __str__(self) -> str:
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # pole question jest kluczem do modelu Question i on_delete wskazuje, że razem z Question zniknie Choice.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text
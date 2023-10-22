from django.db import models

class Review (models.Model):
    class Meta(object):
        db_table = 'createReview'


    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )

    body = models.TextField(
        'Body', blank=False, null=False, db_index=True
    )

    created_at = models.DateField(
        'Created DateField', blank=True, auto_now_add=True
    )
from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User

class Poke(models.Model):
    poker = models.ForeignKey(User, related_name="the_poker")
    pokee = models.ForeignKey(User, related_name="the_pokee")
    counter = models.IntegerField(blank=False, default=0, null=True)
    total_pokes = models.IntegerField(blank=False, default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
# Create your models here.

def gen_crypto():
    return get_random_string(length=6 )

class Posts(models.Model):



    post_content = models.CharField(max_length=280)
    boast_or_roast = models.BooleanField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField( default=timezone.now)
    secret = models.CharField(default=gen_crypto, max_length=6)
    
    @property
    def total_votes(self):
        return self.up_votes - self.down_votes

        
        

    def __str__(self):
        return self.post_content
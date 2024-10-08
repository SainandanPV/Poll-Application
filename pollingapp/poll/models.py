from django.db import models

# Create your models here.
class Poll(models.Model):
    question=models.CharField(max_length=400)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
class Option(models.Model):
    poll=models.ForeignKey(Poll,related_name='options',on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
    @property
    def percentage(self):
        total_votes=sum(option.votes for option in self.poll.options.all())
        if total_votes>0:
            return round((self.votes/total_votes)*100,3)
        return 0



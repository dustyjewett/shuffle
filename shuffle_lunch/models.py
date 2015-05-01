from django.db import models
from django.contrib.auth.models import User

class Shuffle(models.Model):
    display_name = models.CharField(max_length=200)
    members = models.ManyToManyField(User, blank=True)
    type_description = models.CharField(max_length=20)
    time = models.TimeField()
    firstDate = models.DateTimeField()
    schedule = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.display_name

class ShuffleEvent(models.Model):
    shuffle = models.ForeignKey(Shuffle)
    display_name = models.CharField(max_length=200)
    start = models.DateTimeField('start time of the event')
    end = models.DateTimeField('end time of the event')
    ideal_pod_size = models.IntegerField(default=4)
    def __str__(self):              # __unicode__ on Python 2
        return "%s at %s" % (self.display_name, self.start)

class ShuffleEventRSVP(models.Model):
    shuffle_event = models.ForeignKey(ShuffleEvent)
    response = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

class ShuffleEventPod(models.Model):
    display_name = models.CharField(max_length = 50)
    shuffle_event = models.ForeignKey(ShuffleEvent)
    members = models.ManyToManyField(User)
    def __str__(self):              # __unicode__ on Python 2
        return "Pod '%s' (s:%s) for Event: %s" % (self.display_name, self.members.all().__len__(), self.shuffle_event.display_name)

class ShuffleEventPodConfirmation(models.Model):
    pod = models.ForeignKey(ShuffleEventPod)
    member = models.ForeignKey(User)
    comments = models.CharField(max_length=300)
    created_at = models.DateTimeField()




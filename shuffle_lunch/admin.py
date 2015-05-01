from django.contrib import admin

# Register your models here.
from .models import Shuffle
from .models import ShuffleEvent
from .models import ShuffleEventPod

admin.site.register(Shuffle)

admin.site.register(ShuffleEvent)

admin.site.register(ShuffleEventPod )
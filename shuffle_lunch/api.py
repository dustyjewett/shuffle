from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from django.contrib.auth.models import User

from .models import Shuffle

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ShuffleResource(ModelResource):
    members = fields.ManyToManyField(UserResource, attribute = 'members', null=True, full=True)

    class Meta:
        queryset = Shuffle.objects.all()
        resource_name = 'shuffle'
        authorization= Authorization()
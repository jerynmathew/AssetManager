from django.db import models
from jsonfield import JSONField
from collections import OrderedDict


class BaseObject(models.Model):
    '''
    The base model from which all apps inherit
    '''

    # Type represents the app that uses it. Assets, Persons, Orgs, etc
    type = models.CharField(max_length=256)

    # Related-to represents the the relation of this object with other objects (of any type)
    related_to = models.ManyToManyField("self", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True, auto_now=True)

    # Store all attributes/properties of the object as dictionary
    attributes = JSONField(load_kwargs={'object_pairs_hook': OrderedDict})

    def __init__(self, *args, **kwargs):
        super(BaseObject, self).__init__(*args, **kwargs)

        if not self.pk and not self.type:
            self.type = self.TYPE


class ProxyObject(BaseObject):

    class Meta:
        proxy = True

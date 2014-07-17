from django.db import models
from jsonfield import JSONField
from collections import OrderedDict


class BaseObject(models.Model):
    """
    The base model from which all apps inherit
    """

    # Type represents the app that uses it. Assets, Persons, Orgs, etc
    type = models.CharField(max_length=256)

    # Related-to represents the the relation of this object with other objects (of any type)
    related_to = models.ManyToManyField("self", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True, auto_now=True)

    # Store all attributes/properties of the object as dictionary
    attributes = JSONField(load_kwargs={'object_pairs_hook': OrderedDict}, blank=True)

    def __init__(self, *args, **kwargs):
        super(BaseObject, self).__init__(*args, **kwargs)

        if not self.pk and not self.type:
            self.type = self.TYPE


class BasePropertyManager(models.Manager):
    def create_attributes(self, baseobject, **attributes):
        """
        Given a set of key-value attributes for a given object,
        create the attribute-set in table
        """
        property_set = []
        for attr, value in attributes.items():
            property_set.append(BaseProperty(baseobject=baseobject, key=attr, value=value))

        self.bulk_create(property_set)


class BaseProperty(models.Model):
    """
    Key-Value attributes of objects are stored here.
    """

    baseobject = models.ForeignKey(BaseObject)

    key = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

    objects = BasePropertyManager()

    def __unicode__(self):
        """Representation of field"""
        return {self.baseobject.id: {self.key: self.value}}


class ProxyObject(BaseObject):

    class Meta:
        proxy = True

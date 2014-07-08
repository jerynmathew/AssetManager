from rest_framework import serializers

from .models import Assets


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assets
        fields = ('type', 'created_on', 'updated_on', 'attributes')


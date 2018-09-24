from rest_framework import serializers

from .models import Position


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        # fields = ('uuid', 'name', 'latitude', 'longitude', 'update')
        exclude = ('',)

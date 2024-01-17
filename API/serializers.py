from database.models import *
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fam', 'name', 'otc', 'email', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['summer', 'autumn', 'winter', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    date_added = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Images
        fields = ['title', 'date_added', 'image']


class PerevalsSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    user = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True, required=False)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Perevals
        fields = ['beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'status',
                  'add_time',
                  'level',
                  'user',
                  'coord',
                  'images'
                  ]

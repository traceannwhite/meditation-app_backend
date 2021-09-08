from .models import Timer
from rest_framework import serializers

## serializer for our model
class TimerSerializer(serializers.HyperlinkedModelSerializer):
    #nest meta data for the serializer
    class Meta: 
        # model to serialize
        model = Timer
        #which fields to serialize
        fields = ["id", "time_field"]
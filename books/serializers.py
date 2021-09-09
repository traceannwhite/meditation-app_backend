from .models import Books
from rest_framework import serializers

## serializer for our model
class BooksSerializer(serializers.HyperlinkedModelSerializer):
    #nest meta data for the serializer
    class Meta: 
        # model to serialize
        model = Books
        #which fields to serialize
        fields = ["id", "image", "title", "author", "description", "read"]
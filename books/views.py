from .models import Books
from rest_framework import viewsets, permissions
from .serializers import BooksSerializer


# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    #main query for index route
    queryset=Books.objects.all()
    #serializer
    serializer_class = BooksSerializer
    # permissions
    permission_classes = [permissions.AllowAny]
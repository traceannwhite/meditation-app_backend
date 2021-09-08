from .models import Timer 
from rest_framework import viewsets, permissions
from .serializers import TimerSerializer


# Create your views here.
class TimerViewSet(viewsets.ModelViewSet):
    #main query for index route
    queryset=Timer.objects.all()
    #serializer
    serializer_class = TimerSerializer
    # permissions
    permission_classes = [permissions.AllowAny]
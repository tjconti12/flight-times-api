from rest_framework import generics
from .serializers import AirportSerializer
from .models import Airport

# Create your views here.
class AirportList(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class AirportDetail(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
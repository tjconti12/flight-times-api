from rest_framework import generics, filters
from .serializers import AirportSerializer
from .models import Airport

# Create your views here.
class AirportList(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class AirportDetail(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
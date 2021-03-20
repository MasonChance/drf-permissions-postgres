from rest_framework import generics
from .models import Deck
from .serializer import DeckSerializer


# Create your views here.
class DeckListView(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
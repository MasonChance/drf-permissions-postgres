from deck.permissions import isOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Deck
from .serializer import DeckSerializer


# Create your views here.
class DeckListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
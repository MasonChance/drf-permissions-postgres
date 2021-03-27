from deck.permissions import isOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Deck
from .serializer import DeckSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response 
# import unicode 

# Create your views here.
class DeckListView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),
    #         'auth': unicode(request.auth),
    #     }
    #     return Response(content)

class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes= [SessionAuthentication, BasicAuthentication]
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),
    #         'auth': unicode(request.auth),
    #     }
    #     return Response(content)

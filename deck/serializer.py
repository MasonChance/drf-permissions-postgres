from rest_framework import serializers
from .models import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'owner', 'mana_type', 'cast_cost', 'size')
        model = Deck


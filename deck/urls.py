from django.urls import path
from .views import DeckListView, DeckDetailView

urlpatterns = [
    path('', DeckListView.as_view(), name='deck_list'),  # Home Route
    path('api/v1/deck/<int:pk>/', DeckDetailView.as_view(), name='deck_detail'), # Detail is a single Item from the Model table
]



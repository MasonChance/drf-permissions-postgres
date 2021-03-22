from django.urls import path
from .views import DeckListView, DeckDetailView

urlpatterns = [
    path('', DeckListView.as_view()),  # Home Route
    path('<int:pk>/', DeckDetailView.as_view()), # Detail is a single Item from the Model table
]



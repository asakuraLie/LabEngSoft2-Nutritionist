from django.urls import path

from .views import NutritionistView

urlpatterns = [
    path("nutritionist/", NutritionistView.as_view(actions={"post": "create", "get": "list_all"})),
    path("nutritionist/<int:pk>/", NutritionistView.as_view(actions={"get": "retrieve"})),
]
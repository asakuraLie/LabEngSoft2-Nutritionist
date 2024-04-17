from django.urls import path

from .views import NutritionistView, PatientView, EvaluationView, EvolutionView, DietView

urlpatterns = [
    # path nutritionist
    path("nutritionist/list/", NutritionistView.as_view(actions={"get": "list_all"})),
    path("nutritionist/create/", NutritionistView.as_view(actions={"post": "create"})),
    path("nutritionist/<int:pk>/", NutritionistView.as_view(actions={"get": "retrieve"})),
    # path patient
    path("patient/list/", PatientView.as_view(actions={"get": "list_all"})),
    path("patient/create/", PatientView.as_view(actions={"post": "create"})),
    path("patient/<int:pk>/", PatientView.as_view(actions={"get": "retrieve"})),
    # path evaluation
    path("evaluation/list/", EvaluationView.as_view(actions={"get": "list_all"})),
    path("evaluation/create/", EvaluationView.as_view(actions={"post": "create"})),
    path("evaluation/<int:pk>/", EvaluationView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("evaluation_from_patient/<int:pk>/", EvaluationView.as_view(actions={"get": "retrieve_by_patient"})),
    # path evolution
    path("evolution/list/", EvolutionView.as_view(actions={"get": "list_all"})),
    path("evolution/create/", EvolutionView.as_view(actions={"post": "create"})),
    path("evolution/<int:pk>/", EvolutionView.as_view(actions={"get": "retrieve", "delete": "delete", "put": "update"})),
    path("evolution_from_patient/<int:pk>/", EvolutionView.as_view(actions={"get": "retrieve_by_patient"})),
    #path diet
    path("diet/list/", DietView.as_view(actions={"get": "list_all"})),
    path("diet/create/", DietView.as_view(actions={"post": "create"})),
    path("diet/<int:pk>/", DietView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("diet_from_patient/<int:pk>/", DietView.as_view(actions={"get": "retrieve_by_patient"}))
]
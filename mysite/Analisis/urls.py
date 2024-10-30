from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name=""),
    path('analysis/', views.AnalysisURL, name=""),
    path('recommendation/', views.RecommendationURL, name=""),
]

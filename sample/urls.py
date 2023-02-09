from sample.views import HomeView
from django.urls import include, path

urlpatterns = [
    path('', HomeView.as_view())
]

from django.urls import path
from .views import *

app_name = "notes"
urlpatterns = [
    # Your stuff: custom urls includes go here
    path("", Index.as_view(), name="notes"),
    path("delete/<int:pk>", Delete.as_view(), name="delete"),
    path("update/<int:pk>", Update.as_view(), name="update"),
]

from django.urls import path
from first_app.views import first_one_view, first_three_view, first_two_view

urlpatterns = [
    path("first_one", first_one_view),
    path("first_two", first_two_view),
    path("first_three", first_three_view),
]

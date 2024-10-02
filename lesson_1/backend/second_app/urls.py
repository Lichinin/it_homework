from django.urls import path
from second_app.views import second_one_view, second_two_view, second_thee_view

urlpatterns = [
    path("second_one", second_one_view),
    path("second_two", second_two_view),
    path("second_three", second_thee_view),
]

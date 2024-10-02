from django.urls import path
from third_app.views import third_one_view, third_three_view, third_two_view

urlpatterns = [
    path("third_one", third_one_view),
    path("third_two", third_two_view),
    path("third_three", third_three_view),
]

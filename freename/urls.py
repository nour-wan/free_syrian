from django.urls import path
from . import views
from .views import AddView,SearchView, GetView

urlpatterns = [
    path('add',AddView.as_view()),
    path('search',SearchView.as_view()),
    path('get',GetView.as_view()),
] 
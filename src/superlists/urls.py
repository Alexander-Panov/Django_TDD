from django.urls import path

from superlists import views
from superlists.views import home_page

app_name = "superlists"

urlpatterns = [
    path("new", views.new_list, name="new_list"),
    path("<int:list_id>/", views.view_list, name="view_list"),
]

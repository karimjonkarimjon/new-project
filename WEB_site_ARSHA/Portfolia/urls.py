from django.urls import path
from .views import Ad_Services, getID, Detail

urlpatterns = [
    path("", Ad_Services, name="portfolia"),
    path("<slug:category_slug>/", Ad_Services, name="category_url"),
    path("detail/<int:id>/", getID, name="get_id"),
    path("detaila/<int:id>/", Detail, name="get_id_pk")
]

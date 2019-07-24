from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.UpdateProductView.as_view(), name="update"),
    path("create/", views.CreateProductView.as_view(), name="create"),
    path("<int:pk>/delete/", views.DeleteProductView.as_view(), name="delete"),
]

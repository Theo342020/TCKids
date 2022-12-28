from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
	path("", views.index, name="index"),
	path("about", views.about, name="about"),
	path("accounts", views.accounts, name="accounts"),
	path("accessories", views.accessories, name="accessories"),
	path("boys", views.boys, name="boys"),
	path("girls", views.girls, name="girls"),
	path("<int:id>", views.cPage, name="cPage")
]
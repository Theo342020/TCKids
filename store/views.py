from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Clothes

# Create your views here.


def index(request):
	Articles = Clothes.objects.all()
	return render(request, "store/index.html", {
		"Articles": Articles
	})

def about(request):
	return render(request, "store/about.html")

def accessories(request):
	return render(request, "store/accessories.html")

def accounts(request):
	return render(request, "store/accounts.html")

def boys(request):
	boysClothes = Clothes.objects.get(gender="male")
	return render(request, "store/boys.html", {
		"boysClothes": boysClothes
	})

def girls(request):
	girlsClothes = Clothes.objects.get(gender="female")
	return render(request, "store/girls.html", {
		"girlsClothes": girlsClothes
	})

def cPage(request, id):
	selectedClothes = Clothes.objects.get(id=id)
	return render(request, "store/cPage.html", {
		"selectedClothes": selectedClothes
	})


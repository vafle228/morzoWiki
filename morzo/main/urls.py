from django.urls import path
from .views import getMorzo

urlpatterns = [
	path('', getMorzo)
]
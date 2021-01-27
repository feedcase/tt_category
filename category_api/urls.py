from django.urls import path
from django.conf.urls.static import static
from runa import settings
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:pk>', views.CategoryDetailsView.as_view()),
    path('categories/create/', views.CategoryCreateView.as_view()),
]

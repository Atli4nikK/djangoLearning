from django.urls import path, include
from django.views.generic import ListView, DetailView
from mysite.news.models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                              template_name="news/posts.html")),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^store/', views.store, name='store'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
]

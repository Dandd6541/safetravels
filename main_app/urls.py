from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('covid/', views.covid, name='covid'),
    path('covid/query/', views.covid_query, name='covid_query'),
    path('trips/', views.trips_index, name='index'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('trips/<int:trip_id>', views.trips_detail, name='detail'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('trips/<int:trip_id>/assoc_people/<int:people_id>/', views.assoc_people, name='assoc_people'),
    path('trips/<int:trip_id>/unassoc_people/<int:people_id>/', views.unassoc_people, name='unassoc_people'),
    path('accounts/signup/', views.signup, name='signup'),
    path('peoples/', views.PeopleList.as_view(), name='peoples_index'),
    path('peoples/<int:pk>/', views.PeopleDetail.as_view(), name='peoples_detail'),
    path('peoples/create/', views.PeopleCreate.as_view(), name='peoples_create'),
    path('peoples/<int:pk>/update/', views.PeopleUpdate.as_view(), name='peoples_update'),
    path('peoples/<int:pk>/delete/', views.PeopleDelete.as_view(), name='peoples_delete'),
]


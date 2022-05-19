from django.urls import path
from . import views
from .views import report,profile,update_profile,units,runits,all_units


urlpatterns= [
   
    
    path('report/',report.as_view(),name='report'),
    path('profile/',profile.as_view(),name='profile'),
    path('',all_units.as_view(),name='aunits'),
    path('runits/',runits.as_view(),name='runits'),
    path('units/',units.as_view(),name='units'),
    # path('',create_profile.as_view(),name='create-profile'),
    path('profile/<int:pk>/update',update_profile.as_view(),name='update-profile'),
 
    
   
    
]
from django.urls import path
from .views import *


urlpatterns= [
    
    path('', ConferenceListView.as_view(), name='listViewconf'),  
    path('list/', conferenceList, name="listconf"),
    path('Details/<int:pk>/', DetailsViewConference.as_view(), name='confDetail')

]
"""path('list/',conferenceList,name="listconf"),
    path('ConferenceListView/',ConferenceListView.as_view(),name='listViewconf'),"""
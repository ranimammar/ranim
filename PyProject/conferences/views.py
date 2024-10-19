from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView

# Create your views here.
def conferenceList(req):
    liste=Conference.objects.all().order_by('-start_date')
    return render(req,'conferences/conferenceList.html',{'conferenceList':liste})

class ConferenceListView(ListView):
    model=Conference
    template_name='conferences/conference_list.html'
    context_object_name='conferences'
    def get_queryset(self):
        return Conference.objects.order_by('start_date')

class DetailsViewConference(DetailView):
    model=Conference
    template_name='conferences/conference_details.html'
    context_object_name='conference'


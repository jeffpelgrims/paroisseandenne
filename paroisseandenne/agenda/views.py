from django.shortcuts import render
from .models import Agenda
from datetime import date, timedelta

startdate = date.today()
enddate = startdate + timedelta(days=6)

agenda = Agenda.objects.filter(date_evenement__range=(startdate, enddate)).order_by('date_evenement')


def accueil(request):
    return render(request,
                  'agenda.html',
                  {'agenda': agenda}
                  )

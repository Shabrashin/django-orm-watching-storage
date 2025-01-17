from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long, format_duration, get_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)
    serialized_not_leaved = []

    for visit in not_leaved:
        serialized_not_leaved.append(
            {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
            }
        )

    context = {
        'non_closed_visits': serialized_not_leaved
    }
    return render(request, 'storage_information.html', context)

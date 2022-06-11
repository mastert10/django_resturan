from django.shortcuts import render
from .forms import ReserveForm


# Create your views here.
def Reserve(request):
    reserve_form = ReserveForm()
    if request.method == "POST":
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()
    context = {   
            "form" : reserve_form,
    }
    return render(request, 'reservation/reservation.html', context)

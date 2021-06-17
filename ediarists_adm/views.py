from ediarists_adm.models import Diarist
from django.shortcuts import redirect, render
from .forms import diarist_form

# Create your views here.

def register_diarist(req):
    if req.method == "POST":
        form = diarist_form.DiaristForm(req.POST, req.FILES)

        if form.is_valid():
            form.save()

            return redirect('list_diarists')
    else:
        form = diarist_form.DiaristForm()

    return render(req, 'diarist_form.html', {'diarist_form': form})


def list_diarists(req):
    diarists = Diarist.objects.all()

    return render(req, 'diarists_list.html', {'diarists': diarists})

def edit_diarist(req, diarist_id):
    diarist = Diarist.objects.get(id=diarist_id)

    if req.method == 'POST':
        form = diarist_form.DiaristForm(req.POST or None, req.FILES, instance=diarist)

        if form.is_valid():
            form.save()

            return redirect('list_diarists')
    else:
        form = diarist_form.DiaristForm(instance=diarist)
    
    return render(req, 'diarist_form.html', { 'diarist_form': form})

def remove_diarist(req, diarist_id):
    diarist = Diarist.objects.get(id=diarist_id)

    diarist.delete()

    return redirect('list_diarists')

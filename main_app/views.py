from django.shortcuts import render
from .models import Master, Service
from .forms import RecordForm

def MasterServiseView(request, service_id):
    masters = Master.objects.all()
    show_masters = []
    for master in masters:
        service = master.master_service.filter(id = service_id)
        if len(service):
            show_masters.append(master)
    data = {'masters': show_masters}
    return render(request, 'main_app/find_master.html', data)

def ServiceView(request):
    services = Service.objects.all()
    data = {'services':services}
    return render(request, 'main_app/services.html', data)

def RecordFormView(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        name = form.cleaned_data['master_name']
        time = form.cleaned_data['visit_time']
        masters = Master.objects.all()
        for master in masters:
            if master.master_name == name:
                for master_time in master.free_time.all():
                    if master_time == time:
                        master = Master.objects.filter(master_name=name)
                        master.free_time.filter(time = time).update(free_or_not = False)

        form = RecordForm()

    return render(request, 'main_app/record.html', {'form':form})


def FindMaster(request):
    masters = Master.objects.all()
    data = {'masters': masters}
    return render(request, 'main_app/find_master.html', data)

def MainPage(request):
    return render(request, 'main_app/main_page.html')

# Create your views here.

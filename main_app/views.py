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

def RecordFormView(request, master_id, time_id):
    master = Master.objects.get(id = master_id)
    time = master.free_time.get(id = time_id)
    form = RecordForm(request.POST or None, initial = {'master_name': master.master_name,'visit_time': time.time.strftime("%Y-%m-%d %H:%M:%S") })#'visit_time':([('12','10'),('32','7'),])
    if form.is_valid():
        form.save()
        master.free_time.filter(id = time_id).delete()
        form = RecordForm()

    return render(request, 'main_app/record.html', {'form':form})


def FindMaster(request):
    masters = Master.objects.all()
    data = {'masters': masters}
    return render(request, 'main_app/find_master.html', data)

def MainPage(request):
    return render(request, 'main_app/main_page.html')

# Create your views here.

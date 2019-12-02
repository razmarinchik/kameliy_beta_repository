from django.urls import path, include
from .views import MainPage, FindMaster, RecordFormView, ServiceView, MasterServiseView

urlpatterns = [
    path('service/<int:service_id>/', MasterServiseView),
    path('service/', ServiceView, name = 'service_page'),
    path('record/<int:master_id>/<int:time_id>/', RecordFormView),
    path('record/', RecordFormView, name = 'record_page'),
    path('masters/', FindMaster, name = 'masters_page'),
    path('', MainPage, name='main_page'),
]

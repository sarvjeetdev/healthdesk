from django.urls import path
#from .views import worklist, workdetail,workcreate,workupdate,workdelete,worklogin,workregister
from .views import RecordListView,RecordDetailView,RecordCreateView,RecordUpdateView,RecordDeleteView


urlpatterns = [
    
    path('work', RecordListView.as_view(), name='works'),
    path('work/<int:pk>/', RecordDetailView.as_view() , name='detail'),
    path('work_create/', RecordCreateView.as_view() , name='create'),
    path('work_update/<int:pk>/', RecordUpdateView.as_view() , name='update'),
    path('work_delete/<int:pk>/', RecordDeleteView.as_view() , name='delete'),
]
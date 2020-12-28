from django.urls import path

from games_info.front_end.views import Index, ResultDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>', ResultDetail.as_view(), name='result_detail')
]

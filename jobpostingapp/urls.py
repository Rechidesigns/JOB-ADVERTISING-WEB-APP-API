from django.urls import path
from . import views


urlpatterns = [
    path('Job_advert/', views.Job_advertView().as_view(), name="Job_advert_list"),
    path('Job_advert/<int:job_advert_id>/', views.Job_advertDetailView.as_view(), name="Job_advert_detail"),
    path('Job_application/', views.Job_applicationView().as_view(), name="Job_application_list"),
    path('Job_application/<int:job_application_id>/', views.Job_applicationDetailView.as_view(), name="Job_application_detail"),
]
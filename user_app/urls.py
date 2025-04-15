from django.urls import path
from . import views


urlpatterns = [
    path("",views.createProfile),
    path("project/",views.createProject,name='project'),
    path('listview/',views.listProfile,name='listview'),
    path('details_view/<int:profile_id>/', views.detailsView,name='details_view'),
    path('update_view/<int:profile_id>/', views.updateProfile,name='update_view'),
    path('delete_view/<int:profile_id>/', views.deleteView,name='delete_view')

]
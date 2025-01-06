from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name=""),
    path('register/',views.register,name="register"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),

    # CRUD
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addRecord/',views.create_record,name="addRecord"),
    path('updateRecord/<int:pk>/',views.update_record,name="updateRecord"),
    path('viewRecord/<int:pk>/',views.read_record,name="viewRecord"),
    path('deleteRecord/<int:pk>/',views.delete_record,name="deleteRecord"),
    
]

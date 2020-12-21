from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('user',views.get_current_user,name='get_current_user'),
    path('logout',views.logout,name='logout'),
    path('notes',views.get_notes,name='get_notes'),
    path('add',views.create_note,name='create_note'),
    path('notes/<int:id>',views.get_one_note,name='get_one_note'),
    path('update/<int:id>',views.update_note,name='update_note'),
    path('delete/<int:id>',views.delete_note,name='delete_note'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view/<int:id>',views.view,name='view'),
    path('add',views.add_note_page,name='add_note_page'),
    path('create',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),

]
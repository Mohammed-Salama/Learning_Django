from django.urls import path
from . import views
urlpatterns=[
    path('add_student',views.insert_student),
    path('get_student/<int:id>',views.get_student),
    path('delete_or_update_student/<int:id>',views.delete_or_update_student),
]
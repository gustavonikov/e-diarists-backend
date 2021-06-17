from ediarists_adm.views import edit_diarist, list_diarists, register_diarist, remove_diarist
from django.urls import path

urlpatterns = [
    path('register_diarist', register_diarist, name='register_diarist'),
    path('list_diarists', list_diarists, name='list_diarists'),
    path('edit_diarist/<int:diarist_id>', edit_diarist, name='edit_diarist'),
    path('remove_diarist/<int:diarist_id>', remove_diarist, name="remove_diarist")
]

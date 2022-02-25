from django.urls import path

from exam_27_06_2021.notes.views import show_index, create_note, edit_note, delete_note, details_note, show_profile, \
    create_profile, delete_profile

urlpatterns = (
    path('', show_index, name='show index'),
    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/<int:pk>/', delete_profile, name='delete profile'),
)

from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_contacts, name="get_contacts"),
    path("add_contact/", views.add_contact, name="add_contact"),
    path("remove_contact/<int:contact_id>/", views.remove_contact, name="remove_contact"),
    path("edit_contact/<int:contact_id>/", views.update_contact, name="edit_contact"),
    path("filter_contacts/", views.filter_contacts, name="filter_contacts"),
]
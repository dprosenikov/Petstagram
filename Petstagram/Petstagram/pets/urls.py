from django.urls import path
from Petstagram.pets.views import like_pet, comment_pet, \
    PetDetailsView, PetsListView, PetCreateView, PetEditView, PetDeleteView

urlpatterns = [
    path('', PetsListView.as_view(), name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', PetCreateView.as_view(), name='create pet'),
    path('edit/<int:pk>', PetEditView.as_view(), name='edit pet'),
    path('delete/<int:pk>', PetDeleteView.as_view(), name='delete pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),
]

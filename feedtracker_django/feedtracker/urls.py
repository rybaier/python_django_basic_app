from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('horses/', views.horse_index, name='horse_list'),
    path('horse/<int:horse_id>/', views.horse_detail, name='horse_detail'),
    path('horse/create/', views.Create_Horse.as_view(), name='create_horse'),
    path('horse/<int:horse_id>/update/', views.Update_Horse.as_view(), name='update_horse'),
    path('horse/<int:horse_id>/delete/', views.Delete_Horse.as_view(), name='delete_horse'),
    path('horse/<int:horse_id>/add_a_feeding', views.add_a_feeding, name='add_a_feeding'),
    # path('horse/<int:horse_id>/remove_feeding', )
    path('accounts/signup/', views.signup, name='signup'),
]
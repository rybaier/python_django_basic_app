from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('horses/', views.horse_index, name='horse_list'),
    path('horse/<int:horse_id>/', views.horse_detail, name='horse_detail'),
    path('horse/create/', views.Create_Horse.as_view(), name='create_horse'),
    path('horse/<int:pk>/update/', views.Update_Horse.as_view(), name='update_horse'),
    path('horse/<int:pk>/delete/', views.Delete_Horse.as_view(), name='delete_horse'),
    path('horse/<int:horse_id>/add_a_feeding', views.add_a_feeding, name='add_a_feeding'),
    path('horse/<int:horse_id>/create_feeding/', views.Create_Feeding.as_view(), name='create_feeding'),
    path('feedings/<int:horse_id>', views.feeding_index, name= 'feed_list'),
    path('feedings/<int:pk>/update_feeding/', views.Update_Feeding.as_view(), name='update_feeding'),
    path('feedings/<int:pk>/delete_feeding/', views.Delete_Feeding.as_view(), name='delete_feeding'),
    path('accounts/signup/', views.signup, name='signup'),
]

    # path('feedings/create_feeding/', views.Create_Feeding.as_view(), name='create_feeding'),
    # path('feedings/<int:pk>/update/', views.Update_Feeding.as_view(), name='update_feeding'),
    # path('feedings/<int:pk>/delete/', views.Delete_Feeding.as_view(), name='delete_feeding'),
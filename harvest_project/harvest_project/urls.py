# harvest_project/urls.py
from django.urls import path
from harvest.views import RegisterView, HarvestListCreateView, HarvestRetrieveUpdateDeleteView  # Ajuste a importação para a pasta 'harvest'
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('harvests/', HarvestListCreateView.as_view(), name='harvest-list-create'),
    path('harvests/<int:pk>/', HarvestRetrieveUpdateDeleteView.as_view(), name='harvest-retrieve-update-delete'),

    # JWT Auth
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


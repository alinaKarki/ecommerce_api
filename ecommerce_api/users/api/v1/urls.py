from django import views
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserRegisterView

app_name = "users_api_v1"

router = DefaultRouter()
# router.register(r"register", UserViewSet)
# router.register(r"product",ProductView)


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="login"),
    # path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
]

urlpatterns += router.urls

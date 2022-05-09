from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ecommerce_api.users.api.v1.serializers import UserSerializer

from .serializers import UserRegistrationSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        "password1", "password2", "new_password1", "new_password2"
    )
)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(UserRegisterView, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"detail": ("User Created Successfully")},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

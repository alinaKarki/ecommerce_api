from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as VError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "first_name","last_name","email"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserRegistrationSerializer(serializers.Serializer):
    """
    Customer signup serializer.
    """

    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email"]

  
    def validate(self, data):
        email = data["email"]
        password = data["password1"]
        errors = {}

        if password != data["password2"]:
            errors["password2"] = "password1 and password2 did not match."
        if User.objects.filter(email=email).exists():
            errors["email"] = "User with that email already exists"
        if errors:
            raise serializers.ValidationError(errors)
        return data

    # def validate_email(self, email):
    #     return email

    def create(self, validated_data):
        email = self.validated_data["email"]
        user = User(email=email)
        user.set_password(validated_data["password1"])
        user.save()
        return user



from rest_framework import serializers
from users.models import User as UserManager



class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields="username", "password"

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user


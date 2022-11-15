from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserManager

class UserRegisterationAPIViewTestCase(APITestCase):
    def test_registeration(self):
        url = reverse("user_view")
        user_data = {
            "username":"test1",
            "password":"1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data["message"], "가입 완료!!")
        
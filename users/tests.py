from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Test Course', description='Test Course description')
        self.client.force_authenticate(user=self.user)

    def test_subscription_toggle(self):
        url = reverse("users:subscription_toggle", args=(self.course.pk,))
        response = self.client.post(url)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        response = self.client.post(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        response = self.client.post(url)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

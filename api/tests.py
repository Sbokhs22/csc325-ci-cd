from django.test import TestCase
from django.urls import reverse

class StatusAPITests(TestCase):
    def test_status_returns_http_200(self):
        response = self.client.get(reverse('api-status'))
        self.assertEqual(response.status_code, 200)

    def test_status_response_contains_expected_fields(self):
        response = self.client.get(reverse('api-status'))
        self.assertEqual(response.json()['status'], 'ok')
        self.assertEqual(response.json()['message'], 'CSC 325 CI/CD API')

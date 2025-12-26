"""
Test file for core app
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import HousePlan

class HousePlanTestCase(TestCase):
    def setUp(self):
        HousePlan.objects.create(
            name="Test Plan",
            price=250000,
            bedrooms=3,
            bathrooms=2,
            square_feet=2500
        )

    def test_house_plan_creation(self):
        plan = HousePlan.objects.get(name="Test Plan")
        self.assertEqual(plan.bedrooms, 3)

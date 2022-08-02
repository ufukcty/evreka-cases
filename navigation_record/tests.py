from django.test import TestCase
from rest_framework.test import APIClient
from .models import Vehicle, NavigationRecord
import datetime


class NavigationRecordTestCase(TestCase):
    vehicle = None

    def setUp(self) -> None:
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.vehicle = Vehicle.objects.create(plate="06 TST 71")
        cls.navigation_record = NavigationRecord.objects.create(
            latitude=06.06,
            longitude=71.71,
            vehicle=cls.vehicle,
            datetime=datetime.datetime(2022, 8, 2, 9, 3, 23, 402177)
        )

    def test_navigation_record(self):
        navigation_record = NavigationRecord(
            latitude=06.06,
            longitude=71.71,
            vehicle=self.vehicle,
            datetime=datetime.datetime(2022, 8, 2, 9, 3, 23, 402177)
        )
        self.assertEqual(navigation_record.latitude, 06.06)
        self.assertEqual(navigation_record.longitude, 71.71)
        self.assertEqual(navigation_record.vehicle.plate, self.vehicle.plate)
        self.assertEqual(navigation_record.datetime, datetime.datetime(2022, 8, 2, 9, 3, 23, 402177))

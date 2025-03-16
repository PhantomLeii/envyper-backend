from django.test import TestCase
from unittest import mock
from ..models import User, UserManager


class UserModelTests(TestCase):
    def setUp(self):
        # Set up mock manager
        self.manger = UserManager()
        self.manager.create_user = mock.MagicMock(return_value=True)

        # Set mock manger as model objects attribute
        self.model = User()
        self.model.objects = self.manager

        # User creation data
        self.user_data = {
            "email": "test@email.com",
            "password": "testuser123",
            "first_name": "test",
        }

    def test_create_user(self):
        pass

    def test_str_repr(self):
        pass

    def test_objects(self):
        pass

    def test_username_field(self):
        pass

    def test_required_fields(self):
        pass

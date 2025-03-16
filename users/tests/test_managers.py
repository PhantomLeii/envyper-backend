from django.test import TestCase
from ..models import UserManager, User


class TestUserManager(TestCase):
    def setUp(self):
        self.user_model = User
        self.user_manager = UserManager()

        # Set Manager's model attribute
        self.user_manager.model = self.user_model

        # Test payload data
        self.valid_user_data = {
            "email": "test@email.com",
            "password": "testuser123",
            "first_name": "Test",
            "last_name": "User",
        }

        self.valid_superuser_data = {
            "email": "admin@email.com",
            "password": "adminuser123",
            "first_name": "Admin",
            "last_name": "User",
        }

    def test_create_user(self):
        user = self.user_manager.create_user(**self.valid_user_data)

        with self.subTest("User of the correct type"):
            self.assertTrue(isinstance(user, self.user_model))
            self.assertEqual(str(user), self.valid_user_data["email"])

        self.assertEqual(
            user.email,
            self.valid_user_data["email"],
            "User object email is not the same as provided data.",
        )
        self.assertEqual(
            user.first_name,
            self.valid_user_data["first_name"],
            "User object first_name is not the same as provided data",
        )
        self.assertEqual(
            user.last_name,
            self.valid_user_data["last_name"],
            "User object last_name is not the same as provided data",
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(
            user.check_password(self.valid_user_data["password"]),
            "User object password does not match provided data",
        )

    def test_invalid_create_user(self):
        with self.assertRaises(ValueError):
            self.user_manager.create_user({**self.valid_user_data, "email": ""})

        with self.assertRaises(ValueError):
            self.user_manager.create_user({**self.valid_user_data, "password": ""})

        with self.assertRaises(ValueError):
            self.user_manager.create_user({**self.valid_user_data, "first_name": ""})

    def test_valid_create_superuser(self):
        superuser = self.user_manager.create_superuser(self.valid_superuser_data)

        self.assertEqual(
            superuser.email,
            self.valid_superuser_data["email"],
            "Super user object email does not match provided data",
        )
        self.assertEqual(
            superuser.first_name,
            self.valid_superuser_data["first_name"],
            "Super user object first name does not match provided data",
        )
        self.assertEqual(
            superuser.last_name,
            self.valid_superuser_data["last_name"],
            "Super user object last name does not match provided data",
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertTrue(
            superuser.check_password(self.valid_superuser_data["password"]),
            "Super user object password does not match provided data",
        )

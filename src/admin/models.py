from fastapi_admin.models import User
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class AdminUser(User):
    """Модель Амдин-пользователя."""

    is_active = fields.BooleanField(default=False, description="Is Active")
    is_superuser = fields.BooleanField(default=False, description="Is Superuser")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "admin_user"


AdminUser_Pydantic = pydantic_model_creator(AdminUser, name="AdminUser")
AdminUserIn_Pydantic = pydantic_model_creator(
    AdminUser, name="AdminUser", exclude_readonly=True
)

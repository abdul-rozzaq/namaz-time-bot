from tortoise.models import Model
from tortoise import fields


class TelegramUser(Model):
    id = fields.IntField(primary_key=True)
    telegram_id = fields.BigIntField(unique=True)
    region_id = fields.IntField()

    def __str__(self):
        return f"User(id={self.id}, telegram_id={self.telegram_id}, region_id={self.region_id})"

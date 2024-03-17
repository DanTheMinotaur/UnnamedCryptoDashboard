from tortoise.models import Model
from tortoise import fields


class Crypto(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    symbol = fields.CharField(max_length=10, unique=True)
    meta = fields.JSONField(null=True)

    def __str__(self):
        return f'{self.name}({self.symbol})'

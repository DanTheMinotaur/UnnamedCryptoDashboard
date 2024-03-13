from tortoise.models import Model
from tortoise import fields


class CryptoPriceHistory(Model):
    id = fields.IntField(pk=True)
    unit_value = fields.FloatField()
    timestamp = fields.DatetimeField()
    fiat_currency = fields.CharField(max_length=10)
    updated_at = fields.DatetimeField(null=False, auto_now_add=True)

    crypto = fields.ForeignKeyField('models.Crypto', 'history_crypto')
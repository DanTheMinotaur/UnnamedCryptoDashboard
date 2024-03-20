from tortoise.models import Model
from tortoise import fields


class Crypto(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    symbol = fields.CharField(max_length=100, unique=True)


class Historical(Model):
    dollar_value = fields.FloatField()
    date = fields.DateField()

    crypto = fields.ForeignKeyField('models.Crypto', 'history_crypto')

    class Meta:
        unique_together = (('date', 'crypto'),)

from tortoise.models import Model
from tortoise import fields

class Holdings(Model):
    id = fields.IntField(pk=True)
    units = fields.FloatField()
    entry_added = fields.DatetimeField(null=False, auto_now_add=True)

    crypto = fields.ForeignKeyField('models.Crypto', 'holdings_crypto')

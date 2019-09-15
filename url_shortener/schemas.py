from flask import Blueprint
from flask_marshmallow import Marshmallow

short = Blueprint('short', __name__)
ma = Marshmallow(short)


# Account Schema
class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'account_id', 'password')


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)


# Link Schema
class LinkSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'original_url',
            'short_url',
            'redirect_type',
            'visits',
            'account_id'
            )


link_schema = LinkSchema()
links_schema = LinkSchema(many=True)

import random
import string

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from .models import Account
from .schemas import accounts_schema

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account_id, password):

    all_accounts = Account.query.all()
    account_dicts = accounts_schema.dump(all_accounts)

    for item in account_dicts:
        if item["account_id"] == account_id:
            account = Account.query.filter(Account.account_id == account_id).first()
            return check_password_hash(account.password, password)
    return False


def randomString(stringLength=8):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

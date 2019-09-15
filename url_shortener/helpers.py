import random
import string
from flask_httpauth import HTTPBasicAuth
from .models import Account, Link
from .schemas import account_schema, accounts_schema, link_schema, links_schema
from werkzeug.security import generate_password_hash, check_password_hash

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

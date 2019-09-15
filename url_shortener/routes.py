from flask import Blueprint, redirect, request
from werkzeug.security import generate_password_hash

from .extensions import db
from .helpers import auth, randomString
from .models import Account, Link
from .schemas import accounts_schema, links_schema

short = Blueprint('short', __name__)


@short.route('/account', methods=['POST'])
def add_user():
    new_password = randomString()
    try:
        account_id = request.json['account_id']
    except KeyError:
        return {
            "success": False,
            "description": "Please provide account_id."
        }, 400

    all_accounts = Account.query.all()
    account_dicts = accounts_schema.dump(all_accounts)

    for item in account_dicts:
        if item["account_id"] == account_id:
            return {
                "success": False,
                "description": "Account_id already exists."
            }, 400

    password = generate_password_hash(new_password)

    new_account = Account(account_id, password)

    db.session.add(new_account)
    db.session.commit()

    return {
        "success": True,
        "description": "Account created successfully.",
        "password": new_password
        }, 201


@short.route('/register', methods=['POST'])
@auth.login_required
def add_link():
    try:
        original_url = request.json['url']
    except KeyError:
        return {"error": "Please provide a url."}, 400

    try:
        redirect_type = request.json['redirect_type']
    except KeyError:
        redirect_type = 302

    all_links = Link.query.all()
    link_dicts = links_schema.dump(all_links)

    for item in link_dicts:
        if item["original_url"] == original_url:
            return {"error": "Url already in database."}, 400

    auth = request.authorization
    if auth:
        account = Account.query.filter_by(
            account_id=auth.username).first_or_404()

    link = Link(
        original_url=original_url,
        account_id=account.id,
        redirect_type=redirect_type
        )
    db.session.add(link)
    db.session.commit()

    return {"short_url": "http://localhost:5000/" + link.short_url}, 201


@short.route('/statistic/<account_id>', methods=['GET'])
def stats(account_id):
    account = Account.query.filter_by(id=account_id).first_or_404()

    links = Link.query.filter_by(account_id=account_id)
    link_dict = {}

    for link in links:
        link_dict[link.original_url] = link.visits

    return link_dict


@short.route('/<short_url>')
@auth.login_required
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits += 1
    db.session.commit()

    return redirect(link.original_url, code=link.redirect_type)

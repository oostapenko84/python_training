__author__ = 'olga.ostapenko'

from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group (Group(name="updated name", header="updated header", footer="updated footer"))
    app.session.logout()

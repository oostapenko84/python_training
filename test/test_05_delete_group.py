__author__ = 'olga.ostapenko'

from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.delete_first_group()
    app.session.logout()

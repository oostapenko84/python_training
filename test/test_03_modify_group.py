__author__ = 'olga.ostapenko'

from model.group import Group


def test_modify_group_fields(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    old_groups = app.group.get_group_list()
    group = Group(name="updated", header="updated", footer="updated")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.session.logout()

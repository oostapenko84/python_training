# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="yyy", header="yyy", footer="yyy")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # add new group to old groups list
    old_groups.append(group)
    # sort old_groups (that already included new group) by int(id) and compare it to sorted new_groups by int(id)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.session.logout()

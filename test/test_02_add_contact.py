# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(First_Name="Olga", Middle_Name="Sergeevna", Last_Name="Ostapenko", Company_Name="Test Company",
                Address="Test Address", Home_Phone="12345", Mobile_Phone="12345", Work_Phone="12345",
                Email="test@test.com", Homepage="www.test.com", Birthday="1984", Anniversary="2017",
                Secondary_Address="Test Address"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(First_Name="", Middle_Name="", Last_Name="", Company_Name="", Address="", Home_Phone="",
                               Mobile_Phone="", Work_Phone="", Email="", Homepage="", Birthday="", Anniversary="",
                               Secondary_Address=""))
    app.session.logout()

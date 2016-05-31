# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(First_Name="Olga", Middle_Name="Sergeevna", Last_Name="Ostapenko", Company_Name="Test Company", Address="Test Address", Home_Phone="12345", Mobile_Phone="12345", Work_Phone="12345",Email="test@test.com", Homepage="www.test.com", Birthday="1984", Anniversary="2017", Secondary_Address="Test Address"))
    app.logout()

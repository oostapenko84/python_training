__author__ = 'olga.ostapenko'

from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(First_Name="test", Middle_Name="test", Last_Name="test", Company_Name="Test Company",
                                   Address="Test Address", Home_Phone="12345", Mobile_Phone="12345", Work_Phone="12345",
                                   Email="test@test.com", Homepage="www.test.com", Birthday="1984", Anniversary="2017",
                                   Secondary_Address="Test Address"))
    app.contact.delete_first_contact()
    app.session.logout()

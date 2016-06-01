__author__ = 'olga.ostapenko'

from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(First_Name="Updated First_Name", Middle_Name="Updated Middle_Name", Last_Name="Updated Last_Name", Company_Name="Updated Company_Name", Address="Updated Address", Home_Phone="Updated Home_Phone", Mobile_Phone="Updated Mobile_Phone", Work_Phone="Updated Work_Phone", Email="Updated Email", Homepage="Updated Homepage", Birthday="1984", Anniversary="2017", Secondary_Address="Updated Secondary_Address"))
    app.session.logout()
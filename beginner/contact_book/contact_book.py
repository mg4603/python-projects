import sqlite3
import helper
import phonenumbers
connection = sqlite3.connect('contact_book.db')


def add_contact():
    first_name = helper.validated_name("Enter first name")
    second_name = helper.validated_name("Enter second name")
    phone_no = phonenumbers.parse(
            input("Enter phone number: +(country_code) phone_number "))
    email = helper.validated_email("Enter email")
    
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT
            INTO
                contacts
            VALUES(
                %(first_name)s,
                %(second_name)s,
                %(country_code)s,
                %(phone_no)d,
                %(email)s)
        """,{'first_name':first_name,
             'second_name':second_name,
             'country_code': phone_no.country_code,
             'phone_no':phone_no.national_number,
             'email': email
            })

def update_contact():
    

def show_contact(name):
    with connection.cursor as cursor:
        cursor.execute("""
                SELECT 
                    *
                FROM
                    contacts
                WHERE
                    first_name = %(first_name)s
                """,{'first_name': name})


def show_all_contacts():
    with connection.cursor as cursor:
        cursor.execute("""
                SELECT 
                    *
                FROM
                    contacts
                """)

def delete_contact(name):
    with connection.cursor as cursor:
        cursor.execute("""
                DELETE FROM
                    contacts
                WHERE
                    first_name = %(first_name)s
                """,{'first_name':name})


def main():

    print("Contact Book:")
    print("\t1. search")
    print("\t2. show all")
    print("\t3. add contact")
    print("\t4. update contact")
    print("\t5. delete contact")
    print("\t6. close")
    
if __name__=="__main__":
    main()

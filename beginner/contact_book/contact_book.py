import sqlite3
import helper

connection = sqlite3.connect('contact_book.db')


def add_contact():
    first_name = input("Enter first name")

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT
            INTO
                contacts
            VALUES(
                %(first_name)s,
                %(second_name)s,
                %(phone_no)d,
                %(address)s,
                %(email)s)
        """,{'first_name':first_name,
             'second_name':second_name,
             'phone_no':phone_no,
             'address': address,
             'email': email
            })

def update_contact():
    pass

def show_contact(name):
    pass

def show_all_contacts():
    pass

def delete_contact(name):
    pass


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

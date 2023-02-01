from xml.dom import UserDataHandler
import random
import string

 
def user_details():
    """
    Prompt user input
    """
    firstName = input("Enter Fist Name")
    lastName = input("Enter Last Name")
    chort = input("Enter Chort")
    finalCampus = input("Enter Final Campus")

    print(firstName,lastName, chort, finalCampus)

def create_username(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    letters = string.ascii_letters + string.digits
    length = 10
    cohort = str(cohort)[:3]
    username = first_name[0] + last_name + cohort + final_campus[:2]
    if len(username) > length:
        username = username[:length]
    else:
        username += ''.join(random.choice(letters) for i in range(length - len(username)))
    return username

print(create_username("John", "Doe", 123456, "Campus1"))


def user_campus(campus):
    """
    Return valid campus abbreviations
    """


if __name__ == '__main__':
    user_details()
    
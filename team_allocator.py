
def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_campus_students = []
    for student in student_list:
        if "Durban" in student:
            dbn_campus_students.append(dbn_campus_students)

    return dbn_campus_students

def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []
    for student in student_list:
        if "CPT" in student:
           
            cpt_students.append(student)
    return cpt_students

def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []
    for student in student_list:
        if "JHB" in student:
            jhb_students.append(student)
    return jhb_students


def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []
    for student in student_list:
        if "North West" in student:
            nw_students.append(student)
    return nw_students
    
def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_campus_students
    for student in student_list:
        if "Durban Physical" in student:
            dbn_physical_students.append(student)
    return dbn_physical_students

def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    ''' 
    for student in dbn_physical_students:
        count += 1
        team.append(student)
        if count % 4 == 0:
            dbn_physical_teams.append(team)
            team = []
            return dbn_physical_teams


def show_employee(name, salary):
    print(name, salary)
    
    name = input()
    salary = int(input())


def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    with open("student_list", "w") as file:
        for key, value in dbn_physical_teams.items():
           file.write(f"{key}: {value}\n")
        

def cpt_physical_students(cpt_physical_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    for students in student_list:
        if("Cape Town Physical" in students):
            print(students)

    return cpt_physical_students


def cpt_physical_teams(cpt_physical_teams):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    with open("cpt_physical_teams.txt", "w") as file:
        file.write(cpt_physical_teams)

    
    return cpt_physical_teams


def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    with open(cpt_physical_teams, "w") as file:
        file.write(cpt_physical_teams)

    return

def jhb_physical_students(jhb_physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    with open(jhb_physical_students, "w") as file:
        file.write(cpt_physical_teams)

    return jhb_physical_students

def jhb_physical_teams(jhb_physical_teams):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    with open("cpt_physical_teams.txt", "w") as file:
        file.write(cpt_physical_teams)

    return jhb_physical_teams

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    with open(jhb_physical_teams, "w") as file:
        file.write(cpt_physical_teams)

    return jhb_physical_teams


def nw_physical_students(nw_physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    with open(jhb_physical_teams, "w") as file:
        file.write(cpt_physical_teams)

    return nw_physical_students


def nw_physical_teams(nw_physical_teams):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    with open(jhb_physical_teams, "w") as file:
        file.write(cpt_physical_teams)


    return nw_physical_teams

def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    with open(jhb_physical_teams, "w") as file:
        file.write(cpt_physical_teams)

    return nw_physical_students

def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []

    return virtual_campus

def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []

    return virtual_teams

def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    with open(jhb_physical_teams, "w") as file:
        file.write(cpt_physical_teams)


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    studenrt_list= student_list()
    cpt_students = cpt_campus_students(studenrt_list)
    print(cpt_students)

import csv
def write_in_csv(Student_info):
    with open('student_info.csv','a',newline='') as csv_file:
        a=csv.writer(csv_file)
        if csv_file.tell()== 0:
            a.writerow(["Name","Age","Contact Number","E-Mail ID"])
        a.writerow(Student_info)
if __name__=='__main__':
    condition=True
    student_Num=1
    while(condition):
        student_info=input("Enter the student #{} information in the following format (Name Age Contact_Number Email_ID):".format(student_Num))
        student_info_list=student_info.split(' ')
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nEmail_ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check_here=input("Is the above Entry is correct? Y/N:")
        if check_here=='Y':
            write_in_csv(student_info_list)
            check_next=input('Do you want to add another student student information? Y/N:')
            if check_next=='Y':
                condition=True
                student_Num=student_Num+1
            elif check_next=='N':
                condition=False
        elif check_here=='N':
            print('Please re-enter the correct details!')



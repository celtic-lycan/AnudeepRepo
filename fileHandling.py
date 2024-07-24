# file = open("Kunal.txt",'r')
# file.write("Welcome to python class ...")
# file.write("hii I am pd ...")
# file.write("hii he is pratham ")
# print(file.tell())
# file.seek(5)
# print(file.read(10))
# print(file.tell())                #to get the position of file pointer
# file.close()

# print("Data inserted successfully .")



# question - 1   
# Searching data in file 

# file_path = "kunal.txt"
# search_keyword = input("Enter the text which you want to search : ")
# with open(file_path,'r') as f:
#     for line in f:
#         if(search_keyword.lower() in line.lower()):
#             print(line.strip())

# print(f"Search for {search_keyword} completed. ")

# import pickle
# file = open("anudip.dat","wb")
# li = [10,20,60,80,90]
# pickle.dump(li,file)

# f = open("anudip.dat",'rb')
# data = pickle.load(f)
# print(data)
# f.close()

# import csv
# f = open("anudip.csv",'a',newline='')
# wo = csv.writer(f)
# data = [["a",'b','c','d'],[43,75,34,89],[23,45,68,698],[65,87,98,54]]
# wo.writerows(data)
# f.close()


# import csv 
# f = open('anudip.dat','r')
# re = csv.reader(f)
# li = list(re)
# print(li)
# # for row in li:
# #     print(row)
# f.close()

# question - 2
# count number , vowel and consonant in file

# vowel = ['a','e','i','o','u']
# n , v, c = 0,0,0
# with open("Kunal.txt",'r') as file:
#     for line in file:
#         for ch in line:
#             if(ch.isdigit()):
#                 n += 1
#             elif(ch.lower() in vowel):
#                 v += 1
#             elif(ch.isalpha() and ch.lower() not in vowel):
#                 c += 1

# print(f"Numbers are : {n}")
# print(f"Vowels are : {v}")
# print(f"Consonants are : {c}")


# question -3
# count uppercase characters in a text file 

# count = 0
# with open("kunal.txt",'r') as file:
#     for line in file:
#         for ch in line:
#             if(ch.isupper()):
#                 count += 1
# print(f"Uppercase characters are : {count}")

# question - 4
# count and display total number of words in a text file 

# with open("Kunal.txt",'r') as file:
#     content = file.read()
#     words = content.split()
#     count = len(words)
# print(f"Total number of words in file : {count}")
# print(words)

# question - 5
# read the content line by line and display the same 

# with open("Kunal.txt",'r') as file:
#     for line in file:
#         print(line)


# question - 6
# read line and display words which contain less than 4 characters

# def display_words(filename):
#     with open(filename,'r') as file:
#        for line in file:
#            words = line.split()
#            for word in words:
#                if(len(word) < 4):
#                    print(word, end=' ') 
#            print(end='\n')

# display_words("Kunal.txt")

# question - 7
# count occurance of a word in a text file 
# def occurance(filename,searchword):
#     count = 0
#     with open(filename,'r') as file:
#         content  = file.read()
#         words = content.split()
#         for word in words:
#             if(word.lower() == searchword.lower()):
#                 count += 1
#         print(f"Count of {searchword} is : {count}")
# occurance("Kunal.txt",'in')


# question - 8
# store data of students as id, name and marks in a binary file and display name if marks greater than 90

# import pickle

# def get_student_data():
#     students = []
#     while True:
#         # Get user input for student details
#         student_id = input("Enter student ID (or type 'done' to finish): ")
#         if student_id.lower() == 'done':
#             break
#         name = input("Enter student name: ")
#         marks = int(input("Enter student marks: "))
        
#         # Create a dictionary for the student
#         student = {'id': student_id, 'name': name, 'marks': marks}
#         students.append(student)
    
#     return students

# # Step 1: Get student data from user and store it in a binary file
# students = get_student_data()

# with open('students.pkl', 'rb') as file:
#     existing_data = pickle.load(file)

# whole_data = students + existing_data

# with open('students.pkl', 'wb') as file:
#     pickle.dump(whole_data, file)

# # Step 2: Read the data from the binary file and display names with marks >= 90
# with open('students.pkl', 'rb') as file:
#     loaded_students = pickle.load(file)

# # Display names of students with marks >= 90
# print("\nStudents with marks >= 90:")
# for student in loaded_students:
#     if student['marks'] > 90:
#         print(student['name'])




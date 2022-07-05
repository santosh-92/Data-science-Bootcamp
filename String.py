#1 . Try to extract data from index one to index 300 with a jump of 3
import logging
logging.basicConfig(filename="stringTasks.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(message)s')

class StringTasks :

    def extract_data(self, s):


        try:

            logging.info("Given string is: %s",s)
            s1 = s[1:300:3]
            logging.info("The output of the operation is: %s",s1)
            return s1
        except Exception as e:
            logging.exception("The exception received is:" + "\n" + str(e))

obj=StringTasks()

obj.extract_data("this is My First Python programming class and i am learNING python string and its function")

#2. Try to reverse a string without using reverse function

    def reverse_string(self,s):
        try:
            logging.info("Given string for this operation is: %s" , s)
            s2 = s[::-1]
            logging.info("Output of reverse operation is: %s" , s2)
            return s2
        except Exception as e:
            logging.exception("Exception we have received is:" + "\n" + str(e))

obj=StringTasks()
obj.reverse_string("this is My First Python programming class and i am learNING python string and its function")


#3. Try to split a string after conversion of entire string in uppercase
    def split_upper(self,s):
        try:
            logging.info("Given string is: %s" , s)
            s3 = s.upper().split(' ')
            logging.info("Output after converting upper case and split is: %s" ,s3)
        except Exception as e:
            logging.exception("The exception we have received is:" + "\n" + str(e))

obj=StringTasks()
obj.split_upper("this is My First Python programming class and i am learNING python string and its function")

#4. try to convert the whole string into lower case
    def lower(self,s):
        try:

            logging.info("Given string is: %s" , s)
            s4 = s.lower()
            logging.info("The output of lower operation is: %s", s4)
            return s4
        except Exception as e:
            logging.exception("The exception have received is:" + "\n" + str(e))

obj=StringTasks()
obj.lower("this is My First Python programming class and i am learNING python string and its function")


#5 . Try to capitalize the whole string
    def capitalize(self,s):
        try:
            logging.info("Given string is: %s", s)
            s5 = s.capitalize()
            logging.info("Output after capitalization is: %s", s5)
            return s5
        except Exception as e:
            logging.info("Exception received is %s" + "\n" + str(e))

obj=StringTasks()
obj.capitalize("this is My First Python programming class and i am learNING python string and its function")

#6 . Write a diference between isalnum() and isalpha()
#isalnum()--->It works with or condition, whether string atleast contains alphabetic or numeric, then it gives true
#isalpha()--->It checkes whether string of all characters  contains numeric only or not


#7. Try to give an example of expand tab
    def expand(self, s):
        try:
            logging.info("The given string is: %s",s)
            s6 = s.expandtabs()
            logging.info("Output after expand is: %s",s6)
            return s6
        except Exception as e:
            logging.exception("Exception received is %s" + "\n" + str(e))

obj=StringTasks()
obj.expand("this is My First Python programming class and i am learNING python string and its function")

#8 . Give an example of strip , lstrip and rstrip
    def strip(self, s):
        try:
            logging.info("The given string for this operation is: %s", s)
            s7 = s.strip()
            logging.info("The output of the operation is: %s", s7)
            return s7
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def lstrip(self, s):
        try:
            logging.info("The given string for this operation is: %s", s)
            s8 = s.lstrip()
            logging.info("The output of the operation is: %s", s8)
            return s8
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def rstrip(self, s):
        try:
            logging.info("The given string for this operation is: %s", s)
            s9 = s.rstrip()
            logging.info("The output of the operation is: %s", s9)
            return s9
        except Exception as e:
            logging.exception("The exception that we have got: " + "\n" + str(e))

obj=StringTasks()
obj.strip("this is My First Python programming class and i am learNING python string and its function")
obj.lstrip("this is My First Python programming class and i am learNING python string and its function")
obj.rstrip("this is My First Python programming class and i am learNING python string and its function")

#9. Replace a string character by another charactor by taking your own example "sudhanshu"
    def replace(self, s, a, b):
        try:
            logging.info("The given string for this operation is: %s", s)
            s10 = s.replace(a, b)
            logging.info("The output of the operation is: %s", s10)
            return s10
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

obj=StringTasks()
obj.replace("this is My First Python programming class and i am learNING python string and its function" , 'Python', 'java')

#10 . Try to give a definition of string center function with and example
#Defnition of string center function Ans-Return a centered string of length width. see below example
    def filling_spaces_with_characters(self, s):
        try:
            logging.info("The given string for this operation is: %s", s)
            s11 = s.center(20, '*')
            logging.info("The output of the operation is: %s", s11)
            return s11
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
obj=StringTasks()
obj.filling_spaces_with_characters("Ineuron")


#11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
#Compiler: On any programming language platoform, Whenever we gives logic with inputs, it converts program into its own machine language  and processes in backend and throws output.
#interpreter: It dont translates in some other format. It directly executes the written instruction in the program

#12 . Python is a interpreted of compiled language give a clear ans with your understanding
#Python is complied as well as interpreted language, first it compiles and then it interprets (.pyc) the writen progam

#13 . Try to write a usecase of python with your understanding.
#Python is used for:
#-To develop websites & software
#-Task automation
#-Data analysis
#-data visulization
#-etc


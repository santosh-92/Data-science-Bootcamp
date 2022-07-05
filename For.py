import logging

logging.basicConfig(filename="list.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class Task()
    def

row = int(input("Please enter how many rows you want to print: "))
print()
for i in range(row):
    print("ineuron "*(i+1))

for i in range(6):
    if i <= 3:
        n = i
    else:
        n = 6 - i
    print(("ineuron "*n).center(30,' '))

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

#q3 : Try to extract all the list entity
    def exctractList(self, l):

        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list:
                    l1.append(i)
            logging.info("Required list is: %s", l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))


obj = Task()
obj.exctractList([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                   {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])


#q4 : Try to extract all the dict enteties
    def exctractDict(self, l):

        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == dict:
                    l1.append(i)
            logging.info("Required dictionary is: %s", l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj = Task()
obj.exctractDict([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3":"kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])


#q5 : Try to extract all the tuples entities
    def exctractTuple(self,l):
        try:
            l1= []
            logging.info("Given list is: %s",l)
            for i in l:

                if type(i) == tuple:
                    l1.append(i)
            logging.info("Required tuple is: %s",l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj=Task()
obj.exctractTuple([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])




#q6 : Try to extract all the numerical data it may b a part of dict key and values

    def exctractnumbers(self,l):
        try:
            l1= []
            logging.info("Given list is: %s",l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            logging.info("Required numbers is: %s",l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj=Task()
obj.exctractnumbers([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])


#q7 : Try to give summation of all the numeric data

    def summation(self, l):
        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            logging.info("Required numbers is: %s", l1)
            logging.info("sum of numbers: %s", sum(l1))
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj = Task()
obj.summation([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])


#q8 : Try to filter out all the odd values out all numeric data which is a part of a list

    def exctractoddnumbers(self, l):
        try:
            l1 = []
            odd_list = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)

            logging.info("Required numbers is: %s", l1)
            for i in l1:
                if i % 2 != 0:
                    odd_list.append(i)
            logging.info("odd numbers are : %s", odd_list)
            return odd_list

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))


obj = Task()
obj.exctractoddnumbers([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                     {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])

#q9 : Try to extract "ineruon" out of this data
    def exctractword(self, l):
        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l1.append(g)
            logging.info("Required word is: %s", l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj = Task()
obj.exctractword([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])



#q10 : Try to find out a number of occurances of all the data
    def exctractoccurances(self, l):
        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l1.append(g)

            logging.info("Required occurances is: %s", l1)
            for i in set(l1):
                print(i , ":" , l1.count(i))

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))


obj = Task()
obj.exctractoccurances([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])



#q11 : Try to find out number of keys in dict element

    def extractKeys(self, l):
        try:
            logging.info("Given list is : %s", l)
            for i in l:
                if type(i) == dict:
                    for k in i.keys():
                        logging.info("Required keys are : %s", k)
            l.append(k)
            return l

        except Exception as e:
            logging.exception(e)


obj = Task()
obj.extractKeys([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])




#q12 : Try to filter out all the string data
    def exctract_string(self, l):
        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:
                if type(i) == str:
                    l1.append(i)
            logging.info("Required string is: %s", l1)
            return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))


obj = Task()
obj.exctract_string([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                   {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])




#q13 : Try to Find  out alphanum in data
    def exctract_alnum(self, l):
        try:
            l1 = []
            logging.info("The given list for this operation is %s", l)
            for i in l:
                if (type(i) == list or type(i) == tuple or type(i) == set):
                    for j in i:
                        if (type(j) == str and j.isalnum()):
                            l1.append(j)
                if (type(i) == dict):
                    for k, v in i.items():
                        if (type(k) == str and k.isalnum()):
                            l1.append(k)
                        if (type(v) == str and v.isalnum()):
                            l1.append(v)
            logging.info("The output of the operation is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


obj = Task()
obj.exctract_alnum([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":"kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])


#q14 : Try to find out multiplication of all numeric value in the individual collection inside dataset
    def multiply(self, l):
        try:
            l1 = []
            logging.info("Given list is: %s", l)
            for i in l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            logging.info("Required numbers is: %s", l1)
            j = 1
            for i in l1:
                if type(i) == int:
                    j = j * i
                    logging.info("Multiplication of  numbers is: %s", j)
            return j


        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))


obj = Task()
obj.multiply([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
               {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])
#Task 2
import logging

logging.basicConfig(filename="list.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

# 1 . Try to reverse a list

class ListTasks:

  def reverse_list(self,l):
    try:

      logging.info("Given list is: %s", l)
      l.reverse()
      logging.info("Output after reverse is: %s", l)
      return l

    except Exception as e:
      logging.exception("Exception received is:" + "\n" + str(e))


obj=ListTasks()
obj.reverse_list( [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])



#2 . try to access 234 out of this list
  def access(self, l):
      try:
        logging.info("Given list is: %s", l)
        l1 = l[7][0]
        logging.info("the exact number is: %s", l1)
        return l1
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.access([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])



#3 . try to access 456
  def access1(self, l):
      try:
        logging.info("Given list is: %s", l)
        l2 = l[5][1]
        logging.info("the exact number is: %s", l2)
        return l2
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.access1([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])



#4 . Try to extract only a list collection form list l

  def List1(self, l):
      try:
        logging.info("Given list is: %s", l)
        l3 = l[5:7]
        logging.info("The only list is: %s", l3)
        return l3
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.List1([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])


#5 . Try to extract "sudh"
  def word(self, l):
      try:
        logging.info("Given list is: %s", l)
        l5=l[8]['key1']
        logging.info("The required word is: %s", l5)
        return l5
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.woard([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])



#6 . Try to list all the key in dict element available in list
  def keys(self, l):
      try:
        logging.info("Given list is: %s", l)
        l6=list(l[8].keys())
        logging.info("The required keys are: %s", l6)
        return l6
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.keys([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])


#7 . Try to extract all the value element form dict available in list
  def values(self, l):
      try:
        logging.info("Given list is: %s", l)
        l7=list(l[8].values())
        logging.info("The required keys are: %s", l7)
        return l7
      except Exception as e:
        logging.exception("Exception received is:"+"\n"+str(e))
obj=ListTasks()
obj.values([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])


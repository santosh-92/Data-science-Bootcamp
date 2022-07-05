import logging

logging.basicConfig(filename="listmix.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class Task():
    def exctractnumbers(self, l):
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
            for i in l1:
                if i % 2 != 0:
                    l1.append(i)
                    logging.info("odd numbers are : %s", l1)
                    return l1

        except Exception as e:
            logging.exception("Exception received is" + "\n" + str(e))

obj = Task()
obj.exctractnumbers([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])

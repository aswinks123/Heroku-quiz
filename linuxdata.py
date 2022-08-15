from pywebio.input import *
from pywebio.output import *
from flask import  Flask
from pywebio.session import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH




def linux(): #Method
    c=0
    count=0
    #Dictionary that stores questions and answers. Key is the correct answer.
    dict = {'Mac': ["Which is not a linux distribution?", 'Debian', 'Ubuntu', 'Redhat', "Mac"],
            'free': ["Command to see RAM usage?", "df", "free", "w", "ram"],
            '/etc/passwd':["Where is userid stored?",'/etc/passwd','/usr/details','/etc/login','/etc/hosts'],
            'wc': ["Which of the following command is used to count the total number of lines, words, and characters contained in a file?", 'wc', 'grep', 'top', 'count'],
            'rm': ["Identify the command which is used to remove files?", 'mv', 'rm', 'delete', 'trash'],
            'useradd': ["Which of the following command is used to add a new user to the system?", 'addnew', 'newuser', 'useradd', 'uadd']

            #Add more questions are per Requirement

            }


    #Adding the extracted dictionart data to radio button
    for key, value in dict.items():

        x = value
        y = key

        q1 = radio(x[0], [x[1], x[2], x[3], x[4]],required=True)
        if q1 == y:
            c += 1  #to count the correct answer
        count += 1  #to count total questions

    return c, count #returnig these count to main function





















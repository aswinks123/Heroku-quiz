from pywebio.input import *
from pywebio.output import *

def docker():
    c = 0
    count = 0

    # Dictionary that stores questions and answers. Key is the correct answer. (format : ans : [question, options])
    dict = {'-p': ["Which option is used to publish a port?", '-r', '-p', '-socket', "No port in Docker"],
            'docker pull': ["Command to download an image in Docker?", 'docker pull', 'docker fetch', 'docker import', "docker download"],
            'To save container state': ["Use of docker commit command?", 'To stop container', 'To save container state', 'To delete container', "No command name commit"],



            # Add more questions are per Requirement

            }

    # Adding the extracted dictionart data to radio button
    for key, value in dict.items():

        x = value
        y = key

        q1 = radio(x[0], [x[1], x[2], x[3], x[4]], required=True)
        if q1 == y:
            c += 1  # to count the correct answer
        count += 1  # to count total questions

    return c, count  # returnig these count to main function

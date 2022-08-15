from pywebio.input import *
from pywebio.output import *

def aws():
    c = 0
    count = 0

    # Dictionary that stores questions and answers. Key is the correct answer. (format : ans : [question, options])
    dict = {'EC2': ["Compute Engine of AWS?", 'MongoDB', 'Load Balancer', 'EC2', "S3"],
            'S3': ["Object Storage of AWS?", 'Lambda', 'ASG', 'EC2', "S3"],
            'ALB': ["layer 7 Load balancer?", 'ALB', 'ASG', 'EC2', "VPC"],
            'lambda': ["Serverless Engine?",'EC2', 'Pyserv', 'HyperV', 'lambda'],
            'Amazon web services': ["AWS full form?", 'Amazon web services', 'Amazon web server', 'Azure web services', 'Amazon world service'],


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

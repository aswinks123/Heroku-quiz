#Created by Aswin KS
#This project uses Python,Pywebio,Flask and other modules to create this Quiz App
#Feel free to clone the code.

import argparse
import setuptools.msvc
from pywebio.input import *
from pywebio.output import *
from flask import  Flask
from pywebio.session import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import re
import  time
from pywebio.session import run_js
from linuxdata import linux
from awsdata import aws
from dockerdata import docker
from pywebio import start_server
from kubernetesdata import kubernetes


#Creating  a flask app
app=Flask(__name__)

def exam():
    set_env(title="Devops Quiz")


    put_html(r"""<h1  align="center"><strong>DevOps Master Quest</strong></h1>""")




    c=0
    img = open('devops.png', 'rb').read()  # logo
    put_image(img, width='50px')  # size of image

    name = input("Enter your Name to start the Quiz", type="text", required=True)  # Accepting url or data


    type = select("Choose your favorite DevOps Technology",options=['Linux', 'AWS', 'Docker', 'Kubernetes'], required=True)

    if type=='Linux':
        put_html(r"""<h2  align="center"><strong>Category Linux</strong></h2>""")  # App Name in Main screen


        c,count=linux()
        wrong=int(count)-int(c)


    elif  type=="AWS":
        put_html(r"""<h2  align="center"><strong>Category AWS</strong></h2>""")  # App Name in Main screen
        c,count=aws()
        wrong = int(count) - int(c)

    elif type == "Docker":
        put_html(r"""<h2  align="center"><strong>Category Docker</strong></h2>""")  # App Name in Main screen
        c, count = docker()
        wrong = int(count) - int(c)

    elif type == "Kubernetes":
        put_html(r"""<h2  align="center"><strong>Category Kubernetes</strong></h2>""")  # App Name in Main screen
        c, count = kubernetes()
        wrong = int(count) - int(c)

    # Adding Progress bar
    put_processbar('bar')
    for i in range(1, 8):
        set_processbar('bar', i / 7)
        time.sleep(0.1)



    if int(c) == int(count) :
        popup("You Score Full Marks.Great!" + '🎉',
              put_table([

                  ['Total Question', count],
                  ['Correct Answers', c],
                  ['Wrong Answers', wrong]])

              )



    elif int(c)>=int(count)/2:
        popup("You Pass"+'😍',
              put_table([

                  ['Total Question', count],
                  ['Correct Answers', c],
                  ['Wrong Answers', wrong]])

              )

    elif int(c)<int(count)/2:
        popup("You Failed.No worries,Try Again"+'😉',
              put_table([

                  ['Total Question', count],
                  ['Correct Answers', c],
                  ['Wrong Answers', wrong]])
              )

    put_html(r"""<h3  align="center"><strong>Result</strong></h3>""")
    put_text("Hi",name,"check your Score.")
    def btn_click(btn_val): #To do function of the 3 buttons

        # To show About sessiono
        def about():
                popup("About",
                      [put_html('<h2>Created by Aswin Ks</h2>'),
                       put_html('<h3>This Project is created using Python, Pywebio and Flask</h3>'),
                       'Find More @ https://github.com/aswinks1995',
                       ]

                      )


        if btn_val=='Retry':
            run_js('window.location.reload()')
        elif btn_val=="About":
            about()

    put_buttons(['Retry','About'], onclick=btn_click)
    put_table([

        ['Total Question', count],
        ['Correct Answers', c],
        ['Wrong Answers', wrong]])

    if type=='Linux':
        img = open('linux.png', 'rb').read()  # logo
        put_image(img, width='60px')  # size of image
    elif type=="AWS":
        img = open('aws.png', 'rb').read()  # logo
        put_image(img, width='60px')  # size of image
    elif type=="Docker":
        img = open('docker.png', 'rb').read()  # logo
        put_image(img, width='60px')  # size of image
    elif type=="Kubernetes":
        img = open('kube.png', 'rb').read()  # logo
        put_image(img, width='60px')  # size of image


#To allow reloading of web browser and mentioning the port
app.add_url_rule('/qr','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()

    start_server(exam,port=args.port)
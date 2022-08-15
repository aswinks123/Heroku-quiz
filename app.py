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
from pywebio import start_server


#Creating  a flask app
app=Flask(__name__)

def exam():
    set_env(title="Devops Quiz")

    put_html(r"""<h1  align="center"><strong>Devops Quiz</strong></h1>""")


    c=0
    img = open('devops.png', 'rb').read()  # logo
    put_image(img, width='50px')  # size of image
    type = select("Choose your favorite DevOps Technology",options=['Linux', 'AWS', 'Docker', 'Kubernetes'], required=True)

    if type=='Linux':
        put_html(r"""<h2  align="center"><strong>Category Linux</strong></h2>""")  # App Name in Main screen


        c,count=linux()
        wrong=int(count)-int(c)


    elif  type=="AWS":
        put_html(r"""<h2  align="center"><strong>Category AWS</strong></h2>""")  # App Name in Main screen
        c,count=aws()
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
        popup("You Fail.No worries,Try Again"+'😉',
              put_table([

                  ['Total Question', count],
                  ['Correct Answers', c],
                  ['Wrong Answers', wrong]])
              )

    put_html(r"""<h3  align="center"><strong>Result</strong></h3>""")
    def btn_click(btn_val): #To do function of the 3 buttons


        if btn_val=='Retry':
            run_js('window.location.reload()')

    put_buttons(['Retry'], onclick=btn_click)
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



#To allow reloading of web browser and mentioning the port
app.add_url_rule('/qr','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()

    start_server(exam,port=args.port)
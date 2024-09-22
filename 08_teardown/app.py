#Victor Casado
#The Flying Mice
#SoftDev
#K08 -- Teardown
#2024-09-20
#time spent: tbd

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0.
1.
2.
3.
4.
5.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
                                         # In Java, when you instantiate a new object, you write Class object = new Class(object0

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():                       # In file systems, it often means the home directory
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? It will print to the console, and it will print the str() of the __name__ object
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? It will appear on the web page in your route directory http://ip/

app.run()                                # Q5: Where have you seen similar constructs in other languages? This is like calling a method on a java class with no parameters

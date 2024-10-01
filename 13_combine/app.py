import random as r


def pickrand():
    f = open("occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-2] #removes example row, total row, and new line row

    names = []
    nums = []
#counter = 0
    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:]
        else:
            split = list[i].split(",")
            name = split[0]
            num = split[1]
        names.append(name)
        nums.append(float(num))
    #counter += 1
    #print(str(counter) + ": " + name)
#print(names)
#print(nums)
#print(dict)
    return r.choices(names, nums)[0]

def gettable():
    f = open("occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-1] #removes example row, total row, and new line row

    dict = {}
    #counter = 0
    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:]
        else:
            split = list[i].split(",")
            name = split[0]
            num = split[1]
        dict.update({i:[name,num]})
        #counter += 1
        #print(str(counter) + ": " + name)
    #print(names)
    #print(nums)
    #print(dict)
    return dict

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"



@app.route("/wdywtbwygp")
def test_tmplt():

    return render_template( 'htmltmplt.html', title="An Appropriate Title", roster = "Victor Casado, Tawab Berri, Jacob Lukose", TNPG = "VICTOOOOOORIOUS", heading = "A website that chooses a job for you and provides job info", job = pickrand(), dictionary = gettable())


if __name__ == "__main__":
    app.debug = True
    app.run()

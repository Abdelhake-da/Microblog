import datetime
from os import truncate
from flask import Flask, render_template, request
import methode
app = Flask(__name__)

list_of_dict = [
    {
        "title":"A bit of a chill day today",
        "date":"Oct 24",
        "ldate":"24-10-2023",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic voluptas quas velit minima nihil odit tempora ipsum aut dolorum sit?",
    },
    {
        "title":"A bit of a chill day today",
        "date":"Oct 24",
        "ldate":"24-10-2023",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic voluptas quas velit minima nihil odit tempora ipsum aut dolorum sit?",
    },
    {
        "title":"A bit of a chill day today",
        "date":"Oct 24",
        "ldate":"24-10-2023",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic voluptas quas velit minima nihil odit tempora ipsum aut dolorum sit?",
    },   
]

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        data = request.form.get("data")
        dict = {
            "title":data[0:30] ,
            "date":datetime.datetime.today().strftime("%b %d"),
            "ldate":datetime.datetime.today().strftime("%Y-%m-%d"),
            "content":data
        }
        list_of_dict.append(dict)
    return render_template("index.html",list_of_dict=list_of_dict)

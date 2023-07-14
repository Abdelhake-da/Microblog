import datetime
from mongodbConnection import *
from flask import Flask, render_template, request, redirect

def create_app():
    app = Flask(__name__)
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
            insert_element(dict)
            
        return render_template("index.html",list_of_dict=get_element())
    return app
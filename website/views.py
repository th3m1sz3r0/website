from flask import Blueprint, render_template

views = Blueprint(__name__, "views", template_folder="templates")

@views.route('/')
def home():
    return render_template("home.html")
    
    
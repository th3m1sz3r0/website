from flask import Blueprint, render_template

auth = Blueprint(__name__, "auth", template_folder="templates")

@auth.route('/')
def auth1():
    return render_template(r'C:\Users\Adam Daoud\Documents\ALL\python projects\website\templates\auth.html')
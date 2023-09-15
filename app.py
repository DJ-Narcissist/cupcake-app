"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, request, url_for
from models import Cupcake, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='Cakes_for_less'

connect_db(app)




if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask

def Server():
    return Flask(__name__)

app = Server()
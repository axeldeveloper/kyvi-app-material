# Boilerplate for Kivy CRUD

This project is intended to put together minimal code necessary to start a Kivy application with CRUD. The MVC approach is used.

## Model and Database

Persistence uses the SQLAlchemy framework, which makes it easy to handle database queries from Python, and the SQLite database system, which can easily be packed and shipped with a desktop or mobile application.

## Install requirements in a virtual environment

`pip install -r requirements.txt`

Before installing the requirements in a virtual environment, make sure you have installed python-dev, if using Python 2, or python3-dev, if using Python 3.

In case you do not want to use a virtual environment, just install requirements like this:

`sudo apt-get install python-kivy`

or

`sudo apt-get install python3-kivy`

Then, assuming you have installed Pip, you may use it to install SQLAlchemy:

`pip install sqlalchemy`


https://samridhiagarwalblog.wordpress.com/2020/08/30/getting-started-with-mobile-application-development-using-python-and-kivy/


# Boilerplate para CRUD com Kivy

Este projeto tem como objetivo reunir o mínimo de código necessário para iniciar um aplicativo com CRUD. É usada a abordagem MVC.

## Modelo e banco de dados

A persistência de dados utiliza o framework SQLAlchemy, que facilita lidar com queries do Python, e o sistema de banco de dados SQLite, que pode ser facilmente embalado e transportado com um aplicativo destktop o móvel.

# Kivy CRUD

This project is intended to put together minimal code necessary to start a Kivy application with CRUD.

## Model and Database

Persistence uses the SQLAlchemy framework, which makes it easy to handle database queries from Python, and the SQLite database system, which can easily be packed and shipped with a desktop or mobile application.

## View using KivyMD
    using in front




## Install requirements in a virtual environment

`pip install -r requirements.txt`

Before installing the requirements in a virtual environment, make sure you have installed python-dev, if using Python 2, or python3-dev, if using Python 3.

In case you do not want to use a virtual environment, just install requirements like this:

`sudo apt-get install python-kivy`

or

`sudo apt-get install python3-kivy`

Then, assuming you have installed Pip, you may use it to install SQLAlchemy:

`pip install sqlalchemy`


`pip freeze > requirements.txt`


# CRUD com Kivy

Este projeto tem como objetivo reunir o mínimo de código necessário para iniciar um aplicativo com CRUD. 

## Modelo e banco de dados

A persistência de dados utiliza o framework SQLAlchemy, que facilita lidar com queries do Python, e o sistema de banco de dados SQLite, que pode ser facilmente embalado e transportado com um aplicativo destktop o móvel.




# docker 

docker run --volume "$HOME/.buildozer":/home/user/.buildozer   --volume "$PWD":/home/user/hostcwd kivy/buildozer android debug


docker run --volume "$HOME/.buildozer":/home/user/.buildozer   --volume "$PWD":/home/user/hostcwd kivy/buildozer android clean


docker run --volume "$(pwd)":/home/user/hostcwd buildozer --version


adb -s 0058823888 install ./bin/myapp-0.1-armeabi-v7a-debug.apk

adb devices


# python env
virtualenv -p /usr/bin/python3.7 kivymd_env

source ../kivymd_env/bin/activate
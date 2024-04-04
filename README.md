# Todo App

This project was an exercise to build a backend, using FastAPI, to make an existing REACT FrontEnd ToDo App run. The initial project used a list to store individual Todos. This list would reset every time the backend server was reset. Outside of class, I converted the todo list to a SQLite database. The TODO app now has perpetual storage for todos. I incorporated SQLmodel for the connection between python and SQL database.

## Technologies used in this project

- Python
- SQL Database
- SQLModel
- REACT
- FastAPI
- JavaScript

## Installation

Download the files to your computer. Within the `backend` folder, create a python virtual environment:  
`python3 -m venv .venv`

Activate your new python environment within the `backend` folder:  
`source .venv/bin/activate`

Within the `backend` folder, run the following command to install the requirements:  
`pip install -r requirements.txt`

## Generate new database file

within `backend` folder, run:  
`python db.py`

This will create the db for your todo items.

## Running the Backend Server

Open a terminal session and run the following command within the `backend` folder:  
`uvicorn main:app --reload`

Your backend server should now be running on `http://127.0.0.1:8000`

## Running the Frontend Server

Open another separate terminal session and run the following command withing the `frontend` folder:  
`npm start`

Your frontend server should now be running on `http://127.0.0.1:3000`.

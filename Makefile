# Makefile for Hotel Booking Analysis Project

.PHONY: setup preprocess analyze model clean

setup:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt

preprocess:
	venv\Scripts\activate && python src/preprocess.py

analyze:
	venv\Scripts\activate && jupyter notebook Hotelbooking.ipynb

model:
	venv\Scripts\activate && python src/model.py

clean:
	rm -rf venv
	rm -rf data/processed/*
	rm -rf outputs/models/*
	rm -rf outputs/visuals/*

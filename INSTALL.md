# Installation Guide

## Clone Repository

git clone your_repo_link

## Move into Project Folder

cd ai-return-reduction

## Install Dependencies

py -m pip install -r requirements.txt

## Run Preprocessing

py src/preprocessing.py

## Train Model

py src/train.py

## Run API

py -m uvicorn api.app:app --reload

## Run Frontend

py -m streamlit run frontend/app.py

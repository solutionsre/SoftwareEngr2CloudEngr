#!/bin/bash
pip install -r requirements.txt -t package/
cp main.py package/
cd package
zip -r ../lambda.zip .

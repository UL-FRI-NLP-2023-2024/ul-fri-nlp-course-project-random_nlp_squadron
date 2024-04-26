#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install scrapy

cd webcrawler/webcrawler

scrapy crawl spider
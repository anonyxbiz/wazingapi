# /algo/initialize.py
import os, asyncio as a, random, json_stream, base64, json as j, secrets, sqlite3, random, requests, pathlib, textwrap
from re import sub
from bottle import Bottle, route, run, request, static_file, response as r, post, get, put, delete, template, redirect, HTTPResponse, abort, hook
import asyncio as a
import argparse
from threading import Thread
import requests as rqs
from bs4 import BeautifulSoup as bs4
from time import sleep
from datetime import datetime as dt
from cryptography.fernet import Fernet
from discord import SyncWebhook
from googleapiclient.discovery import build
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai

p = print

app_info = {'title': 'Ytdl', 'url': 'https://wazingapi-zsda.onrender.com'}

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--thread",)    
args = parser.parse_args()

dis_hook = os.environ['dis_hook']
GOOGLE_API_KEY = os.environ['Ai']
system_prompt = os.environ['system_prompt']

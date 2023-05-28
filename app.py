# Import the necessary libraries
from flask import Flask, request, render_template, send_file
from flask_cors import CORS
import requests
from bardapi import Bard

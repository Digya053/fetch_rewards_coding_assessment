import json
from flask import Flask, render_template, request
from src.pixel_coordinates import PixelCoordinates

app = Flask(__name__)

@app.route('/')
def index():
	"""Render simple UI on localhost:port_no/"""
	return render_template('simple_ui.html')

@app.route('/submit', methods=['POST'])
def submit():
	"""Pass the input values of the user to the PixelCoordinates class and return the output obtained."""
	result = {}
	submitted_text = request.data.decode('utf-8')
	filled_elements = [float(i) for i in submitted_text.split(",")]
	corner_points = [(filled_elements[2], filled_elements[3]), (filled_elements[4], filled_elements[5]), (filled_elements[6], filled_elements[7]), (filled_elements[8], filled_elements[9])]
	result["res"] = PixelCoordinates(corner_points, int(filled_elements[0]), int(filled_elements[1]), filled_elements[10]).get_result() 
	return json.dumps(result)

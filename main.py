from flask import Flask, Response, request, render_template, jsonify
import requests, subprocess 

ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]

app = Flask(__name__)

@app.route('/face_detect',methods = ['GET'])
def result():
	image_url = request.args.get('url')
	try:
		if valid_image_url(image_url):
			number_faces = callFaceDetect(image_url)
			return number_faces
		else:
			return "error"
	except requests.exceptions.RequestException as e:
		Pass


def callFaceDetect(image_url):
	try:
		r = requests.get(image_url)
		with open("image.png",'wb') as f: 
		    f.write(r.content)

		number_faces = subprocess.run(['python3', './face_detect_cv3.py', 'image.png'], stdout=subprocess.PIPE)
		
		return number_faces.stdout
	except Exception as e:
		print(e)
		return "error"


def valid_image_url(filename):
	if filename == "":
		return False
	if not "." in filename:
		return False

	ext = filename.rsplit(".", 1)[1]

	if ext.upper() in ALLOWED_IMAGE_EXTENSIONS:
		return True
	else:
		return False

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from flask import request
from flask import redirect
import sys,os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


"""api"""

@app.route('/api/upload/', methods=['POST'])
def upload():
	if 'img' not in request.files:
		return {
			'error': 'img not in request.files',
		}
	img = request.files['img']
	#print(os.path.join(sys.path[0],'static','pictures','input.jpg'))
	img.save(os.path.join(sys.path[0],'static','pictures','input.jpg'))
	return {
		#随便给个值，这个url并不需要给前端返回参数
		"stats": 'success',
	}
	
@app.route('/api/style/<style>', methods=['GET'])
def transfer_style(style):
	return {
		'transfer_style': style,
	}
import os
from flask import Flask, jsonify, request
from gradio_client import Client

app = Flask(__name__)
async def predict_async(num, about):
    read_key = os.environ.get('HF_TOKEN', None)
    client = Client("Nyandori/Germini", hf_token=read_key)
    result = client.predict(
		num=num,
		about=about,
		api_name="/predict"
    )
    return result

@app.route('/predict', methods=['GET'])
async def predict():
    num = request.args.get('num')
    about = request.args.get('about')
    result = await predict_async(num, about)
    return jsonify({"result": result})

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, jsonify, request
from gradio_client import Client

app = Flask(__name__)
async def predict_async(num, about):
    
    client = Client("Nyandori/Germini", hf_token="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")
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
    final_list = []
    
    for i in range(3):
        result = await predict_async(num, about)
        final_list.append(result)
        

    return jsonify({"result": final_list})

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
if __name__ == '__main__':
    app.run(debug=True)

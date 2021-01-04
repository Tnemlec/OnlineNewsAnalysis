from flask import Flask, request, jsonify
from sklearn.preprocessing import MinMaxScaler
import json
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.sav', 'rb'))

@app.route('/api/submit', methods=['POST'])
def index():
    if request.method == 'POST':
        content = request.json

        #! Clean data
        contentDF = pd.read_json(content)

        scaler = MinMaxScaler()
        numerical = ['n_tokens_title', 'n_tokens_content', 'num_hrefs', 'num_self_hrefs', 'num_imgs','num_videos','average_token_length','num_keywords','self_reference_min_shares','self_reference_max_shares','self_reference_avg_sharess']
        scaled_data = contentDF
        scaled_data[numerical] = scaler.fit_transform(contentDF[numerical])
        
        #!Prediction
        prediction = model.predict(scaled_data)

        return json.dumps(list(prediction)), 200, {'ContentType':'application/json'}

@app.route('/', methods=['GET'])
def homepage():
    return 'Hello world'
    
if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
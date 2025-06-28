import pickle
from flask import *
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    feas=[float(x) for x in request.form.values()]
    return render_template('index.html',pred_text=f'Profit for Startup is {feas}')
@app.route('/predict_api',methods=['POST'])
def pred_api():
    data=request.get_json(force=True)
    return jsonify(list(data.values()))

app.run(debug=True)
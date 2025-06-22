# app.py
from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from model import train_isolation_forest, predict_anomalies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        contamination = float(request.form['contamination'])
        
        if file:
            data = pd.read_csv(file)
            model = train_isolation_forest(data, contamination)
            result = predict_anomalies(model, data)
            csv_io = BytesIO()
            result.to_csv(csv_io, index=False)
            csv_io.seek(0)
            return send_file(csv_io,
                             mimetype='text/csv',
                             as_attachment=True,
                             download_name='anomaly_result.csv')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

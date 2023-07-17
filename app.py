import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, static_url_path='/static')


model = pickle.load(open('my_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('page.html')


@app.route('/predict',methods=['POST','GET'])

def predict():
    x_0=request.form['x_0']
    x_1=request.form['x_1']
    x_2=request.form['x_2']
   

   

    features = [x_1,x_2]
    row = np.array(features).reshape(1,-1)
    prediction = model.predict(row)

    if (prediction == [0]):
        return render_template("result.html",Gender="Male", Age =x_0 , Annual_Income=x_1, Spending_Score=x_2,prediction_text ="This Values Include Cluster has the highest Annual Income, but the lowest Spending Score, which may indicate that this cluster consists of customers who are financially well-off but not big spenders.")
    elif (prediction == [1]):
        return render_template("result.html",Gender="Male", Age =x_0 , Annual_Income=x_1, Spending_Score=x_2, prediction_text="Values Include Cluster has intermediate values for both Annual Income and Spending Score, suggesting that this cluster may consist of customers who are neither particularly wealthy nor big spenders.")
    elif (prediction == [2]):
         return render_template("result.html",Gender="Male", Age =x_0 , Annual_Income=x_1, Spending_Score=x_2, prediction_text="This Values Include in Cluster has the highest Spending Score, indicating that this cluster consists of customers who are big spenders.")
    elif (prediction == [3] or prediction == [4] ):
         return render_template("result.html",Gender="Male", Age =x_0 , Annual_Income=x_1, Spending_Score=x_2, prediction_text="This Values Include Cluster have the lowest values for both Annual Income and Spending Score, indicating that these clusters may consist of customers who are not financially well-off and not big spenders.")
    else:
         return render_template("result.html", prediction_text="Woring Values")
  


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from logic import preprocessDataAndPredict
#create an instance of Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict/', methods=['GET','POST'])
def predict():
        if request.method == "POST":
                #get form data
                tv = request.form.get('tv')
                radio = request.form.get('radio')
                newspaper = request.form.get('newspaper') 
                #call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(tv, radio, newspaper) 
            #pass prediction to template
            return render_template('predict.html', prediction = prediction) 
        except ValueError:
            return "Please Enter valid values"
            pass
if __name__ == '__main__':
    app.run(debug=True)



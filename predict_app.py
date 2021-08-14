# import a library

from flask import Flask , render_template, request
import joblib

# instance of an app
app = Flask(__name__)

#load the model
model=joblib.load('diabetic_79.pkl')

@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict_form.html')


@app.route('/data', methods=['POST'])
def data():
    

    user_preg = request.form.get('preg')
    user_plas = request.form.get('plas')
    user_pres = request.form.get('pres')
    user_skin = request.form.get('skin')
    user_test = request.form.get('test')
    user_mass = request.form.get('mass')
    user_pedi = request.form.get('pedi')
    user_age = request.form.get('age')

    # print(user_preg,user_plas,user_pres,user_skin,user_test,user_mass,user_pedi,user_age)

    #If we get a text then we will have to convert to number by int() casting
    # If we have got it with number as type then type casting is not required
    
    result=model.predict([[user_preg,user_plas,user_pres,user_skin,user_test,user_mass,user_pedi,user_age]])

    if result[0] == 1:
        user_output ='Person is diabetic'
    else:
        user_output ='Person is not diabetic'
        
    return render_template('result.html',output=user_output)

if __name__ == '__main__':
    app.run(debug = True)
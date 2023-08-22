from flask import Flask, request, render_template
from flask_mail import Mail, Message
import pandas as pd
import numpy as np
import pickle




app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com' 
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="niteshspandey08@gmail.com"
app.config['MAIL_PASSWORD']="uwlewqvjyslokbvl"


# app.config['MAIL_SERVER']=os.environ['MAIL_SERVER']
# app.config['MAIL_PORT']=os.environ['MAIL_PORT']
# app.config['MAIL_USE_TLS']=os.environ['MAIL_USE_TLS']
# app.config['MAIL_USE_SSL']=os.environ['MAIL_USE_SSL']
# app.config['MAIL_USERNAME']=os.environ['MAIL_USERNAME']
# app.config['MAIL_PASSWORD']=os.environ['MAIL_PASSWORD']
mail = Mail(app)

pickle_in=open('linear_model.pkl','rb')
regression=pickle.load(pickle_in)

@app.route('/')
def hello():
    return render_template('pages/index.html')

@app.route('/blog')
def blog():
    return render_template('pages/blogs.html')

@app.route('/success-mail',methods=['POST'])
def msg_send():
    if request.method =='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']

        msg = Message('Mail Received from Portfolio Sites', sender = 'niteshspandey08@gmail.com', recipients = ['niteshspandey08@gmail.com'])
        msg.body = 'Name : ' + name + '\n' +'Email : ' + email + '\n' +'Message : ' + message 
        mail.send(msg)
    return render_template('pages/success_mail.html')



@app.route('/certification')
def certificates():
    return render_template('pages/certificates.html')

@app.route('/linear-regression')
def form():
    return render_template('pages/form.html')

@app.route('/result',methods=['POST'])
def submit_form():
    if request.method =='POST':
        CRIM    = request.form['CRIM']
        ZN	    = request.form['ZN']
        INDUS   = request.form['INDUS']
        CHAS    = request.form['CHAS']
        NOX     = request.form['NOX']
        RM	    = request.form['RM']
        AGE     = request.form['AGE']
        DIS     = request.form['DIS']
        RAD     = request.form['RAD']
        TAX     = request.form['TAX']
        PTRATIO	= request.form['PTRATIO']
        B       = request.form['B']
        LSTAT   = request.form['LSTAT']
        input=[[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
        prediction=regression.predict(input)

    return render_template("pages/result.html", n=prediction)

@app.route('/admission-prediction')
def movie_rating():
    return render_template('pages/prediction-Admission.html')

@app.route('/predict-rating', methods=['POST'])
def predict_rating_form():
    if request.method == 'POST':
        try:

            gre_score=request.form['gre_score']
            toefl_score = request.form['toefl_score']
            university_rating = request.form['university_rating']
            sop = request.form['sop']
            lor = request.form['lor']
            cgpa = request.form['cgpa']
            is_research = request.form['research']
            filename = 'Admission_prediction.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,is_research]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('/pages/result-admission.html',n=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')

@app.route('/titanic-survival')
def decision_tree():
    return render_template('pages/titanic_predict.html')

@app.route('/titanic_prediction', methods=['POST'])
def decision_tree_form():
    pickle_in = open('DecisionTreePrediction.pkl', 'rb')
    Decision_Tree = pickle.load(pickle_in)
    if request.method == 'POST':
        Pclass = request.form['ticket_class'] 
        print('Value of class',Pclass)               
        Age = request.form['Age']
        SibSp = request.form['SibSp']
        Parch = request.form['Parch']
        Fare = request.form['Fare']
        Gender = request.form['gender']
        print('Value ofgender',Gender)
        input = [[Pclass, Age, SibSp, Parch, Fare, Gender]]
        prediction = Decision_Tree.predict(input)
        def pred_new(prediction):
            if prediction == 1:
                return 'Passenger is Survived'
            else:
                return 'Passenger is not Survived'

    return render_template("pages/result.html", n=pred_new(prediction))


@app.route('/diabetes-prediction')
def random_forest():
    return render_template('pages/diabetes_prediction.html')

@app.route('/diabetes-prediction-result', methods=['POST'])
def diabetes_prediction_form():
    try:
        pickle_in = open('Diabetes_prediction.pkl', 'rb')
        diabetes = pickle.load(pickle_in)
        if request.method == 'POST':
            num_preg = request.form['num_preg']
            glucose_conc = request.form['glucose_conc']
            diastolic_bp = request.form['diastolic_bp']
            thickness = request.form['thickness']
            bmi = request.form['bmi']
            diab_pred = request.form['diab_pred']
            age = request.form['age']
            input = [[num_preg, glucose_conc, diastolic_bp, thickness, bmi, diab_pred,age]]
            prediction = diabetes.predict(input)

        def pred_new(prediction):
            if prediction == 1:
                return 'Patient Suffering from Diabetes'
            else:
                return 'Patient not Suffering from Diabetes'
    except:
        print('Please try again')

    return render_template("pages/result.html", n=pred_new(prediction))



if __name__=='__main__':
    app.debug = True
    app.run()
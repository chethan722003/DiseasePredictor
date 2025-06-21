from flask import Flask, render_template, request
import joblib, numpy as np

app = Flask(__name__)

# Load model and encoder
model = joblib.load('model/model.pkl')
label_encoder = joblib.load('model/label_encoder.pkl')

# List of symptoms
symptoms_list = [
    'nausea', 'joint_pain', 'abdominal_pain', 'high_fever', 'chills', 'fatigue',
    'runny_nose', 'pain_behind_the_eyes', 'dizziness', 'headache', 'chest_pain',
    'vomiting', 'cough', 'shivering', 'asthma_history', 'high_cholesterol', 'diabetes',
    'obesity', 'hiv_aids', 'nasal_polyps', 'asthma', 'high_blood_pressure',
    'severe_headache', 'weakness', 'trouble_seeing', 'fever', 'body_aches',
    'sore_throat', 'sneezing', 'diarrhea', 'rapid_breathing', 'rapid_heart_rate',
    'pain_behind_eyes', 'swollen_glands', 'rashes', 'sinus_headache', 'facial_pain',
    'shortness_of_breath', 'reduced_smell_and_taste', 'skin_irritation', 'itchiness',
    'throbbing_headache', 'confusion', 'back_pain', 'knee_ache'
]

@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms_list)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect core inputs
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        temp = float(request.form.get('temp', 0))
        humidity = float(request.form.get('humidity', 0)) / 100  # ✅ Normalize %
        wind = float(request.form.get('wind', 0))
        selected_symptoms = request.form.getlist('symptoms')

        # Binary symptom vector
        symptoms_input = [1 if s in selected_symptoms else 0 for s in symptoms_list]

        # Final feature vector
        features = [age, gender, temp, humidity, wind] + symptoms_input

        if len(features) != 50:
            return f"❌ Error: Input feature length is {len(features)}, expected 50. Check form fields."

        # Predict
        prediction = model.predict([features])[0]
        disease = label_encoder.inverse_transform([prediction])[0]

        return render_template("result.html", disease=disease)

    except Exception as e:
        return f"Error occurred during prediction: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

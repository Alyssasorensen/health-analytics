# health-analytics
This assignment is a primer for the 504/507 classes.

For my assignment, I created variables based on a patient's health information record. 

The number variable was the patient's heart rate. 
The string variable was the patient's name. 
The list variable was the patient's medications. 
The dictionary encompassed all of the patient's health information; this includes name, age, gender, current diagnoses, medications, and present assessment. Present assessment includes heart rate, blood pressure, temperature, glucose level, respirations, and oxygen saturation. 
I was then able to print out all of the patients health information based on the variables I inserted. 

Based on the example data, I got the folllowing output,

Patient health information:
Name: Mary Smith
Age: 60 years
Gender: female
Diagnoses: High cholesterol, Asthma, Hypertension
Medications: Atorvastatin, Metoprolol, Albuterol
Heart Rate: 65 bpm
Blood Pressure: 136/88 mmHg
Temperature: 98.4 °F
Glucose Level: 105 mg/dL
health assessment:
Patient needs to take albuterol for asthma, continue monitoring.

The health assessment was the second portion that used an if/else statement to emphasize that based on the patient's status, 

if age >= 59 and oxygen_saturation < 96:
        return "Patient needs to take albuterol for asthma, continue monitoring."

The patient's age is above 59 and their oxygen saturation is below 96, therefore resulting in the above statement. 
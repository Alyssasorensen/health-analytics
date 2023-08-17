import pandas as pd  
import numpy as np   

# Number variable, patient's heart rate 
heart_rate = 65  # beats per min

# String variable, patient's name 
patient_name = "Mary Smith"

# List, patient's medication list
medications = ["Atorvastatin", "Metoprolol", "Albuterol"] 

# Dictionary, patient's health information 
health_information = {
    "name": patient_name,
    "age": 60,
    "gender": "female",
    "current_diagnoses": ["High cholesterol", "Asthma", "Hypertension"],
    "medications": medications,
    "present_assessment": {
        "heart_rate": heart_rate,
        "blood_pressure": {"systolic": 136, "diastolic": 88},
        "temperature": 98.4,
        "glucose_level": 105,
        "respirations": 14,
        "oxygen_saturation": 95
    }
}
# Patient health information 
print("Patient health information:")
print(f"Name: {health_information['name']}")
print(f"Age: {health_information['age']} years")
print(f"Gender: {health_information['gender']}")
print("Diagnoses:", ", ".join(health_information['current_diagnoses']))
print("Medications:", ", ".join(health_information['medications']))
print(f"Heart Rate: {health_information['present_assessment']['heart_rate']} bpm")
print(f"Blood Pressure: {health_information['present_assessment']['blood_pressure']['systolic']}/{health_information['present_assessment']['blood_pressure']['diastolic']} mmHg")
print(f"Temperature: {health_information['present_assessment']['temperature']} °F")
print(f"Glucose Level: {health_information['present_assessment']['glucose_level']} mg/dL")


def assess_patient_health(oxygen_saturation, medications):
    if age >= 59 and oxygen_saturation < 96:
        return "Patient needs to take albuterol for asthma, continue monitoring."
    elif age >= 59:
        return "Increased age, continue monitoring."
    elif oxygen_saturation < 96:
        return "Low oxygen saturation, potential health risk, continue monitoring."
    else: 
        return "Patient's health is unremarkable."

oxygen_saturation = 95
age = 60

assessment_result = assess_patient_health(oxygen_saturation, age)

print("health assessment:")
print(assessment_result)
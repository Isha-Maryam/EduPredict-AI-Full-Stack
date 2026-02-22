import os
import joblib
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from .forms import StudentPerformanceForm
from .models import StudentPrediction

# 1. Dynamic Path Setup
# This builds the path: your_project_folder/ML_Model/math_model.pkl
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ML_Model', 'math_model.pkl')

# Load the model once when the server starts for speed
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def predict_score(request):
    prediction_result = None
    form = StudentPerformanceForm()

    if request.method == 'POST':
        form = StudentPerformanceForm(request.POST)
        if form.is_valid():
            
            input_dict = {
                'StudyHours': [form.cleaned_data['StudyHours']],
                'PracticeHours': [form.cleaned_data['PracticeHours']],
                'TestPrep': [int(form.cleaned_data['TestPrep'])],
                'AttendanceRate': [form.cleaned_data['AttendanceRate']],
                'ParentEducationLevel': [int(form.cleaned_data['ParentEducationLevel'])],
                'SleepHours': [form.cleaned_data['SleepHours']],
                'PreviousGradeAverage': [form.cleaned_data['PreviousGradeAverage']],
            }

            # 3. Create DataFrame for the Random Forest
            df_input = pd.DataFrame(input_dict)

            # 4. Predict (only if model loaded correctly)
            if model:
                prediction_result = model.predict(df_input)[0]
                prediction_result = round(float(prediction_result), 2)

                # 5. Save to Database (The 'Full Stack' step)
                StudentPrediction.objects.create(
                    study_hours=form.cleaned_data['StudyHours'],
                    practice_hours=form.cleaned_data['PracticeHours'],
                    test_prep=int(form.cleaned_data['TestPrep']),
                    attendance_rate=form.cleaned_data['AttendanceRate'],
                    parent_edu_level=int(form.cleaned_data['ParentEducationLevel']),
                    sleep_hours=form.cleaned_data['SleepHours'],
                    previous_grade=form.cleaned_data['PreviousGradeAverage'],
                    predicted_math_score=prediction_result
                )

    return render(request, 'predictor/predict.html', {
        'form': form, 
        'prediction': prediction_result
    })
def prediction_history(request):
    history = StudentPrediction.objects.all().order_by('-created_at')
    return render(request, 'predictor/history.html', {'history': history})
   
    
   
   
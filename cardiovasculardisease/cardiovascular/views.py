from django.shortcuts import render

from joblib import load 

model = load('model.joblib')
#model = load('./cardiovasculardisease/savedModel/model.joblib')

def prediction(request):
    return render(request, 'main.html')

def cardioForm(request):
    return render(request, 'cardioform.html')

def final_result(request):
    listt = []
    listt.append(request.GET['age'])
    listt.append(request.GET['gender'])
    listt.append(request.GET['height'])
    listt.append(request.GET['weight'])
    listt.append(request.GET['ap_high'])
    listt.append(request.GET['ap_low'])
    listt.append(request.GET['cholesterol'])
    listt.append(request.GET['glucose'])
    listt.append(request.GET['smoke'])
    listt.append(request.GET['alcohol'])
    listt.append(request.GET['activity'])

    ans = model.predict([listt])

    for x in ans:
        if x == 0:
            anss = "Congratulation!! you dont have cardiovascualr disease"
        else:
             anss = "Very sad!! you have cardiovascular disease."

    return render(request, 'result.html', {'ans':anss, 'listt':listt})



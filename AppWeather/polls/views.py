from django.shortcuts import render
from django.http import HttpResponse
import joblib
from .forms import ModelForm
from .models import Prediction



def prediction(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            temp_max = form.cleaned_data['temp_max']
            temp_min = form.cleaned_data['temp_min']
            wind = form.cleaned_data['wind']


            # Run new features through ML model
            model_features = [
                [temp_max, temp_min, wind]]
            loaded_model = joblib.load('weather_ml/rfc_model.pkl')
            prediction = loaded_model.predict(model_features)[0]



            # Save prediction to database Predictions table
            Prediction.objects.create(temp_max=temp_max,
                                       temp_min=temp_min,
                                       wind=wind,
                                       prediction=prediction)

            return render(request, 'home.html', {'form': form, 'prediction': prediction,
                                                 'prediction_name': prediction,})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'Home.html', {'form': form})



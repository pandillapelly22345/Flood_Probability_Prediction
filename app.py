from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

model = joblib.load('mlp_model.pkl')
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve the form data using request.form.get() and convert to appropriate data types
        monsoon_intensity = float(request.form['MonsoonIntensity'])
        topography_drainage = float(request.form['TopographyDrainage'])
        river_management = float(request.form['RiverManagement'])
        deforestation = float(request.form['Deforestation'])
        urbanization = float(request.form['Urbanization'])
        climate_change = float(request.form['ClimateChange'])
        dams_quality = float(request.form['DamsQuality'])
        siltation = float(request.form['Siltation'])
        agricultural_practices = float(request.form['AgriculturalPractices'])
        encroachments = float(request.form['Encroachments'])
        ineffective_disaster_preparedness = float(request.form['IneffectiveDisasterPreparedness'])
        drainage_systems = float(request.form['DrainageSystems'])
        coastal_vulnerability = float(request.form['CoastalVulnerability'])
        landslides = float(request.form['Landslides'])
        watersheds = float(request.form['Watersheds'])
        deteriorating_infrastructure = float(request.form['DeterioratingInfrastructure'])
        population_score = float(request.form['PopulationScore'])
        wetland_loss = float(request.form['WetlandLoss'])
        inadequate_planning = float(request.form['InadequatePlanning'])
        political_factors = float(request.form['PoliticalFactors'])

        # Prepare input data as a list or array, depending on your model's input format
        input_data = [
            monsoon_intensity, topography_drainage, river_management, deforestation, urbanization,
            climate_change, dams_quality, siltation, agricultural_practices, encroachments,
            ineffective_disaster_preparedness, drainage_systems, coastal_vulnerability, landslides,
            watersheds, deteriorating_infrastructure, population_score, wetland_loss, inadequate_planning,
            political_factors
        ]
        print(monsoon_intensity)

        # Make prediction using the model
        print(model.n_features_in_)
        prediction = model.predict([input_data])

        # Return the prediction result to the user
        result = "Flood Expected" if prediction[0] >= 0.7 else "No Flood"
        return render_template('index.html', result=result)

    except Exception as e:
        # In case of error, show an error message
        return render_template('index.html', result="Error: " + str(e))


if __name__ == '__main__':
    app.run(debug=True)

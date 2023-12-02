# get predictions from the trained model
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

##### To use in case where only 2 features are given #####
# Create a dict for all the types and categories of accidents
categories = {'Alkoholunfälle': 0, 'Fluchtunfälle': 1, 'Verkehrsunfälle': 2}
types = {'Verletzte und Getötete': 0, 'insgesamt': 1, 'mit Personenschäden': 2}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the API!"

@app.route("/", methods=["POST"])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Extract features
        year = data["year"]
        month = data["month"]
        
        # check if data only has 2 features
        if len(data) == 2:
            # Make a prediction by summing up all the predictions for each type and category
            prediction = 0
            for category in categories:
                for _type in types:
                    prediction +=int(np.round( model.predict(np.array([[categories[category], types[_type], int(year), int(month)]]))[0]))
            
        elif len(data) == 4:
            #gather additional features
            category = data["category"]
            _type = data["type"]
            # Make a prediction
            prediction = int(np.round(model.predict(np.array([[categories[category], types[_type],year,month]]))[0]))
        
        # Return the result in the specified format
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

import pickle
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

from common_module import encode_predict_data, preprocess_data


model_file = "model.bin"

with open(model_file, "rb") as file:
    cols_str, OHE, models, stack_model = pickle.load(file)
    logreg_model, rf_model, boosting_model = models

app = Flask("adaptability")


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    customer = pd.DataFrame([customer])

    X = preprocess_data(customer, cols_str)

    X_processed = OHE.transform(X)
    X_stacked_predictions_encoded = encode_predict_data(
        logreg_model, rf_model, boosting_model, X, X_processed
    )

    preds = stack_model.predict(X_stacked_predictions_encoded)

    result = {"adaptability": str(preds)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

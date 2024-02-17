import numpy as np


def encode_predict_data(logreg_model, rf_model, boosting_model, X, X_OHEd):
    """Predicts X's score from 3 models, combines and encodes the results,
    returns:
    - stacked_predictions_encoded
    """
    preds_logreg = logreg_model.predict(X_OHEd)
    preds_rf = rf_model.predict(X_OHEd)
    preds_boosting = boosting_model.predict(X)

    stacked_predictions = np.column_stack((preds_logreg, preds_rf, preds_boosting))
    classes = {"Low": 0, "Moderate": 1, "High": 2}
    stacked_predictions_encoded = [
        [classes[label] for label in row] for row in stacked_predictions
    ]

    return stacked_predictions_encoded


def preprocess_data(df, cols_str):
    df.columns = df.columns.str.replace(" ", "_").str.lower()
    df[cols_str] = df[cols_str].apply(lambda x: x.str.lower().str.replace(" ", "_"))

    df.institution_type = df.institution_type.replace(
        {"government": 1, "non_government": 0}
    )
    df.it_student = df.it_student.replace({"yes": 1, "no": 0})
    df.location = df.location.replace({"yes": 1, "no": 0})
    df.self_lms = df.self_lms.replace({"yes": 1, "no": 0})

    df = df.fillna(0)

    return df

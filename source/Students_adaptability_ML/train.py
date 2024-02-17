# coding: utf-8

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import catboost

from common_module import encode_predict_data, preprocess_data

import pickle


def prepare_train_get_metrics(X_1, y_1, X_2, y_2):
    """Trains a stack model on the data X_1 and y_1,
    returns:
    - accuracy for X_2 and y_2,
    - f1 for X_2 and y_2,
    - fitted OneHotEncoder,
    - list with 3 fitted models: [logreg_model, rf_model, boosting_model]
    - fitted final model
    """
    OHE = OneHotEncoder(sparse=False, handle_unknown="ignore", drop="first")

    X_1_processed = OHE.fit_transform(X_1)
    X_2_processed = OHE.transform(X_2)

    logreg_model = LogisticRegression(C=1, max_iter=1000, n_jobs=-1, penalty="l2")
    rf_model = RandomForestClassifier(
        random_state=1,
        n_jobs=-1,
        criterion="entropy",
        max_depth=10,
        max_features="sqrt",
        n_estimators=10,
    )
    boosting_model = catboost.CatBoostClassifier(
        cat_features=cols, depth=7, iterations=1000, l2_leaf_reg=0.0
    )

    logreg_model.fit(X_1_processed, y_1)
    rf_model.fit(X_1_processed, y_1)
    boosting_model.fit(X_1, y_1, silent=True)

    X_1_stacked_predictions_encoded = encode_predict_data(
        logreg_model, rf_model, boosting_model, X_1, X_1_processed
    )

    final_model = LogisticRegression()
    final_model.fit(X_1_stacked_predictions_encoded, y_1)

    X_2_stacked_predictions_encoded = encode_predict_data(
        logreg_model, rf_model, boosting_model, X_2, X_2_processed
    )

    final_preds = final_model.predict(X_2_stacked_predictions_encoded)

    return (
        accuracy_score(y_2, final_preds),
        f1_score(y_2, final_preds, average="macro"),
        OHE,
        [logreg_model, rf_model, boosting_model],
        final_model,
    )


if __name__ == "__main__":
    print("Reading data")
    raw_df = pd.read_csv("students_adaptability_level_online_education.csv")

    print("Data processing")

    raw_X = raw_df.drop("Adaptivity Level", axis=1)
    raw_y = raw_df["Adaptivity Level"]

    X_full_train, X_test, y_full_train, y_test = train_test_split(
        raw_X, raw_y, test_size=0.2, random_state=1
    )

    X_full_train.reset_index(drop=True, inplace=True)
    X_test.reset_index(drop=True, inplace=True)
    y_full_train.reset_index(drop=True, inplace=True)
    y_test.reset_index(drop=True, inplace=True)

    X_full_train.columns = X_full_train.columns.str.replace(" ", "_").str.lower()

    cols = X_full_train.columns.tolist()

    cols_str = cols.copy()
    cols_str.remove("age")
    cols_str.remove("class_duration")

    X_full_train[cols_str] = X_full_train[cols_str].apply(
        lambda x: x.str.lower().str.replace(" ", "_")
    )

    X_full_train.institution_type = X_full_train.institution_type.replace(
        {"government": 1, "non_government": 0}
    )
    X_full_train.it_student = X_full_train.it_student.replace({"yes": 1, "no": 0})
    X_full_train.location = X_full_train.location.replace({"yes": 1, "no": 0})
    X_full_train.self_lms = X_full_train.self_lms.replace({"yes": 1, "no": 0})

    X_test = preprocess_data(X_test, cols_str)

    print("Training of the model")

    full_train_acc, full_train_f1, OHE, models, stack_model = prepare_train_get_metrics(
        X_full_train, y_full_train, X_test, y_test
    )
    print(f"Accuracy: {full_train_acc}, f1: {full_train_f1}")

    model_file = "model.bin"

    print("Saving the model")

    with open(model_file, "wb") as f_out:
        pickle.dump((cols_str, OHE, models, stack_model), f_out)

    print(f"the model is saved to {model_file}")

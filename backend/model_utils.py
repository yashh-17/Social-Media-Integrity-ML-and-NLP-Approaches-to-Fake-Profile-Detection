import datetime
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from gender_guesser.detector import Detector

# Load the model
model = load_model("user_classifier_model.keras")
scaler = StandardScaler()

# Define a fixed language mapping
LANGUAGE_MAPPING = {"en": 1, "es": 2, "fr": 3, "de": 4, "unknown": 0}

def predict_sex(name):
    sex_predictor = Detector(case_sensitive=False)
    first_name = name.split(" ")[0] if name else "unknown"
    sex = sex_predictor.get_gender(first_name)
    sex_dict = {"female": -2, "mostly_female": -1, "unknown": 0, "mostly_male": 1, "male": 2}
    return sex_dict.get(sex, 0)

def extract_features(user_data):
    user_data = pd.DataFrame([user_data])

    # Handle missing values
    user_data["lang"] = user_data.get("lang", "unknown")
    user_data["name"] = user_data.get("name", "unknown")
    user_data["statuses_count"] = user_data.get("statuses_count", 0)
    user_data["followers_count"] = user_data.get("followers_count", 0)
    user_data["friends_count"] = user_data.get("friends_count", 0)
    user_data["favourites_count"] = user_data.get("favourites_count", 0)
    user_data["listed_count"] = user_data.get("listed_count", 0)

    # Convert language to numerical representation
    user_data["lang_code"] = user_data["lang"].apply(lambda x: LANGUAGE_MAPPING.get(x, 0))

    # Predict gender
    user_data["sex_code"] = user_data["name"].apply(predict_sex)

    # Calculate additional features
    user_data["followers_to_friends_ratio"] = user_data["followers_count"] / (user_data["friends_count"] + 1)
    user_data["has_profile_image"] = user_data["profile_image_url"].notna().astype(int)

    # Convert date
    user_data["created_at"] = pd.to_datetime(user_data["created_at"], errors="coerce")
    if user_data["created_at"].notna().any():
        user_data["created_at"] = user_data["created_at"].apply(lambda dt: dt.tz_localize(None) if dt.tzinfo else dt)
    user_data["account_age"] = (datetime.datetime.now() - user_data["created_at"]).dt.days.fillna(0).astype(int)

    feature_columns = [
        "statuses_count", "followers_count", "friends_count", "favourites_count", "listed_count",
        "sex_code", "lang_code", "followers_to_friends_ratio", "has_profile_image", "account_age"
    ]
    user_data = user_data.loc[:, feature_columns]

    # Normalize numerical values
    user_data[["followers_count", "friends_count", "favourites_count", "listed_count", "account_age"]] = scaler.fit_transform(
        user_data[["followers_count", "friends_count", "favourites_count", "listed_count", "account_age"]]
    )

    return user_data

def predict_account(user_data):
    features = extract_features(user_data)
    prediction = model.predict(features)
    prediction_label = np.argmax(prediction, axis=1)[0]
    return "FAKE" if prediction_label == 0 else "GENUINE"

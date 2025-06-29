import pandas as pd
import hashlib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.encoders = {}

    def preprocess(self, df):
        df = df.copy()
        for col in ['location', 'device']:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.encoders[col] = le
        return df

    def train(self, df):
        df_processed = self.preprocess(df)
        self.model.fit(df_processed[['amount', 'location', 'device']])

    def predict(self, data_point):
        df = pd.DataFrame([{
    "amount": data_point["amount"],
    "location": data_point["location"],
    "device": data_point["device"]
}])

        for col in ['location', 'device']:
            le = self.encoders[col]
            df[col] = le.transform([df[col][0]])
        score = self.model.decision_function(df)[0]
        pred = self.model.predict(df)[0]
        is_anomaly = True if pred == -1 else False

        if is_anomaly:
            hash_input = str(data_point).encode()
            fraud_hash = hashlib.sha256(hash_input).hexdigest()
        else:
            fraud_hash = None

        return {
            "is_anomaly": is_anomaly,
            "anomaly_score": float(score),
            "fraud_hash": fraud_hash
        }

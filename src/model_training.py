from sklearn.ensemble import GradientBoostingClassifier

def train_model(X, y):
    model = GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(X, y)
    return model

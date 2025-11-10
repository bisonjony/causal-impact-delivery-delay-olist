from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def estimate_pscore(X, T):
    logit = LogisticRegression(max_iter=1000)
    logit.fit(X, T)
    return logit.predict_proba(X)[:,1]
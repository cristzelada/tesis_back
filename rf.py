from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import cross_val_score

def clasification_v2(x1,x2,x3,x4,x5,x6,x7):
    data = pd.read_csv('./CancelacionInfo.csv')
    features = np.array(data[['ReservationMonth','ChannelCode','TypeRoom','LeadTime','NumberRooms','NumNights','RoomRate']])
    labels = np.array(data[['IsCancel?']])
    clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=None, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
                oob_score=False, random_state=None, verbose=0,
                warm_start=False)          
    clf.fit(features, labels)
    predictions = clf.predict([[x1,x2,x3,x4,x5,x6,x7]])
    score = clf.predict_proba([[x1,x2,x3,x4,x5,x6,x7]])
    print(predictions[0],score[0][0], score[0][1])
    return predictions[0], score[0][0], score[0][1]
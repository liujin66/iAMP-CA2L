import sklearn
import featuresByYBZDJ
import numpy as np
from tensorflow.keras.models import load_model
import joblib

def predict():
    result_load = featuresByYBZDJ.CA_Img(184, 25)
    result_load = result_load.flatten()
    result_load = np.reshape(result_load, (1, 1000))
    result_load = result_load.reshape((result_load.shape[0], result_load.shape[1], 1))
    cnn_model = load_model('static/models/CNN+BiLSTM.h5')
    feature = cnn_model.predict(result_load)
    svm_model = joblib.load('static/models/svm_model.model')
    prediction = svm_model.predict(feature)
    if prediction.flatten()[0] == 0:
        result = "The result of the iAMP-CA2L predictor shows that the peptide is not an antibacterial peptide."
    else:
        result = "The result of iAMP-CA2L predictor shows that the peptide is an antibacterial peptide.\n\tThe predicted antimicrobial peptide functions are as follows: "
        cnn_model_second = load_model('static/models/CNN+BiLSTM_second.h5')
        feature_second = cnn_model_second.predict(result_load)
        svm_model_second = joblib.load('static/models/svm_model_second.model')
        prediction = svm_model_second.predict(feature_second)
        prediction = prediction.todense().A.flatten()
        name = ["Antibacterial", "Antiviral", "Antiparasital", "Anti-HIV", "Anticancer (antitumor)", "anti-MRSA", "Antifungal", "anti-endotoxin", "Antibiofilm", "Chemotactic"]
        count = 0
        for i in prediction.tolist():
            if i == 1:
                result += " " + name[count] + "\t"
            count += 1
    return result

import pickle 
import sklearn
import warnings
from sklearn.exceptions import InconistentVersionWarning

# catch the InconsistentVersionWarnings and print the original scikit-learn version 
warnings.simplefilter("error",InconistentVersionWarning)

try:
    model = pickle.load(open('saved_model.pk1','rb'))
except InconistentVersionWarning as w:
    print(w.original_sklearn_version)    
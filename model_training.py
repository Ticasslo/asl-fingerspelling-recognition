# model_training.py
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier #scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
# Load data WITH PICKLE OR PANDAS BASE ON WHICH TYPE OF FILE YOU CHOSE, ALSO WRITE THE MODEL NAME DOWN BELOW
data_dict = pd.read_pickle('datatest.csv')
data = data_dict.drop(columns=['label'])
labels = data_dict['label']

# with open('datatest.pickle', 'rb') as f:
#     data_dict = pickle.load(f)
# data = data_dict['datatest']
# labels = data_dict['labels']


# Delete any data that isn't 42 length long, only for if getting error bc image from data set have 2 hands
# Delete any data that isn't 42 length long, only for if getting error bc image from data set have 2 hands
# Delete any data that isn't 42 length long, only for if getting error bc image from data set have 2 hands
# Delete any data that isn't 42 length long, only for if getting error bc image from data set have 2 hands
# filtered_data = []
# filtered_labels = []
# for i, item in enumerate(data):
#     if np.array(item).shape == (42,):
#         filtered_data.append(item)
#         filtered_labels.append(labels[i])
#     else:
#         print(f"Xóa Index {i}: {np.array(item).shape}")
# # Gán lại data và labels với danh sách đã lọc
# data = filtered_data
# labels = filtered_labels



# Split data
X_train, X_test, y_train, y_test = train_test_split(np.array(data), labels, test_size=0.15, random_state=22, shuffle=True)

# THIS PART IS USE THE BEST VALUE FOR THE BEST PREDICTION 200, 35, 42 BY GRIDSEARCH
# THIS PART IS USE THE BEST VALUE FOR THE BEST PREDICTION 200, 35, 42 BY GRIDSEARCH
# THIS PART IS USE THE BEST VALUE FOR THE BEST PREDICTION 200, 35, 42 BY GRIDSEARCH
# THIS PART IS USE THE BEST VALUE FOR THE BEST PREDICTION 200, 35, 42 BY GRIDSEARCH
# Model
# Changing the n_es , max_depth and random_state will affect the prediction accuracy
model = RandomForestClassifier(n_estimators=200, max_depth=35, random_state=42)
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
# END PART


# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# Save model SELECT THE RIGHT NAME OR IT WILL DELETE ANY MODEL THAT HAVE SAME NAME!!!
# SAVE FILE WITH PICKLE BECAUSE MODEL IS A VERY COMPLEX TYPE OF FILE, R.I.P Pandas
# SAVE FILE WITH PICKLE BECAUSE MODEL IS A VERY COMPLEX TYPE OF FILE, R.I.P Pandas
# SAVE FILE WITH PICKLE BECAUSE MODEL IS A VERY COMPLEX TYPE OF FILE, R.I.P Pandas
# SAVE FILE WITH PICKLE BECAUSE MODEL IS A VERY COMPLEX TYPE OF FILE, R.I.P Pandas
with open('modeltest.p', 'wb') as f:
    pickle.dump({'modeltest': model}, f)
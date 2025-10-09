import pickle
#THIS PART JUST FOR DETECT RANDOM FOREST MODEL FROM SCIKIT LEARN TO SEE THE NUMBER OF IT
#THIS PART JUST FOR DETECT RANDOM FOREST MODEL FROM SCIKIT LEARN TO SEE THE NUMBER OF IT
#THIS PART JUST FOR DETECT RANDOM FOREST MODEL FROM SCIKIT LEARN TO SEE THE NUMBER OF IT
#THIS PART JUST FOR DETECT RANDOM FOREST MODEL FROM SCIKIT LEARN TO SEE THE NUMBER OF IT

# Load model from the pickle file
with open('model3_2.p', 'rb') as f:
    model_dict = pickle.load(f)
    model = model_dict.get('model3_2')

# Check the type of the model
print(type(model))

# Check the n_estimators, the max_depth and the random_state
if hasattr(model, 'n_estimators'):
    n_estimators = model.n_estimators
    print("n_estimators:", n_estimators)
else:
    print("n_estimators is not applicable to this model type.")

if hasattr(model, 'max_depth'):
    max_depth = model.max_depth
    print("max_depth:", max_depth)
else:
    print("max_depth is not applicable to this model type.")
    
if hasattr(model, 'random_state'):
    random_state = model.random_state
    print("random_state:", random_state)
else:
    print("random_state is not applicable to this model type.")
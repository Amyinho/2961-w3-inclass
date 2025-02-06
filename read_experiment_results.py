import pickle

with open('experiment_results_deberta-v3-base_00000samp_20221006-1.pkl', 'rb') as file:
    data = pickle.load(file)

print(data)

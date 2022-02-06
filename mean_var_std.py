import numpy as np

def calculate(matrix):
    if len(matrix) < 9:
        raise ValueError ("List must contain nine numbers.")
    np.array(matrix)
    calc = {'mean':[], 'variance':[], 'standard deviation':[], 'max':[], 'min':[], 'sum':[]}
    new_matrix = np.reshape(matrix, (3, 3))
    for x in range(2):
        calc['mean'].append(list(np.mean(new_matrix, axis=x)))
        calc['variance'].append(list(np.var(new_matrix, axis=x)))
        calc['standard deviation'].append(list(np.std(new_matrix, axis=x)))
        calc['max'].append(list(np.max(new_matrix, axis=x)))
        calc['min'].append(list(np.min(new_matrix, axis=x)))
        calc['sum'].append(list(np.sum(new_matrix, axis=x)))
    calc['mean'].append(np.mean(new_matrix))
    calc['variance'].append(np.var(new_matrix))
    calc['standard deviation'].append(np.std(new_matrix))
    calc['max'].append(np.max(new_matrix))
    calc['min'].append(np.min(new_matrix))
    calc['sum'].append(np.sum(new_matrix))
    return calc

# Ran 3 tests in 0.004s :D
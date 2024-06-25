import numpy as np
def calculate(lst):
    #convert the list given by user in a 3x3 matrix
    arr=np.array(lst).reshape(3,3)
    #calculating mean, standard deviation, variance, maximum, minimum, sum of the list
    caculation= {
        'mean': [
            np.mean(arr, axis=0).tolist(), #calculating the mean along the row
            np.mean(arr, axis=1).tolist(), #calculating the mean along the column
            np.mean(arr).tolist() #calculating the mean of all the elements
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),  #calculating the variance along the row
            np.var(arr, axis=1).tolist(), #calculating the variance along the column
            np.var(arr).tolist() #calculating the variance of all the elements
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(), #calculating the standard deviation along the row
            np.std(arr, axis=1).tolist(), #calculating the standard deviation along the column
            np.std(arr).tolist() #calculating the standard deviation of all the elements
        ],
        'max': [
            np.max(arr, axis=0).tolist(), #calculating the maximum along the row
            np.max(arr, axis=1).tolist(), #calculating the maximum along the column
            np.max(arr).tolist() #calculating the maximum of all the elements
        ],
        'min': [
            np.min(arr, axis=0).tolist(), #calculating the minimum along the row
            np.min(arr, axis=1).tolist(), #calculating the minimum along the column
            np.min(arr).tolist() #calculating the minimum of all the elements
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(), #calculating the sum along the row
            np.sum(arr, axis=1).tolist(), #calculating the sum along the column
            np.sum(arr).tolist() #calculating the sum of all the elements
        ]
    }
    return caculation
lst = [0,1,2,3,4,5,6,7,8]
print(calculate(lst))

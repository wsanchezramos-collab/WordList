import numpy as np
data_1 = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_4 = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
def num_letters(num_rows, num_columns):

    return num_rows + num_columns + num_rows+ num_columns -4 

assert num_letters(13, 4)== 30
assert num_letters(4,4)== 12
assert num_letters(6,4)== 16
assert num_letters(6,7)== 22
    
        
print("Checking assertion.")
    
#print(data_1.shape)
#print(data_2.shape)
#print(data_3.shape)
#print(data_4.shape)


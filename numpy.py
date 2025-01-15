import time
import random
matrix_size = 10
A_list = [[random.random() for i in range(matrix_size)]for i in range(matrix_size)]
B_list=[[random.random() for i in range(matrix_size)]for i in range(matrix_size)]
def traditional_matrix_multiplication(A,B):
    result =[[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j]+=A[i][k]*B[k][j]
    return result
start_time=time.time()
traditional_result=traditional_matrix_multiplication(A_list,B_list)
python_list_time=time.time()-start_time
print(f"Time taken with python lists:{python_list_time:6f}seconds")




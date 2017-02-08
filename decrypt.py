#!/usr/bin/env python

import sys
from fractions import gcd

def with_zero_bis(string, n):
    while len(string) % n != 0:
        string.append(0)
    return string

def calcul_det(matrix):                                                                   
    result = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return result

def min_matrix(exept_c, matrix, n, sign):
    c = 0
    l = 1
    c_tmp = 0
    l_tmp = 0
    matrix_tmp = [[0] * (n - 1) for _ in range(n - 1)]
    while l_tmp < n - 1:
        while c_tmp < n - 1:
            if c == exept_c:
                c = c + 1
            matrix_tmp[l_tmp][c_tmp] = matrix[l][c]
            c = c + 1
            c_tmp = c_tmp + 1
        c_tmp = 0
        c = 0
        l_tmp = l_tmp + 1
        l = l + 1
    if n == 3:
        result = calcul_det(matrix_tmp)
        result = sign * matrix[0][exept_c] * result
        return result
    else:
        return sign * matrix[0][exept_c], matrix_tmp

def det_matrix(matrix, n, result):
    c = 0
    matrix_tmp = 0
    sign = 1
    result = 0
    fact = 1
    if n == 2:
        return calcul_det(matrix)
    while c < n and n > 2:
        if n > 3:
            fact, matrix_tmp = min_matrix(c, matrix, n, sign)
            result = result + (det_matrix(matrix_tmp, (n - 1), result) * fact)
            sign = sign * -1
            c = c + 1
        else:
            result = result + min_matrix(c, matrix, n, sign)
            sign = sign * -1
            c = c + 1
    return result

def matrix_calcul_bis(l, c, matrix_msg, matrix_key, square_size):                          
    result = 0                                                                              
    i = 0                                                                                   
    while i < square_size:                                            
        result = result + (matrix_msg[i][c] * matrix_key[l][i])
        i = i + 1                                                                        
    if (0 <= int(result) and int(result) <= 127):                                           
        if gcd(result, 1) == 1:                                                             
            return (unichr(int(result)), 0)                                                 
        else:                                                                               
            return (unichr(0), 1)                                                   
    else:                                                                                
        return (unichr(0), 1)

def print_string(string):                                                                   
    i = 0                                                                                   
    while i < len(string):                                                        
        sys.stdout.write(string[i])                 
        i = i + 1                                                    
    print ""

def decrypting(l_max, c_max, matrix_msg, matrix_key):                                    
    c = 0                                                                                  
    l = 0                                                                                 
    end = 0                                                                               
    string = []                                                                            
    while l < l_max and end == 0:                                                        
        while c < c_max and end == 0:                                                     
            tmp, tmp2 = matrix_calcul_bis(l, c, matrix_msg, matrix_key, c_max)            
            end = end + tmp2                                                              
            string.append(tmp)                                                           
            c = c + 1                                                                     
        c = 0                                                                               
        l = l + 1                                                                           
    if end == 0:                                                                            
        print_string(string) 

def matrix_det(matrix_key, det, square_size, exept_c, exept_l):                         
    matrix_tmp = [[0] * (square_size - 1) for _ in range(square_size - 1)]                
    c = 0                                                                                
    l = 0                                                                                 
    c_tmp = 0                                                                             
    l_tmp = 0                                                                             
    while l_tmp < square_size - 1:                                                        
        if l == exept_l:                                                                   
            l = l + 1                                                                      
        while c_tmp < square_size - 1:                                                     
            if c == exept_c:                                                               
                c = c + 1                                                                   
            matrix_tmp[l_tmp][c_tmp] = matrix_key[l][c]                                    
            c = c + 1                                                                     
            c_tmp = c_tmp + 1                                                               
        c_tmp = 0                                                                           
        c = 0                                                                               
        l_tmp = l_tmp + 1                                                                   
        l = l + 1                                                                           
    det_m = det_matrix(matrix_tmp, square_size - 1, 0)                                     
    return det_m * det

def resizing(matrix_key, square_size):                                                      
    c = 0                                                                                   
    l = 0                                                                                   
    sign = 1                                                                                
    matrix_tmp = [[0] * (square_size) for _ in range(square_size)]                          
    while l < square_size:                                                                 
        while c < square_size:                                                              
            if square_size % 2 == 0:                                                        
                if c == 0 and l > 0:                                                        
                    sign = sign * -1                                                       
                matrix_tmp[l][c] = sign * matrix_key[c][l]                                  
            else:                                                                           
                matrix_tmp[c][l] = sign * matrix_key[l][c]                                  
            c = c + 1                                                                       
            sign = sign * -1                                                                
        c = 0                                                                               
        l = l + 1                                                                           
    return matrix_tmp

def matrix_inverse(det, square_size, matrix_key):
    c = 0                                                                                   
    l = 0                                                                                   
    matrix_tmp = [[0] * (square_size) for _ in range(square_size)]                          
    while l < square_size:                                                                  
        while c < square_size:                                                              
            matrix_tmp[l][c] = matrix_det(matrix_key, det, square_size, c, l)               
            c = c + 1                                                                       
        c = 0                                                                               
        l = l + 1                                                                          
    matrix_tmp = resizing(matrix_tmp, square_size)                                          
    return matrix_tmp

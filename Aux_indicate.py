import math

one_list =  [ 1, 1 ]

def frac_part(num):                     #Given a 2-tuple, returns the fractional part
    numFrac_list = list(num)
    numFrac_list[0] = numFrac_list[0]%numFrac_list[1]
    return numFrac_list

def substract_lists(list1, list2):              #substracts lists as fractions
    list = [ 0 for j in range(2) ]
    list[1] = list1[1]*list2[1] /math.gcd(list1[1],list2[1])
    list[0] = list1[0]*list2[1]-list2[0]*list1[1] /math.gcd(list1[1],list2[1])
    return list

def mult_lists(list1, list2):                   #multiplies lists as fractions
    list = [ 1 for j in range(2) ]
    list[1] = list1[1]*list2[1] /math.gcd(list1[1],list2[1])
    list[0] = list1[0]*list2[0]
    return list

def indicate(num, alpha):                       #indicator function of interval 1-alpha to 1
    frac_alpha = frac_part(alpha)
    numtemp = frac_part(num)
    temp = substract_lists(one_list, frac_alpha)
    if 0<= numtemp[0] and numtemp[0] <temp[0]:
        return 0
    if numtemp[0]>=temp[0]:
        return 1

def ret_num( num ):                             #returns the fraction form of a list
    return num[0] / num[1]
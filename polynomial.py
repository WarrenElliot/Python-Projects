#Compute a Polynomial Equation
#https://www.geeksforgeeks.org/python-program-to-compute-a-polynomial-equation/

#Using For Loop
def for_poly(poly, n, x):
    result = 0
    for i in range(n):
        Sum = poly[i]
        for j in range(n-i-1):
            Sum = Sum * x
        result = result + Sum
    return str(result)

def horner(poly, n, x):
    result = poly[0]
    for i in range(1,n):
        result=result*x + poly[i]
    return str(result)   

def main():
    n = int(input("Enter the highest degree of the polynomial Equation: "))
    n=n+1
    i=0
    poly = [None]*n
    while i < n:
        print("Enter the coefficient of X^"+str(n-i-1) + " variable")
        poly[i] = int(input())
        i=i+1
    x = int(input("Enter the value of X:"))
        
    #print("The value of the polynomial equation using for-loop is: " + for_poly(poly,n,x))
    print("The value of the polynomial equation using horner method is: " + horner(poly,n,x))

if __name__ == '__main__':
    main()
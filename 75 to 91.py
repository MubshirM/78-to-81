# function in side funnction
def greatest(a,b,c):
    if a >b:
        return a
    elif b>a:
        return b
    else:
        return c

print (greatest(1000,5000,60))

# chaptor 3 exersize (4)
def is_palindrom(word):
    return word==word[::-1]
print (is_palindrom("madam"))
print (is_palindrom("rashid"))

# fefine febonancci
def fibonacci_seq(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif b== 2:
        print(a, b)
    else:
        print(a,b, end =" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

print(fibonacci_seq(10))

# Define para meaters
def user_info(first_name,last_name, age, Email, Password):
    print(f"your name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
    print(f"your Email is {Email}")
    print(f"your Password is{Password}")
    user_info('Rashid','Naeem',34,'mub@gmail.com',2364564)

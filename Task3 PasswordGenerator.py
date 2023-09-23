import string
import random
while True:
    password_len = input("Enter the length of passsword you want: ")
    if password_len.isdigit():
        password_len = int(password_len)
        break
    else:
        print("\nPlease enter only valid integer for password length!\n")
str1 = string.ascii_lowercase
str2 = string.ascii_uppercase
str3 = string.digits
str4 = string.punctuation
str = str1+str2+str3+str4
temp = random.sample(str,password_len)
password = "".join(temp)
print("YOUR PASSWORD IS:",password)
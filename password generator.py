import random

passss = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
takeinput = int(input("Enter the length of the password you want to generate:"))

generated_password = "".join(random.sample(passss,(takeinput)))
print(generated_password)

#password generator

'''imp info 
1.(.join command = join elements of a list with a sign in between/or no sign)
2.(.sample command = sample(a string,count of samples))'''
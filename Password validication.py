def pasword(x):
    if len(x)>8 or len(x)<8:
        print("This password is not valid")
        if len(x)>8:
            print("More than 8 characters")
        else:
            print("Less than 8 characters")
        return
    if x in ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd","M!n3r4L^", "T7r$eN8f"]:
        print("This passwords are not valid due to certain circumstances")
        return
    if len(x)==8: 
            l=list(x)
            first_char=l[0]
            if first_char.isdigit():
                 print("Password is not valid cannot start with a number")
            elif not(first_char.isalpha() or first_char.isdigit()):
                 print("Passwords is not valid,starts with a special character")
            elif not(any(i.isupper() for i in x)):
                 print("Password is not valid,Please include a capital letter")
            elif not(any(i.islower() for i in x)):
                 print("Password is not valid,Please include a small letter")
            elif x.isalnum():
                print("Paassword is not valid,Please include a special character")
            else:
                print("Your password is checked and verified")
            return
#main code
print("""Instructions for the user:
1.Should be of length 8
2.Should not start with a number or special character
3.Must include a capital letter and one small letter(atleast)
4.Must include a special character(atleast)""")
print("Type exit for exiting")
while True:
    x=input("enter the password:")
    pasword(x)
    exit=input("enter exit if u wanna exit or any other character to continue:")
    if exit in ["exit",'EXIT']:
        break
print("Your password:",x)
print("program exiting")

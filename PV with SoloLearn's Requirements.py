#By: Donald Lee
#SoloLearn Password Validator Challenge
#Rules
#1. Minimum length is 5 /
#2. Maximum length is 10 /
#3. Should contain atleast 1 number /
#4. Should contain atleast 1 capital letter /
#5. Should contain atleast 1 special character /
#6. Should not contain spaces
spechar = ["!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?",
           "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}",
           "~"]  #Refer to (https://owasp.org/www-community/password-special-characters) if you lose some special characters
stype = 0  #Type of special character
score=0
#Second. Checks if password contains a special character
def sptest():
    global stype
    global sp
    global score
    if (spechar[stype] in p):
        score = score + 1
        print("Password contains a special character.   Pass")
    else:
        if stype < 31:  # stype cannot be greater than the number of special characters in spechar, there is a total of 32 (31, starts at 0) special characters.
            stype = stype + 1
            sptest()
        else:
            print("Password contains a special character.   Fail")
#First. Checks if the password is strong or not, then calls sptest()
def process():
    global score
    if len(p)>=5:
        score=score+1
        print("Password is 5 or greater.                Pass")
    else:
        print("Password is 5 or greater.                Fail")
    if len(p)<=10:
        score = score + 1
        print("Password is 10 or below.                 Pass")
    else:
        print("Password is 10 or below.                 Fail")
    #Checks if the password contains a number or not
    if any([character.isnumeric() for character in p]):
        score = score + 1
        print("Password contains a number.              Pass")
    else:
        print("Password contains a number.              Fail")
    #Checks if the password contains a capital letter or not
    if any(x.isupper() for x in p):
        score = score + 1
        print("Password contains a capital letter.      Pass")
    else:
        print("Password contains a capital letter.      Fail")
    sptest() #Calls the function sptest to check if the password contains a special character or not
    #Checks if the password contains spaces or not
    if any(x.isspace() for x in p):
        print("Password doesn't contain spaces.         Fail")
    else:
        score = score + 1
        print("Password doesn't contain spaces.         Pass")
p = input("Please type your desired password:")
print("") #New line = cleaner output
process() #Calls the function to check if the password is strong/weak
print("                     -------")
print("                     | " + str(int(score)) + "/6 |")
print("                     -------")

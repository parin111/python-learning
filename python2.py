aliens = 2
password = "ALIENS" 
print("aliens are invading the planet")
print("you need to activate global defence platforms")
print("hope you have the password bitch")
guess = input("please enter the password").upper()
while guess != password:
    print("incorrect password")
    aliens = aliens ** 2
    print("there are", aliens, "on earth, try again")
    if aliens > 7400000000:
        break
    print("password hint: things that are attacking us")
    guess = input("quick! enter the password:").upper()
if aliens > 7400000000:
    print("noo aliens have outnumbered us.all is lost")
else:
    print("yay we won the fight earth is saved")
    
{} []
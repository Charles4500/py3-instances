##Functions --> These are reusable codes that execute when called
# In python they are defined by the def keyword followed by the function name

def fun():
    print("Python functions")
fun()


state = True
def check_user():
    if state != True:
      print("Access granted")
    else:
       print("Access denied")

check_user()

#Inside the functions you can pass in arguments

def passing_arg(amArg):
    print(f"An argument has been passed in {amArg}")
passing_arg("Python")

weather = "rainy"

weather_display = True

if weather == "rainy":
   print("Carry and umbrella")

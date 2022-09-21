import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, type=int, help="First Number")
ap.add_argument("-s", "--second", required=True, type=int, help="Second Number")
ap.add_argument("-n", "--name", type=str, help="Your name")
args = vars(ap.parse_args())

print("Hello my name is "+ args["name"])
print("The first number is : " + str(args["first"]))
print("The second number is : " + str(args["second"]))
print("First number + second Number : " +str(args["first"] + args["second"]))
print("First number - second Number : " +str(args["first"] - args["second"]))
print("First number * second Number : " +str(args["first"] * args["second"]))
print("First number / second Number : " +str(args["first"] / args["second"]))
from IP_Username_Manager import * #Call the script

# Debugging note: Debugging default is set to false

# Generate external username
print(IpUnCreate(True)) # Prints the username and sets debugging to true
print(IpUnCreate()) # Prints the username and sets debugging to false

print("---") #Print a visual separator 


# Decode username
Username = "a-made-body-knew" # Sets username variable
print(IpUnDecode(Username, True)) # Prints the decoded username and sets debugging to true
print(IpUnDecode(Username)) # Prints the decoded username and sets debugging to false
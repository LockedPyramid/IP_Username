from IP_Username_Manager import * #Call the script

# Debugging note: Debugging default is set to false

# Generate external username
print(IpUnCreateExternal(True)) # Prints the username generated and sets debugging to true
print(IpUnCreateExternal()) # Prints the username generated without debugging


print("---") #Print a visual separator 


#Generate internal username
print(IpUnCreateInternal(True)) # Prints the username generated and sets debugging to true
print(IpUnCreateInternal()) # Prints the username generated without debugging


print("---") #Print a visual separator 


#Generate username with variable
_Ip = "192.168.1.1" # Sets the variable to be use in the username generation
print(IpUnCreateManual(_Ip, True)) # Prints the username using the inputted Ip with debugging
print(IpUnCreateManual(_Ip)) # Prints the username using the inputted Ip without debugging


print("---") #Print a visual separator


# Decode username
Username = "a-made-body-knew" # Sets username variable
print(IpUnDecode(Username, True)) # Prints the decoded username and sets debugging to true
print(IpUnDecode(Username)) # Prints the decoded username and sets debugging to false
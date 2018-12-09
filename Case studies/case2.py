# Create a simple IF function that compares two values and prints result.
nativeVLAN = "1"
dataVLAN = "100"

vlan = input("Podaj VLAN: ")

if vlan == nativeVLAN:
    print("Podany VLAN jest natywnym VLANEM.")
elif vlan == dataVLAN:
    print("Podany VLAN jest data VLANEM.")
else:
    print("Brak VLANow o tym numerze.")

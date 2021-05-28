import getpass
import telnetlib

vlan = input("Enter new vlan code: ")
nameVlan = input("Enter new vlan name: ")
print("Example: 0/7")
portVlan = input("Enter new vlan port connect: ")
HOST = input("Enter your host: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"configure terminal\n")
tn.write(b"vlan ", vlan, "\n")
tn.write(b"name ", name, "\n")
tn.write(b"interface fastEthernet " portVlan, "\n")
tn.write(b"switchport mode access vlan " vlan "\n")
tn.write(b"show vlan brief\n")

tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
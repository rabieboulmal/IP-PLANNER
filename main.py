import ipaddress as ip

CLASS_A_ADDR = "10.0.0.0"
CLASS_B_ADDR = "172.16.0.0"
CLASS_C_ADDR = "192.168.1.0"



print("==================================================\n")
print("\tWelcome to this IP planner\n")
print("==================================================\n")
print("\tFor Private IP addressess:")
print("A: for class A")
print("B: for class B")
print("C: for class C")
print("\tFor Public IP addresses:")
print("O: for Others\n")


stay = True
while stay:
    choice = input("choose your class IP address:\n")

    if choice.lower() == 'a':
        prefix = int(input("Insert a prefix btw 8-30:\n"))
        if prefix not in range(7,30):
            raise Exception("Must be a valid prefix...")
        addr = CLASS_A_ADDR + '/' + str(prefix)

    elif choice.lower() == 'b':
        prefix = int(input("Insert a prefix btw 16-30:\n"))
        if prefix not in range(15,30):
            raise Exception("Must be a valid prefix...")
        addr = CLASS_B_ADDR + '/' + str(prefix)

    elif choice.lower() == 'c':
        prefix = int(input("Insert a prefix btw 24-30:\n"))
        if prefix not in range(23,30):
            raise Exception("Must be a valid prefix...")
        addr = CLASS_C_ADDR + '/' + str(prefix)

    elif choice.lower() == 'o':
        print("You choose an IP from a non-private range...")
        addr = input("Type your IP address:\n")
        prefix = input("Insert a prefix:\n")
        addr = addr + '/' + prefix
    else:
        raise Exception("Enter a valid class")
    try:
        network = ip.ip_network(addr)
    except:
        raise Exception("Failed to create network")

    print("\n==================================================\n")
    print(f"This prefix will provide {network.num_addresses} ip adresses...")
    print(f"broadcast: {network.broadcast_address}")
    print(f"Subnet Mask: {network.netmask} ")
    print(f"\t***Hosts***")
    hosts = list(network.hosts())
    print(f"First host IP: {hosts[0]}")
    print(f"Last host IP: {hosts[-1]}")
    print("\n==================================================")
    status = input("would you like to repeat? [Y/n]: ")
    if status.lower() == 'n':
        stay = False

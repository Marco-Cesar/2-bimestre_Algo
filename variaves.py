status = "maravilhoso"

def comportamento():
    global status
    status = "cansativo"
    print("Python é " + status)

comportamento()
print("Python é " + status)
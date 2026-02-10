with open("auth.log", "r") as file:
    count = 0
    for line in file:       
        if "from" in line:
            count += 1
            parts = line.split()
            for word in parts:
                if word.count(".") == 3:
                    print(word)
print("--------------------")
print("The number of IP's used are:  ",count)
    

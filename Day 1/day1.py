current = 50
count_of_zero = 0
hehe_list = []

try:
    with open("Day 1/real.txt", 'r') as file:
        for line in file:
            value = line.strip()
            hehe_list.append(value)
            
       

except Exception as e:
    print(f"Error: {e}")


for hehe in hehe_list:
    direction = hehe[0]
    distance = int(hehe[1:])
    if current == 0 and direction == "L":
        count_of_zero -= 1
    if direction == "L":
        new_current = current - distance
        while True:
            if new_current  < 0:
                new_current = 100 + new_current
                count_of_zero += 1
            else:
                current = new_current
                if current == 0:
                    count_of_zero += 1
                break
    if direction == "R":
        new_current = current + distance
        while True:
            if new_current > 99:
                new_current = new_current - 100
                count_of_zero += 1
            else:
                current = new_current
                break

print(count_of_zero)


import random

first_field = random.randint(3, 20)
result = []
for i in range(1,first_field):
    for j in range(2,first_field):
        if first_field % (i + j) == 0:
            if i != j and (j,i) not in result:
                kod = i,j
                result.append(kod)
                continue

result = str(result)
del_ = [',', '(', ')', ']','[',' ']
for i in del_:
    result = result.replace(i, "")
print(str(first_field)+ ' - '+ str(result))



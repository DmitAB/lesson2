
import random
first_field = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
first_field = random.choice(first_field)
# first_field = random.randint(3, 20) думал ещё так сделать, возможно так правильней?
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



def invalid_transactions(transactions):
    if len(transactions) == 0:
        return ['']
    
    obj1 = transactions[0].split(',')
    obj2 = transactions[1].split(',')
    invalid = []
    
    if obj1[0] == obj2[0] and obj1[3] != obj2[3]:
         invalid.append(','.join(obj1))
         invalid.append(','.join(obj2))
         return invalid
    else:
        if int(obj1[1]) > 60 or int(obj1[2]) > 1000:
            invalid.append(','.join(obj1))
        if int(obj2[1]) > 60 or int(obj2[2]) > 1000:
            invalid.append(','.join(obj2))
            
    return invalid


print(invalid_transactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print(invalid_transactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
print(invalid_transactions(["alice,20,800,mtv","bob,50,1200,mtv"]))
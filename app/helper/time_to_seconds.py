
def t2sec(time_str):
    
    total_seconds = int()
    multiplier=[1,60,3600,122400,44676000]
    c=1
    for i in map(int, time_str.split(':')):
        total_seconds+=i*(multiplier[c])
        c+=1
        
    return total_seconds

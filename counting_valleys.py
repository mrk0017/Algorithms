# Complete the countingValleys function below.
def countingValleys(n, s):
    position=0
    count_valley=0
    for i in range(n):        
        if s[i]=='U':
            position=position+1
        elif s[i]=='D':
            position=position-1
        if s[i]=='U' and position==0:
            count_valley=count_valley+1
    print(count_valley)

countingValleys(8,'UDDDUDUU')
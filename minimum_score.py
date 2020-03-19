def cal_minimum_hours(scores, r):
    count=0
    for i in range(len(scores)):
        per_row= (scores[i][0]/scores[i][1])*100
        while per_row<r:
            scores[i][0]=scores[i][0]+1
            scores[i][1]=scores[i][1]+1
            per_row= (scores[i][0]/scores[i][1])*100
            count=count+1
    return count

if __name__ == "__main__":
    scores=[[1,2],[3,3]]
    r=75
    print(cal_minimum_hours(scores,r))
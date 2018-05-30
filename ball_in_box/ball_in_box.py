import random 
import os
import math
#blocks can be concentrated into points
#the area of this problem is [-1,1],[-1,1]

def floatrange(startnum,stopnum,steps):
    return [startnum+float(i)*(stopnum-startnum)/(float(steps)-1) for i in range(steps)]
def ball_in_a_box(m,blockers):
    MaxRadius=0
    k=0
    BalloonXPos=[0]*int(m)
    BalloonYPos=[0]*int(m)
    while k<1000000:
        flag1=0
        flag2=0
        flag3=0
        for j in range(0,int(m)):
            BalloonXPos[j]=random.random()*2-1
            BalloonYPos[j]=random.random()*2-1
        for BalloonRadius in floatrange(0.0,1.0,11):
            for ii in range(0,int(m)):
                if(BalloonXPos[ii]+float(BalloonRadius)>1 or BalloonXPos[ii]-float(BalloonRadius)<-1 or BalloonYPos[ii]+float(BalloonRadius)>1 or BalloonYPos[ii]-float(BalloonRadius)<-1):
                    flag1=1
                    TempRadius=float(BalloonRadius)
                    break
            if(flag1==1):
                break
			
            for jj in range(0,int(m)-int(1)):
                for kk in range(1,int(m)):
                    if(math.sqrt(pow(BalloonXPos[kk]-BalloonXPos[jj],2)+pow(BalloonYPos[kk]-BalloonYPos[jj],2))<2*float(BalloonRadius)):
                        flag2=1
                        TempRadius=float(BalloonRadius)
                        break
                if(flag2==1):
                    break
            if(flag2==1):
                break
			
            for mm in range(0,int(m)):
                for ll in range(0,int(len(blockers))):
                    if(math.sqrt(pow(BalloonXPos[mm]-blockers[ll][0],2)+pow(BalloonYPos[mm]-blockers[ll][1],2))<float(BalloonRadius)):
                        flag3=1
                        TempRadius=float(BalloonRadius)
                        break
                if(flag3==1):
                    break
            if(flag3==1):
                break
        if(MaxRadius<=TempRadius):
            MaxRadius=TempRadius
            CurrentXPos=BalloonXPos
            CurrentYPos=BalloonYPos
        k=k+1
    circles=[]
    for circle_index in range(0,m):
        x=CurrentXPos[circle_index]
        y=CurrentYPos[circle_index]
        r=MaxRadius
        circles.append((x,y,r))
    return circles
print(ball_in_a_box(5,[(0.3,0.4),(0.7,0.9),(-0.4,-0.6)]))
print(MaxRadius**2*math.pi*m)
		
#os.system("pause")

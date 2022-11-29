import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import glob
import os
import scipy.stats as stats
import matplotlib.ticker as ticker

os.chdir('C:\\Users\\Yapicilab\\Dropbox\\Claire\\female_vs_male_starved_fed\\1109male_24') #SET THIS TO YOUR FOLDER WHERE YOU HAVE KEPT THE DATA FILES
# real_food_all=pd.read_csv('food_timing_yeast_starvation.csv')


# starvationlist=["0","16","24"]


# foodlist=os.listdir()
# foodlist.remove('food_timing_yeast_starvation.xlsx')
# foodlist.remove('food_timing_yeast_starvation.csv')

# foodlist.remove('results')
# # foodlist.remove('ss46202') #Removes this genotype because there is some problem with this data
# genotypelist=foodlist


# genotypelist=["1yeast","5yeast","10yeast"] #USE THIS LINE OF CODE TO SET YOUR GENOTYPE.
# starvation="0"
# time_list=[5,10,30,60]

time_thres=240


def find_index(l,t):
    for j in l:
        if j>t:
            return l.index(j)
            break
        else:
            continue
def find_jumps(l):
    if len(l)==0:
        jumps=0
    else:
        jumps=1
    for j in range(len(l)-1):
        if l[j+1]-l[j]>=3:
            jumps=jumps+1
        else:
            continue
    return jumps        
            



rad_dist_dict={} #Creating empty dictionary to store data


fnames = sorted(glob.glob('*.csv'))
index=0
# real_food_df=real_food_all[real_food_all['genotype']==genotype]
# real_food_df=real_food_df[real_food_df['starvation']==int(starvation)]
# real_food_bout_list=list(real_food_df['final_first_bout'])




for u in fnames: #goes thru files in the folder.
    
    
    n1=[]
    n2=[]
    n3=[]
    n4=[]
    n5=[]
    n6=[]
    n7=[]
    n8=[]
    num_of_visits={}
    all_nodes=[n1,n2,n3,n4,n5,n6,n7,n8]
    """
    Loading the data into a dataframe
    # """
    # print(u)
    df=pd.read_csv(u, header=None)
    # print("before",df.shape[1])
    df=df.dropna(axis=1,thresh=20000)
    # print("after",df.shape[1])
    if(df.shape[1]==10):
        data_header = ['Time', 'Latency', 'Fx1', 'Fy1', 'Fx2', 'Fy2', 'Fx3', 'Fy3','Fx4','Fy4']
    elif(df.shape[1]==8):
        data_header = ['Time', 'Latency', 'Fx1', 'Fy1', 'Fx2', 'Fy2', 'Fx3', 'Fy3']
    elif(df.shape[1]==6):
         data_header = ['Time', 'Latency', 'Fx1', 'Fy1', 'Fx2', 'Fy2']
    elif(df.shape[1]==4):
         data_header = ['Time', 'Latency', 'Fx1', 'Fy1']
    
    df.columns=data_header
    latency=list(df['Latency'])
    latency[0]=0
    df['Time']=df['Time']-round(df['Time'][0])
    time=df['Time']
    x_coord=list(df['Fx1'])
    y_coord=list(df['Fy1'])
    for i in range(0,len(x_coord)-1,1):
        if(np.sqrt((x_coord[i]-250)**2+(y_coord[i]-150)**2)<=30):
            n1.append(time[i])
        elif(np.sqrt((x_coord[i]-55)**2+(y_coord[i]-500)**2)<=30):
            n2.append(time[i])
        elif(np.sqrt((x_coord[i]-290)**2+(y_coord[i]-885)**2)<=30):
            n3.append(time[i])
        elif(np.sqrt((x_coord[i]-700)**2+(y_coord[i]-890)**2)<=30):
            n4.append(time[i])
        elif(np.sqrt((x_coord[i]-750)**2+(y_coord[i]-890)**2)<=30):
            n5.append(time[i])
        elif(np.sqrt((x_coord[i]-1150)**2+(y_coord[i]-890)**2)<=30):
            n6.append(time[i])
        elif(np.sqrt((x_coord[i]-1390)**2+(y_coord[i]-500)**2)<=30):
            n7.append(time[i])
        elif(np.sqrt((x_coord[i]-1180)**2+(y_coord[i]-150)**2)<=30):
            n8.append(time[i])
        else:
            pass
    
    i=1
    for rev in all_nodes:
        # print(rev)
        print(i)
        num_of_visits["n"+str(i)]=find_jumps(rev)
        i=i+1
    fig, ax = plt.subplots()
    ax.set_xlim(0,1444)
    ax.set_ylim(0,1080)
    ax.scatter(x_coord, y_coord, s = 0.1, c = df['Time'])
    # ax.axis('off')
    # fig.colorbar(ax=ax)
    ax.add_patch(plt.Circle((250,150), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((55,490), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((290,890), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((700,890), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((750,890), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((1155,890), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((1390,490), 30,color='b',alpha=0.5))
    ax.add_patch(plt.Circle((1185,150), 30,color='b',alpha=0.5))
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)
    plt.show()
    #         # del x_coord[0:split_point_index]
            # del y_coord[0:split_point_index]
    # test

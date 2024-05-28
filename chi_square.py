#IMPORTING NECESSARY MODULES
from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random

#EXTRACTING VARIABLES FROM THE OVERALL RESPONSES
def chi_square():
    
    random_number = random.randint(1000, 9999)
    
    responses = pd.read_csv("responses.csv")
    responses['fe'] = responses['fe'].apply(lambda x: "Positive" if x == 'pos' else x)
    responses['fe'] = responses['fe'].apply(lambda x: "Negative" if x == 'neg' else x)
    responses['fe'] = responses['fe'].apply(lambda x: "Neutral" if x == 'neu' else x)

    emotions=responses["fe"]
    time=responses["tm"]
    sleep=responses["sl"]
    pa=responses["pa"]

    #SETTING SIGNIFICANCE LEVEL
    alpha=0.05

    #CONTINGENCY TABLE FOR EMOTION/TIME MANAGEMENT
    ct_tm = pd.crosstab(emotions, time, margins=True)

    ylabels=[x for x in ct_tm.columns[:len(ct_tm.columns)-1]]
    ylabels=[x+" ("+str(ylabels.index(x))+")" for x in ylabels]

    xlabels=[x for x in ct_tm.index[:len(ct_tm.index)-1]]
    xlabels=[x+" ("+str(xlabels.index(x))+")" for x in xlabels]

    final_ct_tm =pd.DataFrame(ct_tm.iloc[:3,:3].values,columns=ylabels,index=xlabels)
    # print(final_ct_tm)


    obs_tm = np.array([ct_tm.iloc[:3,:3].values])

    test_statistic, p, dof, expected=chi2_contingency(obs_tm)

    # Calculate the percentage deviation matrix
    deviation_tm = ((obs_tm - expected) / expected) * 100

    # Create a color-coded graph
    plt.imshow(deviation_tm[0], cmap='coolwarm', vmin=-100, vmax=100)
    plt.colorbar(label='Percentage Deviation')

    # Add gridlines and labels
    #plt.grid(True, which='both', color='black', linewidth=0.5)
    plt.xticks(np.arange(0, deviation_tm.shape[2]), np.arange(0, deviation_tm.shape[2]))
    plt.yticks(np.arange(0, deviation_tm.shape[1]), np.arange(0, deviation_tm.shape[1]))
    # plt.xlabel(xlabels)
    # plt.ylabel(ylabels)

    # Add value annotations
    for i in range(deviation_tm.shape[1]):
        for j in range(deviation_tm.shape[2]):
            plt.text(j, i, f'{deviation_tm[0, i, j]:.2f}', ha='center', va='center', color='white')

    # Set plot title and axis labels
    plt.title('Percentage Deviation Matrix for Sentiments and Time Management\n')
    plt.ylabel('Sentiments')
    plt.xlabel('Categories of Time Management')

    # Show the plot
    # plt.show()
    [os.remove('static/Website_Images/' + file) for file in os.listdir('static/Website_Images/') if file.startswith("Time_management")]

    result_file1 = f'static/Website_Images/Time_management{random_number}.png'
    plt.savefig(result_file1)
    plt.close()

    print()
    if p <= alpha:
        res1 = 'Emotions are dependent on time management.'
    else:
        res1 = 'Emotions are independent of time management.'

    #CONTINGENCY TABLE FOR EMOTION/SLEEPING HABITS
    ct_sl = pd.crosstab(emotions, sleep, margins=True)

    ylabels=[x for x in ct_sl.columns[:len(ct_sl.columns)-1]]
    ylabels=[x+" ("+str(ylabels.index(x))+")" for x in ylabels]

    xlabels=[x for x in ct_sl.index[:len(ct_sl.index)-1]]
    xlabels=[x+" ("+str(xlabels.index(x))+")" for x in xlabels]

    final_ct_sl = pd.DataFrame(ct_sl.iloc[:3,:3].values,columns=ylabels,index=xlabels)
    # print(final_ct_sl)


    obs_sl = np.array([ct_sl.iloc[:3,:3].values])
    test_statistic, p, dof, expected=chi2_contingency(obs_sl)

    # Calculate the percentage deviation matrix
    deviation_sl = ((obs_sl - expected) / expected) * 100

    # Create a color-coded graph
    plt.imshow(deviation_sl[0], cmap='coolwarm', vmin=-100, vmax=100)
    plt.colorbar(label='Percentage Deviation')

    # Add gridlines and labels
    #plt.grid(True, which='both', color='black', linewidth=0.5)
    plt.xticks(np.arange(0, deviation_sl.shape[2]), np.arange(0, deviation_sl.shape[2]))
    plt.yticks(np.arange(0, deviation_sl.shape[1]), np.arange(0, deviation_sl.shape[1]))

    # Add value annotations
    for i in range(deviation_sl.shape[1]):
        for j in range(deviation_sl.shape[2]):
            plt.text(j, i, f'{deviation_sl[0, i, j]:.2f}', ha='center', va='center', color='white')

    # Set plot title and axis labels
    plt.title('Percentage Deviation Matrix for Sentiments and Sleeping Habits\n')
    plt.ylabel('Sentiments')
    plt.xlabel('Categories of Sleeping Habits')

    # Show the plot
    # plt.show()
    [os.remove('static/Website_Images/' + file) for file in os.listdir('static/Website_Images/') if file.startswith("Sleeping_habits")]

    result_file2 = f'static/Website_Images/Sleeping_habits{random_number}.png'
    plt.savefig(result_file2)
    plt.close()

    print()
    if p <= alpha:
        res2 = 'Emotions are dependent on sleeping habits.'
    else:
        res2 = 'Emotions are independent of sleeping habits.'

    #CONTINGENCY TABLE FOR EMOTION/PHYSICAL ACTIVITY
    ct_pa = pd.crosstab(emotions, pa, margins=True)

    ylabels=[x for x in ct_pa.columns[:len(ct_pa.columns)-1]]
    ylabels=[x+" ("+str(ylabels.index(x))+")" for x in ylabels]

    xlabels=[x for x in ct_pa.index[:len(ct_pa.index)-1]]
    xlabels=[x+" ("+str(xlabels.index(x))+")" for x in xlabels]

    final_ct_pa=pd.DataFrame(ct_pa.iloc[:3,:3].values,columns=ylabels,index=xlabels)
    # print(final_ct_pa)


    obs_pa = np.array([ct_pa.iloc[:3,:3].values])
    test_statistic, p, dof, expected=chi2_contingency(obs_pa)

    # Calculate the percentage deviation matrix
    deviation = ((obs_pa - expected) / expected) * 100

    # Create a color-coded graph
    plt.imshow(deviation[0], cmap='coolwarm', vmin=-100, vmax=100)
    plt.colorbar(label='Percentage Deviation')

    # Add gridlines and labels
    #plt.grid(True, which='both', color='black', linewidth=0.5)
    plt.xticks(np.arange(0, deviation.shape[2]), np.arange(0, deviation.shape[2]))
    plt.yticks(np.arange(0, deviation.shape[1]), np.arange(0, deviation.shape[1]))

    # Add value annotations
    for i in range(deviation.shape[1]):
        for j in range(deviation.shape[2]):
            plt.text(j, i, f'{deviation[0, i, j]:.2f}', ha='center', va='center', color='white')

    # Set plot title and axis labels
    plt.title('Percentage Deviation Matrix for Sentiments and Physical Activity\n')
    plt.ylabel('Sentiments')
    plt.xlabel('Categories of Physical Activity')

    # Show the plot
    # plt.show()
    [os.remove('static/Website_Images/' + file) for file in os.listdir('static/Website_Images/') if file.startswith("physical_activity")]

    result_file3 = f'static/Website_Images/physical_activity{random_number}.png'
    plt.savefig(result_file3)
    plt.close()

    print()
    if p <= alpha:
        res3 = 'Emotions are dependent on physical activity.'
    else:
        res3 = 'Emotions are independent of physical activity.'
        
    return final_ct_tm,final_ct_pa,final_ct_sl,res1,res2,res3,result_file1,result_file2,result_file3

chi_square()

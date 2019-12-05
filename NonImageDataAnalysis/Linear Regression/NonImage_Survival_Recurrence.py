import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset\\Prediction of 5 year survival_V3.csv')



X = df [[ 'Year']].values
Y = df [[ 'Percent Surviving 5 Years - SEER 9']].values ## 5 year Survival
Y_rec = df [[ 'Percent Recurrence']].values ## Cancer Recurrence


#### 5 Year Survival Prediction

def estimate_coef (x, y):
    n = np.size (x)
    mu_x , mu_y = np. mean (x), np. mean (y)
    SS_xy = np.sum (y*x) - n* mu_y * mu_x
    SS_xx = np.sum (x*x) - n * mu_x * mu_x
    slope = SS_xy / SS_xx
    intercept = mu_y - slope * mu_x
    return (slope , intercept )

def plot_regression (x, y, slope , intercept ):
    plt.subplot(2, 1, 2)
    plt.scatter (x, y, color = "blue",
    marker = "o", s = 100)
    y_pred = slope * x + intercept
    plt.plot (x, y_pred , color = "green", lw = 3)
    plt.xlabel ('Year')
    plt.ylabel ('Percent 5-year survival')
    plt.show ()

slope , intercept = estimate_coef (X,Y)


#y = slope*x + intercept
welcome = '''
                          Welcome!
      
      This system will predict the following for a colon cancer patient:
          a. 5 year survival rate
          b. Recurrence rate after treatment
'''
print(welcome)
newYear = input('Enter the year in which the cancer sample was taken: ')
prediction = slope.item()*int(newYear) + intercept.item()
plot_regression (X,Y,slope , intercept )


print('*******************************************************')
print('Chances of 5 year survival are',round(prediction,2),'%')
print('*******************************************************')


##### Colon Cancer Recurrence Prediction

def estimate_coef_Rec (x, y):
    n = np.size (x)
    mu_x , mu_y = np. mean (x), np. mean (y)
    SS_xy = np.sum (y*x) - n* mu_y * mu_x
    SS_xx = np.sum (x*x) - n * mu_x * mu_x
    slope = SS_xy / SS_xx
    intercept = mu_y - slope * mu_x
    return (slope , intercept )

def plot_regression_Rec (x, y, slope , intercept ):
    plt.subplot(2, 1, 1)
    plt.scatter (x, y, color = "red",
    marker = "o", s = 100)
    y_pred = slope * x + intercept
    plt.plot (x, y_pred , color = "green", lw = 3)
    plt.xlabel ('Year')
    plt.ylabel ('Percent recurrence')
    plt.show ()

slope , intercept = estimate_coef_Rec (X,Y_rec)


#y = slope*x + intercept
#newYear = input('Enter the year in which the cancer sample was taken: ')
predictionRec = slope.item()*int(newYear) + intercept.item()

plot_regression_Rec (X,Y_rec,slope , intercept )
print('*******************************************************')
print('Chances of cancer recurrence are',round(predictionRec,2),'%')
print('*******************************************************')


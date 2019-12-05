# CancerDetection
The project leverages both image and non-image data to make predictions for the cancer patients

1. Non-Image Data
One of the two main goals of the project was to assist doctors in diagnosing the cancer in patients by analyzing histopathological images. 
In line with this, image data was leveraged and two CNN models were implemented and studied, based on AlexNet and ResNet-50. 
The models were able to classify images into malignant and benign with an accuracy of 92.1% and 98.6% respectively.

2. Image Data:
Second goal was to leverage non image data and provide supplemental information to the doctors and colon cancer patients. 
For this, a linear regression model was developed that predicts following based on past data for years 1975 to 2011:
a) 5-year survival rate and 
b) Recurrence rate of colon cancer


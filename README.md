# Jeopardy

## Dataset

I have used the dataset [200,000+ Jeopardy! Questions](https://www.kaggle.com/tunguz/200000-jeopardy-questions)

## Problem statement

Train the model  to predict the "value" of the "question".


## Assumptions :

1.Value of question does not depend on show number , Air Date , Round , Category , Answer.

2.I have used "question" as independent variable in predicting the value of the question


## Approach 

1. Consider the problem as a classification question
2. Each  unique value in "Value" column in dataset is a "class".
3. As number of classes can be more, we use the concept of binning in order to reduce the no of classes
4. Then perform a Simple Logistic Regresion model. ( Jeopardy.ipynb is the notebook corresponding to this approach.)


## Using pre-trained Model ( Bert ) and testing it locally.

1. I trained the model using BERT. ( BERT.ipynb is the notebook corresponding to this approach.)
2. As the model.h5 file is so large,  I ran and tested it locally
3. Corresponding files are provided in Deployment folder
4. Below are few screenshots for local testing of the model.
 
 
 ## Server active 
 ![serverlast](https://user-images.githubusercontent.com/54733971/109376338-cc959400-78e9-11eb-9b8e-5ac46ed4853b.jpeg)

 ![a](https://user-images.githubusercontent.com/54733971/109376375-09fa2180-78ea-11eb-934e-816621b142ae.jpeg)

 ## Testing locally
 
 ![Testing](https://user-images.githubusercontent.com/54733971/109376210-0e720a80-78e9-11eb-9bdf-2d151f74a43f.jpeg)

 

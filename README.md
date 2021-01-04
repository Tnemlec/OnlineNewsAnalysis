# OnlineNewsAnalysis
Hello, my name is Clément LAJOUX, student in Data Analysis and Artificial Intelligence at ESILV engineering school
This is an analysis of the Online News dataset hosted on UCI.
# Project content
This project contain 4 main part :
- Part 1. Powerpoint introduction
- Part 2. A jupyter notebook containing the data analysis of the dataset
- Part 3. A jupyter notebook containing the creation of a predictive model
- Part 4. A flask API that can serve the model created previously + a client exemple to test the API

# Introduction
First, I highly recommend you to check out the powerpoint introduction since it helps you understand what I've done and gives you a better understanding of the study context.

# Analysis and Model
The analysis help you understand with plots the content of the dataset and its repartition. It is very usefull in order to understand the model generation.

I didn't go too far on analysis because lot of the features where based on an NLP programme so not very intelligible. The dataset doesn't fit that much for plot analysis.

In the modelisation notebook, I tried different model and there is a conclusion at the end with the comparison of all model, but the most successfull model was a grid search tuned gradient boosting that achieve an accuracy of **68%**.

**Be carefull** if you want to try executing the notebook, the gridsearch step took me over **4 hours** to complete since I tried a large panel of parameters even on a powerfull computer.

# API
 How to use the API ?
 Open a terminal and lauch the app<i></i>.py file

    C:> py app.py
Now that the server is listening you can execute the client (API_client_exemple.py) and it will print you the accuracy of the prediction for the first 4000 elements. This can be modify in the API_client_exemple.py

# Credit

Thanks to :
K. Fernandes, P. Vinagreand P. Cortez. A Proactive Intelligent DecisionSupport System for Predictingthe Popularityof Online News. Proceedingsof the 17th EPIA 2015 - PortugueseConferenceon ArtificialIntelligence, September, Coimbra, Portugal.

For letting me use their work.

# Contact
Feel free to contact me by email at : clement.lajoux@edu.devinci.fr
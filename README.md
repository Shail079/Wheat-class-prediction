# Wheat Class Prediction

# 0. Introduction
This project focuses on building a web application to predict Wheat Class on the basis of their Physical appearance.

We developed our application using a series of logical steps to ensure that users can easily use the application and make accurate predictions.

0) Introduction
1) Problem definition
2) Solution approach
3) Results and discussions
4) Use Website for Wheat Class Prediction

# 1. Problem definition
This dataset is a record of 3 common different wheat classes in food market sales. With this dataset, a predictive model can be performed using machine friendly data and estimate the classes of wheat can be predicted.

# 2. Solution approach

1) Define requirements
2) Gather data, analyze and build models
3) Build web backend API to use model
4) Design and develope frontend
7) Intergrate both frontend and backend
8) Test the entire application
9) Host the Application on Heroku


## Define requirements
The requriements were gathered from the problem and formally defined.

### User function
* Verify the different physical features of Wheat seed
* Enter these features in Web App to predict class of wheat

### Operating enviroment
* client/server system (Web)
* client: Web browers
* server: Python/Flask
* database: sqlite
* platform: Python/HTML5/CSS3
* Operating system: Windows, Mac, Linux

## 2. Gather data, analyze and build models
Data was downloaded from [here](https://www.kaggle.com/jmcaro/wheat-seedsuci)
We broke everything into the following steps
We started by loading data and packages we needed for the research.I then
analyzed the data to understand the relationships between features. We cleaned the data and using some domain knowlegde replaced some
missing values. The next step was feature tranformation to make the data
compatible with our models. We then trained our model and started perfoming
some predictions.

## 3. Build web backend API to use model
Using python and the flask web framework I built a web API the takes advantage of our model. The
flask server recieves this request and sends a response containing the predicted species.

## 6. Design and develope frontend
The User interface of the application was built using HTML and CSS.

## 7. Intergrate both frontend and backend
We send data from the forms on the webpage to the Cloud server
and the server sends a reponse, which is a prediction of the class matching those features

## 8. Test the entire application
We run multiple tests fixed bugs in the code.

# 3. Results and discussions

We were able to build a web application that can predict the class of wheat seed given certain features. The application runs in the cloud platform named Heroku and talks to a flask server that is taking data and passing it to a machine learning model.

# 4. Use Website for Fish Species Prediction

We have hosted my webpage on Heroku platform. If anyone want to try please click on https://wheat-class-prediction.herokuapp.com/ . 

# Flight Delay Predictor

Develop from September 2019 to January 2020 in Milan, Italy.

## About:

This Python application allow you to train a model to predict if a flight would be delay, using a labeled .csv dataset containing flight and wheather data. The user can choose from 3 different algoriths to train the model: KNearest Neightbors, Naive Bayes and Gradient Boosting. The dataset to be used must contain the following information in this specific order: Flight destination (string), Airline (string), Expected departure time (Time, format 00:00), Temperature (int) Atmosferic preasure (int), Wind velocity (int), Wind direction (string), Visibility distance (string), Cloud type (string) and Cloud height (int). 

The application also allows you to use the previusly created model to predict if a flight would be delayed or not based on an unlabeled dataset containing the same information. The application also has some example datasets "VuelosYTiempo.csv" and "VuelosYTiempoUnlabeled.csv" which contain the flight and wheather data from the Adolfo Suarez Madrid Barajas airpoty, in Spain. These datasets have been used to test the application, and mention that the labeled and unlabeled datasets contain compleatly different sets of data.

## Development:

This project was developed by my self during the first semester of my year studing in the Politecnico di Milano. 

First, I use a Pentaho workflow to extract the data and create the example dataset using web scrapping. Then after having the dataset I cleaned the data using Open Refine. Once the dataset was ready, I tested different training alforithm in Rapid Miner with the dataset to figure out what were the algotithm that worked the best with this data and have the best results. At the end, I found out that the best algorithm for this data was KNearest Neighbor with K = 4, with an accuracy of 89%. The other two best were, Gradient Boosted Tree, with an accuracy of 75%, and Naive Bayes, with an accuracy of 65%.

After knowing the best algorithms to implement I started with the Python code. I began designing and coding the GUI, for this matter I used the PyQt5 library together with the Designer to create the interface in an easier and faster way. Then I coded the logic of the application, for this I used the Pandas library to handle and modify the data, and the Scikit Learn library to train the model and clasify the data. Once the application was fully coded, I performed extensive testing on it using the example datasets previusly created. In this testing I found out that there were a difference from the performance of the algorithms seen in the application in comparation with the performance seen in Rapid Miner, presenting the algorithms implemented in Rapid Miner a slighty better accuracy than the ones in my application.

## Languages and tools:

During the development of this project the following lenguages and tools were used:

<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.pn"/> Python, 
<img align="left" alt="Pandas" width="26px" src="https://es.m.wikipedia.org/wiki/Archivo:Pandas_logo.svg#/media/File%3APandas_mark.svg"/> Pandas, 
<img align="left" alt="Scikit Learn" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/scikit-learn/scikit-learn.png"/> Scikit Learn, 
<img align="left" alt="Qt" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/qt/qt.png"/> Qt
<img align="left" alt="Pentaho" width="26px" src="https://logodix.com/logo/1960244.png"/> Pentaho, 
<img align="left" alt="Rapid Miner" width="26px" src="https://avatars0.githubusercontent.com/u/4490278?s=280&v=4"/> Rapid Miner, 
<img align="left" alt="Open Refine" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/4/4b/OpenRefine_New_Logo.png"/> Open Refine

## Images of the proyect:

Training section:
<img align="left" alt="Training section" width="350" src="/img/Training1.png"/>

Training the model:
<img align="left" alt="Training the model" width="350" src="/img/Training2.png"/>

Clasification section:
<img align="left" alt="Clasification section" width="350" src="/img/Clasification1.png"/>

Final clasification:
<img align="left" alt="Final clasification" width="350" src="/img/Clasification2.png"/>
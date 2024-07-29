## 2401FTDS_Unsupervised learning_Project

# Anime Recommender System Project 2024


![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](URL_TO_YOUR_APP)

<div align="center" style="font-size: 40%; text-align: center; margin: 0 auto">
    <img src="https://mcdn.wallpapersafari.com/medium/67/98/JKSuGa.jpg" style="display: block; margin-left: auto; margin-right: auto; width: 800px; height: 200px;" />
</div>


## Table of contents
* [1. Project Overview](#project-description)
* [2. Dataset](#dataset)
* [3. Kaggle](#kaggle)
* [4. Packages](#packages)
* [5. Environment](#environment)
* [6. MLFlow](#mlflow)
* [7. Streamlit](#streamlit)
* [8. Team Members](#team-members)

## 1. Project Overview <a class="anchor" id="project-description"></a>

In today’s technology-driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. One application where this is especially true surrounds movie content recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.

…ever wondered how Netflix, Amazon Prime, Showmax, Disney and the likes somehow know what to recommend to you?

Well, you are about to find out! In this project, we require you to use all your skills to build a collaborative and content-based recommender system for a collection of anime titles, capable of accurately predicting how a user will rate an anime title they have not yet viewed, based on their historical preferences.

The dataset consists of thousands of users and thousands of anime titles, gathered from myanimelist.net.

## 2. Dataset <a class="anchor" id="dataset"></a>
This dataset contains information on anime content (movies, television series, music, specials, OVA, and ONA*), split between a file related to the titles (anime.csv) and one related to user ratings of the titles (training.csv). The test.csv file will be used to create the rating predictions and must be submitted for grading. The submissions.csv file illustrates the expected format of submissions.

*OVA: Original Video Animation - anime film / series made for release in home-video formats, ONA: Original Net Animation is an anime that is directly released onto the Internet.

> Supplied files:
anime.csv: This file contains information about the anime content, including aspects such as the id, name, genre, type, number of episodes (if applicable), an average rating based on views, and the number of members in the anime 'group'.

> train.csv:This file contains rating data, supplied by individual users for individual anime titles. It contains user_id information, the anime_id of the title watched, and the rating given (if applicable).

> test.csv: This file will be used to create the final submission. It contains a user_id and an anime_id column only - no rating (that's your task!). These ids will be used to create the rating predictions.

> submission.csv:This file is for illustrative purposes only, showing the submission format for the final predictions.


#### Anime.csv

This dataset contains detailed information about various anime. Each row represents an anime with the following columns:

- **anime_id**: Unique ID identifying an anime from MyAnimeList.net.
- **name**: Full name of the anime.
- **genre**: Comma-separated list of genres associated with the anime.
- **type**: Type of anime, such as movie, TV, OVA, etc.
- **episodes**: Number of episodes in the series (1 if the anime is a movie).
- **rating**: Average rating out of 10 for the anime.
- **members**: Number of community members that are in this anime's "group."


#### train.csv

This dataset contains user ratings for various anime. Each row represents a rating given by a user with the following columns:

- **user_id**: Non-identifiable randomly generated user ID.
- **anime_id**: The ID of the anime that the user has rated.
- **rating**: Rating assigned by the user out of 10 for the anime. A value of `-1` indicates that the user watched the anime but did not assign a rating.



#### test.csv

This dataset contains information about user-anime interactions. Each row represents an instance of a user and an anime with the following columns:

- **user_id**: Non-identifiable randomly generated user ID.
- **anime_id**: The ID of the anime that the user has rated.



#### submission.csv

This dataset contains the predicted ratings for user-anime pairs. Each row represents a prediction with the following columns:

- **ID**: A concatenation of `user_id` and `anime_id` from the test file, separated by an underscore (e.g., `user_id_anime_id`).
- **rating**: The predicted rating for the given user-anime pair.

 
Acknowledgements
Original creator & myanimelist.net API for providing anime data and user ratings.

Source: Open source Kaggle dataset (https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database), adjusted for the purpose of this project.

## 6. Kaggle<a class="anchor" id="Kaggle"></a>

### What is Kaggle?

[Kaggle](https://www.kaggle.com/) Kaggle is an online community and platform for data scientists and machine learning enthusiasts to collaborate, compete, and share their work. It offers various features and resources

Competitions:To obtain additional information about the competitions related to the Anime Recommender System Project in 2024, get more  details about the registration process, evaluation criteria, submission guidelines and more [here](https://www.kaggle.com/competitions/anime-recommender-system-project-2024) 

## 4. Packages <a class="anchor" id="packages"></a>

To carry out all the objectives for this repo, the following necessary dependencies were loaded:
+ `Pandas 2.2.2` and `Numpy 1.26`
+ `Matplotlib 3.8.4`
 

## 5. Environment <a class="anchor" id="environment"></a>


Using a virtual environment for your projects is highly recommended. There are several methods to create one; we have detailed one approach below. Regular updates to this section are essential to ensure clarity for anyone cloning your repository. By following the provided instructions, they will be able to set up the necessary environment and quickly get started.

### Create the new evironment - you only need to do this once

```bash
# create the conda environment
conda create --name <env>
```

### This is how you activate the virtual environment in a terminal and install the project dependencies

```bash
# activate the virtual environment
conda activate <env>
conda install pip
#get list of packages and pipe to txt file
pip list --format=freeze > requirements.txt
# install the pip package
conda install pip
pip install Scikit-learn
pip install sklearn
# install the requirements for this project
pip install -r requirements.txt
```
## 5. MLFlow<a class="anchor" id="mlflow"></a>

Machine Learning Operations, or MLOps, is dedicated to the management and optimization of the lifecycle of machine learning models. MLflow, a contemporary MLOps tool, supports team collaboration on data projects by providing features for tracking experiments, managing models, and simplifying deployment processes. In this project, we will utilize MLflow to conduct experiments, perform tests, and ensure the reproducibility of our machine learning models. This will enable us to easily identify the best-performing model using the logged metrics.

- Please have a look here and follow the instructions: https://www.mlflow.org/docs/2.7.1/quickstart.html#quickstart

## 6. Streamlit<a class="anchor" id="streamlit"></a>

### What is Streamlit?

[Streamlit](https://www.streamlit.io/)  is a framework that acts as a web server with dynamic visuals, multiple responsive pages, and robust deployment of your models.

> Streamlit provides an effortless way for data scientists and machine learning engineers to build attractive, high-performance apps in just a few hours. Best of all, it’s done entirely in pure Python and is completely free to use.

> It's an intuitive and robust application framework that allows for the rapid creation of feature-rich user interfaces.

[Streamlit](https://www.streamlit.io/) 
It eliminates much of the behind-the-scenes effort required to establish a platform for deploying models to clients and end users. This means you can concentrate on the crucial aspects related to the data while disregarding the rest. As a result, you'll significantly enhance your productivity

##### Description of files

For this repository, we are only concerned with a file:

| File Name              | Description                       |
| :--------------------- | :--------------------             |
| `base_app.py`          | Streamlit application definition. |



#### 7.1 Running the Streamlit web app on your local machine

As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine. To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

- Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -U streamlit numpy pandas scikit-learn
 ```

- Navigate to the base of your repo where your base_app.py is stored, and start the Streamlit app.

 ```bash
 cd 2401FTDS_Unsupervised learning /Streamlit/
 streamlit run base_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```
You should also be automatically directed to the base page of your web app. This should look something like:

<div id="s_image" align="center">
  <img src="https://github.com/AmandaM2/mlflow-classification/blob/main/Deploy.jpeg" width="850" height="400" alt=""/>
</div>

Congratulations! You've now officially deployed your first web application!

#### 7.2 Deploying your Streamlit web app

- To deploy your app for all to see, click on `deploy`.
  
- Please note: If it's your first time deploying it will redirect you to set up an account first. Please follow the instructions.

## 8. Team Members<a class="anchor" id="team-members"></a>

| Name:Email                                                                          | Github                             | Kaggle                                                                 |
|-------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------|
| [Amanda Mokoena](zalmokeona@gmail.com)                         | https://github.com/AmandaM2        | https://www.kaggle.com/amandamokoena                                |
| [Sharon Mokgadi Ramapuputla](sharonramapuputla24@gmail.com)                      | https://github.com/Sharonramapuputla   | https://www.kaggle.com/sharonramapuputla                                |
| [Siphosethu Rululu](Siphosethurululu2@gmai.com)                                 |  https://github.com/SIPHOSETHU2303             |  https://www.kaggle.com/siphosethurululu                               |
| [Kgolo Motshegoa](motshegoakgolo@gmail.com)                     | https://github.com/Kgolo       | https://www.kaggle.com/motshegoakgolo                                |
| [Sandiso Magwaza](khayelihlesandiso@gmail.com)                      |  https://github.com/M0scode                |  https://www.kaggle.com/sandisokhayelihle                                |
| [Nkhubalale Emmanuel Nkadimeng,](physimanuel@gmail.com)                          | https://github.com/NKHUBALALE         | https://www.kaggle.com/nkhubalale                                |


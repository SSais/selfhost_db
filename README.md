# Introduction

This is a personal project where I have downloaded my workout data from an app called strong. My intention is to set up a database on my local server, then upload my data on the server and  then draw visualise the data using Tableau.

## The Database
I have a local server, it is a cheap Lenovo mini PC bought from Ebay for about £50. It has the  Ubuntu server distro installed. 
I will be setting up a PostgreSQL database onto it.

I created a directory in my server. 
Using github SSH I pulled the attached docker-compose.yml file onto my local server.
I changed the password and database username, as well as the port number (as I have other programs installed). 
The first port number is the port that will need to be used to connect to your server. 

Following the adjustments in the file I entered the following command in the terminal: 

```terminal
docker-compose up -d 
```
![](img/img1.png)


This runs the container and installs the database!

### Install Confirmation

To confirm that the database has been set up, I opened DBeaver on my main computer. 

I connected to the database as per the following image:

![](img/img2.png)
![](img/img3.png)

Test the connection and finally confirm! 

Now I can upload data into the database!

![](img/img4.png)
![](img/img5.png)

## The Data
The data was downloaded from the app in the CVS format.

![](img/img6.png)

As you can see, I will now need to clean the data to standardise it.
For this project I will keep the data in one table, ideally I would normalise the data however this would not be efficient with SQL.
I would normalise the data as per the following image:

![](img/img7.png)

Created with [quickdatabasediagrams.com](https://app.quickdatabasediagrams.com/#/)


## SQL Data Cleaning 

I have performed the following quality checks and adjustments in SQL:
- Check rows
- Check columns
- Check for nulls 
- Drop unwanted columns
- Add a primary key
- Adjust column names  


Data was visualised using Tableau: 

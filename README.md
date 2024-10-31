# Project Description

This is a simple application I wrote in Python to display the availability of HDB Car Parks to users. The aim was to help drivers in Singapore highlight the available parking spaces at HDB Carparks, by checking the app in advance and eliminate any inconvenience they may face when arriving at a carpark, before realising that there were no more parking spaces there. This was my first final year project I did for my Year 1 Semester 1 in Ngee Ann Poly ICT, enjoy using!

## How to Use (For PC)

Before launching the app, it is important to download the CSV files into your C:\\ main folder in order for the application to function properly. If not, the code will not be able to read the data and the app will not work as intended. 

## Features

Display Total Number of Carparks from a CSV File
Display All Basement Carparks from a CSV File
Read Carpark Availability Data File
Print Total Number of Carparks in the File Read
Display Carparks Without Available Lots
Display Carparks With At Least x% Available Lots
Display Addresses of Carparks With At Least x% Available Lots
Display all Carparks at given location
Display Carpark with the Most Parking Lots
Create an Output File with Carpark Availability with Addresses and Sort by Lots Available

## CSV Files
Up-to-date CSV Files can be found from the data.gov.sg website, but the scenario used in this repository follows that of June 2023.
- **carpark-information.csv**: Base CSV File which provides information about the Carparks in SG (e.g. Number, Type, Parking System, Address)
- **carpark-availability-v1.csv**: Example CSV File of Carparks in SG with the total lots and total lots available (Timestamp: 2023-06-19T11:10:27+08:00)
- **carpark-availability-v2.csv**: Another example CSV File of a Carparks in SG with the total lots and total lots available (Timestamp: 2023-06-20T23:01:26+08:00)

## Technologies Used

Python programming language.

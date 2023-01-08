# Flight Deal Finder

## Description
Finds cheap flight deals 6 months ahead and sends an email when a good deal has been found and a link to book the flight.

## Implmentation
Each file is responsible for each component and is constructed using OOP; 

###### Imports:
    from twilio.rest import Client
    import smtplib
    from datetime import datetime, timedelta
    

###### API Endpoints and use: 
- [Sheety](https://dashboard.sheety.co) 
  - Get requests to see the current members added
  - Post requests to add users
- [Tequila](https://tequila-api.kiwi.com)
  - Get requests to get airport codes and flight data
- [Twilio](https://www.twilio.com)
  - to send sms messages


###### Flies responsible for what:
- flight_search: 
  - getting airport codes, and flight data
- flight_data: 
  -  holds the information for each flight search request
- data_manager: 
  - managing data in google sheets holding user's data, flight prices and destinations
- notfication_manager: 
  - sends messages (if user's numbers are requests) and emails
- users_data_manager: 
  - adds users and gets their email


## Images
![image](https://user-images.githubusercontent.com/90845534/211181376-8e669d85-7beb-4f62-952b-5b819c3874df.png)

![image](https://user-images.githubusercontent.com/90845534/211181392-f2bdd2b6-28bc-4e42-b88b-3e560b68b262.png)

![image](https://user-images.githubusercontent.com/90845534/211181407-1987851a-92b9-4583-94b1-a29975f0283d.png)


## To improve 
 - Add a delete option.
 - Check for duplicates in the sheet.
 - Security issues, set up better authentication i.e bearer tokens. 
 - Move the code from users_data_managers to the data manager, it just makes more sense and is redundant.

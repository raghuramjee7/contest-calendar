# Contest Calendar

This web-app allows you to connect your Google Calendar to our internal scrapper which catalogs all the upcoming contests in various platforms like  
1. CodeChef
2. Codeforces
3. Leetcode
4. AtCoder

The new contests are updated everyday in your calendar and the data is either scrapped or got through an API. The authentication for the calendar access is done through OAuth and all the new contests are added to calendar

![sys-design](static/image.png)

## Functionality 
1) **Register** -  Users can register for the calendar updates, the authentication would be done google account
2) **Unregister** - Users who have previous registered can be unregistered
3) Notification for Users - if they have previously registered or not register according to subscribe or not subscribe.
4) The platform should be parameterised, i.e, it would be easy to add new platforms - add the platform name, create a scraper for that platform, create an extractor.
5) The contest searching should be optimised, i.e, since the platform adds new contests ater a few days, we need to scrape and update accordingly
6) Future Update - Users can choose the platform they want to get notified - this would create additional table to map each user, and a seperate app to edit and update preferences
7) Challenges
   1) Time convert to IST
   2) Class structure to DB structure  

## Database Design - 

### Tables 
1. **User table** - Table to store the User data
   1. *Name* - user
   2. *Schema* - UserID (int), email (string)
2. **Contest table** -  Stores contest data
   1. *Name* - contests
   2. *Schema* - platform (string), date (date), startTime (time), endTime (time)


## TO-DO
1) Look at google calendar API
2) Google OAuth to update calendar
3) Security challenges and address them
4) Does google cal API use epoch time?
5) DB changes for epochTime 
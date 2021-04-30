# Money XChange - A Cryptocurrency Trading App
## Overview
This web application is meant to demonstrate knowledge of Django and
Python.  Money XChange is an application where a user can use pretend 
money to buy and sell cryptocurrency.  

Django's default Authentication system is used for authentication.  

## About Money XChange

### Authentication

The user has a choice whether they would like to create an account on Money XChange or not.  

Without an account, the user is able to view current and historical data about many different types of Cryptocurrencies.  They cannot buy or sell cryptocurrencies however.  

To create an account, the user first goes to 'Login'.  From there, they can click the 'Create an Account' link.  All that is needed is a Username and Password.  

Once the user is logged in, they will notice that the home page now includes the ability to buy Cryptocurrencies.  New menu items, Portfolio and Transactions, have also now appeared.  The user will also have an account balance, all new users start with $10,000 USD.  


### Information Page / Home Page
The home page contains current information about each cryptocurrency registered in the Money XChange Cryptocurrency database.  If the user is not logged in, they can view information but cannot make a purchase.

Once logged in, a 'Buy' button will appear for them to use for purchases.  

A Search bar is also provided.  The user can use this to search for Cryptos either in the database or not.  If not in the database, information will still be provided (assuming the crypto was found); however, the user is unable to purchase crypto not in the Money XChange database.  If the crypto symbol was not known to Quandl, a message will appear to the user.  


### Buying Cryptocurrency
To buy a cryptocurrency, the user navigates to the buy page via either the 'Buy' button within the home page table or the 'Buy' button within that crypto's Info page.  The 'Buy' page will allow the user to specify how much of that crypto to purchase.  The user will not be allowed to buy more than their current account balance can purchase.  

### Portfolio
Any crypto holdings the user currently has will be displayed in their Portfolio.  The
quantity and current values will also be specified here.  

The user also has the ability to sell their cryptos here.  

### Transactions
The user can view all of their prior transactions (Buying or Selling) here.  

### Selling Cryptocurrency
To sell their cryptocurrency, the user navigates to their Portfolio page.  From there,
they can navigate to the sell page via the crypto's 'Sell' button.  

The 'Sell' page will allow the user to specify how much of the crypto to sell.  
Once the user confirms the sale, all proceeds will be placed back into the user's account.  


# Resetting the Account
At some point, the user may want to start all over again.  To reset their account,
the user navigates to their Account page.  Towards the bottom of the page is a 'Reset'
button.  Once this button is pressed, all transactions will be cleared and the account
balance will be reset back to $10,000 USD.  This also means that all prior holdings will be removed.  

From this page, the user can also update information about themselves.  They can update First Name, Last Name, email (none of this is used in the app btw... simply stored in Django's User table).


## Technologies Used
This web application was build using Django, Python, HTML, JQuery, and CSS.  Django's default SQLite3 DBMS was used to store information in the Account, Cryptocurrencies, Transactions, and Portfolio tables.

Quandl's REST endpoint with BITFINEX was used to discover current crypto prices and historical data.  

For this project, I did not use SASS or Bootstrap directly.  However, I did pull in a Bootswatch css file. 


## Future Improvements
The goal of this project was to focus on learning Django.  Django for me was a different way of thinking that took a bit of time for me to learn.  I learned so much as I went along and there are parts I wish I could just rewrite.  I know that I've just scratched the surface of Django.  

I did not focus as much on the UI as I typically would.  Simply wrapping my head around the new concepts and getting things to work took most of my time.  

- Search:  I ran out of time to really implement Search properly.  Right now, it simply searches the prebuilt table of known cryptos.  I would like it to search Quandl instead.  

- Crypto info page:  There is more data I would have like to add here.  24hr change would have been awesome - complete with color coding for up or down valuations.  

- Error handling - I really need to start writing unit tests at the beginning of a project.  I never feel like there is enough time.  

- Email:  I really wanted to add a Contact page where the user could really email me.  Not really part of the project though, so it go put off and then purged.  

- Details, details, details - Every cryptocurrency site I see gives me more ideas.  None of them are necessarily hard; at some point, it is just time to let go and move on.  


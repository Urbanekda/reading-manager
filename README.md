# Reading Manager App

This is my first attempt at creating a web application in [Django](https://www.djangoproject.com/). It is a simple app intended as a reading tracker, storing the data of your current, finished, or upcoming reads. Apart from Django I have used plain CSS for styling, an icon package from [Font Awesome](https://fontawesome.com/icons), and vanilla Javascript for interactivity.

## Functionality

The main view consists of a book list, which can be easily modified by control elements on the top of the page.

Books are added through a creation form which saves the data to a database through Django's ORM.

Key attributes of each book include:
- *name and author*
- *topic*
- *rating*
- *notes*
- *status* (finished/upcoming/ongoing)

Upon clicking the "Show more" button you will see a profile page of each respective book displaying the attributes in a more detailed format. From here the book can also be modified or deleted.

## Rationale

The purpose of this application is driven mainly by own forgetfulness in regards to the books I read. By organizing book notes and summaries through this app I hope to remind myself of the important stuff from these books.

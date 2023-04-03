# Frequently Asked Questions

[Link to the deployed site](https://app-faq.herokuapp.com "Link to the site")

An interface for handling frequently asked questions on a website

It is designed to be used on any device.

![Mockup images](/faq/static/images/responsive.jpg "Mockup Images")

## Table of Contents

- [User Experience UX](#user-experience-ux)
- [Design Strategy](#design-strategy)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

* ### User Stories
  - #### First Time Visitor Goals
  
    a. As a first time visitor, I would like to be able to register to ask questions.
  
    b. As a first time visitor, I want to be able to ask a question without needing further instructions.

    c. As a first time visitor, I want to be able to see if my question has already been answered.
    
  - #### Returning Visitor Goals
  
    a. As a returning visitor, I want to be able to see if the question I asked, has been answered.

    b. As a returning visitor, I want to be able to delete a question I asked

    c. As a returning visitor, I would like to contact the site owner
    
  - #### Frequent User Goals
  
    a. As a frequent user, I want to be able to browse the questions asked by others.

    b. As a frequent user, I want to be able to delete my account and all questions I asked
    
* Design Considerations
  - Colour Scheme
  
  The colour scheme is the standard bootstrap colour scheme using white background, black text and blue buttons.
  Edit buttons will be yellow and delete buttons, red.

  Messages will be yellow text on a black background to make them more visible from the rest of the content

  Messages will be used to confirm any actions by the user
  
  - Typography
    
    For simplicity, only one font style will be used. The Poppins font is a clear sans-serif font which works well for all elements of the site. The fallback sans-serif is specified in case the Poppins font fails to load.
    
  - Imagery
  
    Hero Image from [Backstagecrew](https://backstagecrew.com)

    The icons used are sourced from [Font Awesome](https://fontawesome.com/)
    
  - Wireframes

  Initial designs for the site. All pages to be responsive.
  
  ![Landing Page](/faq/wireframes/landing.jpg "Landing Page")

  On entering the site users see the overview of the company
  
  ![FAQ Page](/faq/wireframes/faq.jpg "FAQ Page")

The FAQ page shows all categories in an accordion. Each category opens to show another accordion with the category's questions. Each question can be opened to show the answer.

  ![Contact Page](/faq/wireframes/contact.jpg "Contact Page")

The Contact page is for customers to send information or request quotes etc.

  ![Register Page](/faq/wireframes/register.jpg "Register Page")

The users can resister an account which allows them to ask a question.

  ![Login Page](/faq/wireframes/login.jpg "Login Page")

Once an account has been created, a returning customer can log to be able to ask questions

  ![Ask a question](/faq/wireframes/ask.jpg "Ask a question")

The ask question page where customers can post a question

  ![List categories](/faq/wireframes/categories.jpg "List categories")

The admin can see and edit or delete categories on the categories page

  ![Edit Categories](/faq/wireframes/editC.jpg "Edit Categories")

The edit category page which allows the admin to change the name of a category

  ![Answer Questions](/faq/wireframes/answer.jpg "Answer Questions")

  The answer questions accordion allows the admin to select a question to answer and they can then answer the question and assign it to a category.

[Back to Index](#table-of-contents)

## Design Strategy

### The strategy plane:
**What are you aiming to achieve in the first place and for whom?**

*** Users
The site is designed to allow visitors to the site to register and ask questions of the site owner.

Users should be able to use the site without needing additional instruction.

The interface should be simple and work on a variety of devices.

Submitted questions should be visible to users with a default answer ("Awaiting answer") until they are answered by the admin.

***Admin
Once answered, questions should be assigned to an appropriate category to help other users to find the answer to their question.

The admin should be able to create and edit categories.

The admin should be able to assign questions to categories.

Each question should be able to belong to only one category.

### The scope plane:
**Which features, based on information from the strategy plane, do you want to include in your design?**

**Must Have**

Users must be able to submit questions.

Questions and answers must be displayed on the page.

There must be a contact form

Admins must be able to answer a question and assign it to one of the categories.

Admins must be able to add and edit categories.

**Could Have**

When a new question is submitted, it could automatically be assigned to a "Pending" category


**Future plans**

A future version could allow users to upvote answers to affect their position in the list

A furture version could include a password recovery option using the user's email address.

When a new question is submitted, it could send an email notification to an admin

**Usability**
Users are assumed to be accessing the site on a mobile device so the site should adopt a mobile first design.

Users should be able to navigate the site without instructions, so navigation should be intuitive.

For the initial build, this site will incorporate:
* The basic pages.
* Registration and login pages
* A form to submit a new question.
* A contact form
* An Accordion section will contain the category headings allowing quick access to each category's answers.
* An Admin area to answer questions
* An admin area to add and edit categories.

**Future Development:**
* An voting system to allow users to upvote answers.
* Password recovery option
* email notifications of new questions and answers

### The structure plane:
**How is the information structured and how is it logically grouped?**

The information should be grouped by;

* The landing page will show the basic company information.
* This is a small website for the company and the FAQ is just one section of the site.
* The main FAQ page will contain the Accordion section with answer categories. 
* A page will contain the Ask Question form.
* A page will handle the user registration.
* A page will handle the user profile including account deletion
* Terms and conditions for registration should be on a modal.

* Admin functions will only be visible to the admin user. 


### The skeleton plane:
**How will our information be represented, and how will the user navigate to the information and the features?**

The main user page will contain a menu which allows users and the admin to login and access further pages

Messages will be displayed to tell the user their question has been submitted and to confirm actions.

### The surface plane:
**What will the finished product look like? What colors, typography, and design elements will we use?**

Wireframes for the site are below:

Initial designs for the site. All pages to be responsive.
  
  ![Landing Page](/faq/wireframes/landing.jpg "Landing Page")
  
  ![FAQ Page](/faq/wireframes/faq.jpg "FAQ Page")

  ![Contact Page](/faq/wireframes/contact.jpg "Contact Page")

  ![Register Page](/faq/wireframes/register.jpg "Register Page")

  ![Login Page](/faq/wireframes/login.jpg "Login Page")

  ![Ask a question](/faq/wireframes/ask.jpg "Ask a question")

  ![List categories](/faq/wireframes/categories.jpg "List categories")

  ![Edit Categories](/faq/wireframes/editC.jpg "Edit Categories")

  ![Answer Questions](/faq/wireframes/answer.jpg "Answer Questions")

The pages will use the default Bootstrap colours for all elements.

Messages will be yellow on a black background.

[Back to Index](#table-of-contents)

## Features

### Responsive
The site must be designed to work on on all devices from mobile to desktop.

### Intuitive
Navigation and use of the website must be intuitive allowing the user to be able to navigate the site without instructions

[Back to Index](#table-of-contents)

## Technologies Used

### Languages Used
[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/CSS)

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Libraries & Programs Used

[Bootstrap 5.3.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
Bootstrap was used to assist with the responsiveness and styling of the website.

[Google Fonts:](https://fonts.google.com/)
Google fonts were used to import the 'Poppins' font into the style.css file which is used on all pages throughout the project.

[jQuery:](https://en.wikipedia.org/wiki/JQuery) is used for additional functions in Bootstrap function.

[Git:](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

[GitHub:](https://github.com/) is used to store the projects code after being pushed from Git.

## Image Credits

Hero Image from [Backstagecrew](https://backstagecrew.com)

[Back to Index](#table-of-contents)

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapp-faq.herokuapp.com%2F)

W3C CSS Validator - Results [link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fapp-faq.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors)

## Testing User Stories from User Experience (UX) Section

* ### User Stories
  - #### First Time Visitor Goals
  
    a. As a first time visitor, I would like to be able to register to ask questions.

    There is a registration page to allow users to create an account which will allow them to ask a question
  
    b. As a first time visitor, I want to be able to ask a question without needing further instructions.

    On clicking the 'Ask Quesion" button, if the user is not logged in, a modal will prompt the user to log in or register a new account.

  ![User not logged in modal](/faq/static/images/modal1.JPG "User not logged in modal")

    c. As a first time visitor, I want to be able to see if my question has already been answered.

    All visitors can access the questions and answers without having to create an account
    
  - #### Returning Visitor Goals
  
    a. As a returning visitor, I want to be able to see if the question I asked, has been answered.

    A logged in user can see their questions and answers when logged into their profile page

    b. As a returning visitor, I want to be able to delete a question I asked

    The questions on the user's profile page each have a delete button to give the option to delete

    c. As a returning visitor, I would like to contact the site owner

    There is a contact form 
    
  - #### Frequent User Goals
  
    a. As a frequent user, I want to be able to browse the questions asked by others.

    All users can see the questions and answers on the faq page

    b. As a frequent user, I want to be able to delete my account and all questions I asked

    The user profile page has an option to delete the user account. This will also automatically delete all that users questions
    
### Further Testing

#### Testing the register function for valid entries
While building the register function, I used conditional print statements to check that the inputs were valid before coding the functionality. eg

      `if terms != 'on':
        print ("Terms not accepted")`

      `if password1 != password2:
        print("Passwords don't match")`

      `if terms and (password1 == password2):
        print("Everything OK")`

#### Testing the user and admin options.

All of the nav links were tested from each page for functionality before the conditionals were added to restrict access to users or admins as apppropriate.
These links were then tested again from each page with logged in user and admin omly options to confirm that they funtion correctly.

The functionality of the user asking questions has been checked to ensure that the user can only post when logged in and that the question can only be deleted by the user.

The answer question function has been tested to ensure that only the admin can answer questions and assign a category to the question.

Only the admin is able to create, edit and delete categories. This has been checked to ensure the non-admin users do not have this ability.

Test questions and answers have been submitted, assigned to categories and then the category deleted to ensure that the cascade workes to delete the appropriate questions.

Test questions and answers have been submitted, assigned to categories and then the user deleted to ensure that the cascade workes to delete the appropriate questions.


#### Layout tests

The Website was tested on Google Chrome on both a laptop, tablet and mobile phone for functionality and responsiveness

The responsivity of the website was checked on a variety of devices using [Responsive Design Checkers](https://responsivedesignchecker.com/checker.php?url=app-faq.herokuapp.com&width=1500&height=1200) and [AmIResponsive](https://ui.dev/amiresponsive?url=https://app-faq.herokuapp.com)

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Solved Bugs

Bug: Form data not being passed to the @app.route

Cause: The form was built with `id` attributes but not `name` attributes

Solution: Added `name` attributes to the form elements

------------------------------------------------------------

Bug: The 'Ask Question button on the faq page allowed anyone to ask a question without logging in

Cause: All users need to be able to view the faq whether logged in or not.

Solution: Add a pop up modal if the usert is not logged in, to offer a redirect to register page

------------------------------------------------------------

Bug: userid session not set on registration enabling the user to ask a question without an id which throws an error

Cause: userid session set on login only

Solution: added userid session declaration into register route

------------------------------------------------------------

Bug: User 'logged out' message not showing on logout

Cause: Flashed messages are session variables and are cleared when the session is cleared.

Solution: Call session.clear() before setting the flashed message

------------------------------------------------------------

Bug: Unable to add questions on initial deployment.

Cause: New questions assigned to category-name 'Unanswered' with category.id '0'. Category doesn't exist on creation

Solution: Add conditional in categories route to check category.id[0] exists and add if not create it

------------------------------------------------------------

Bug: No way to create first user as admin.

Cause: All users are created as non-admin by default

Solution: Check if admin exists and if not, add first user as admin on registration


[Back to Index](#table-of-contents)

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/BackstagecrewIS)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section on the left column.
4. Under "Source", select 'Deploy from Branch then click the dropdown called "None" and select "Main".
5. Click Save to confirm the choice.
6. Scroll back to the top of the page to locate the link to the published site in the "GitHub Pages" section.

[Back to Index](#table-of-contents)


### Forking the GitHub Repository

A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project by using the following steps

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) above the Settings Button on the menu, click the Fork Button.
3. Scroll down the page and click the Create Fork button to make a copy.
4. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click the Code button next to the green Gitpod button.
3. To clone the repository using HTTPS, under the HTTPS tab, copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
7. Press Enter. Your local clone will be created.

Click [Here](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for the Github tutorial.

### Deploying to Heroku

#### Set up a database on ElephantSQL

1. Navigate to ElephantSQL.com and click “Get a managed database today”

2. Select “Try now for FREE” in the TINY TURTLE database plan

3. Select “Log in with GitHub” and authorise ElephantSQL with your selected GitHub account

4. In the Create new team form:
  a. Add a team name (your own name is fine)
  b. Read and agree to the Terms of Service
  c. Select Yes for GDPR
  d. Provide your email address
  e. Click “Create Team”

5. Click “Create New Instance”

6. Set up your plan
  a. Give your plan a Name (this is commonly the name of the project)
  b. Select the Tiny Turtle (Free) plan
  c. You can leave the Tags field blank

7. Select “Select Region” (Select a data center near you)

8. Then click “Review”

9. Check your details are correct and then click “Create instance”

10. Return to the ElephantSQL dashboard and click on the database instance name for this project

11. In the URL section, clicking the copy icon will copy the database URL to your clipboard

12. Log into Heroku.com and click “New” and then “Create a new app”

13. Choose a unique name for your app, select the region closest to you and click “Create app”

14. Go to the Settings tab of your new app

15. Click Reveal Config Vars, then add the config variables from the env.py file

16. Return to your ElephantSQL tab and copy your database URL

17. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”

18. Navigate to the “Deploy” tab of your app

19. In the Deployment method section, select “Connect to GitHub”

20. Search for your repo and click Connect
    Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository

21. As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch. This will start the build process

22. Now, we have our project in place, and we have an empty database ready for use. We still need to add our tables to our database. To do this, we can click the “More” button and select “Run console”

23. Type python3 into the console and click Run

24. This opens the Python terminal. Now create the tables with the commands:

  `from taskmanager import db`

  `db.create_all()`

25. Exit the Python terminal, by typing exit() and hitting enter, and close the console. The Heroku database should now have the tables and columns created from the models.py file.

26. The app should be up and running now, so click the “Open app” button

## Credits

Nav, Buttons, Cards, Modals Adapted from example code at [Bootstrap](https://getbootstrap.com/)

Nested Accordion adapted from [CodePen](https://codepen.io/WinterSilence/pen/abpopXa)

Hero image CSS adapted from [W3Schools](https://www.w3schools.com/howto/howto_css_hero_image.asp)

Hero Image from [Backstagecrew](https://backstagecrew.com)

Icons sourced from [Font Awesome](https://fontawesome.com/)

Heroku deplyment sourced from [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+2022_Q3/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

Thanks go to my mentor Narender Singh for advice and guidance.

[Back to Index](#table-of-contents)

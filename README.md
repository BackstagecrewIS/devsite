<h1 align="center">Frequently Asked Questions</h1>

[Link to the deployed site](# "Link to the site")

An interface for handling frequently asked questions on a website

It is designed to be used on any device.

![The Site](Link "FAQ Site")

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
    
  - #### Frequent User Goals
  
    a. As a frequent user, I want to be able to browse the questions asked by others.

    b. As a frequent user, I want to be able to delete my account and all questions I asked
    
* Design Considerations
  - Colour Scheme
  
  The colour scheme is the standard bootstrap colour scheme using white background and blue buttons.
  Edit buttons will be yellow and delete buttons, red.

  The error messages and confirmation in the registration process will be yellow text on a black background to differentiate them from the buttons

  The messages confirm to the user that their question has been submitted. These will be yellow text on a black background to differentiate them from the buttons
  
  - Typography
    
    For simplicity, only one font style will be used. The Poppins font is a clear sans-serif font which works well for all elements of the site. The fallback sans-serif is specified in case the Poppins font fails to load.
    
  - Imagery
  
    Hero Image from [Backstagecrew](https://backstagecrew.com)

    The icons used are sourced from [Font Awesome](https://fontawesome.com/)
    
  - Wireframes
  
  ![User Page](# "FAQ Main user page")  
  
  ![Admin Page](# "FAQ Main admin page")
  
  ![Admin Page](# "FAQ Admin page")

[Back to Index](#table-of-contents)

## Design Strategy

### The strategy plane:
**What are you aiming to achieve in the first place and for whom?**

*** Users
The site is designed to allow visitors to the site to register and ask questions of the site owner.

Users should be able to use the site without having additional instruction.

The interface should be simple and work on a variety of devices.

Submitted questions should be visible to users with a default answer ("Awaiting answer") until they are answered by the admin.

Submitted questions should be assigned to a pending question category until they are answered.

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

Admins must be able to answer a question and assign it to one of the categories.

Admins must be able to add and edit categories.

**Could Have**

When a new question is submitted, it could automatically be assigned to a "Pending" category

When a new question is submitted, it could send an email notification to an admin

**Future plans**

A future version could allow users to upvote answers to affect their position in the list

Better user password options could include the option for special characters.

A furture version could include a password recovery option using the user's email address.

**Usability**
Users are assumed to be accessing the site on a mobile device so the site should adopt a mobile first design.

Users should be able to navigate the site without instructions, so navigation should be intuitive.

For the initial build, this site will incorporate:
* The basic pages.
* A form to submit a new question.
* An Accordion section will contain the category headings allowing quick access to each category's answers.
* An Admin area to answer questions
* An admin area to add and edit categories.

**Future Development:**
* An voting system to allow users to upvote answers.
* Password recover option

### The structure plane:
**How is the information structured and how is it logically grouped?**

The information should be grouped by;

* This is a small website for the company and the FAQ is just one section of the site.
* The main FAQ page will contain the Accordion section with answer categories. 
* A page will contain the Ask Question form.
* A page will handle the user registration.
* A page will handle the user management including account deletion
* Terms and conditions for registration should be on a modal.

* Admin functions will only be visible to the admin user. 


### The skeleton plane:
**How will our information be represented, and how will the user navigate to the information and the features?**

The main user page will contain a menu which allows the admin to login and access admin pages

A message will be displayed to tell the user their question has been submitted.

### The surface plane:
**What will the finished product look like? What colors, typography, and design elements will we use?**

Wireframes for the game display and instructions modals are below:

![The User Page](# "The User Page")

![Admin Pages](# "Admin Pages")

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

[Balsamiq:](https://balsamiq.com/)
Balsamiq was used to create the wireframes during the design process.

## Image Credits

Hero Image from [Backstagecrew](https://backstagecrew.com)

[Back to Index](#table-of-contents)

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbackstagecrewis.github.io%2Ftictactoe%2F)

W3C CSS Validator - Results [link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbackstagecrewis.github.io%2Ftictactoe%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

## Testing User Stories from User Experience (UX) Section

* ### User Stories
  - #### First Time Visitor Goals
  
    a. As a first time visitor, I want to learn how to play the game.
    
    The instructions button is on the game screen and opens a modal with game instructions. when closed, the game is ready to play.
    
  - #### Returning Visitor Goals
  
    a. As a returning visitor, I want to be able to play the game immediately.
    
    As soon as the page loads, the game is ready to play.
    
    b. As a returning visitor, I want to be able to play an opponent multiple times and keep score.
    
    The game records and displays the number of wins for each player and updates after each game.
    
  - #### Frequent User Goals
  
    a. As a frequent user, I want to be able to play an opponent multiple times with an equal chance of either of us winning.
    
    The first move alternates between players at the start of each new game.
    
    b. As a frequent user, I want to be able to play different opponents.
    
    If a different opponent is needed, the game scores can be reset using the reset scores button.

### Further Testing

#### Testing the register function for valid entries
While building the register function, I used conditional print statements to check that the inputs were valid before coding the functionality.

      `if terms != 'on':
        print ("Terms not accepted")`

      `if password1 != password2:
        print("Passwords don't match")`

      `if terms and (password1 == password2):
        print("Everything OK")`

#### Testing the nav options.

All of the nav links were tested from each page for functionality before the conditionals were added to restrict access to users or admins as apppropriate.
These links were then tested again from each page with logged in user and admin omly options 


MORE NEEDED IN THIS SECTION

The Website was tested on Google Chrome on both a laptop and mobile phone for functionality

The responsivity of the website was checked on a variety of devices using [Responsive Design Checkers](http://responsivedesignchecker.com/checker.php?url=https%3A%2F%2Fbackstagecrewis.github.io%2Ftictactoe%2F&width=1400&height=700) and [AmIResponsive](https://ui.dev/amiresponsive?url=https://backstagecrewis.github.io/tictactoe/)

MORE NEEDED IN THIS SECTION

A large amount of manual testing was done to ensure that the game functions correctly.

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

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

Bug: 

Cause:

Solution:


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

## Credits

Nav, Buttons, Cards, Modals Adapted from example code at [Bootstrap](https://getbootstrap.com/)

Nested Accordion adapted from [CodePen](https://codepen.io/WinterSilence/pen/abpopXa)

Hero image CSS adapted from [W3Schools](https://www.w3schools.com/howto/howto_css_hero_image.asp)

Hero Image from [Backstagecrew](https://backstagecrew.com)

Icons sourced from [Font Awesome](https://fontawesome.com/)

Thanks go to my mentor Narender Singh for advice and guidance.

[Back to Index](#table-of-contents)

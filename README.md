# WorKout App
## Background 🏞
This application is a workout out app where you can create a workout and routine as well as put the amount of food you had that day. Also you can upload a picture of yourself to help give you a visual track of your progress.

This CRUD application was developed using RESTful architecture principles and using Python, Django and SQL through Postgres.

## Application Details 📝
Upon starting the application, they will be in the main page of the site where the tables would be updated, before logging in with the regular login features that most websites have such as username and password. If you are new to the site you can click on the sign up on the nav bar. You an enter a username of your choosing with the certain criteria that must be meet same goes for the password.

Once a user has logged in with the above login, they will be brought to an index view of all the workouts they might have added. Also on the nav bar the user will be able to see their username being displayed beside a welcome message. If the user already has workouts in the table they can check the details about that workout. If you want to create a new workout then you can click the `New Workout` button on the navigation bar. Once clicked you will be in a new page where you will be adding the workout name and date. After that you click on `Add Workout` button. You will then be redirected to the index view. From there you can click on the name of that workout and then be redirected to the workout details page. Once on the page the user can look at your workout on the left side of the page where you can see the workout name and date. Below it you will have two button one being `Edit` and `Delete`. The user can click on the `Edit` button and edit the workout details and change the information such as the name and date.  The user can also delete the workout and so it will not only delete the workout but the other things associated with that such as the diet, a photo/s, and routine. All these features we will talk about right now. A user can on the right side of the details page there is a form were the user can create a routine in which you can put the name of that routine, the number of sets and reps of that routine as well. Once that information is add they can add the routine to the workout page by having clicked on the `Add Routine` button and it will be shown right below the form. Also below the workout details there is a diet form in which similar to the routine one you enter the name and the number fo grams of that food that you are having. That information once entered and having clicked the `Add Diet` button will be below the diet form. At the very bottom of the details page there is the option to also upload a picture of yourself using the AWS feature. We thought this would be great so that the user can have almost of visual of their progress as they go through their fitness journey.


## Technologies Used:
[HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/python-%23323330.svg?style=for-the-badge&logo=python&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-6DA55F?style=for-the-badge&logo=django&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-%234ea94b.svg?style=for-the-badge&logo=sql&logoColor=white)
![PIP3](https://img.shields.io/badge/pip3-%23000000.svg?style=for-the-badge&logo=pip3&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23000000.svg?style=for-the-badge&logo=aws&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)


## App Images

Login Page :![My Image](/Travel-Itinerary/assets/images/Screen%20Shot%202022-11-25%20at%209.05.25%20PM.png)

Sign up Page :![My Image](/Travel-Itinerary/assetsimagesScreen%20Shot%202022-11-25%20at%209.05.25%20PM.png)

Front page :
![My Image](/Travel-Itinerary/assets/images/Screen%20Shot%202022-11-25%20at%209.05.25%20PM.png)


Details page:
![My Image](/Travel-Itinerary/assets/images/Screen%20Shot%202022-11-25%20at%209.05.58%20PM.png)

New Workout page:
![My Image](/Travel-Itinerary/assets/images/Screen%20Shot%202022-11-25%20at%209.16.21%20PM.png)



## Getting Started

Trello:
[Live Site](https://trello.com/b/QuvYgKRu/workout-app)

ERD:
[Live Site](https://app.diagrams.net/#G1a_0YrvwpETLdeMa0cbhyCzxbXqIoDQSY)

WireFrame:
[Live Site](https://app.diagrams.net/#G1DY7EuXlKSAvfgCL_RIhBpmRE4eMorna7)


## Icebox Features 🧊
While this application accomplishes some user-functionality, there are a number of icebox features which will be added as availability permits. Here are some of the future upgrades...

- A calorie count feature so the user can see the calories consumed and the calories burned(The app can either get this through user entry or through a fitness tracking device that the app can get the information from.)

- A feature that can keep track of your progress such as increases of certain things in a routine such as weight, reps, or sets.

- A goals feature that can keep the user more engaged in the app. So a user can enter certain workout goals or diet goals and once they achieve them they can rank up. Sort of like on your smart watch device if get a certain amount of steps in you get a medal.






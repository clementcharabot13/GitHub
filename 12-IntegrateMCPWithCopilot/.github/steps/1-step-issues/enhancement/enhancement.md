# Hard to change activities

Teachers are afraid to modify the program since they think they might break it. Move the list of activities out of the python file into a dedicated `activities.json` file.

# Add filters

There seems to be no order to the activities. Please fix this.

Here are my ideas, maybe in a toolbar above the activity cards.

- Add some filters, for example by category. If needed, add a field to the JSON.
- Add options to sort, for example by name or time. If needed, add a date field but leave the textual description version of the time.
- Add a free text search.

Obviously, make sure it still looks good on desktop and phone.

----- COMMENTS -----
This will be so useful. We should be proactive and do this before the list gets even longer.
Let's do it! I would love to help out. I just took a coding class. 🤓

# Admin Mode

## Problem

Students are removing each other to free up space for themselves in the activities.

## Recommended Solution

Add a user icon in the top right. When clicked it shows a login button. When the login button is clicked, it presents a window to enter a username and password.

- Only the teachers (logged in) have the ability to register and unregister students to activities.

- The students (not logged in) can still view who is registered.

- There is no need for an account maintenance page. Teachers will be assigned passwords.

## Context

Since there is no database yet, please store the teacher usernames and passwords in a `json` file that is checked by the backend.

# 🚨 Missing Activity: GitHub Skills

The GitHub Skills activity announced by our principal is missing from the school activities signup page.

Yesterday in the school assembly, the principal announced a new partnership with GitHub to teach students practical coding and collaboration skills. However, when I try to sign up for this activity, I can't find it on the website.

I can see several other activities, like these, so I think I have access.

- ✅ Chess Club
- ✅ Programming Class
- ✅ Gym Class

## ⏱️ Timeline

This is time-sensitive as the announcement mentioned registrations would close by the end of this week. Many students are eager to join. It's the first part of our [GitHub Certifications program](https://resources.github.com/learn/certifications/), which will help with college applications.

## 💡 Expected Outcome

The GitHub Skills activity should be added to the system and available for registration like other activities

Hewbie C.
11th Grade Student

# Prettier Interface

Now that we have many activities, the list on the left is too long so it is hard to navigate. And the add dialog is far away from the activity.

- Move the cards to the bottom

- Remove the registration form and replace it with a "register student" button on each activity card.

- Make sure it looks good on desktop and phone.

----- COMMENTS -----
I second this idea. I'm having trouble finding my activity.
100% support this. Nice idea! Looking forward to the update.
Don't forget about tablet's too.

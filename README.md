# CruzHacks 2023: "Pictrician" by Coding Connoisseurs 😼💻
https://github.com/crystalh000/coding-connoisseurs-

## Brief Overview

A poor diet and lack of nutrition can lead to detrimental effects on one's health in both the short and long term. It can be difficult to constantly keep track of and consume the right amount of nutrients, especially since human bodies can sometimes take longer to respond negatively to a poor diet. The best defense is to maintain a healthy diet with a balance of nutrients, but this approach demands a lot of time and effort with all the nutrients and foods consumed by the average person every day.

Our app attempts to ease the amount of labor involved in the process by only requiring the user to photograph their meals through the app. Then we use AI photo analysis to extract and record nutritional information from each meal, and run a data analysis algorithms to provide feedback on their nutritional intake after set time intervals. Users will also be able to manually input nutritional and personal information or goals to further improve the accuracy of recommendations.

## User experience

Users begin by creating an account and inputting information about themselves. Then we will introduce the app throguh a tutorial, including how to use its features and what to do every day.

Every day, the user will use the app to photograph their food and/or drinks before eating. The app will display data to confirm that the AI got it right, then records the information to the user's account data.

Every week, the user will receive a notification containing their weekly summary of nutrtitional intake and how well they did compared to the healthy ranges for their demographic. The app will give suggestions for what foods to try and eat more of to make up nutritional deficiencies, or recommend cutbacks for foods that contain too much of a nutritional category. The summary would also contain information on progress toward goals, if the user has set any.

## Implementation

We use HTML and Javascript to set up a website where users log in. [FRONTENT]

We use a food distinguishing AI to process photos that the user uploads. This is done through our stand-in AI in Python (since we do not have enough time to train a model). Instead, we will use a pseudo-AI that knows the colors of a small selection of food categories and compares the photo to known examples. After user confirmation, the category data, photo, and other data are written to a file. At the end of the week, the file is iteratively read and processed algorithmically. We calculate the expected/healthy ranges for each nutrition field and display it next to the user's intake for that week. For every value outside of the range, we will check what foods from the week contributed too much, or what foods to eat more of to get into range. The weekly data is then moved to another file for archival, only to be accessed if the user wants to look back. The app is now ready to record data again.

## If we had more time

We would train a gradient descent AI to take in an array as input and then return an integer as output. This integer will correspond to an index in a multi-dimentional array sorted by categories of food where closer categories are closer together in index position. This allows the error to be helpful to the AI in training. We would also train it to determine the quantity of different food categories in each photo and get a more precise identification of the type of meat, vegetable, etc... This means extracting the exact nutritional values of different nutrients instead of recording the types of food eaten.

We would like to expand the app to cover more aspects of health, such as movement/activity data, and help users better track their other habits alongside their nutritianal data. This would help them maintain awareness about their lifestyle's healthiness and lets the app provide recommendations for how to reach their goals.

We would also add options to share pictures that they took or share some statistics. We might also add a particularly healthy meal to the weekly summary.

We would also recommend places where the user could go to get food that makes up deficiencies, or alternatives that cut back on surpluses. This could be done by searching local restaurants and recommending a range of nearby places where the user could go.
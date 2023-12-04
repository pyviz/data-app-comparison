# Problem description
It's often a good idea to change the UI of your app to respond to user input.
This problem tests how easy it is to include dynamic UI elements, and to communicate between elements which are dynamically generated.

# Requirements

- The app should have three top level components
    - A slider or numeric input which determines how many cards render
    - A `clear all` button
    - A `fields_completed` text output which shows how many cards have user-entered text
- The cards consist of two elements:
    - A textbox input 
    - A text output which echos back the text input for that card
- When the user changes the numeric input, it should generate that many cards. So if the user selects 9, 9 cards should generate. 
- When the user clicks "clear all", all input text should be cleared
- The `fields_completed` output should report the number of fields where the user has entered text
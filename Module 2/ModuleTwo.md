## Module Two
### M02 Lecture Lab Activity 1
A short program which asks the user for a number (but really brings it in as a string).  Then parses the string to see if each position is a number.  If it is, then it output "You entered a valid number" - but if it is not valid, it output "You entered an invalid character in position: " and the position where it finds the bad value.  
Reminder, the user starts counting from 1, then computer starts from 0, so this program is adjusted accordingly.

This is the output of this specific code:
![M02 Lecture Lab Activity 1]()

### M02 Lecture Lab Activity 2
A program which uses a datatype "byte" and asks for a value for it.  But this is in a loop and inside a try-catch. It uses a catch for out-of-range, range-error, and overflow-error (see https://www.javatpoint.com/cpp-exception-handlingLinks to an external site. for details).

This is the output of this specific code:
![M02 Lecture Lab Activity 2]()

### M02 Programming Assignment - Part 1
This creates a class called Date that has integer data members to store month, day, and year. The class will only have a single 3-parameter constructor which allows the date to be created by specifying the numerical month, day, and year. If the user creates a Date object when any of the values passed are invalid, an invalid argument exception should be thrown with appropriate text:

- The month must be a valid month (1-12),
- The day must be in the appropriate range for that month (do not worry about leap years), and
- The year must be between 1900 and 2020.

It should include mutator methods for setting the month, day, and year. It should also throw invalid parameter exceptions if invalid parameters are provided. It includes a toString() method that returns the date in the format “Month DD, YYYY” (ex: August 22, 1984).

This is a program that utilizes this class to create and display dates based on user input. Utilizes try-catch blocks to validate the user input. Ensures that the exception thrown includes appropriate text to describe the problem (e.g. “Invalid Value – there are only 28 days in February” or “There are only 12 months in the year”). Demonstrates usage of the class and its embedded exception handling in a program that prompts users for initial date values, creates a date object, and then prompts the user to change the month, change the day, and change the year.

This is the output of this specific code:
![M02 Programming Assignment - Part 1]()

### M02 Programming Assignment - Part 2
This modifies the Stereo Receiver class created in [Module One](). If the user attempts to create or modify a stereo receiver object when any of the values passed are invalid, an invalid argument exception will throw with appropriate text:

- Manufacturer, Model, or Serial Number not provided
- Inappropriate values for Wattage, Number of Channels, Band, Frequency, Volume, or Power 

The constructor and mutator methods will throw invalid parameter exceptions if invalid parameters are provided.

This is a program that utilizes this class to create and display stereo receivers based on user input. Utilizes try-catch blocks to validate the user input. Ensures that the exception thrown includes appropriate text to describe the problem (e.g. “Invalid Value – volume cannot exceed 10” or “Invalid Frequency”). Demonstrates usage of the class and its embedded exception handling in a program that prompts users for initial values, creates a receiver object, and then prompts the user to change the various values.

This is the output of this specific code:
![M02 Programming Assignment - Part 2]()
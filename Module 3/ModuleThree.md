## Module Three
### M03 Programming Assignment - Part 1
This is a two part assignment actually.

#### Grade Statistics
A modular program that analyzes a student’s quiz scores (0-15). In addition to main, the program has a getData function that accepts the quiz scores for 16 weeks from the user and stores it in a template array. It'll also have two value-returning functions that compute and return to main:

- highScore
- lowScore

These functions return the number of the module with the lowest and highest quiz scores, not the quiz scores for those modules. Notice that this module number can be used to obtain the quiz score for that module. This information should be used by the main program to print a summary quiz report similar to the following:

```
{
Fall 2019 Quiz Grades:
    Module 1: 9
    Module 2: 15
    ...
    Module 16: 12

Average Grade: 13
Your lowest score was in Module 5 with 0.
Your highest score was in Module 2 with 15.
}
```

This is the output of this specific code:
![M03 Programming Assignment - Part 1 (Grade Statistics)]()

### Personal Computer
You are an IT Manager for a small company and must create a program to track your company’s personal computer inventory.

This program creates a class that can be used for a Personal Computer. The class has attributes for the:

- Manufacturer (e.g. Dell, Gateway, etc.),
- Form Factor (laptop/desktop),
- Serial Number
- Processor ( I3, I5, I7, AMD Ryzen 3, AMD Ryzen 5, etc.),
- RAM (4, 6, 8, 16, 32, or 64GB),
- Storage Type (UFS, SDD, HDD) and
- Storage Size (128GB, 256GB, 512GB, 1TB, 2TB).
- The constructor accepts the manufacturer, form factor, serial number, processor, RAM, storage type/size.

It Creates accessor methods that allow these attributes to be retrieved individually. Also Creates mutator methods that allow the RAM and the storage drive (type and size) to be changed. Incorporates exception handling to reject invalid values in the constructor and mutator methods. Creates a toString() method formulate a string containing the manufacturer, form factor, serial number, processor, RAM, and storage type/size.

Also a main program that creates a vector that can contain personal computers. The program will prompt the user for an indeterminate number of personal computers, create a personal computer object, and add the object to the vector. After each personal computer is entered the program should display the object that was just created and the total number of personal computers in the list/vector. When the user has finished entering personal computers into their inventory, the program should display the contents of the inventory list (complete list of personal computers).

This is the output of this specific code:
![M03 Programming Assignment - Part 1 (Personal Computer)]()

### M03 Programming Assignment - Part 2
This is another two part assignment.

#### Duplicate Words
A program that reads words from a text file and displays all the non-duplicate words. Uses a set container to accumulate non-duplicate words and display a list of the unique words in ascending order at the end of the program.

This is the output of this specific code:
![M03 Programming Assignment - Part 2 (Duplicate Words)]()

#### State Abbreviations
A program to store pairs of each state (two letter abbreviation) with a structure containing its long name, current Governor, and state flower in a map. At startup THE program should read the abbreviations, long name, and governor's name for each state from a text file and store the values in a map. The program should then prompt the user to enter a state's two-letter abbreviation and display the corresponding long name, Governor and flower for that state, looping until a sentinel value is entered. An appropriate non-fatal error message should be displayed for any invalid state abbreviation entered.

This is the output of this specific code:
![M03 Programming Assignment - Part 2 (State Abbreviations)]()
## Module One
### M01 Lecture/Lab Activity 1
This is a short program with a class that has a private integer value, and a public function which will set it if the value passed in is positive. Then in main, it will print the value (notice that this needs to write an accessor function also).

This is the output of this specific code:
![M01 Lecture/Lab Activity 1 Output]()

### M01 Programming Assignment - Part 1
This is a program that will create a cube object and display its volume. It includes a class Cube that includes private data members length (int), width (int), height (int), and color (string).

Includes a constructor for the class that receives the length, width, height, and color. The constructor will set the attributes with the values provided. The class should have public member functions:

- Accessor methods getLength, getWidth, getHeight, and getColor returning the appropriate attribute of the cube.
- Mutator methods setLength, setWidth, setHeight, and setColor that allow the attributes of the cube to be changed.
- A calculateVolume method that will return the volume of the cube (volume = length*width * height).

Has a main program that utilizes the Cube class

- Prompts the user for the length, width, height, and color of a cube
- Validates the information
- After Information from the user has been validated, it creates an object for the Cube.
- Using the Accessor Methods, it displays the cube’s information (length, width, height, color, and volume).
- Allows the user to change/set the length, width, height, and color. Validates any input before calling the appropriate functions.
- Displays the cube’s attributes after the cube has been changed using the appropriate methods.

This is the output of this specific code:
![M01 Programming Assignment - Part 1]()

### M01 Programming Assignment - Part 2
Includes a StereoReceiver class.

- The attributes for the StereoReceiver are:
    - Manufacturer
    - Model
    - Serial Number
    - Wattage,
    - Number of Channels
    - Band (AM/FM)
    - Frequency (i.e. ‘station’)
    - Volume (0-10)
    - Power (i.e. On/Off)
    - Wifi
    - Bluetooth
- Creates a constructor for the class that receives a Manufacturer, Model, Serial Number, Wattage, and Number of Channels. The constructor will set the attributes provided and also initialize any other attributes (e.g. power, volume, band, frequency, etc.)
- Provides separate Accessor/Get Methods that will return Manufacturer, Model, Serial Number, Wattage, Number of Channels, Band, Frequency, Volume, and Power.
- Provides separate Mutator/Set Methods that will allow a user to turn the receiver on/off, change the volume, change the band, set the frequency/station, etc.
- Provides Accessor/Mutator methods for the attributes you provided as appropriate.
 
Create a main program that utilizes the StereoReceiver class

- Prompts the user for the Manufacturer, Model, Serial Number, Wattage,, and Number of Channels
- Validates the information
- After Information from the user has been validated, it creates an object for the StereoReceiver.
- Using the Accessor Methods, it displays the StereoReciever’s information (manufacturer, model, etc.).
- Turns on the StereoReceiver using the appropriate method.
- Allows the user to change/set the band, frequency, and volume. Validates any input before calling the appropriate functions.
- Allows the user to change any of the attributes (appropriately)
- Displays the StereoReceiver’s settings (power, band, station, and volume)
- Turns off the StereoReceiver.

This is the output of this specific code:
![M01 Programming Assignment - Part 2]()
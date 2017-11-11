Welcome to CircuitPython!
#############################

Visit the Trinket M0 product page here for more info: 
                              https://adafruit.com/product/3500


#############################

The Trinket has a very tiny disk drive so we have disabled Mac OS X indexing
which could take up that valuable space. 

So *please* do not remove the empty .fseventsd/no_log, .metadata_never_index 
or .Trashes files! 

#############################

The pre-loaded demo shows off what your Trinket M0 can do with CircuitPython:
  * The built in DotStar LED can show any color, it will swirl through the rainbow
  * Pin D0 is an analog input, the REPL will display the voltage on this pin 
    (0-3.3V is the max range)
  * Pin D1 is a true analog output, you will see the voltage slowly rise
  * Pin D2 is a digital input with a pull-up, you can touch this pad to GND
    to activate the button (or wire up a tactile button or switch!)
    If you update main.py to uncomment the relevant lines, it will act as a 
    mini keyboard and emulate an 'a' key-press whenever D2 is grounded.
  * Pin D3 is a capacitive input, when touched, it will turn on the red LED. 
  * Pin D4 is a NeoPixel output, you can wire up a strip of NeoPixels to this
    pin (power from USB and GND). The first 16 NeoPixel will rainbow swirl

For more details on how to use CircuitPython, visit 
https://adafruit.com/product/3500 and check out all the tutorials we have!

#############################
CircuitPython Quick Start:

Changing the code is as easy as editing main.py in your favorite text editor. 
We recommend Atom, Notepad++, or Visual Studio Code. After the file is saved,
CircuitPython will automatically reload the latest code. Try enabling the 
single-button keyboard (HINT: look for the "# optional! uncomment below..." text)

Connecting to the serial port will give you access to better error messages and
interactive CircuitPython (known as the REPL). On Windows we recommend Tera Term
or PuTTY. On Mac OSX and Linux, 'screen' can be used from a terminal.

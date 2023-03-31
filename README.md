# KML2GPX Converter, with Google Earth and Garmin icons capacity. 
A simple Python program that converts .kml files to .gpx files taking into account the POIs icons. :octocat: :octocat:

This project contains both, an .exe executable file and a Python program, that allow the user to convert his .kml files 
to .gpx files offline. The translator also takes into account the icons used during the design of the route in Google 
Earth, and renames them to Garmin default (or custom) icons.

<table>
  <tr>
    <td> <b>Manhattan route in Google Earth.</b></td>
  </tr>
  <tr>
    <td> <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/ManhattanEarth.png"  
         title="Manhattan Route in Google Earth" alt="Manhattan Route in Google Earth" width="900" height="400" /></td>
 </tr>
</table>
<table>
  <tr>
    <td> <b>Manhattan route in Garmin Etrex Touch 35</b> </td>
  </tr>
  <tr>
    <td><img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/ManhattanGarmin1.bmp"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="300" height="400" /></td>
    <td>
         <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/ManhattanGarmin2.bmp"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="300" height="400" /></td>
    <td>
         <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/ManhattanGarmin3.bmp"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="300" height="400" /></td>
<td>
  </tr>
</table>

## Table of Contents

* [Introduction](#introduction)
* [The Icons](#the-icons) 
* [Executable](#executable)
* [Program](#program)

## Introduction

This project was born as a request from my father (67 years old, at the time of writing). My father has been riding a motorcycle
since he was a child, but over the years he has turned more to planning routes and long distances.

He was using a flimsy government-developed tool for agriculture (I won't go into more detail on
this tool, but it was outdated, with poor image quality and with a minimum number of coordinates, it failed). 
In addition, this tool didn't allow to export the files to any format, so he was writing down notes by hand to a book. 
And finally from there to his Garmin device also one by one... 
So I decided to show him how Google Earth could improve and streamline the way he was doing the routes.

Everything went as planned, my father was impressed by how easy we could create the routes, how precise and well we could
see the terrain that he was going to pass through with his enduro bike. 

The problem appeared when we wanted to pass the route to the Garmin GPS. To convert the google KML format to GPX, we 
found web pages that allowed to do it online. I don't know why, but this was beyond the technological capabilities of my
father, who with changing web pages, ads (click here, download this, wait 2 minutes...) and gerographic names, couldn't
manage alone. 

Personally, the straw that broke the camel's back was that all my father's effort in selecting icons, was 
wasted when these online converters didn't take images into account.

So I decided to create this program for him.

## The Icons
Most of the developing time has been spent in gathering and relating the most frequently used icons from Google Earth 
and the default Garmin icons. The Excel file 
[IconRelation.xlsx](https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/IconRelation.xlsx) is the result
of this effort.
    <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/IconTable.png"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="300" />

Notice that not all Garmin icons have an equivalent in the Google Map column and vice-versa. This is because I didn't 
find a nice match. Feel free to edit this file to interchange icons & names, to add new icons or delete old ones. Keep in mind that
this file is just a reference for the converter and no icons are added to Google Maps nor the GPS from this file. 

Also notice that there are some custom icons that appears  at the same time in Garmin and Google. These icons are custom-made 
icons that my father wanted to have to better plan his routes. 
    <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/CustomIcon.png"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="400" />

If you want, you can add these custom icons to your device. They are placed in 
[/Resources/Icons](https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Icons):
- [PNG](https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Icons/PNG): Images to import in Google Earth with
transparency.
- [BMP](https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Icons/BMP): Equivalent images to import in the 
Garmin device (transparency as magenta ![#f03c15](https://placehold.co/15x15/ff00ff/ff00ff.png) ).

To install custom icons in the Garmin device refer to: [GARMIN](https://support.garmin.com/en-US/?faq=VTS8XTdjCW5Tx3HyfJ3eQ6&productID=156873&searchQuery=symbols%20waypoint&tab=topics)


## Executable
Use the executable file is straight forward (at least in Windows):

1. Run the kml2gpx.exe file:

    <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/Step1.png"  
         title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="400" />

2. Select the IconRelation.xlsx file:
       <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/Step2.png"  
            title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="400" />

3. Select the *.kml file (ManhattanRoute.kml in my case):
       <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/Step3.png"  
            title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="400" />

4. You did it!!! Three clicks, and we have converted the KML file to GPX:
       <img src="https://github.com/SergioOyaga/KML2GPX/blob/master/Resources/Images/Step4.png"  
            title="Manhattan Route in Gamin" alt="Manhattan Route in Gamin" width="600" height="400" />

Now we only have to move the gpx file to our device, and we are done :smiley:

## Program

Other option that could be more interesting for advanced users is to download and execute the python code. For those:
1. Download and unzip or git clone the repo (from the command prompt/git bash/anaconda prompt/... ):
 ```code
git clone https://github.com/SergioOyaga/kml2gpx.git
```
2. Create, activate a new environment and install requirements.txt
   1. Create a new virtual environment. [Python Doc](https://docs.python.org/3/library/venv.html)
   2. Activate the venv. [Python doc](https://docs.python.org/3/library/venv.html)
   3. Install the requirements.txt. [Pip Doc](https://pip.pypa.io/en/stable/user_guide/)


3. Redy to go. Now you can choose an editor of your preference to modify the code. You can also run the python code 
directly from de command ([activate](https://docs.python.org/3/library/venv.html) first the venv):
 ```code
python path/to/kml2gpx/kml2gpx.py
```

Note for the programmer, the code is super simple and use two main libraries to convert kml to gpx:
- fastkml
- gpxpy.gpx

There is also installed auto-py-to-exe which I use to create the .exe file. Feel free to remove it 
(and its dependencies) or to use it t create your own executables.

## Disclaimer
Feel free to download, use or edit this code under your own responsibility.
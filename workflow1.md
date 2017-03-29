## Formatting/Categorizing the Data

To make this process easier so the user is able to update this on his own without me, 
I've detailed out here the work flow to make this map. If you ever have questions, please contact me. 

For this to work properly, you need some way to run python code on your computer. I personally use Jupyter Notebooks,
but I saved my work here as plain python. 

* Create a spreadsheet that follows the format: 

> **Column A:** *Destinations* **Column B:** *ID*

* Remove duplicates based only on the ID in the spreadsheet

* Use [this python code](https://github.com/hillele/internshipWork/blob/master/stateClassifier.py) 
to go through the spreadsheet and categorize each of the entries. 

> **NOTE:** This code will not categorize everything, especially mispellings (although it does account for some)
This code also marks entries that do not have a destination - as NONE. 

> Be sure to change the name of the workbook you are categorizing and also the name of the new workbook you want it saved as. 

* Quality check the new spreadsheet and also fill out the categories of the entries the code could not. 

> **NOTE:** If this code can not categorize an item, it defaults to putting in a 0 for the state abbreviation. Those entries
with a 0 will need to be manually entered by the user during the quality check process. 

> If you ever feel like there's a recurring spelling or problem that the code should be able to see, you can most likely 
add it to the python code. Simply go to the end of the possibleInputs line, add your entry, and then add the corresponding 
state abbreviation to the end of the matchAbbrev line. This will help ensure they are on the same index so the code continues 
to work properly. 

* Save the workbook.

* Now use [this python code]() 
to go through the fully categorized data and create counts, ranks, and percentages for each state. 

> The above python code outputs a javascript file. It will be saved as ---.js. Find this file, as it contains all the information 
needed to create/update the map properly. 

And that is it for this section. Now that everything is properly prepped we can move into hosting this data on your website. 



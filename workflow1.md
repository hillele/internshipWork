## Formatting/Categorizing the Data

To make this process easier so the user is able to update this on his own without me, 
I've detailed out here the work flow to make this map. If you ever have questions, please contact me. 

* Create a spreadsheet that follows the format: 

> **Column A:** *Destinations* **Column B:** *ID*

* Remove duplicates based only on the ID in the spreadsheet

* Use [this python code](https://github.com/hillele/internshipWork/blob/master/stateClassifier.py) 
to go through the spreadsheet and categorize each of the entries. 

> **NOTE:** This code will not categorize everything, especially mispellings (although it does account for some)
This code also marks entries that do not have a destination - as NONE. 

> Be sure to change the name of the workbook you are categorizing and also the name of the new workbook you want it saved as. 

* Quality check the new spreadsheet and also fill out the categories of the entries the code could not. 

> If you ever feel like there's a recurring spelling or problem that the code should be able to see, you can most likely 
add it to the python code. Simply go to the end of the possibleInputs line, add your entry, and then add the cooresponding 
state abbreviation to the end of the matchAbbrev line. This will help ensure they are on the same index so the code continues 
to work properly. 

* Save the workbook.

* Select the entire spreadsheet and then 'Insert' a pivot table. 

* In this pivot table, make sure the setup on the right is stAbbrev in both the 'ROWS' and 'VALUES' section. 

> **NOTE:** This table will not show state abbreviations for states that have not appeared in the data

* To account for this, we are going to copy the contents of this pivot table into a new sheet in the same workbook. 
This new sheet should follow the format: 

> **Column A:** *State* **Column B:** *Count*

> **NOTE:** It is very important that these columns have this exact capitalization. 

* Go through this sheet and add any state abbreviation that are missing, and give them a count of 0. 
Also remove the row with 'NONE' in it. 

> An excel file in this repo has been included [here](https://github.com/hillele/internshipWork/blob/master/CategorizedUSStates-March2017.xlsx) 
as an example of how this should turn out. You can download it to view it. 
The code was run in March 2017. The time the data was collected is marked as one of the sheets named, but 
the full data that was provided was sent in an email February 2nd, 2017. 

* Finally make sure you currently are selected on the StateCounts sheet of the workbook, and then hit 'Save As'. 
Give it a new name like 'StateCounts' and then select the file type to be a csv. Save this new file. We need it saved as 
a csv to create the maps. 

And now all of the data is prepped and ready to mapped. 



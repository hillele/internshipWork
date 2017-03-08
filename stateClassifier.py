# Define which workbook you want to classify
currWorkbook = 'USStates.xlsx'
newWorkbook = 'CategorizedUSStates.xlsx'

import openpyxl

wb = openpyxl.load_workbook(currWorkbook)
names = wb.get_sheet_names()
sheet = wb.get_sheet_by_name(names[0])

# Making dictionary of possible inputs and matching abbreviation 
# They must share the same index
possibleInputs = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington d.c.', 'washington dc', 'd.c.', 'washington', 'west virginia', 'wisconsin', 'wyoming', ' dc ', ' dc,', ' al,',' ak,',' az,',' ar,',' ca,',' co,',' ct,',' de,',' fl,',' ga,',' hi,',' id,',' il,',' in,',' ia,',' ks,',' ky,',' la,',' me,',' md,',' ma,',' mi,',' mn,',' ms,',' mo,',' mt,',' ne,',' nv,',' nh,',' nj,',' nm,',' ny,',' nc,',' nd,',' oh,',' ok,',' or,',' pa,',' ri,',' sc,',' sd,',' tn,',' tx,',' ut,',' vt,',' va,',' wa,',' wv,',' wi,',' wy,',  ' al ',' ak ',' az ',' ar ',' ca ',' co ',' ct ',' de ',' fl ',' ga ',' hi ',' id ',' il ',' ia ',' ks ',' ky ',' la ',' me ',' md ',' ma ',' mi ',' mn ',' ms ',' mo ',' mt ',' ne ',' nv ',' nh ',' nj ',' nm ',' ny ',' nc ',' nd ',' oh ',' ok ',' or ',' pa ',' ri ',' sc ',' sd ',' tn ',' tx ',' ut ',' vt ',' va ',' wa ',' wv ',' wi ',' wy ', 'lousiana', 'louisianna', 'tennesse', 'neveda', 'tx','tenesse', 'viginia', 
                  'none','unknown','not', 'no us destination', 'no destination'] 
matchAbbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','DC','DC','DC','WA','WV','WI','WY','DC','DC','AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT', 'VA','WA','WV','WI','WY', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL','GA','HI','ID','IL','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT', 'VA','WA','WV','WI','WY', 'LA', 'LA', 'TN', 'NV', 'TX', 'TN', 'VA',
               'NONE', 'NONE', 'NONE', 'NONE', 'NONE']

# Use this code to check to make sure these all match up appropriately
#i = 0
#while i < len(possibleInputs):
#    print possibleInputs[i] + ", " + matchAbbrev[i]
#    i += 1

# Initialize count of State Abbreviation tracker
st_Abbrev = {'NONE': 0,'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA': 0, 'WA':0, 'WV':0, 'WI':0, 'WY':0, 'DC':0}

# Sometimes only one of these loops works on different computers. If the current loop is giving you an error, try this one:
# for row in sheet.columns[0]:
currRow = 1
for row in sheet['A']:
    i = 0
    foundMatch = False
    curr = " " + row.value.lower() + " "
    newStAbb = '0'
    while (i < len(possibleInputs) and foundMatch == False):
        if possibleInputs[i] not in curr:
            i += 1
        else: # Contains the possible input
            newStAbb = matchAbbrev[i]
            foundMatch = True
    if foundMatch == True:
        st_Abbrev[newStAbb] = 1 + st_Abbrev[newStAbb]
    # Updating rows
    if currRow == 1: # Title row
        sheet['C1'] = "stAbbrev"
    else: 
        cell = 'C' + str(currRow)
        sheet[cell] = newStAbb
    currRow += 1

# Save File
wb.save(filename = newWorkbook)

# Print count of each state
print "Counts:"        
for each in st_Abbrev:
    print each + ": " + str(st_Abbrev[each])


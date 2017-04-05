import openpyxl # May need other imports, but I doubt it

### Pulling full state counts
# Getting access from Excel sheet created in past code
# Note if you changed the name of the file you saved it as 
# Change the file name here, and also if you aren't running 
# Your python from the same place, change the name.
wb = openpyxl.load_workbook('CategorizedUSStates.xlsx')
names = wb.get_sheet_names() 
sheet = wb.get_sheet_by_name(names[0]) 
#Initializing the dictionary so will have zeros for all counts
st_Abbrev = {'NONE': 0,'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA': 0, 'WA':0, 'WV':0, 'WI':0, 'WY':0, 'DC':0}
# Cycling through the spreadsheet to populate the dictionary
for row in sheet['C']:
    if row.value != "stAbbrev": #Skip header
        st_Abbrev[row.value] = st_Abbrev[row.value] + 1

### Determine breakup for the rank
# Default breaks up the counts into 4 even quantiles,
# Counts 0 as part of ranking 1,
# Creates an array category[] that contains all the upperbounds
# Option to manually put in the category breaks
category = []
list_cnts = []
highest = -1
total_cnt = 0
for each in st_Abbrev:
    total_cnt = total_cnt + st_Abbrev[each]
    if st_Abbrev[each] != 0:
        list_cnts.append(st_Abbrev[each])
    if st_Abbrev[each] > highest:
        highest = st_Abbrev[each]
list_cnts.sort() 
num = len(list_cnts) / 4        # change this division number to the number of rankings you want
for i in range(3):              # change this number to the number of rankings you want minus one
    category.append(list_cnts[num * (i + 1)])
category.append(highest)
# If you want to set your own break ups for the data, you can manually set them here
# Simply put the top level of the count for a state for all the breaks except for the last one
# category = [x, y, z] # can handle more/less boundaries
category = [50, 107, 355, 1799] # the boundaries set forth by Ian for beginning interation of this(03/28/2017)

### Attaching the ranking to the appropriate State Abbreviation
st_Rank = {'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA': 0, 'WA':0, 'WV':0, 'WI':0, 'WY':0, 'DC':0}
# Defining a recursive function to determine the rank 
def determine_Rank(count, x, limit):
    if (x == limit or count <= category[x]):
        return x + 1
    else: 
        return determine_Rank(count=count, x=x + 1, limit=limit)
# Cycling through the undefined state ranks and utilizing the above 
# function to determine and then set the rank for each state
for each in st_Rank:
    rank = determine_Rank(limit=len(category), x=0, count=st_Abbrev[each])
    st_Rank[each] = rank
    
### Attaching the percentage to the appropriate State Abbreviation
# Total counts pulled from early in total_cnt
st_Perc = {'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA': 0, 'WA':0, 'WV':0, 'WI':0, 'WY':0, 'DC':0}
# Cyclying through the undefined state percentages and 
# Calculating the percentage student count out of the total
for each in st_Perc:
    perc = st_Count[each] / float(total_cnt) * 100
    st_Perc[each] = perc

### Create a javascript file that contains a dictionary
# in javascript that connects the state abbreviation to
# the rank and percantage. Leaves out the exact counts
j = 0
f = open("st_counts.js", "w+")
f.write("var st_Cnt = [{")
for curr in st_Rank:
    f.write("'" + str(curr) + "': [" + str(st_Rank[curr]) + ", " + str(st_Perc[curr]) + "]")
    if j < 50: # inputs the appropriate amount of commas
        f.write(", ")
    j += 1
f.write("}];")
f.close()

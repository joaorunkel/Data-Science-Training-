# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damage_conversion(damages):
  converted_damage=[]
  for damage in damages:
    if damage!='Damages not recorded':
        if "M" in damage:
          new_damage=damage.replace("M","")
          converted_damage.append(float(new_damage)*100000000)
        if "B" in damage:
          new_damage=damage.replace("B","")
          converted_damage.append(float(new_damage)*100000000000)
    else:
      converted_damage.append("Damages not recorded")
  return converted_damage


# test function by updating damages
converted_damages=damage_conversion(damages)

# 2 
#Sorting the hurricanes

def dictionary_creator(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes={}
  for i in range(len(names)):
    hurricanes[names[i]]={"Month":months[i], "Year":years[i], "Wind":max_sustained_winds[i], "Area Affected":areas_affected[i], "Damage":damages[i], "Deaths":deaths[i] }
  return hurricanes      

hurricanes=dictionary_creator(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# 3
# Organizing by Year

def dictionary_creator_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes={}
  for i in range(len(names)):
    hurricanes[years[i]]={"Name":names[i] ,"Month":months[i], "Wind":max_sustained_winds[i], "Area Affected":areas_affected[i], "Damage":damages[i], "Deaths":deaths[i] }
  return hurricanes      

hurricanes_by_year=dictionary_creator_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths)



# 4
# Counting Damaged Areas

def words_count(hurricanes):
    area_count = {}
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]["Area Affected"]:
            if area not in area_count:
                area_count[area] = 1
            else:
                area_count[area] += 1
    return area_count

areas_count=words_count(hurricanes)

# 5 
# Calculating Maximum Hurricane Count

number_of_hurricanes=len(hurricanes)

# find most frequently affected area and the number of hurricanes involved in
def find_most_affected_area(areas_count):
   area=max(areas_count, key=areas_count.get)
   return area


most_affected_area="The most affected area is " +find_most_affected_area(areas_count)+": "+str(areas_count[find_most_affected_area(areas_count)])
print(most_affected_area)

# 6
# Calculating the Deadliest Hurricane

def count_deaths(hurricanes):
   death_count={}
   for hurricane in hurricanes:
      death_count[hurricane] = hurricanes[hurricane]["Deaths"]
   return death_count

death_count=count_deaths(hurricanes)
     
# find highest mortality hurricane and the number of deaths

most_deadly_hurricane=max(death_count, key=death_count.get)
print("The deadliest hurricane is "+most_deadly_hurricane+": "+str(death_count[most_deadly_hurricane]))

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key

def death_rating(death_count):
   raiting={}
   for hurricane in death_count:
      if death_count[hurricane]==0:
         raiting[hurricane]=0
      if 0< death_count[hurricane] <= 100:
         raiting[hurricane]=1
      if 100< death_count[hurricane] <= 500:
         raiting[hurricane]=2
      if 500< death_count[hurricane] <= 1000:
         raiting[hurricane]=3
      if 1000< death_count[hurricane] <= 10000:
         raiting[hurricane]=4

   return raiting

hurricane_death_rating=death_rating(death_count)

# 8 Calculating Hurricane Maximum Damage

def damage_count(hurricanes, damages):
   damage_count={}
   i=0
   for hurricane in hurricanes:
      damage_count[hurricane]=damages[i]
      i+=1
   return damage_count

damage_dict=damage_count(hurricanes, converted_damages)


# find highest damage inducing hurricane and its total cost
numeric_damage_dict = {hurricane: damage for hurricane, damage in damage_dict.items() if isinstance(damage, float)}
highest_damage = max(numeric_damage_dict, key=numeric_damage_dict.get)
print("The hurricane with biggets damage is "+highest_damage+": "+str(damage_dict[highest_damage]))

# 9
# Rating Hurricanes by Damage
#damage_scale = {0: 0, 1: 100000000, 2:1000000000,3: 10000000000, 4: 50000000000}

def damage_rating(damage_dict):
   rating = {}
   for hurricane in damage_dict:
      if damage_dict[hurricane] == 'Damages not recorded':
         rating[hurricane] = 'Damages not recorded'
      elif damage_dict[hurricane] == 0:
         rating[hurricane] = 0
      elif 0 < damage_dict[hurricane] <= 100000000:
         rating[hurricane] = 1
      elif 100000000 < damage_dict[hurricane] <= 1000000000:
         rating[hurricane] = 2
      elif 1000000000 < damage_dict[hurricane] <= 10000000000:
         rating[hurricane] = 3
      elif 10000000000 < damage_dict[hurricane] <= 50000000000:
         rating[hurricane] = 4

   return rating

  
# categorize hurricanes in new dictionary with damage severity as key
hurricane_damage_rating = damage_rating(numeric_damage_dict)

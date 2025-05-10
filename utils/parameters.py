######################################
# SCRIPT TO HOLD PARAMETERS FOR WHICH DATA TO INCLUDE
#########################################

### IMPORTS
from ScraperFC import FBref

### PARAMATERS

#leagues
leagues = ["Bundesliga","EPL", "La Liga", "Ligue 1", "Serie A"]

#seasons
fbr = FBref()
all_seasons = fbr.get_valid_seasons("Big 5 combined")
seasons = list(all_seasons.keys())[0:5] # current season plus previous five
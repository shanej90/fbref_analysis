#############################################
# FUNCTIONS FOR TAKING FBREF MATCH DATA AND WRITING TO GOOGLE SHEETS
##############################################

### IMPORTS
import ScraperFC as sfc

### READ DATA
def read_fbref_match_data(season, league):
    
    fbr = sfc.FBref() #fbref object
    
    df = fbr.scrape_matches(season, league) #read the data
    
    df["season"] = season
    
    return df





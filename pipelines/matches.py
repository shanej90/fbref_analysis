###############################################
# PIPELINE FOR SCRAPING, SAVING AND PROCESSING MATCH DATA
################################################

### IMPORTS
import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd

from ..utils.parameters import leagues, seasons
from ..scraping.get_matches import read_fbref_match_data

### RUN SCRAPING

match_data = [read_fbref_match_data(s, l) for s in seasons for l in leagues]
all_match_df = pd.concat(match_data) #concatenate into a single dataframe

### WRITE TO SHEETS

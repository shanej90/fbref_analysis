# Analysing football data using FBref

This is a data analytics project that analyses football data across Europe's 'top five' leagues, using data sourced from [FBref](https://fbref.com/en/), a site which compiles a wide range of statistics about matches.

The leagues covered are:
- Bundesliga (Germany)
- La Liga (Spain)
- Ligue Un (France)
- Premier League (England)
- Serie A (Italy)

## Pipeline

The original source for the data is FBref. I use Python to scrape data from the site using `ScraperFC`, a package designed specifically for this purpose. I then transform that data into formats appropriate for a Power BI star schema. I then import the data into Power BI. The Power BI semantic model is made publicly available via NovyPro.

Ideally I would be using SQL here; however in the absence of free cloud storeage options, I have done what you must never do and used spreadsheets as a database. Specifically I have used Google Sheets. This enables automation via Google Cloud Console.

## Links index

- [FBref](https://fbref.com/en)
- [NovyPro](https://www.novypro.com/)
- [ScraperFC](https://github.com/oseymour/ScraperFC/)
- [ScraperFC docs](https://scraperfc.readthedocs.io/en/latest/index.html)
Python script to use column entries as keywords to search on Google (News tab). It stores the data gathered inside a pandas dataframe which will be saved to a CSV file, checks for duplicate entries and keep the last one. This was required because Google News displays the date not in "mm/dd/yyyy" format, but in "X time ago" for recent news, and only converts after some time.


GoogleNews module: https://pypi.org/project/GoogleNews/

# Webscraping-Wikipedia-with-Beautiful-Soup
Scraping ~200 webpages from Wikipedia to determine the most influential western philosopher.
Uses BeautifulSoup to extract text and links from Wikipedia pages.

The computer program will determine the number of times each western philosopher is mentioned and 
follow the most pertinent links on the page. This will be repeated one more time. Weights are 
assigned as such: since there are 23 first-order webpages and 184 second-order webpages, names
mentioned on the main 'western philosophy' page will be assigned a weight of 184, first-order 
webpages a weight of 8, and second-order webpages a weight of 1, thus creating an equal 
distribution. These weights are added together for a comprehensive score, and the ten
most influential philosophers are shown with a bar graph. A pie chart shows the nationalities
of the top ten most influential philosophers.

First run wikilistclean.py, then wiki.py, then wikiwebcrawl.py, then wikivisualize.py.

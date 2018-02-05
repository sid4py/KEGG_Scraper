# KEGG_Scraper
A web scraper for KEGG databse

KEGG_Scraper.py is a program that reads an input file containing the 3 letter codes that KEGG uses as organism identifiers, fires up an instance of a web browser, queries each organism against the PATHWAY database and retrieves the web pages for the search query. 

Next, the programs scrapes the Pathway information from the page and interacts with the page dynamically to navigate to subsequent pages thus scraping all available pathway information, finally closing the browser when it has run through the complete list or organims.

The 3 letter organism codes can be obtained from get_OrgCode.py program.

The Heatmap folder contains format_Heatmap_data.py, a program which takes the output of KEGG_Scraper.py as its input and reformats the data to as a table with the pathways as coloumn headers, the organisms as row headers and a 1/0 value indicating presence or absence of pathway, respectively.

The program also generates histogram data indicating the frequencies at which the pathways occur and number of pathways occuring in each individual organism.

gen_Heatmap.py generates a simple heatmap of the above table.

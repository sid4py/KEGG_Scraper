# KEGG_Scraper

**Background**

A tremendous amount of recent research has focused on the Human Mircobiome and many exciting discoveries have come forth as a result. The Human Mircobiome has been implicated in a host of human health factors, from obesity to mental health. Drugs that alter the gut microbiome to treat diseases such as C.diff are already on the market. Often the starting point of microbiome research is a list of bacterial species that comprise the microbiome, determined using deep sequencing experiments. The composition of the microbiome in terms of relative frequncies of individual bacterial species can be quite informative. However, associating each species with its metabolic pathway information can often add an additional layer of insight.

For example, the bacteria from genus Streptococcus colonize both the nasal tract as well as the skin, however when individual species composition is compared, we see a marked difference between the two samples. The answer to this difference may lie in the pathways that are different to these species.

Similarly, in the gut microbiome, no single genus/species combination might be representative of a certain effect but when the pathway information is clustered, there is a possibility that a certain pathway is over-represented as opposed to others, leading to a particular phenotypic effect.

Thus it can be quite useful to derive metabolic pathway information from the list of individual organisms.

**Context and Program Description**

I wanted to build a program that could start with the list of organisms as an input and output a list of all metabolic pathways from each individual organism. This information can be found within the excellent Kyoto Encyclopedia of Genes and Genomes (KEGG), a Japanese database which maintains highly curated, often Human verified, metabolic pathway information, among many other useful information.

1) The KEGG database has a unique 3 letter code for each organism in their repository. Thus to generate a list of these 3 letter organism-identifiers from our starting list of complete genus-species names, use the get_OrgCode.py program which takes a .txt file of list of organisms as input and outputs the list of 3 letter organism codes.

2) The main program KEGG_Scraper.py does the actual web data scraping from KEGG. It reads an input file containing the 3 letter organism codes, fires up an instance of a web browser, queries each organism against the PATHWAY database and retrieves the web pages for the search query. Next, the programs scrapes the Pathway information from the page and interacts with the page dynamically to navigate to subsequent pages thus scraping all available pathway information, finally closing the browser when it has run through the complete list or organims.

3) Finally, the 'Heatmap' folder contains format_Heatmap_data.py, a program which takes the output of KEGG_Scraper.py as its input and reformats the data as a table with the pathways as coloumn headers, the organisms as row headers and a 1/0 value indicating presence or absence of pathway, respectively. The program also generates histogram data indicating the frequencies at which the pathways occur and number of pathways occuring in each individual organism.

4) The program gen_Heatmap.py generates a simple heatmap of the above table.

**Results**

From a simple input list containing 8 *Streptococcus spp.*, we can see from the pathway histogram data, that certain pathways are pretty rare. For example: pathways 'Fatty Acid Degradation' and 'Synthesis and degradation of ketone bodies' occur only in a one out of 8 organisms. This kind of information can explain an over-representation of one species over another given specific environments like nasal cavity and skin. For example, both these pathways will be useful for a species colonizing the skin where fatty acids based nutrients can be sporadically available (sebum) versus another species colonising the nasal passage where this pathway wont be necessary owing to a vastly different local environment.  

**Remarks and Future possible changes**

This program can be adapted to scrape other kinds of information off the KEGG Database. Similarly the information scraped can be arranged and visualized differently as per the purpose.

Writing this code was a learning exercise in interacting with the web, thus the use of Beautiful Soup and Selenium.
The first program, get_OrgCode.py can be implemented as a function and the list of organisms can be directly input to KEGG_Scraper.py which will in turn import the function from get_OrgCode.py. This will reduce one step and make KEGG_Scraper more convenient.

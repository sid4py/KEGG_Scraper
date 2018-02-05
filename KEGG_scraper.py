from selenium import webdriver

#------------------------------------------------------
#Open organism code text file and store org code in list
orglist = list()
print('\nBuilding organism list\n')
with open('orgCode.txt') as FH :
    for line in FH :
        org = line[0:3]
        orglist.append(org)
#print(orglist)

#------------------------------------------------------
#Open output file
outfile = 'Org_Pathways.txt'
OUT = open(outfile, 'w')

#------------------------------------------------------
#Open browser instance
print('\nOpening web browser\n')
browser = webdriver.Firefox()

#------------------------------------------------------

#Loop through each organism in list and query in KEGG 
for i in orglist :
    
    OUT.writelines('\n'+i+'\n\n')
    
    #--------------------------------------------------
    
    #Open Search URL in KEGG
    print('\nRetreiving query result for', i, end='\n\n')
    url = "http://www.kegg.jp/kegg-bin/search_pathway_text?map=" + i + "&keyword=&mode=1&viewImage=false"
    browser.get(url)
    
    #--------------------------------------------------
    
    #Set init flag for page navigation
    initflag = 0
    
    #--------------------------------------------------
    
    count=0
    while True :
        
        count +=1
        if count == 20 :     # Arbitrary number 20, adjust according to default entries on page
            print('\nExiting due to excess page count. Please check manually\n\n')
            OUT.writelines('\n\nExiting due to excess page count. Please check manually\n')
            break            #Insurace against infinite loop
        
        #----------------------------------------------
        #Assigning first table entry as proxy for page numbers
        thispg = browser.find_element_by_xpath('/html/body/form/p[1]/table/tbody/tr[2]/td[1]').text
        
        #----------------------------------------------
        #This block only executes for the first iteration of while loop
        if initflag == 0 :
            prevpg = thispg
            thispg = 0
            initflag = 1
        #----------------------------------------------
        
        #----------------------------------------------
        #Counting number of rows in table
        row_count = len(browser.find_elements_by_xpath('/html/body/form/p[1]/table/tbody/tr'))
        row_count+=1
        #----------------------------------------------
        
        #----------------------------------------------
        #This block scrapes the data from web page
        #Clicks on the "next" button
        #Breaks from loop after scraping the last page
        if thispg == prevpg :
            break
        else :
            for j in range(2,row_count) :
                row = browser.find_element_by_xpath('/html/body/form/p[1]/table/tbody/tr['+str(j)+']/td[2]').text
                print(row)
                OUT.writelines(row + '\n')
            
            prevpg = browser.find_element_by_xpath('/html/body/form/p[1]/table/tbody/tr[2]/td[1]').text
            #print('\nGoing to next page')
            #Clicking Next
            browser.find_element_by_xpath('/html/body/form/input[12]').click()
            continue
        #----------------------------------------------
    
    print()

#------------------------------------------------------

OUT.close()
print('\n\nFinished scraping KEGG data, please check', outfile, '\n\n\nClosing web browser\n\n')
browser.close()


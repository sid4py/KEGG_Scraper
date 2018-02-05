#########################################################
# This program takes the output file of KEGG_Scraper.py #
# and reformats the data to generate a heat map. The    #
# output file is stored as a .csv with the first row    #
# being coloumn headers, i.e. all pathways, and first   #
# coloumn being the row headers, i.e. all organisms.    #
# Presence and absence of pathway in each organism is   #
# indicated as a 1 or 0 respectively.                   #
#########################################################

import re

pwyHist = dict()
orgHist = dict()
orgDict = dict()

#------------------------------------------------------
#Open output file of KEGG_Scraper.py and generate
#dictionary with pathways as key and organisms they
#occur in as values.
#Generate frequency histograms for Pathways and organisms

with open('Org_Pathways.txt') as FH :
    for line in FH :
        line = line.rstrip()
        if re.findall('Streptococcus', line) :
            kyvl = re.findall('(.*)\s-\s(Streptococcus\s.*)', line)
            
            ky = kyvl[0][0]
            ky = ky.replace(',','')
            
            vl = kyvl[0][1]
            vl = re.sub('[^0-9a-zA-Z\s-]','',vl)
            vl = ' ' + vl
            
            orgDict[ky] = orgDict.get(ky,'') + vl
            
            pwyHist[ky] = pwyHist.get(ky, 0) + 1
            
            vl = vl.lstrip()
            orgHist[vl] = orgHist.get(vl, 0) + 1
        
    
#------------------------------------------------------

#------------------------------------------------------
#Write pathway histogram in an output file

pwyList = list()
with open('Pathways_Hist.txt', 'w') as OUT1 :
    OUT1.writelines('Pathway\tFrequency\n')
    sortky = sorted(pwyHist.items())
    for k,v in sortky :
        pwyList.append(k)
        OUT1.writelines(k + '\t' + str(v) + '\n')
    
#------------------------------------------------------

#------------------------------------------------------
#Write organism histogram in an output file

orgList = list()
with open('Organism_Hist.txt', 'w') as OUT2 :
    OUT2.writelines('Organism\tNumber of Pathways\n')
    for k in orgHist :
        orgList.append(k)
        #print(k,orgHist[k])
        OUT2.writelines(k + '\t' + str(orgHist[k]) + '\n')
    
#------------------------------------------------------

#------------------------------------------------------
#Write pathways and all organisms they occur in as output file

with open('orgSpecificPathway.txt', 'w') as OUT3 :
    OUT3.writelines('Pathway\tOrganisms\n')
    for k in orgDict :
        #print(k,orgDict[k])
        OUT3.writelines(k + '\t' + orgDict[k] + '\n')
    
#------------------------------------------------------

#------------------------------------------------------
#Generate .csv output file with heat map data
#including row and coloumn headers
#If pathway is present - marked as 1, absence of
#pathway marked as zero

pwyLable = ','
with open('heatmap_Data.csv', 'w') as OUT4 :
    for i in range(len(pwyList)) :
        pwyLable = pwyLable + pwyList[i] + ','
    pwyLable = pwyLable + '\n'
    
    OUT4.writelines(pwyLable)
    
    for i in range(len(orgList)) :
        str = orgList[i] + ','
        for j in range(len(pwyList)) :
            if re.findall(orgList[i],orgDict[pwyList[j]]) :
                str = str + '1,'
            else :
                str = str + '0,'
        str = str + '\n'
        #print(str)
        OUT4.writelines(str)
    
#------------------------------------------------------


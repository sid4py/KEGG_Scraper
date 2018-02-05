import plotly
import plotly.graph_objs as go

yax=list()
zax=[]
frow=0

with open('heatmap_Data.csv') as FH :
    for line in FH :
        line = line.rstrip()
        
        if frow == 0 :
            xax = line.split(',')
            xax.pop(0)
            xax.pop()
            #print(x)
            frow=1
            continue
        
        drow = line.split(',')
        yax.append(drow.pop(0))
        drow.pop()
        for i in range(len(drow)) :
            drow[i] = int(drow[i])
        zax.append(drow)
    

trace = go.Heatmap(z=zax, x=xax, y=yax)

data = [trace]

plotly.offline.plot(data, filename='labelled-heatmap')
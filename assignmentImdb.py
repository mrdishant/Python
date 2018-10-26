import requests
import bs4 
from matplotlib import pyplot as plt


yearDict={}

def fetch(year,counting=100):
    

    res=requests.get("https://www.imdb.com/search/title?count="+str(counting)+"&genres=action&release_date="+str(year)+","+str(year)+"&title_type=feature");

    soup=bs4.BeautifulSoup(res.text,'lxml')

    moviesList=soup.findAll("div",{"class":"lister-item mode-advanced"})

    count=0
    sum=0    
    for i in moviesList:
        value=i.find("div",{"class":"inline-block ratings-imdb-rating"})
        # year=i.find("span",{"class":"lister-item-year text-muted unbold"}).text
        if value is not None:
            count=count+1
            sum=sum+float(value['data-value'])
            
            
            # print(i.find("h3",{"class":"lister-item-header"}).text)    
        # print(i.find("div",{"class":"inline-block ratings-imdb-rating"})['data-value'])
    print(year,{"sum":sum,"count":count,"total":len(moviesList)})
    return {"sum":sum,"count":count,"total":len(moviesList)}
    # print("Total is ",sum)
    # print("Average is ",sum/count)

years=[2015,2016,2017,2018]
for i in years:
    yearDict[i] = fetch(i)

print(yearDict)

averages=[]

for i in years:
    averages.append(yearDict[i]['sum']/yearDict[i]['count'])

# plt.scatter(years, averages, label="Movies", color='r')
# plt.bar(years,averages)

# cols = ['r', 'g', 'b','y']
# explode = (0.1, 0, 0,0.1)

# plt.pie(averages,
#         labels=years,
#         colors=cols,
#         startangle=180,
#         shadow=True,
#         explode=explode
#         )


plt.plot(years,averages,'c', label="Movies", linewidth=2)

plt.legend()

plt.title("Movies")
plt.xlabel("Years")
plt.ylabel("Averages")

plt.grid(True,color='g')

plt.show()        


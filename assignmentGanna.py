import requests
import bs4

# from matplotlib import pyplot as plt

artistList={}


# def ploting():
    
#     X=[]
#     for i in artistList.keys():
#         X.append(i)

#     Y=[]
#     for i in artistList.values():
#         Y.append(i)



#     print(X)
#     print(Y)

#     # plt.plot(X,Y,'g', label="Category-A", linewidth=3)

#     cols = ['r', 'g', 'b']
    

#     plt.pie(Y,
#         labels=X,
#         colors=cols,
#         startangle=180,
#         shadow=True,        
#         )

#     plt.legend()

#     plt.show()


def fetch():
    # res=requests.get("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1");
    res=requests.get("https://gaana.com/playlist/gaana-dj-punjabi-top-50-1");
    
    # res=requests.get("https://gaana.com/playlist/gaana-dj-gaana-international-top-50");

    soup=bs4.BeautifulSoup(res.text,'lxml')

    songsList=soup.findAll("ul",{"class":"s_l artworkload _cursor "})

    # print(songsList[2].find("li",{"class":"s_artist p_artist desktop"}).text)

    for i in songsList:
        # print(i.contents[3])
        artist=i.find("li",{"class":"s_artist p_artist desktop"}).text
        # print(artist)
        try:
            if(artist.__contains__(",")):
                artists=artist.split(",")
                # print(artists)
                for i in artists:
                    if i in artistList:
                        artistList[i]=artistList[i]+1
                    else:
                        artistList[i]=1    
            else:
                # print(artist)
                if artist in artistList:
                    artistList[artist]=artistList[artist]+1
                else:
                    artistList[artist]=1
                   
        except Exception as e:
            print("Error for ",artist,e)
            pass
        # print(i.find("li",{"class":"s_artist p_artist desktop"}).text)    
    max=0
    maxKey=""
    for i in artistList.keys():
        if artistList[i] > max:
            max=artistList[i]
            maxKey=i

    print(maxKey," ",max)
    # print(artistList)
    # ploting()

fetch()





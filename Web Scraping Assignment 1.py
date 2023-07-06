#!/usr/bin/env python
# coding: utf-8

# # Q.1 Write a python program to display all the header tags from wikipedia.org
# 

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[6]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[7]:


page


# In[8]:


soup = BeautifulSoup(page.content)
soup


# In[9]:


header = []
for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)
    

header


# In[ ]:





# # Q.2. Write a python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm 

# In[56]:


president_page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[57]:


president_page


# In[58]:


soup = BeautifulSoup(president_page.content, 'html.parser')
print(soup.prettify())


# In[59]:


scraped_president = soup.find_all('div',class_="presidentListing")
scraped_president


# In[71]:


president_name = []
for president in scraped_president:
    president = president.get_text().replace('\n','')
    president_name.append(president)
   


# In[72]:


president_name


# In[ ]:





# # Q.3. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# In[71]:


cricket_page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[72]:


cricket_page


# In[73]:


soup = BeautifulSoup(cricket_page.content, 'html.parser')
print(soup.prettify())


# ##3 a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[74]:


scraped_team = soup.find_all('span',class_="u-hide-phablet")


# In[75]:


scraped_team


# In[76]:


top_rank = []
for rank in scraped_team:
    rank = rank.get_text()
    top_rank.append(rank)
    
top_rank    


# In[77]:


top_rank = top_rank[0:10]
top_rank


# In[78]:


matches = []
for match in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches.append(match.text)

matches 


# In[86]:


matches = matches[0:10]
matches


# In[50]:


ratings = []
for rating in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings.append(rating.text)
    
ratings


# In[88]:


ratings = ratings[0:10]
ratings


# In[89]:


data = pd.DataFrame()
data['Teams'] = top_rank
data['Matches'] = matches
data['Ratings'] = ratings
data


# In[58]:


##b) Top 10 ODI Batsmen players along with the records of their team and rating. 


# In[97]:


cricket_page1 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[98]:


cricket_page1


# In[100]:


soup = BeautifulSoup(cricket_page1.content)
soup


# In[101]:


scraped_players = soup.find_all('td',class_="table-body__cell name")
scraped_players


# In[129]:


top_players = []
for player in scraped_players:
    player = player.get_text().replace('\n','')
    top_players.append(player)
    
top_players


# In[130]:


top_batsman = top_players[0:9]
top_batsman


# In[1]:


top_players


# In[116]:


scraped_team = soup.find_all('td',class_="table-body__cell nationality-logo")
scraped_team


# In[132]:


teams = []
for team in scraped_team:
    team = team.get_text().replace('\n','')
    teams.append(team)
    
teams


# In[131]:


teams_batsman = teams[0:9]
teams_batsman


# In[133]:


ratings_players = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings_players.append(i.text)
    
ratings_players    


# In[140]:


ratings_batsman = ratings_players[0:9]
ratings_batsman


# In[141]:


data = pd.DataFrame()
data['Batsman'] = top_batsman
data['Teams'] = teams_batsman
data['Ratings'] = ratings_batsman
data


# In[77]:


#Top 10 ODI bowlers along with the records of their team and ratings.


# In[136]:


top_bowlers = top_players[9:18]
top_bowlers


# In[138]:


teams_bowlers = teams[9:18]
teams_bowlers


# In[142]:


ratings_bowlers =  ratings_players[9:18]
ratings_bowlers


# In[143]:


data = pd.DataFrame()
data['Bowlers'] = top_bowlers
data['Teams'] = teams_bowlers
data['Ratings'] = ratings_bowlers
data


# In[ ]:





# # Q.4. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# In[78]:


# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating. 


# In[144]:


wcricket_page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[145]:


wcricket_page


# In[146]:


soup = BeautifulSoup(wcricket_page.content)
soup


# In[147]:


scraped_wteam = soup.find_all('span',class_="u-hide-phablet")
scraped_wteam


# In[148]:


wteam_ranking = []
for rank in scraped_wteam:
    rank = rank.get_text()
    wteam_ranking.append(rank)
    
wteam_ranking    
    
    


# In[149]:


len(wteam_ranking)


# In[151]:


w_matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    w_matches.append(i.text)
    
w_matches


# In[152]:


len(w_matches)


# In[85]:


rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
rating    


# In[86]:


# b)


# In[88]:


wbatsman_page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# In[89]:


wbatsman_page


# In[90]:


soup = BeautifulSoup(wbatsman_page.content)
soup


# In[92]:


scraped_wbatsman = soup.find_all('td',class_="table-body__cell name")
scraped_wbatsman


# In[94]:


w_batsman = []
for w_bat in scraped_wbatsman:
    w_bat = w_bat.get_text().replace('\n','')
    w_batsman.append(w_bat)
    
w_batsman  


# In[95]:


scraped_teams_wb = soup.find_all('span',class_="table-body__logo-text")
scraped_teams_wb


# In[96]:


wb_teams = []
for team in scraped_teams_wb:
    team = team.get_text().replace('\n','')
    wb_teams.append(team)
    
wb_teams


# In[98]:


ratings_wplayers = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings_wplayers.append(i.text)
    
ratings_wplayers 


# In[ ]:





# # Q.5. Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world

# In[99]:


news_page = requests.get('https://www.cnbc.com/world/?region=world')


# In[100]:


news_page


# In[153]:


soup = BeautifulSoup(news_page.content)
soup


# In[103]:


#for headlines of news
headlines = []
for h in soup.find_all('div',class_="LatestNews-headlineWrapper"):
    headlines.append(h.text)
    
headlines    


# In[154]:


scraped_link = soup.find_all('a',href)
scraped_link


# In[ ]:





# # Q.6. Write a python program to scrape the details of most downloaded articles from AI in last 90 days.  https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles  

# In[159]:


AI_page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[160]:


AI_page


# In[161]:


soup = BeautifulSoup(AI_page.content)
soup


# In[162]:


scraped_heading = soup.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR")
scraped_heading


# In[163]:


heading = []
for h in scraped_heading:
    h = h.get_text()
    heading.append(h)
    
heading 


# In[164]:


scraped_author = soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT")
scraped_author


# In[165]:


authors = []
for a in scraped_author:
    a = a.get_text()
    authors.append(a)
    
authors    


# In[166]:


dates = []
for d in soup.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    dates.append(d.text)
    
dates    


# In[167]:


data = pd.DataFrame()
data['Headings'] = heading
data['Author'] = authors
data['Dates'] = dates
data


# # Q.7.  Write a python program to scrape mentioned details from dineout.co.in :

# In[2]:


dine_page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[3]:


dine_page


# In[4]:


soup = BeautifulSoup(dine_page.content)
soup


# In[5]:


#Restaurant name

restaurant = []
for r in soup.find_all('div',class_="restnt-info cursor"):
    restaurant.append(r.text)
    
restaurant    


# In[ ]:


#for cuisine


# In[ ]:





# In[6]:


#for location
location = []
for l in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(l.text)
    
location    


# In[7]:


#for rating
rating = []
for r in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(r.text)
    
rating    


# In[8]:


# for image URL
image = []
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
    
image    


# In[15]:


data = pd.DataFrame()
data['Restaurant'] = restaurant
data['Location'] = location
data['Rating'] = rating
data['Image URL'] = image
data.head()


# 
# 

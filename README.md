
<img src="images/dataanalysis.jpg"/>
# Midterm Exam - Spring 2017

>This Assignment consist of analysis on following dataset
- Enron Company Dataset.
- New York Times Dataset
   - Article Archieve
   - Popular User
   - User Comments
   
## Enron Data Set <img src="images/enron.png" align="right" />


- [Enron Scandal Summary](http://www.investopedia.com/updates/enron-scandal-summary/) - Link to Investopedia article to get a brief summary about the what the scandal was.
- The enron data-set is available at [CMU Enron data 1.82 GB tgz file](https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz) .

## Analysis

*Because it is so large, it makes analysis complicated. The question always is: Where do we even start?*

** Dependencies**
- Word cloud
- OS
- Counter
- Email Parser
- NLTK
- NetworkX


**1. Analysis on Kenneth Lay directory, one time CEO and director, who went to prison. I am doing it this way to speed up our code, as otherwise it may take a long time to run.**

**Fetching Data**

*Orginally I was going to parse the code by hand Until I found a good library to open emails in Python*
```
from email.parser import Parser
```

We now create an email parser instance,lopped through each email received, sent,body etc.I have written a function to extract the data from the emails

```
def email_analyse(inputfile, to_email_list, from_email_list, email_body)
```

**Data Wrangling**
```
some of the fields are empty (due to data corruption, old Mime formats that can’t be parsed)So I remove all the newline characters (\n), all the tabs (\t) and empty spaces. This is to ensure the code is parsed correctly.
```

**Result**

<img src ="images/kenlay.PNG" />

```
Most of the emails were sent with Lay’s own email address. It seemed he had two email addreses: *kenneth.lay@enron.com and klay@enron.com*

The most emails he received were from Rosalee Fleming.

I have used NLTK package to analyse most frequent words in file 'email_body.txt' which consist of emails of kennith lay and created *word cloud* of it

Some words like communication and energy are expected, as that’s what Enron did.

But I kept seeing million, and interestingly, bankruptcy.

The word California was mentioned 3734 times. The company had some (bad, I think) history there.

Finally, the word meeting was mentioned 1700 times. K Lay sure was a busy man.


```
<img src ="images/wordcloud.PNG" />

**2.Social Network Analysis **

```
Many time real world problems involve dependencies between record in data.For example sociologist are eager to understand how people influence behaviour of their peer.Problem depending on dependencies can be modeled as graph and scientist have modeled methods to answer such question called network analysis.

Network Analysis can be done using graph.NetworkX is Native Graph structure for python which consist of Nodes and Edges.

Graph,G=(V,E)

V=Vertices/Nodes

E=Edges

Nodes - Can be any Hashable object

Edges - Tuples of nodes with optional edge datawhich is stored in a dictionary
```

**Building Graph**

```
import networkx as nx 
G = nx.Graph() 
```

**Result**

```
Since important people are usually those with power, and power has the potential to corrupt, people with power are more likely to commit crimes. Therefore a good first pass at finding "people of interest" in the Enron scandal would be to look at the nodes ordered by one or more centrality measures. So we analyse kennith lay directory and we find using :

import networkx as nx
G = nx.Graph()
sender = "kenneth.lay@enron.com"
for recipient in from_email_list:
    G.add_edge(sender, recipient)
    nx.write_gexf(G, 'enron.gexf')
    
After visualization we find that most important person of interest are top level employees including kennith lay and
```

<img src ="images/analysis2.PNG" />

<img src ="images/analysis2graph.PNG" />

**3 Checking who sends most emails and who receives most email in ernon dataset. Printing the top 20 users Email id and plotting a graph of it**

**Data Cleaning**
```
some of the fields are empty (due to data corruption, old Mime formats that can’t be parsed)So I remove all the newline characters (\n), all the tabs (\t) and empty spaces. This is to ensure the code is parsed correctly.
```

**Result**
I am running a loop on whole directory to see important insights .It will find the most common to and from  emails in the whole company.

<img src ="images/analysis3.PNG" />

```nce
As we can see the top person is Richard Shapiro. He was the Vice President. A lot of his emails are about handing dollars to politicians, and getting favourable laws passed. The fact that he received the most emails shows he was in touch with everything that was happening.The highest From field, which is emails received from, is Kay Mann, who was the head of legal for Enron. The fact that she sent so many emails is ironical, seeing as how Enron was breaking every law in the book.
```
<img src ="images/analysis3image.PNG" />

<img src ="images/analysis3image1.PNG" />




## New York Times Data Set <img src="images/nytimes.png" align="right" />

- Link to NYT developer docs : [NYT API Documentation](http://developer.nytimes.com/)

- This Analysis is related to Articles , Popular User and  User Comments
- API key is save in Environment Variable which is stored in config file under config/settings.cfg


## Analysis

** Dependencies**

- Request
- OS
- Counter
- Email Parser
- NLTK
- Json
- Plotly
- Matplotlib
- configparser
- Datetime
- CSV
- Re
- Beautiful Soup
- Glob

**1.Sentiment Analysis on New york times article Archieve API**

```
My overall goal was to determine if the sentiment of words in news coverage can be detected. I extracted articles for a month of january which consist of 5206 articles and attempted to perform sentiment analysis.

```

** Collecting Data **

*I have used **Input** method to store data where user can give the path of working directory.The reason for using this way to avoid conflict in the way we give path in Mac OS by single "/" and in windows "//"*
 

```
dirname=input("Enter the current working directory")
os.chdir(dirname)# Set current working directory
os.getcwd() # Get current working directory

```

*I have Created a configuaration file which stores all the configuartion details as **Api Key ,dates, password etc** . We need to use parser to fetch configuration file

```
from configparser import ConfigParser
config = ConfigParser()

path='config/settings.cfg'
config_file = os.path.abspath(path)
config.read(config_file)
```


** Storing Data **

*The New York Times API will not return the full text of articles. However, it will return metadata such as subject terms, abstract, and date, as well as the URL, which I will subsequently use to scrape the full text of articles *

**Content Extraction Algorithms for Python**

There are several packages in Python for extracting content from Web pages. A brief overview of these packages follows:

*Goose*

Goose was originally an article extractor written in Java.
The aim of the software is to take any news article or article-type web page and not only extract what is the main body of the article but also all meta data and most probable image candidate.

*BeautifulSoup*

I also examined BeautifulSoup, although I found it less easy to use than Goose. In retrospect, BeautifulSoup is good to use if you really need to target specific elements on a web page in my case i am targeting the web url element

```
- I used Beautiful soup to extract all the web url and store them in seperate text files data can be found under raw.zip. 
- I looped through that text file in order to find useful information related to articles.
- Read that trxt file and stored in one list to do analysis on data.

```
** Data Wrangling**

```
Remove all the stopwords as they are not the part of analysis besides remove all the newline characters (\n), all the tabs (\t) special charaters and empty spaces
```

**Result**

```
- I created a list of Postive and Negative words and looped to store the result based on dictionary of words created in postive_counter and negative counter list.

- Each time word is located in dictionary counter is incresed which in the end give the analysis about weather article for month of january has postive sentiments or negative sentiments

- We also calucated sentiment score for each article which is:

Sentiment Score=(positive/negative count)/word_count

- All the score are stored in file " Sentiment_article.csv"

- I was trying to create a plot but being a large frequency it is not able to create a plot otf it

Positive counter=134519

Negative counter=79964

We find that articles have more positive words than negative words i:e around 62 % percent of words are postive and approx 38 % percent are negative words used in article
```



**2 Zipf's Law on New york times article Archieve API** 

*Zipf's Law is a statement based on observation rather than theory. It is often true of a collection of instances of classes, e.g., occurrences of words in a document. It says that the frequency of occurrence of an instance of a class is roughly inversely proportional to the rank of that class in the frequency list.

More exactly, suppose a word occurs f times and that in the list of word frequencies it has a certain rank, r. Then if Zipf's Law holds we have (for all words) f = a/rb where a and b are constants and b is close to 1.*



** Collecting Data **

*I have used **Input** method to store data where user can give the path of working directory.The reason for using this way to avoid conflict in the way we give path in Mac OS by single "/" and in windows "//"*
 

```
dirname=input("Enter the current working directory")
os.chdir(dirname)# Set current working directory
os.getcwd() # Get current working directory

```

*I have Created a configuaration file which stores all the configuartion details as **Api Key ,dates, password etc** . We need to use parser to fetch configuration file

```
from configparser import ConfigParser
config = ConfigParser()

path='config/settings.cfg'
config_file = os.path.abspath(path)
config.read(config_file)
```


** Storing Data **

*The New York Times API will not return the full text of articles. However, it will return metadata such as subject terms, abstract, and date, as well as the URL, which I will subsequently use to scrape the full text of articles *


```
- I used Beautiful soup to extract all the web url and store them in seperate text files data can be found under raw.zip. 
- I looped through that text file in order to find useful information related to articles.
- Read that trxt file and stored in one list to do analysis on data.

```
** Data Wrangling**

```
Remove all the newline characters (\n), all the tabs (\t) special charaters and empty spaces
```

**Result**
<img src ="images/Zipf.PNG" />
```
I did analysis by collecting data in a file for a month of january and created a graph using matplotlib and plotly. I find that real word dataset follow zipf's law
I also plotted a graph with most frequent words used
```
<img src ="images/nyanalysis3.PNG" />


**3 New york times Most Popular API**

*We're going to retrieve the most shared articles from the NYT within the past 30 days and determine which author has contributed the most articles.The maximum limit allowed is 30 days we get almost 1406 shared articles*

** Collecting Data **

*I have used **Input** method to store data where user can give the path of working directory.The reason for using this way to avoid conflict in the way we give path in Mac OS by single "/" and in windows "//"*
 

```
dirname=input("Enter the current working directory")
os.chdir(dirname)# Set current working directory
os.getcwd() # Get current working directory

```

*I have Created a configuaration file which stores all the configuartion details as **Api Key ,dates, password etc** . We need to use parser to fetch configuration file

```
from configparser import ConfigParser
config = ConfigParser()

path='config/settings.cfg'
config_file = os.path.abspath(path)
config.read(config_file)
```


** Storing Data **

```
I hit up the most-shared endpoint and store the response as an object.The fields  I am interested  are 'total_shares', 'byline', and, in the interest of fairness, 'published_date',for each article, I'll extract the desired fields and add them to lists.
```
**Result**

<img src ="images/nyanalysis2.PNG" />

```
I Stored the result in csv file and it give insights on publisher publisher date and how many shares it has.
```


** Most Recommended user New york times Community API**


*We're going to retrieve the most user comments in  articles from the NYTa month of january and  determine which user has commented more beside who has got more recommendations.We have list of 750 users and their recommendations*

** Collecting Data **

*I have used **Input** method to store data where user can give the path of working directory.The reason for using this way to avoid conflict in the way we give path in Mac OS by single "/" and in windows "//"*
 

```
dirname=input("Enter the current working directory")
os.chdir(dirname)# Set current working directory
os.getcwd() # Get current working directory

```

*I have Created a configuaration file which stores all the configuartion details as **Api Key ,dates, password etc** . We need to use parser to fetch configuration file

```
from configparser import ConfigParser
config = ConfigParser()

path='config/settings.cfg'
config_file = os.path.abspath(path)
config.read(config_file)
```

** Storing Data**
```
Data is stored in Json file with proper date format it is located under directory "wordAnalysis/user" we can fetch all the data using loop to store the list of users and recommendation in a list
```

**Result**

```

I created a csv file to store Users and recommendations they have got,we found some beautiful analysis on this like:

- Most of the users are in rage of 1-1000 recommendations.
_ Only 1 user has more than 2000 recommendations
_ It give insights about who is most frequent user of site and which is most frequent visitor
- I have created a graph using plotly to visualize the result
```

<img src ="images/nyanalysis4.PNG" />



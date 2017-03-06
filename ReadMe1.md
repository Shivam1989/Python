
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

<img src ="images/kennlay.PNG" />

```
Most of the emails were sent with Lay’s own email address. It seemed he had two email addreses: *kenneth.lay@enron.com and klay@enron.com*

The most emails he received were from Rosalee Fleming.

I have used NLTK package to analyse most frequent words in file 'email_body.txt' which consist of emails of kennith lay and created *word cloud* of it

Some words like communication and energy are expected, as that’s what Enron did.

But I kept seeing million, and interestingly, bankruptcy.

The word California was mentioned 3734 times. The company had some (bad, I think) history there.

Finally, the word meeting was mentioned 1700 times. K Lay sure was a busy man.

<img src ="images/wordcloud.PNG" />
```







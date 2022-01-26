#### web scraping ####
# Import all the packages needed
# Install packages "beautifulsoup4" in terminal
import urllib.request as req
import requests
import bs4
from random import randint
import re
from time import sleep
import pandas as pd
import numpy as np


# Request for the LA lost&found website.
# Set a random zip code 90036 and 120 miles under the "Miles from location" section.
url = "https://losangeles.craigslist.org/d/lost-found/search/laf?postal=90036&search_distance=250"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})

# Create empty list to save titles and contents of each post respectively
pagestitleList = []
pagescontentList = []

# Loop 1 for the titles in the five pages
for i in range(0, 5):
    # Sleep for 10 to 15 seconds after scraping each page
    sleep(randint(10, 15))
    url = "https://losangeles.craigslist.org/d/lost-found/search/laf?postal=90036&" + "s=" + str(
        i * 120) + "&search_distance=120"

    print(url)  # Print out all the urls of each page to make sure we are scraping the correct pages
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("h3", class_="result-heading")
    alltitle = [t.text.replace('\n', '') for t in titles]
    pagestitleList.extend(alltitle)  # Extend all the titles

    # Loop 2 for the contents
    for title in titles:
        link = title.a.get('href')
        url2 = link

        data2 = requests.get(url2)
        html = bs4.BeautifulSoup(data2.text, 'html.parser')
        des = html.find("section", id="postingbody")
        alldes = des.text.replace('\n\nQR Code Link to This Post\n\n\n', '')

        pagescontentList.append(alldes)  # Append the contents

len(pagestitleList) #Check the length of titles list
len(pagescontentList)  #Check the length of contents list

pagestitleList
pagescontentList

# Change into dataframe form
dict = {"Title":pagestitleList, "Content": pagescontentList}
df = pd.DataFrame(dict)

# Save to csv file
scrapy_LA = df.to_csv("Craigslist_LAF_LA.csv")
print(df.head(5))  #Check the first 5 rows in the file

#----------------------------------------------

# Request for the WL lost&found website.
# Set a random zip code 47906 and 250 miles under the "Miles from location" section.
url = "https://tippecanoe.craigslist.org/d/lost-found/search/laf?postal=47906&search_distance=250"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})

# Create empty list to save titles and contents of each post respectively
pagestitleList = []
pagescontentList = []

# Loop 1 for the titles in the five pages
for i in range(0, 5):
    # Sleep for 10 to 15 seconds after scraping each page
    sleep(randint(10, 15))
    url = "https://tippecanoe.craigslist.org/d/lost-found/search/laf?postal=47906&" + "s=" + str(
        i * 120) + "&search_distance=250"

    print(url)  # Print out all the urls of each page to make sure we are scraping the correct pages
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("h3", class_="result-heading")
    alltitle = [t.text.replace('\n', '') for t in titles]
    pagestitleList.extend(alltitle)  # Extend all the titles

    # Loop 2 for the contents
    for title in titles:
        link = title.a.get('href')
        url2 = link

        data2 = requests.get(url2)
        html = bs4.BeautifulSoup(data2.text, 'html.parser')
        des = html.find("section", id="postingbody")
        alldes = des.text.replace('\n\nQR Code Link to This Post\n\n\n', '')

        pagescontentList.append(alldes)  # Append the contents

len(pagestitleList) #Check the length of titles list
len(pagescontentList)  #Check the length of contents list

pagestitleList
pagescontentList

# Change into dataframe form
dict = {"Title":pagestitleList, "Content": pagescontentList}
df = pd.DataFrame(dict)

# Save to csv file
scrapy_LA = df.to_csv("Craigslist_LAF_WL.csv")
print(df.head(5))  #Check the first 5 rows in the file

# ----------------------------------------------
#### Model  ####

# Data Processs
import nltk
import pandas as pd
import gensim
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.corpora import Dictionary
import os
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import savefig

# Read file
# Working directory may be different
os.chdir("D:/2021 Purdue MSBAIM/Course/MGMT 59000 Analyzing Unstructured Data/Group Project")
rev=pd.read_csv('lawl.csv', header=None, encoding = "UTF-8")

df_temp = rev.iloc[:,  0:2]
t1=df_temp.values.tolist()

# Data partition: 7/3
training_docs = t1[:697]
testing_docs = t1[697:997]

# Separate X and Label
training_x = [i[1] for i in training_docs]
training_x.remove(training_x[194])
testing_x = [i[1] for i in testing_docs]
training_c = [i[0] for i in training_docs]
training_c.remove(training_c[194])
testing_c = [i[0] for i in testing_docs]

# Transform those reviews into a TFIDF matrix
t2=[]
for i in training_x:
    token_d1 = nltk.word_tokenize(i)
    token_d4 = [token for token in token_d1 if not token in stopwords.words('english') if token.isalpha()]
    lemmatizer = nltk.stem.WordNetLemmatizer()
    token_d2 = [lemmatizer.lemmatize(token).lower() for token in token_d4 if token.isalpha()]
    t2.append(token_d2)

t3=[]
for i in testing_x:
    token_d1 = nltk.word_tokenize(i)
    token_d4 = [token for token in token_d1 if not token in stopwords.words('english') if token.isalpha()]
    lemmatizer = nltk.stem.WordNetLemmatizer()
    token_d2 = [lemmatizer.lemmatize(token).lower() for token in token_d4 if token.isalpha()]
    t3.append(token_d2)

from sklearn.feature_extraction.text import TfidfVectorizer

# Trick: create a dummy tokenizer
def tk(doc):
    return doc
vec = TfidfVectorizer(analyzer='word',tokenizer=tk, preprocessor=tk,token_pattern=None, min_df=5, ngram_range=(1,2), stop_words='english')
vec.fit(t2)
training_x = vec.transform(t2)
testing_x = vec.transform(t3)

### Naïve Bayes model
from sklearn.naive_bayes import MultinomialNB
NBmodel = MultinomialNB()
# training
NBmodel.fit(training_x, training_c)
y_pred_NB = NBmodel.predict(testing_x)
# evaluation1: model accuracy
from sklearn.metrics import accuracy_score
acc_NB = accuracy_score(testing_c, y_pred_NB)
print("Naive Bayes model Accuracy:: {:.2f}%".format(acc_NB*100))
# evaluation2: confusion matrix
from sklearn.metrics import confusion_matrix
cm_NB = confusion_matrix(testing_c, y_pred_NB)
print('Confusion matrix\n\n', cm_NB)
print('\nTrue Lost(TL) = ', cm_NB[1,1])
print('\nTrue Found(TF) = ', cm_NB[0,0])
print('\nFalse Lost(FL) = ', cm_NB[1,0])
print('\nFalse Found(FF) = ', cm_NB[0,1])
# visualize confusion matrix with seaborn heatmap
cm_NB_matrix = pd.DataFrame(data=cm_NB, columns=['Actual Found:0', 'Actual Lost:1'],
                                 index=['Predict Found:0', 'Predict Lost:1'])
plt.clf()
sns.heatmap(cm_NB_matrix, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix_Naïve Bayes", fontsize = 12)
plt.savefig('Confusion Matrix_Naïve Bayes.png', dpi=400)

### Decision Tree model
from sklearn.tree import DecisionTreeClassifier
DTmodel = DecisionTreeClassifier()
# training
DTmodel.fit(training_x, training_c)
y_pred_DT = DTmodel.predict(testing_x)
# evaluation1: model accuracy
acc_DT = accuracy_score(testing_c, y_pred_DT)
print("Decision Tree Model Accuracy: {:.2f}%".format(acc_DT*100))
# evaluation2: confusion matrix
from sklearn.metrics import confusion_matrix
cm_DT = confusion_matrix(testing_c, y_pred_DT)
print('Confusion matrix\n\n', cm_DT)
print('\nTrue Lost(TL) = ', cm_DT[1,1])
print('\nTrue Found(TF) = ', cm_DT[0,0])
print('\nFalse Lost(FL) = ', cm_DT[1,0])
print('\nFalse Found(FF) = ', cm_DT[0,1])
# visualize confusion matrix with seaborn heatmap
cm_DT_matrix = pd.DataFrame(data=cm_DT, columns=['Actual Found:0', 'Actual Lost:1'],
                                 index=['Predict Found:0', 'Predict Lost:1'])
plt.clf()
sns.heatmap(cm_DT_matrix, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix_Decision Tree", fontsize = 12)
plt.savefig('Confusion Matrix_Decision Tree.png', dpi=400)

### Random Forest model
from sklearn.ensemble import RandomForestClassifier
RFmodel = RandomForestClassifier(n_estimators=50, max_depth=3, bootstrap=True, random_state=0)
# training
RFmodel.fit(training_x, training_c)
y_pred_RF = RFmodel.predict(testing_x)
# evaluation1: model accuracy
acc_RF = accuracy_score(testing_c, y_pred_RF)
print("Random Forest Model Accuracy: {:.2f}%".format(acc_RF*100))
# evaluation2: confusion matrix
from sklearn.metrics import confusion_matrix
cm_RF = confusion_matrix(testing_c, y_pred_RF)
print('Confusion matrix\n\n', cm_RF)
print('\nTrue Lost(TL) = ', cm_RF[1,1])
print('\nTrue Found(TF) = ', cm_RF[0,0])
print('\nFalse Lost(FL) = ', cm_RF[1,0])
print('\nFalse Found(FF) = ', cm_RF[0,1])
# visualize confusion matrix with seaborn heatmap
cm_RF_matrix = pd.DataFrame(data=cm_RF, columns=['Actual Found:0', 'Actual Lost:1'],
                                 index=['Predict Found:0', 'Predict Lost:1'])
plt.clf()
sns.heatmap(cm_RF_matrix, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix_Random Forest", fontsize = 12)
plt.savefig('Confusion Matrix_Random Forest', dpi=400)

### SVM model
from sklearn.svm import LinearSVC
SVMmodel = LinearSVC()
# training
SVMmodel.fit(training_x, training_c)
y_pred_SVM = SVMmodel.predict(testing_x)
# evaluation1: model accuracy
acc_SVM = accuracy_score(testing_c, y_pred_SVM)
print("SVM model Accuracy: {:.2f}%".format(acc_SVM*100))
# evaluation2: confusion matrix
from sklearn.metrics import confusion_matrix
cm_SVM = confusion_matrix(testing_c, y_pred_SVM)
print('Confusion matrix\n\n', cm_SVM)
print('\nTrue Lost(TL) = ', cm_SVM[1,1])
print('\nTrue Found(TF) = ', cm_SVM[0,0])
print('\nFalse Lost(FL) = ', cm_SVM[1,0])
print('\nFalse Found(FF) = ', cm_SVM[0,1])
# visualize confusion matrix with seaborn heatmap
cm_SVM_matrix = pd.DataFrame(data=cm_SVM, columns=['Actual Found:0', 'Actual Lost:1'],
                                 index=['Predict Found:0', 'Predict Lost:1'])
plt.clf()
sns.heatmap(cm_SVM_matrix, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix_SVM", fontsize = 12)
plt.savefig('Confusion Matrix_SVM', dpi=400)

### validation
# We selected the SVM model
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(training_x, training_c,test_size=0.3,
                                                   train_size=0.7,random_state=1)
x_train, x_val, y_train, y_val = train_test_split(x_train,y_train,test_size=0.25,
                                                 train_size=0.75, random_state=1)

tr2 =SVMmodel.score(x_train, y_train)
te2=SVMmodel.score(x_test, y_test)
vali2 = SVMmodel.score(x_val, y_val)
print("\nPerformance of SVM model \ntrain set: " ,tr2, "\ntest set: ", te2, "\nvalidation set: " , vali2 )

# ----------------------------------------------
#### Topic LDA ####
# Read file
rev=pd.read_csv('lawl.csv', header=None, encoding = "UTF-8")
file=rev[1].tolist()
file.remove(file[194])

t1=[]
for i in file:
    token_d1 = nltk.word_tokenize(i)
    token_d4 = [token for token in token_d1 if not token in stopwords.words('english') if token.isalpha()]
    lemmatizer = nltk.stem.WordNetLemmatizer()
    token_d2 = [lemmatizer.lemmatize(token).lower() for token in token_d4 if token.isalpha()]
    t1.append(token_d2)

for i in range(995):
    for j in t1[i]:
        if j == "found" or j =="missing" or j == "lost" or j == "contact" or j == "please" or j == "info" or j =="show" or j == "home":
            t1[i].remove(j)

t2=[]
lemmatizer = nltk.stem.WordNetLemmatizer()
for i in t1:
    temp1=[]
    for word in i:
        temp1.append((lemmatizer.lemmatize(word).lower()))
        t2.append(" ".join(temp1))

from sklearn.feature_extraction.text import CountVectorizer
vectorizer1 = CountVectorizer(ngram_range=(1, 2), min_df=5)
vectorizer1.fit(t2)
v2 = vectorizer1.transform(t2)

terms = vectorizer1.get_feature_names()

from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=3).fit(v2)


for topic_idx, topic in enumerate(lda.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms[i] for i in topic.argsort()[:-5-1:-1]]))

# ----------------------------------------------
#### Image Recognization ####

##Image VGG
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from PIL import Image #after pillow is installed
from pylab import *
import tensorflow
import os

os.chdir("D:/2021 Purdue MSBAIM/Course/MGMT 59000 Analyzing Unstructured Data/Group Project")
model = VGG16()
# prepare image
im = array(Image.open('puppy.jpg').resize((224,224)))
image = im.reshape((1, im.shape[0], im.shape[1], im.shape[2]))
image = preprocess_input(image)
#predict
yhat = model.predict(image)
label = decode_predictions(yhat)
print(label)

# # Image VGG
# from keras.applications.vgg16 import preprocess_input
# from keras.applications.vgg16 import decode_predictions
# from keras.applications.vgg16 import VGG16
# from PIL import Image #after pillow is installed
# from pylab import *
# model = VGG16()

# prepare image
im = array(Image.open('cat.jpg').resize((224,224)))
image = im.reshape((1, im.shape[0], im.shape[1], im.shape[2]))
image = preprocess_input(image)
# predict
yhat = model.predict(image)
label = decode_predictions(yhat)
print(label)
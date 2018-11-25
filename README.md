### Group 21

# ADM_HOMEWORK 3

 In this homework we analyze the text of Airbnb property listings by creating  separate document as tsv file for each record from the dataset, we also built two separate search engines to analyse the text given in the query and fetch the properties that match our query 
 
 All the aspects of questions asked in various steps of this Homework are covered in the attached files.

## Getting Started

Download the required dataset from [here](https://www.kaggle.com/PromptCloudHQ/airbnb-property-data-from-texas) and load them into a dataframe for cleaning the data, Convert the each row of CSV file as a separate document, Extract the text in the documents and save it as dictionary to create an inverted index, and them build your search engine calculating the tfidf based on cosine similarity, For an interactive search results make use of folium and geopy to show it on map.


### Prerequisites

Importing libraries Numpy, pandas , Json ,Natural Language Toolkit for Tokenization, stemming and stop words , Scipy for calculating cosine similarity, Folium and Geopy for maps and calculating the Latitude,Longitude and distance information on maps.


### Installing

Anaconda Navigator
Python with Jupyter Notebook as IDE


### Main Scripts

Homework_3.ipynb          (It has all the code that is required to do this text analysis and populate search results ) 
termiddic.json            (Our vocabulary of words ) 
inv_indx.json             (Inverted Index for first Search Engine  )
new_invindx.json          (Inverted Index for Second Search Engine )
Humble_SearchResults.html (Map showing search results for a place e.g Humble )


## Authors

* **Atefe Moradan** 
  **Giuseppe Stefanelli**
  **Vikranth Ale**
  
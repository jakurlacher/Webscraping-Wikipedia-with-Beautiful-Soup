from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re
import requests
#import nltk
#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#from nltk import sent_tokenize, word_tokenize
#from nltk.stem.snowball import SnowballStemmer
#from nltk import ne_chunk, pos_tag, word_tokenize
#from nltk.corpus import wordnet as wn
import pickle

#list_url = 'https://en.wikipedia.org/wiki/Timeline_of_Western_philosophers'


main_url = 'https://en.wikipedia.org/wiki/Western_philosophy'

#Scrape links from wiki site, assign weights of 8 for references
#on 'western philosophy' wikipedia page, 1 for references on
#pages linked on subfields of 'western philosophy' page.
def soup(link):
    html_main = urllib.request.urlopen(link).read()
    soup_main = BeautifulSoup(html_main, 'html.parser')
    return soup_main
soup_main = soup(main_url)

first_tags = []
second_tags = []
def get_links(soup, tags):
    main_articles = soup.find_all('div',role='note')
    for articles in main_articles:
        tag = articles.find('a')

        try:
            tag = tag.get('href')
        except:
            continue

        tag = 'https://en.wikipedia.org' + tag
        tags.append(tag)


get_links(soup_main, first_tags)
#print(len(first_tags)) == 23
for tag in first_tags:
    tag = soup(tag)
    get_links(tag, second_tags)
#print(len(second_tags)) == 184


#Extract all text
def extract(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    #clean list file of philosophers from wikilistclean.py
    with open("clean_list.txt","r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    counts = {}
    for p in lines:
        if p in text:
            t = text.split()
            for x in t:
                if x == p:
                    if p in counts:
                        counts[p] += 1
                    else:
                        counts[p] = 1
    #Only discludes irrelevant philosophers, i.e. "John of Damascus" and "John the Scot"
    if 'John' in counts:
        del counts['John']
    #Removes "William of Ockman" and "Sir William Hamilton"
    if 'Wiliam' in counts:
        del counts['William']
    #Removes "Alexander of Hales", "Samuel Alexander"
    if 'Alexander' in counts:
        del counts['Alexander']

    return counts
main_dicts = extract(main_url)

print(main_dicts)
with open('main_counts.pickle', 'wb') as handle:
    pickle.dump(main_dicts, handle, protocol=pickle.HIGHEST_PROTOCOL)

    
string = '''
#first_dicts = []
#for tag in first_tags:
#    tag_dict = extract(tag)
#    first_dicts.append(tag_dict)
#print(len(first_dicts))

#second_dicts = []
for tag in second_tags:
    tag_dict = extract(tag)
    second_dicts.append(tag_dict)
print(len(second_dicts))


with open('first_counts.pickle','wb') as handle:
    pickle.dump(first_dicts,handle,protocol=pickle.HIGHEST_PROTOCOL)

with open('second_counts.pickle','wb') as handle:
    pickle.dump(second_dicts,handle,protocol=pickle.HIGHEST_PROTOCOL)
'''

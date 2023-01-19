
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

with open('final_dict.pickle', 'rb') as handle:
    final_dict = pickle.load(handle)

lst = list()
#data visualization intermediary step
def sort_dictionary_by_values(d):
  sorted_d = sorted(d.items(), key=lambda x: x[1])
  for elements in sorted_d:
      lst.append(elements)

sort_dictionary_by_values(final_dict)
final_dict = dict(lst)

values = list(final_dict.values())[-10:]
keys = list(final_dict.keys())[-10:]
# Create a new dictionary with only the last 10 entries
final_dict = dict(zip(keys, values))


#Bar graph
frequencies = list(final_dict.values())
names = list(final_dict.keys())
plt.figure(figsize = (10,5))
sns.barplot(x=names, y=frequencies)
plt.title('Most Influential Philosophers')
plt.ylabel('Weighted score', fontsize = 12)
plt.xlabel('Philosopher name', fontsize = 12)
plt.show()






#Pie chart of nationalities


nationalities = ['Greek', 'British', 'German', 'Greek', 'American', 'German',
'German', 'Greek', 'Greek', 'American']

national_dict = {}
for n in nationalities:
    if n in national_dict:
        national_dict[n] += 1
    else:
        national_dict[n] = 1
labels = []
sizes = []

for x, y in national_dict.items():
    labels.append(x)
    sizes.append(y)
plt.pie(sizes,labels=labels)
plt.axis('equal')
plt.show()

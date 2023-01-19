import pickle
#LOADING DICTIONARIES
with open('main_counts.pickle', 'rb') as handle:
    main_counts = pickle.load(handle)

main_counts_dict = main_counts
with open('first_counts.pickle','rb') as handle:
    first_counts = pickle.load(handle)

first_counts_dict = {}
for dict in first_counts:
    for key in dict:
        if key in first_counts_dict:
            first_counts_dict[key] = first_counts_dict[key] + dict[key]
        else:
            first_counts_dict[key] =  1


with open('second_counts.pickle','rb')as handle:
        second_counts = pickle.load(handle)

second_counts_dict = {}

for dict in second_counts:
    for key in dict:
        if key in second_counts_dict:
            second_counts_dict[key] = second_counts_dict[key] + dict[key]
        else:
            second_counts_dict[key] =  1

#ASSIGNING WEIGHTS
main_counts_weight = 184
first_counts_weight = 8
second_counts_weight = 1


final_dict = {}

def update(dictionary, weight):
    return dictionary.update((key, value * weight) for key, value in dictionary.items())

update(main_counts_dict,main_counts_weight)
print(main_counts_dict)
update(first_counts_dict,first_counts_weight)
print(first_counts_dict)
update(second_counts_dict,second_counts_weight)
print(second_counts_dict)

def final(dictionary):
    for name in dictionary:
        if name in final_dict:
            final_dict[name] = final_dict[name] + dictionary[name]
        else:
            final_dict[name] = dictionary[name]
final(main_counts_dict)
final(first_counts_dict)
final(second_counts_dict)

#There are no influential philosophers with last names of
#'More' or 'William' -- these are just common words, i.e. 'William James'
del final_dict['More']
del final_dict['William']


with open('final_dict.pickle','wb') as handle:
    pickle.dump(final_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(final_dict)

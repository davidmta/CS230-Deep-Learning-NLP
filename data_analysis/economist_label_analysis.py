
import pickle
import settings
import matplotlib.pyplot as plt

dir = settings.ROOT_DIR+'\\processed_data\\'
file = 'Econ_corpus_raw.p'

[data, labels] = pickle.load(open(dir+file, 'rb'));

## FILTER OUT SMALL LENGTH DATA SAMPLES
less_50_count = 0;
length_histogram = list();
for i in range(len(labels)):
    length_histogram.append(len(data[i]));
    if(len(data[i]) < 200):
        less_50_count+=1;
print(less_50_count);
plt.hist(length_histogram, 50);
plt.show()

unique_labels = set(labels)
print(unique_labels)

## label histogram:
label_dict = dict();
for label in labels:
    if(label not in label_dict.keys()):
        label_dict[label] = 0;
    label_dict[label]+=1;

print(label_dict);
counter = 0;
for i in label_dict.keys():
    if(label_dict[i] < 50):
        counter+=1;
    else:
        print(str(i)+', '+str(label_dict[i]));
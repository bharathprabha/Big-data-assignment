import csv
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

with open("./data/survey_results_public.csv") as f:
    csv_reader = csv.DictReader(f)

    language_counter = Counter()

    for line in csv_reader:
        languages = line['PlatformWorkedWith'].split(';')

        language_counter.update(languages)


graph_language = []
graph_language_count = []
print(list(language_counter.most_common(10)))

for language, value in language_counter.most_common(10):
    graph_language.append(language)
    graph_language_count.append(value)

y_pos = np.arange(len(graph_language))
plt.bar(y_pos, graph_language_count, color=(0.8, 0.5, 0.3, 0.8))

plt.title('Programming language survey 2020')
plt.xlabel('Programming language')
plt.ylabel('percentage')

plt.ylim(0, 60000)
plt.xticks(y_pos, graph_language)

plt.show()

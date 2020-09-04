import csv
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

with open("./data/survey_results_public.csv") as f:
    csv_reader = csv.DictReader(f)

    webframework_counter = Counter()
    language_counter = Counter()

    for line in csv_reader:
        webframeworks = line['WebframeWorkedWith'].split(';')

        webframework_counter.update(webframeworks)


graph_webframework = []
graph_webframework_count = []

for webframework, value in webframework_counter.most_common(10):
    graph_webframework.append(webframework)
    graph_webframework_count.append(value)

graph_webframework.remove(graph_webframework[0])
graph_webframework_count.remove(graph_webframework_count[0])

y_pos = np.arange(len(graph_webframework))
plt.bar(y_pos, graph_webframework_count, color=(0.8, 0.5, 0.3, 0.8))

plt.title('Web Frameworks survey 2020')
plt.xlabel('Web Frameworks')
plt.ylabel('percentage')

plt.ylim(0, 30000)
plt.xticks(y_pos, graph_webframework)

plt.show()

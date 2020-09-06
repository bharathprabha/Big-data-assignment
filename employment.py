import csv
import numpy as np
import matplotlib.pyplot as plt


from collections import Counter

with open("./data/survey_results_public.csv") as f:
    csv_reader = csv.DictReader(f)

    employment_counter = Counter()

    for line in csv_reader:
        genters = line['Employment'].split(';')
        employment_counter.update(genters)

print(list(employment_counter.most_common()))

graph_employment = []
graph_employment_count = []

for type, value in employment_counter.most_common(10):
    graph_employment.append(type)
    graph_employment_count.append(value)


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(graph_employment_count, autopct=lambda pct: func(pct, graph_employment_count),
                                  textprops=dict(color="w"))

ax.legend(wedges, graph_employment,
          title="Employment",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Employment survey of 2020 (developer)")

plt.show()

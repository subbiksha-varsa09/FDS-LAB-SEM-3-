import matplotlib.pyplot as hscmark
import numpy as np

Names = ['SHREE', 'DEV', 'KEERTHI', 'PRIYA', 'SHAN', 'KUMARAN']
Percentage_hsc = [96, 91, 94, 75, 45, 81]

xaxis = np.arange(len(Names))

hscmark.bar(Names, Percentage_hsc)

hscmark.xticks(xaxis, Names, rotation=45)

hscmark.xlabel("Names of Pupil")
hscmark.ylabel("Percentage")

hscmark.title(
    "Comparison of HSC Percentage",
    fontsize=20,
    color="green"
)
hscmark.show()
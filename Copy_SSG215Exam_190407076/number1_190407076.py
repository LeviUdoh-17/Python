from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from numpy import diag_indices, greater

#The strings are defined and are also converted to lists and then into a set
string1 = set("The quick brown fox jumped over the lazy dog".split())
string2 = set("a brown dog and a lazy fox are similar in nature".split())
string3 = set("Dami is so lazy that she could not make an effort to get brown sugar".split())
print(string1, string2, string3)

#The intersection of the strings are found using the intersection method
newSet = string3.intersection(string1.intersection(string2))
newSet1 = string1.intersection(string3)
newSet2 = string2.intersection(string3)
print(newSet, newSet1, newSet2)
pass

#used venn 3 plt.show() to plot the venn diagram
venn3([string1, string2, string3], set_labels=("String1", "String2", "String3"), set_colors=("Red", "Yellow", "Green"), alpha=1.0)
venn3_circles([string1, string2, string3])
plt.show()

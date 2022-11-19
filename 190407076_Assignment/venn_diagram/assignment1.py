from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
from numpy import diag_indices, greater

OutstandingNigerianFootballers = {'Victor Osimhen', 'Ahmed Musa', 'Obafemi Martins', 'Kelechi Iheanacho', 'Joseph Yobo', 'Nwankwo Kanu', 'Vincent Eyeama', 'Rashidi Yekini', 'John Obi Mikel', 'Jay Jay Okocha'}
OutstandingAFCON_Footballers = {'Essam El-Hadary', 'Abedi Ayew', 'Yaya Toure', 'Nwankwo Kanu', 'Roger Milla', 'Sadio Mane', 'Mohammws Salah', 'Didier Drogba', 'Samuel Eto\'o', 'George Weah'}

newSet = OutstandingNigerianFootballers.intersection(OutstandingAFCON_Footballers)
print(newSet)
pass

venn2([OutstandingNigerianFootballers, OutstandingAFCON_Footballers], set_labels=('Outstanding Nigerian Players', 'Outstanding AFCON Players'), set_colors=('Red', 'Pink'), alpha=1.0)

venn2_circles([OutstandingNigerianFootballers, OutstandingAFCON_Footballers])
plt.show()
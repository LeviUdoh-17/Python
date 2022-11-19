from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from numpy import diag_indices, greater 

EuropeanCountries = {'Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czechia','Denmark','Estonia','Finland','France','Georgia','Germany','Greece','Hungary','Iceland','Ireland','Italy','Kazakhstan','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','North Macedonia','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Turkey','Ukraine','United Kingdom (UK)','Vatican City (Holy See)'}

WesternEuropeanCountries = {'Austria','Belgium','France','Germany','Liechtenstein','Luxembourg','Monaco','Netherlands','Switzerland'}

EuropeanUnionCountries = {'Belgium','Bulgaria','Croatia','Czechia','Denmark','Germany','Estonia','Greece','Spain','France','Ireland','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania','Slovenia','Slovakia','Finland','Sweden'}

newSet1 = EuropeanCountries.intersection(EuropeanUnionCountries)
print(newSet1)
pass

newSet2 = EuropeanCountries.intersection(WesternEuropeanCountries)
print(newSet2)
pass

newSet3 = EuropeanCountries.intersection(EuropeanUnionCountries.intersection(WesternEuropeanCountries))
print(newSet3)
pass

venn3([EuropeanCountries,EuropeanUnionCountries,WesternEuropeanCountries],
    set_labels=('THE EUROPEAN COUNTRIES', 'THE EU COUNTRIES', 'THE WESTERN EUROPEAN COUNTRIES'),
    set_colors=('Red','Blue','Yellow'),alpha=1.0)

venn3_circles([EuropeanCountries,EuropeanUnionCountries,WesternEuropeanCountries])
plt.show()
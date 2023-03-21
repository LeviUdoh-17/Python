from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
nigerianGreatFootballers={'Nwankwo Kanu', 'Austin Okocha', 'Sunday Oliseh', 'Rashidi Yekini','Segun Odegbami', 'Stephen Keshi', 'Emmanuel Amuneke', 
'Finidi George', 'Christian Chukwu', 'Muda lawal', 'Peter Rufai', 'Daniel Amokachi', 'Taribo West', 'Uche Okechukwu', 'Teslim “Thunder”Balogun',
'Victor Ikpeba', 'Samson Siasia', 'Adokiye Amiesimaka', 'Vincent Enyeama', 'Celestine Babayaro', 'Thomson Usiyan', 'Taiye ‘Taiwo', 'Henry Nwosu'
, 'Emmanuel Okala', 'Felix Owolabi', 'Haruna Ilerika', 'Joseph Yobo', 'Aloysius Atuegbu','Richard Owubokiri','Elkanah Onyeali','Patrick Ekeji',
'Best Ogedengbe','Bright Omokaro','Peter Anieke','Yisa Shofoluwe','Ben Iroha','Julius Aghahowa','Osaze Odemwingie','Albert Onyeawuna','Augustine Eguavoen',
'Yisa Shofoluwe',  'Obafemi Martins', 'Yakubu Aiyegbeni', 'Tijani Babangida', 'Tony Igwe', 'Obi Mikel', 'Garba Okoye', 'Friday Okoh', 'Etim Esin', 'Dan Anyiam'}
afconPlayers={'Lakhdar Bellouni','Mahmoud El Khatib','Roger Milla',
'Ibrahim Sunday','Alex Iwobi','Abedi Pele','Obi Mikel','Emmanuel Ammunike','Riyad Mahrez','George Weah','Rashidi Yekini','Samuel Etiho','Yaya Toure','Ezzaki Badou','Kanu Nwankwo','Pierre-Emerick Aubameyang','Victor Ikpebe',
'Mohamed Salah','Victor Moses','Kalusha Bwalya','Rabah Madjer','Thomas Nkono'}
NewSet = nigerianGreatFootballers.intersection(afconPlayers)
print(NewSet)
pass
venn2([nigerianGreatFootballers, afconPlayers],
    set_labels=('Great Negerian Footballers', 'Footballers that won an African Cup of Nations Cup'),
    set_colors=('blue','yellow'),alpha=0.8)
venn2_circles([nigerianGreatFootballers,afconPlayers])
plt.show()
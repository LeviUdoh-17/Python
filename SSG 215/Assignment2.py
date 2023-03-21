from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
BestCars={'porse', 'Kia', 'Tesla', 'Mazda', 'Toyota', 'Mazda', 'Honda', 'Jaguar', 'Mistbishi', 'Volvo', 'Lexus', 'Ferrari', 'Mercedes-Benz'}
RacingCars={'Ferrari', 'McLauren', 'Renault', 'Mercedes-Benz', 'Honda'}
NewSet = BestCars.intersection(RacingCars)
print(NewSet)
pass
venn2([BestCars, RacingCars],
    set_labels=('Best Cars', 'Racing Cars'),
    set_colors=('Red', 'Blue'), alpha=0.7
)
venn2_circles([BestCars, RacingCars])
plt.show()


def human_years_cat_years_dog_years(human_years):
    # Your code here
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears = 15
    elif human_years == 2:
        catYears = (15+9)
    else:
        catYears = (15+9)+((human_years-2)*4)


    if human_years == 1:
        dogYears = 15
    elif human_years == 2:
        dogYears = (15+9)
    else:
        dogYears = (15+9)+((human_years-2)*5)
    return [human_years, catYears, dogYears]
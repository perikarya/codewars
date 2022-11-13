def bmi(weight, height):
    tot = weight / height ** 2
    if tot <= 18.5:
        return "Underweight"
    elif tot <= 25.0:
        return "Normal"
    elif tot <= 30.0:
        return "Overweight"
    else:
        return "Obese"

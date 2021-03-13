"""data = {'dictA': {'key_1': 'value_1'},
        'dictB': {'key_2': 'value_2'},
        'dictC': 1}

MaClassDeDonne = type("MaClassDeDonne", (object,), data)


class MaClassDeDonne:
    dictA  = {'key_1': 'value_1'}
    dictB  = {'key_2': 'value_2'}





s = JsonParser(data)

s.dictC = 2

print(data)

"""


def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

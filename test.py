from countryinfo import all_countries

countries = all_countries()
country_currencies = {}

# ISO codes of countries you want to exclude if they are territories
excluded = {
    "Åland Islands", "American Samoa", "Anguilla",
    "Aruba", "Bermuda", "British Indian Ocean Territory",
    "Cayman Islands", "Christmas Island", "Cocos (Keeling) Islands",
    "Cook Islands", "Falkland Islands", "Faroe Islands",
    "French Guiana", "French Polynesia", "Gibraltar",
    "Greenland", "Guadeloupe", "Guam", "Guernsey",
    "Hong Kong", "Isle of Man", "Jersey", "Macao",
    "Martinique", "Mayotte", "Montserrat", "New Caledonia",
    "Niue", "Norfolk Island", "Northern Mariana Islands",
    "Pitcairn Islands", "Puerto Rico", "Réunion",
    "Saint Helena", "Saint Pierre and Miquelon",
    "Sint Maarten", "Tokelau", "Turks and Caicos Islands",
    "U.S. Virgin Islands", "Wallis and Futuna",
    "Western Sahara", "Austria", "Belgium", "Bulgaria", "Croatia",
    "Cyprus", "Estonia", "Finland", "France", "Germany", "Greece",
    "Ireland", "Itlay", "Lativa", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain", "Andorra",
    "Monaco", "Vatican City State", "Holy See (Vatican City State)", "Kosovo",
    "Montenegro"
}

for country in countries:
    name = country.name()
    currencies = country.currencies()

    if currencies and name not in excluded:
        country_currencies[name] = currencies[0]

for country, currency in sorted(country_currencies.items()):
    print(f"{country}: {currency}")
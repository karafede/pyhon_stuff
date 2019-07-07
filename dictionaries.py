
monthsConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

monthsConversion2 = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December",
}

print(monthsConversion["Nov"])
print(monthsConversion.get("Dec"))

print(monthsConversion.get("Luv", "not a valid key"))

print(monthsConversion2.get(3, "not a valid key"))
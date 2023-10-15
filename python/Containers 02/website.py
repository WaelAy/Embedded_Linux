import webbrowser
import favourtiteWebsites
import re

print("0 - Add site")

for i in favourtiteWebsites.favouriteSites:
    print(i,'-',favourtiteWebsites.favouriteSites[i])
x = int(input("Enter the Number of site: "))


def add_site(url):
    re.match("https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",url)
    favourtiteWebsites.favouriteSites[len(favourtiteWebsites.favouriteSites)+1] = url


if x == 0:
    url = str(input("Enter the URL of the site: "))
    add_site(url)

elif x < len(favourtiteWebsites.favouriteSites):
    webbrowser.open_new_tab(favourtiteWebsites.favouriteSites[x])
else:
    ValueError
    print("Please Enter a Valid Number")



for i in favourtiteWebsites.favouriteSites:
    print(i,'-',favourtiteWebsites.favouriteSites[i])


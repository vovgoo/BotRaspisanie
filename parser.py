import requests as req
import fake_useragent
from bs4 import BeautifulSoup as BS

user = fake_useragent.UserAgent().random
header = {'user-agent' : user}
def result(x):
    link_document = x
    response_doc = req.get(link_document, headers = header).text
    soup_doc = BS(response_doc, "lxml")
    lessons = soup_doc.find_all("tr")
    one_soup = BS(str(lessons[1]), "lxml")
    less_one = one_soup.find_all("td")

    result = ""
    for i in range(60, 74):
        soup_lessons = BS(str(lessons[i]), "lxml")
        less = soup_lessons.find_all("td")
        if(i == 60):
            result += less_one[0].get_text()[0] + less_one[0].get_text()[1:].lower() + " " + less_one[1].get_text()[0].upper() + less_one[1].get_text()[1:] + "\n" + "\n"
        if len(str(less[4].get_text())) > 0:
            result += str(less[0].get_text()) + " Время: " + str(less[1].get_text()) + " | " + str(less[4].get_text()) + " | Кабинет: " + str(less[5].get_text()) + "\n"
    return result

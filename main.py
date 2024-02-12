from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course_card = soup.find_all('div',class_="card")
    for course in course_card:
        title = course.find('h5').text
        description = course.find('p').text
        price = course.find('a').text.split()[-1]
        print(description)
        print(price)
        print(title)
    print(soup)
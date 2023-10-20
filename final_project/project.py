# from selenium import webdriver
# import time
from bs4 import BeautifulSoup


# driver = webdriver.Chrome()
# url='https://www.youtube.com/watch?v=i1QST3prI7Y&list=RD00ff2UcGLu0&index=2'
# driver.get(url)
# time.sleep(5)
# soup = driver.page_source
# time.sleep(5)
# driver.quit()
# html = BeautifulSoup(soup, "html.parser")
# pllist = html.find_all("div", class_="playlist-items style-scope ytd-playlist-panel-renderer", id="items")
with open("code.html") as cd:
    pllist = []
    for line in cd:
        pllist.append(line.lstrip())

# print(pllist)
lines = []
for line in pllist:
    if line.startswith("<span"):
        lines.append(line)
print(len(lines))
tracks = []
for line in lines[4:]:
    if "title" in line:
        print(line.strip())
        tracks.append(line)

print(len(tracks))
# soup = BeautifulSoup(pllist, "html.parser")
# track = soup.find_all("span")
# print(track)


# response = requests.get("https://www.youtube.com/watch?v=00ff2UcGLu0&list=RD00ff2UcGLu0&start_radio=1&rv=Fy8oAWrzTDE")
# # print(response)
# # soup = BeautifulSoup(response.content, "html.parser")
# # pllist = soup.find("div", id="items", class_="playlist-items style-scope ytd-playlist-panel-renderer")
# # with open("code.html", "a") as code:
# #     code.write(soup.prettify())







# sleep(10)

# driver.quit()












# from bs4 import BeautifulSoup



# def main():
#     response = requests.get("https://www.youtube.com/watch?v=00ff2UcGLu0&list=RD00ff2UcGLu0&start_radio=1&rv=Fy8oAWrzTDE")
#     print(response)
#     soup = BeautifulSoup(response.content, "html.parser")
#     pllist = soup.find("div", id="items", class_="playlist-items style-scope ytd-playlist-panel-renderer")
#     with open("code.html", "a") as code:
#         code.write(soup.prettify())


# def function_1():
#     ...


# def function_2():
#     ...


# def function_n():
#     ...


# if __name__ == "__main__":
#     main()
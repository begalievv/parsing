from bs4 import BeautifulSoup
import requests
import csv



def get_html(url):
    r = requests.get(url)
    return r.text



def write_csv(data):
    with open("lalafo.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow((data["title"],
                          data["price"],
                          data["link"]))


def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")

    ads = soup.find("div", id="main-listing-block").find_all("article", class_="listing-item")

    for ad in ads:
        try:
            title = ad.find("div", class_="listing-item-main").find("a", class_="item listing-item-title").text
            title.strip()
        except:
            title = ""

        try:
            price = price = ad.find("div", class_="listing-item-main").find("p", class_="listing-item-title").text
            price.strip()
        except:
            price = ""

        try:
            link = ad.find("img", class_="listing-item-photo link-image").get("src")
        except:
            link = ""

        data = {
            "title": title,
            "price": price,
            "link": link,
        }
        write_csv(data)

def main():
    url = "https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnyetelefony"
    page_part = "?page="
    

    for i in range(1, 250):
        url_gen = url + page_part + str(i)
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == "__main__":
    main()

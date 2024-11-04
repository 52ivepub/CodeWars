# url = "icann.org"
# url = "http://google.com"
url = "www.xakep.ru"
# ), "google")
# ), "xakep"
# ), "google")


def domain_name(url):
    url_short = url.replace("http://", "").replace("www.", "").replace("https://", "")
    return url_short.split(".")[0]




print(domain_name(url))




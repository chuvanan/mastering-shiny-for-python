
import os
import urllib.request

os.getcwd()
os.makedirs("the-book/04-Case_study/neiss", exist_ok=True)

def download(name):
    url = "https://raw.github.com/hadley/mastering-shiny/main/neiss/"
    urllib.request.urlretrieve(url + name, os.path.join("the-book/04-Case_study/neiss", name))

download("injuries.tsv.gz")
download("population.tsv")
download("products.tsv")

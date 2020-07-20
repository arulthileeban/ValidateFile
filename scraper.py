import urllib.request
import bs4,re
#Should return hash value and hash type
def scrapAll(url):
    fp = urllib.request.urlopen(url)
    data_ib = fp.read()
    data = data_ib.decode("utf8")
    soup=bs4.BeautifulSoup(data,'html.parser')
    h1="MD5"
    h2="SHA1"
    results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(h1)), recursive=True)
    results2 = soup.body.find_all(string=re.compile('.*{0}.*'.format(h2)), recursive=True)
    for content in results1:
        words = content.split()
        for index, word in enumerate(words):
            if h1 == word and index < len(words):
                return (h1, words[index + 1])
    for content in results2:
        words = content.split()
        for index, word in enumerate(words):
            if h1 == word and index < len(words):
                return (h1, words[index + 1])

if __name__ == '__main__':
   print(scrapAll("https://sourceforge.net/projects/keepass/files/KeePass%202.x/2.45/"))
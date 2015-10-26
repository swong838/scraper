import time, re, requests as r, urllib as u
from random import randint as rand
from bs4 import BeautifulSoup as bs

file_pattern = r'([\w\-\.]+)$'
ip_prefix = '66.90'
base_href ="http://downloads.khinsider.com/game-soundtracks/album/flower"
def main():
	for url in fetch_outer_track_pages():
		download_link = get_track_download_link(url)
		if download_link:
			delay = rand(4,9)
			fetch_track(download_link)
			time.sleep(delay)

def fetch_outer_track_pages():
	main_index = r.get(base_href)
	soup = bs(main_index.text, 'html.parser')
	return set([a['href'] for a in soup.findAll('a') if '.mp3' in a['href']])

def get_track_download_link(url):
	page = r.get(url)
	soup = bs(page.text, 'html.parser')
	dls = [a['href'] for a in soup.findAll('a') if ip_prefix in a['href']]
	if(dls[0]):
		return dls[0]
	else:
		return None

def fetch_track(url):
	track = u.URLopener()
	track_name = re.search(file_pattern, url).group(1)
	track.retrieve(url.strip(), track_name)

if __name__ == "__main__":
    main()

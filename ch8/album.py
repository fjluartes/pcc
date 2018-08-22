#!/usr/bin/env python
# album.py: Exercises 8-7, 8-8
# 22 Aug 2018 | fjgl
def make_album(artist, title):
    """Return a dictionary of album titles and its artists."""
    album = {'artist': artist, 'title': title}
    return album
# 8-7. Album
#album1 = make_album('nirvana', 'nevermind')
#print(album1)
#album2 = make_album('the beatles', 'abbey road')
#print(album2)
#album3 = make_album('red hot chili peppers', 'by the way')
#print(album3)

# 8-8. User Albums
while True:
    print("\nEnter an album title and artist:")
    print("(enter 'q' at any time to quit)")
    album_artist = input("Artist: ")
    if album_artist == 'q':
        break
    album_title = input("Album Title: ")
    if album_title == 'q':
        break

    album = make_album(album_artist, album_title)
    print(album)

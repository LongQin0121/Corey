import requests

#https://www.youtube.com/watch?v=tb8gHvYlCFs

#r = requests.get('https://xkcd.com/353/')


r = requests.get('https://imgs.xkcd.com/comics/python.png')
#print(r)

#print(dir(r))
#print(help(r))

#print(r.text)

#print(r.content)
# with open('comic.png','wb') as f:
#     f.write(r.content)

print(r.status_code)
print(r.ok)
print(r.headers)
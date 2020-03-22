#this function takes a youtube link and extracts a video id from it

link = input()

def get_id(l):
    split = link.split('/')
    watch = split[-1].split('=')
    id = watch[-1]
    return id

print(get_id(link))
import re

def findTags(tagLine):
    pattern = re.compile(r'''<\/?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)\/?>''')
    match = pattern.finditer(str(tagLine))
    for mat in match :
        print("Tags : ",mat)
    

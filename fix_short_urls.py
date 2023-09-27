import requests

SHORT_URL = 'lnkd.in'
LINE_CONTAINING_URL_IN_HTML = 'data-tracking-control-name="external_url_click"'
listForNewFile = []

with open('bloglinks.txt', 'r', encoding="utf-8") as f:
    sourcefile = f.readlines()
    for line in sourcefile:
        newlineDescription = line.split(" - ")
        if SHORT_URL in line:
            # Exp: Microsoft - https://lnkd.in/g-UEZMxC
            url = newlineDescription[1].strip()
            httpRequest = requests.get(url, timeout=10)
            for r_line in httpRequest.text.split('\n'):
                if LINE_CONTAINING_URL_IN_HTML in r_line:
                    expandedURL = r_line.split('href="')[-1].rstrip('/>"')
                    listForNewFile.append(newlineDescription[0] + " - " + expandedURL + '\n')
        else:
            listForNewFile.append(line)

with open('expandedBlogLinks.txt', 'w', encoding="utf-8") as newfile:
    newfile.writelines(listForNewFile)

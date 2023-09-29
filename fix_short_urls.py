"""
Reads file named bloglinks.txt containing a blog description/name followed
by a dash (-) then a URL either long or short.  

If the URL is a short URL created by LinkedIn ( lnkd.in ) the long URL
will be fetched.  A new file named expandedBlogLinks.txt will be created
that contains both the description/name of the blog and the expanded URL.

If the URL is not lnkd.in it will be copied as is to the new file.
"""

import argparse
import requests
SHORT_URL = 'lnkd.in'
LINE_CONTAINING_URL_IN_HTML = 'data-tracking-control-name="external_url_click"'
list_for_new_file = []

def main():
    """create expanded links"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        help='filename of inputfile that contains shortlinks',
                        required='True')
    parser.add_argument('-o', '--output',
                        help='filename for output',
                        required='True')
    args = parser.parse_args()

    with open( args.input, 'r', encoding="utf-8") as f:
        sourcefile = f.readlines()
        for line in sourcefile:
            description_url_split = line.split(" - ")
            if SHORT_URL in line:
                # Exp: Microsoft - https://lnkd.in/g-UEZMxC
                url = description_url_split[1].strip()
                http_request = requests.get(url, timeout=10)
                for request_line in http_request.text.split('\n'):
                    if LINE_CONTAINING_URL_IN_HTML in request_line:
                        expanded_url = request_line.split('href="')[-1].rstrip('/>"')
                        list_for_new_file.append(description_url_split[0] + " - "
                                                + expanded_url + '\n')
            else:
                # before appending remove trailing "/" from URL if it exists
                list_for_new_file.append(line.rstrip('/\n') + "\n")

    with open(args.output, 'w', encoding="utf-8") as newfile:
        newfile.writelines(list_for_new_file)

if __name__ == '__main__':
    main()

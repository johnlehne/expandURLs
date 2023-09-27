Reads file named bloglinks.txt containing a blog description/name followed
by a dash (-) then a URL either long or short.  

If the URL is a short URL created by LinkedIn ( lnkd.in ) the long URL
will be fetched.  A new file named expandedBlogLinks.txt will be created
that contains both the description/name of the blog and the expanded URL.

If the URL is not lnkd.in it will be copied as is to the new file.

Example bloglinks.txt:
Engineering at Meta - https://lnkd.in/e8tiSkEv
Microsoft - https://lnkd.in/g-UEZMxC
Google Research - https://ai.googleblog.com/
Google Cloud Blog - https://lnkd.in/enNviCF8
AWS Architecture Blog - https://lnkd.in/eEchKJif
...

Example output (expandedBlogLinks.txt):
Engineering at Meta - https://engineering.fb.com
Microsoft - https://grabajobs.co/certification
Google Research - https://ai.googleblog.com
Google Cloud Blog - https://cloud.google.com/blog
AWS Architecture Blog - https://aws.amazon.com/blogs/architecture
...

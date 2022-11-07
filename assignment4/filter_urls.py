import re
from urllib.parse import urljoin
from requesting_urls import get_html 

## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)
    a_pat = re.compile(r"<a[^>]+>", flags=re.IGNORECASE) 
    href_pat = re.compile(r'href="(#{0}[^#"]+)', flags=re.IGNORECASE)

    href_set = set()

    # 1. find all the anchor tags, then
    for a_tag in a_pat.findall(html): 
    # 2. find the urls href attributes
        match = href_pat.search(a_tag)

        if match:
            if re.match('^//', match.group(1)):
                url = 'https:'+match.group(1)

            elif re.match('^/', match.group(1)):
                url = base_url+match.group(1)
            
            elif re.match('^https', match.group(1)):
                url = match.group(1)

            href_set.add(url)
        else:
            continue
    
    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        # open a txt.file 
        f = open(output,"w+")
        # write data into the file
        for url in href_set:
            f.write(url + '\n')
        # close the file instance       
        f.close()

    return href_set

def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    # get all url list from the html text
    urls = find_urls(html)    
    # define article pattern
    article_pat = '.*wikipedia.org/wiki.*$' 
    article_set = set()
    for url in urls:
        protocol, _, rest = url.partition("://") ## devide into three parts : before "://", "://", after "://"

        # if ':' in rest (after ://), discard the url:
        if re.match('.*[:].*$', rest):
            continue

        # if not match article pattern and rest, discard the url
        if not re.match(article_pat,rest): 
            continue 

        # add the filtered url into the article set
        article_set.add(url)

    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        # open a txt.file 
        f = open(output,"w+")
        # write data into the file
        for url in article_set:
            f.write(url + '\n')
        # close the file instance       
        f.close()

    return article_set

## Regex example
def find_img_src(html: str, output=None) -> set:
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
        
    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        # open a txt.file 
        f = open(output,"w+")
        # write data into the file
        for url in src_set:
            f.write(url + '\n')
        # close the file instance       
        f.close()

    return src_set

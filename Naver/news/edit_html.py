import re

def strip_html_tags (html):

    text = str(html)
 
    # apply rules in given order!
    rules = [
    { r'>\s+' : u'>'},                  # remove spaces after a tag opens or closes
    { r'\s+' : u' '},                   # replace consecutive spaces
    { r'\s*<br\s*/?>\s*' : u'\n'},      # newline after a <br>
    { r'</(div)\s*>\s*' : u'\n'},       # newline after </p> and </div> and <h1/>...
    { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # newline after </p> and </div> and <h1/>...
    { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # remove <head> to </head>
    { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # show links instead of texts
    { r'[ \t]*<[^<]*?/?>' : u'' },            # remove remaining tags
    { r'^\s+' : u'' }                   # remove spaces at the beginning
    ]
 
    for rule in rules:
        for (k,v) in rule.items():
            regex = re.compile(k)
            text  = regex.sub(v,text)
 
    # replace special strings
    special = {
        '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
        '&lt;'   : '<', '&gt;'  : '>'
    }
 
    for (k,v) in special.items():
        text = text.replace(k, v)
 
    return text

def strip_script_tag(html):
    script_tag = re.compile('<script(.|\n)*</script>')
    html = script_tag.sub('',str(html))
    return html;

def strip_other_world(html):
    script_tag = re.compile('( 본문 내용| \(// \)*TV플레이어)')
    html = script_tag.sub('',str(html))
    return html

def strip_email_and_link(html):
    script_mail = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    script_link = re.compile(r"'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'")
    html = script_mail.sub('',str(html))
    html = script_link.sub('',str(html))
    return html


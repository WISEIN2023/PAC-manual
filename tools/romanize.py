# -*- coding: utf-8 -*-
import re
CHO=['g','kk','n','d','tt','r','m','b','pp','s','ss','','j','jj','ch','k','t','p','h']
JUNG=['a','ae','ya','yae','eo','e','yeo','ye','o','wa','wae','oe','yo','u','wo','we','wi','yu','eu','ui','i']
JONG=['','k','k','k','n','n','n','t','l','k','m','p','l','l','p','l','m','p','p','t','t','ng','t','t','k','t','p','t']
def rom(s):
    out=[]
    for ch in s:
        o=ord(ch)
        if 0xAC00<=o<=0xD7A3:
            c=o-0xAC00
            out.append(CHO[c//588]+JUNG[(c%588)//28]+JONG[c%28])
        else:
            out.append(ch)
    return ''.join(out)
def slugify(s, maxlen=48):
    s=rom(s)
    s=s.lower()
    s=re.sub(r'[^\w\s\-]',' ',s)
    s=re.sub(r'[\s_]+','-',s.strip())
    s=re.sub(r'-{2,}','-',s).strip('-')
    if len(s)>maxlen:
        s=s[:maxlen].rsplit('-',1)[0]
    return s or 'section'

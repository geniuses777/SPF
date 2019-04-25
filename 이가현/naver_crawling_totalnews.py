import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
lis = hdline_article_list.findAll("li")

for li in lis:
    a_tag = li.find("a")
    print(a_tag.text)

total_p = bs_obj.find("div", {"id":"section_politics"})
politics = total_p.find("ul", {"class":"mlist2 no_bg"})
lis_p = politics.findAll("li")

for li_p in lis_p:
    a_tag_fp = li_p.find("a")
    a_tag_sp = a_tag_fp.find("strong")
    print(a_tag_sp.text)

total_e = bs_obj.find("div", {"id":"section_economy"})
economy = total_e.find("ul", {"class":"mlist2 no_bg"})
lis_e = economy.findAll("li")

for li_e in lis_e:
    a_tag_fe = li_e.find("a")
    a_tag_se = a_tag_fe.find("strong")
    print(a_tag_se.text)

total_s = bs_obj.find("div", {"id":"section_society"})
society = total_s.find("ul", {"class":"mlist2 no_bg"})
lis_s = society.findAll("li")

for li_s in lis_s:
    a_tag_fs = li_s.find("a")
    a_tag_ss = a_tag_fs.find("strong")
    print(a_tag_ss.text)

total_l = bs_obj.find("div", {"id":"section_life"})
life = total_l.find("ul", {"class":"mlist2 no_bg"})
lis_l = life.findAll("li")

for li_l in lis_l:
    a_tag_fl = li_l.find("a")
    a_tag_sl = a_tag_fl.find("strong")
    print(a_tag_sl.text)

total_w = bs_obj.find("div", {"id":"section_world"})
world = total_w.find("ul", {"class":"mlist2 no_bg"})
lis_w = world.findAll("li")

for li_w in lis_w:
    a_tag_fw = li_w.find("a")
    a_tag_sw = a_tag_fw.find("strong")
    print(a_tag_sw.text)

total_i = bs_obj.find("div", {"id":"section_it"})
it = total_i.find("ul", {"class":"mlist2 no_bg"})
lis_i = it.findAll("li")

for li_i in lis_i:
    a_tag_fi = li_i.find("a")
    a_tag_si = a_tag_fi.find("strong")
    print(a_tag_si.text)
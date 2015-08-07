__author__ = 'wxbks'
import os
import xml.etree.ElementTree as ET

def modifyArticleNameinCorpus(indir):
    for fn in os.listdir(indir):
            if not fn.endswith('.xml'): continue
            fullname = os.path.join(indir, fn)

            if os.path.isfile(fullname):
                tree = ET.parse(fullname)
                root = tree.getroot()
                # print root.tag
                page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')
                # print page.tag
                title = page.find('{http://www.mediawiki.org/xml/export-0.7/}title')
                # target = os.path.join(indir,title.text+'.xml')
                t = title.text
                if '/' in t:
                    f = t.replace('/',':')
                    target = os.path.join(indir, f+".xml")
                else:

                    target = os.path.join(indir,t+'.xml')
                print 'Renaming %s to %s' % (fullname, target)
                os.rename(fullname,target)



indir = "/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-corpus_bak/npov-test"
modifyArticleNameinCorpus(indir)
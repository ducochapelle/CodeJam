#TODO: dates as dates, so I can properly compare them
#      numbers as numbers
import csv
import sqlite3

ExcelFiles = ["project"
             ,"fbfield"
             ,"discovery"
             ,"requirement"
             ,"awardedcontract"
             ,"fixedplatform"
             ,"floatingplatform"
             ,"pipeline"
             ,"mooringbuoy"
             ,"subsea"
             ,"tree"]

def UpdateExcels():
    import urllib, urllib2, cookielib
    LoginUrl = r"https://login.ods-petrodata.com/index.php?site=fieldsbase"
    Login_ID = r"DROOK@OFFSHOREINDEPENDENTS.COM"
    Password = r"Offshoreindependents345"
    CookieJar = cookielib.CookieJar()
    Opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
        urllib2.HTTPSHandler(debuglevel=0),
        urllib2.HTTPCookieProcessor(CookieJar)
    )
    Opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]
    login_data = urllib.urlencode({
            'login' : Login_ID,
            'password' : Password,
        })
    Opener.open(LoginUrl, login_data)
    # still returns login page.
    ExcelFiles = ["project"
                 ,"fbfield"
                 ,"discovery"
                 ,"requirement"
                 ,"awardedcontract"
                 ,"fixedplatform"
                 ,"floatingplatform"
                 ,"pipeline"
                 ,"mooringbuoy"
                 ,"subsea"
                 ,"tree"]
    PetrodataUrl = r"http://fieldsbase.ods-petrodata.com/index.php?mod={0}&op=downloadTable&prefix=&skin=fbase"
    print PetrodataUrl.format(ExcelFiles[0])

    
    ExcelFile = urllib2.urlopen(PetrodataUrl.format(ExcelFiles[0]))
    Output = open(ExcelFiles[0]+".xls",'wb')
    Output.write(ExcelFile.read())
    Output.close()
    # doesn't work because i get the login page back.

def CleanSqlProperties(l0):
    l1 = map(lambda x: x.replace(" ","_"),l0)
    l2 = map(lambda x: x.replace("(","["),l1)
    l3 = map(lambda x: x.replace(")","]"),l2)
    l = map(unicode,l3)
    return l
def CleanSqlRecords(arg):
    return map(lambda x: unicode(x, errors='ignore'),arg)
    
def ReadExcels(n):
    records = []
    table_name = ExcelFiles[n]
    with open(table_name+".csv",'r') as table:
        table2 = csv.reader(table, skipinitialspace=True)
        for counter, row in enumerate(table2):
            if counter < 6:
                pass
            elif counter == 6:
                property_names = CleanSqlProperties(row)
            elif row == []:
                pass
            else:
                records += [CleanSqlRecords(row)]
    return table_name, property_names, records
    
def LoadDb(n, c):
    table_name, property_names, records = ReadExcels(n)
    print "{:16s} {:6d}".format(table_name, len(records))
    meh = len(property_names)-1
    
    # isntead of this giberish, read this:https://www.sqlite.org/lang_datefunc.html
    ct = "CREATE TABLE "+table_name+" ("
    ii = "INSERT INTO "+table_name+" VALUES"+" ("
    for i in property_names:
        if "date" in i or "year" in i:
            ct += "{} date"
            print "* {:12s}".format(i)
        else:
            ct += "{} text"
            print "  {:12s}".format(i)
        ii += "?"
        if i != property_names[-1]:
            ct += ", "
            ii += ", "
    ct += ")"
    ii += ")"
    c.execute(ct.format(*property_names))
    c.executemany(ii,records)
    
def main():
    # UpdateExcels()
    global conn, c
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    print "{0:15s} {1:6s}".format("tables","records")
    print "-----------------------"
    for n in range(len(ExcelFiles)):
        LoadDb(n, c)

main()
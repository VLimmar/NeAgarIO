from appdata import *




def searchname(name):
    sess = session(bind=engine)
    getdata = sess.query(Data)
    alldata = getdata.all()
    sess.close()
    for temp in alldata:
        if temp.name == name:   
            return True
    return False

def getinfo(name):
    if searchname(name) is True:
        sess = session(bind=engine)
        getdata = sess.query(Data)
        filtdata = getdata.filter(name == Data.name)
        sess.close()
        score = filtdata[0].score
        return score
    else:
        return 0

def setsave(name, score):
    if searchname(name) is True:
        sess = session(bind=engine)
        getdata = sess.query(Data)
        filtdata = getdata.filter(name == Data.name)
        namedat = filtdata[0]
        namedat.score = score
        sess.commit()
        sess.close()
    else:
        sess = session(bind=engine)
        dat = Data(name = name, score = score)
        sess.add(dat)
        sess.commit()
        sess.close()

def top(count):
    ses = session(bind = engine)
    wh = ses.query(Data)
    sclist = []
    for temp in wh:
        i = (temp.score, temp.name)
        sclist.append(i)
    nesort(sclist)
    ses.close()
    return sclist[0:count]


def nesort(a):
    b = 0
    for temp in range(0, len(a)):
        for timp in range(0, len(a)):
            if a[temp] > a[timp]:
                b = a[temp]
                a[temp] = a[timp]
                a[timp] = b
    return a
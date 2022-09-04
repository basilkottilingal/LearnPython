#Compile all *.bib and storing in _all.bib

import os

#current working dir
path=os.getcwd()
#new files will be written to this dir
path=path+'\_allref'
if not os.path.exists(path):
    os.mkdir(path)


#copy of path. Incase path is changed in future
PATH_TO_WRITE=str(path)
def _write_to(fname):
    _fname = PATH_TO_WRITE+"\\"+fname
    #object of (writing) file
    _fw = open(_fname,"w");
    if _fw == None:
        print('COUDN\'T OPEN')
    return _fw;


articles=[];
_fw=_write_to('all.bib');
NotFound=1
for _file in os.listdir():
    if (_file[-4:]=='.bib'):
        #print(f'{_file}');
        _fr = open(_file, 'r');
        for line in _fr:
            _l=line.strip();
            if (_l != ''):
                if (_l[0] == '@'):
                    _article = _l[_l.find("{")+1:_l.find(",")];
                    if _article not in articles:
                        articles.append(_article);
                        NotFound=1
                    else:
                        Notfound=0
                if (_l[0] != '%' and NotFound == 1):
                    _fw.write(line);

        _fr.close();

_fw.close();

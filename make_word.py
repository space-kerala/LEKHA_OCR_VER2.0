# -*- coding: utf-8 -*-
def form_word(list):
    i=0
    string=''
    while(i<len(list)):
        if(i==(len(list)-1))and(list[i].decode('utf-8')in['o','0','ഠ'.decode('utf-8')]):
            string=string+'ം'.decode('utf-8')
        else: 
            try:
                #checking whether the input is  ' or " or ,
                if(list[i].decode('utf-8')in ['\'',',']):
                    if(list[i+1].decode('utf-8') in ['\'',',']):
                        string=string+'\"'
                        i+=1
                    else:
                        string=string+list[i].decode('utf-8')
                elif(list[i].decode('utf-8')in ['െ'.decode('utf-8'),'േ'.decode('utf-8'),'്ര'.decode('utf-8')]):
                    try:
                        if(list[i+1].decode('utf-8')in ['െ'.decode('utf-8'),'്ര'.decode('utf-8')]):
                            string=string+list[i+2].decode('utf-8')+list[i+1].decode('utf-8')+list[i].decode('utf-8')
                            i+=3
                            continue
                        elif(list[i+2].decode('utf-8')in ['്വ'.decode('utf-8')]):
                            string=string+list[i+1].decode('utf-8')+list[i+2].decode('utf-8')+list[i].decode('utf-8')
                            i+=3
                            continue
                    except IndexError:
                        do_nothing=0
                    string=string+list[i+1].decode('utf-8')
                    string=string+list[i].decode('utf-8')
                    i+=1
                else:
                    string=string+list[i].decode('utf-8')
            except IndexError:
                string=string+list[i].decode('utf-8')    
        i+=1
    return string

# -*- coding: utf-8 -*-
def form_word(list):
    i=0
    
    string =''

    list =[i.decode('utf-8') for i in list ]
    #print(((list[0])))
    while(i<len(list)):
        if(i==(len(list)-1))and(list[i]in['o','0','ഠ']):
            string=string+'ം'
        else: 
            try:
                #checking whether the input is  ' or " or ,
                if(list[i]in ['\'',',']):
                    if(list[i+1] in ['\'',',']):
                        string=string+'\"'
                        i+=1
                    else:
                        string=string+list[i]
                elif(list[i]in ['െ','േ','്ര']):
                    try:
                        if(list[i+1]in ['െ','്ര']):
                            string=string+list[i+2]+list[i+1]+list[i]
                            i+=3
                            continue
                        elif(list[i+2]in ['്വ']):
                            string=string+list[i+1]+list[i+2]+list[i]
                            i+=3
                            continue
                    except IndexError:
                        do_nothing=0
                    string=string+list[i+1]
                    string=string+list[i]
                    i+=1
                else:
                    string=string+list[i]
            except IndexError:
                string=string+list[i]    
        i+=1
    return string


#    Lekha Ocr version 2.0 - Convert your malayalam documents and images to editable text
#    Copyright (C) 2018 Space-kerala (Society For Promotion of Alternative Computing and Employment)

#    Lekha Ocr version 2.0 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Lekha Ocr version 2.0 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


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

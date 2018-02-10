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

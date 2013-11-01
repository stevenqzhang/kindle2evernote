# -*- coding: utf-8 -*-

# Steven Zhang
# StevenZhang.com


'''
TODO

use arguments for clippings and clippings small.txt

use subprocess http://docs.python.org/2/library/subprocess.html#replacing-older-functions-with-the-subprocess-module

CHANGELOG

2013/01/11
    Worked out kinks in UTF8

'''

import os
import codecs

def debug():
    notes = ParseClippingsTextFile("clippings_small.txt");
    notes = MergeSimilarNotes(notes);
    print notes

def main():
    print "=============parsing notes..."
    notes = ParseClippingsTextFile("clippings.txt");
    print "successfully parsed myclippings.txt=============";

    print "=============merging similar notes..."
    notes = MergeSimilarNotes(notes);
    print "successfully merged similar notes=============";
   
    print "=============creating notes..."
    for note in notes:
        print "   creating note " + note['title'].encode('utf-8')
        MakeEvernoteNote(note);
        print "   sucessfully created note "+ note['title'].encode('utf-8')
    
    print "done creating notes============="

# merge notes with same title
# solution inspired by http://stackoverflow.com/questions/3421906/how-to-merge-lists-of-dictionaries
def MergeSimilarNotes(notes):

    # first create a dictionary of merged {note_title: note dictionary} pairs
    merged = {}
    for note in notes:
        if note['title'] in merged:     # if this titled note is the new dictionary
            current_note = merged[note['title']];
            new_note = {}
            new_note['title'] = note['title']
            new_note['content'] = current_note['content'] + '\n====' + note['content']
            merged[note['title']].update(new_note)
        else:
            merged[note['title']] = note
    # then return as a list...
    return [val for (_, val) in merged.items()]
    
'''
Reads a unicode file

INPUT
    input - string filepath

OUTPUT
    data - a unicode object
'''
def ReadUTF8(filepath):
    f = codecs.open(filepath, 'rb', 'utf-8',errors='strict')
    data = "".join(f.readlines())

    return data

'''        
parse myclippings.txt
content has 
    title
    content
'''
def ParseClippingsTextFile(filepath):
    # read data as unicode
    data = ReadUTF8(filepath)
    
    # read encode unicode to string, then split
    encoded_data = data.encode('utf-8')
    # print "Encoded Data:======================"
    # print encoded_data
    encoded_clippings = encoded_data.split('==========\r\n')
    
    # print "Encoded clippings================="
    # print encoded_clippings
    
    notes = []
    for clip in encoded_clippings:
        partitioned_clip = clip.partition('\n')
        
        # each content should be decoded into unicode
        title = partitioned_clip[0].decode('utf-8')
        
        #error catching
        title = title.replace(".", "")
        
        content = partitioned_clip[2].decode('utf-8')
        
        # some error catching
        if title == "":
            title = u" "
        if content == "":
            content = u" "
        
        note = {'title': title, 'content': content}
        print "     note <" + title.encode('utf-8') + "> was parsed"
        notes.append(note)
    return notes

'''
Clean string of Chinese characters
''' 
def CleanStringOfChineseCharacters(content):
    #new_content = content.replace(u"Äê", "bob")     #to be used if replacement is needed
    new_content = content;
    return new_content
'''    
temp file for file contents, using UTF8

INPUT
    unicode object content: stuff to be written onto a file
    
OUTPUT
    string filename (usually "temp.txt")
'''
def CreateTempFile(content):
    fo = codecs.open("temp.txt","w","utf-8-sig")
    fo.write(content)
    fo.close
    

    print "Done writing file!"
    return "temp.txt"
    
    
def MakeEvernoteNote(note):
    title = WrapStringWithQuotes(note['title']);
    content = note['content'];
    file = CreateTempFile(content);
    notebook = '"KindleClippings"'  ;
    cmd = "enscript createNote /i " + title.encode('utf-8')  + " /s " + file + " /n " + notebook;
    os.system(cmd)
    
def WrapStringWithQuotes(str):
    return '"'+str+'"'


if __name__ == '__main__':
    main()
    #debug()

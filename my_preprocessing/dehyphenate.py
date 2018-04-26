#!/usr/bin/python
# Author: Nicolas Spring (17-703-455)

'''
this module converts text extracted from pdf files back to its logical
structure
'''

import io
# import sys

def join_lines(sep_stream, dehyph_stream):
    '''
    joins lines whilst taking hyphenation and structure into account
    
    Params:
    sep_stream (file-like object): the input file that is read
    dehyph_stream (file): file the final output will be written to
    '''    
    local_list2 = []
    
    # Putting all the lines into a list
    for line in sep_stream:
        local_list2.append(line)
    
    # Reading every line/string in the list
    for n in range(len(local_list2)):
        # Handling the IndexError that will happen with the last line
        try:
            # Printing the last lines in a paragraph fully
            if local_list2[n+1] == '\n':
                dehyph_stream.write(local_list2[n])
            # Ignoring blank lines
            elif local_list2[n] == '\n':
                dehyph_stream.write(local_list2[n])
            # Lines not at the end of a paragraph
            else:
                # Hyphen at the end of the line
                if local_list2[n].endswith('-\n'):
                    dehyph_stream.write(local_list2[n][:-2])
                # No hyphen at the end of the line
                else:
                    dehyph_stream.write(
                    ''.join([local_list2[n][:-1], ' ']))
        # The very last line will be written to the file if not empty
        except IndexError:
            if local_list2[n] != '\n':
                dehyph_stream.write(local_list2[n][:-1])
             
    
def join_pages(sep_fns, dehyph_stream):
    '''
    joins pages (files) of text extracted from pdf files together
    
    this function joins pages together, restores the logical
        structure and writes the output into a file
    Params:
    sep_fns (list): a list of file names the user wants to be joined
    dehyph_stream (file): file the final output will be written to
    '''    
    local_list1 = []    
    
    # Putting all the lines into a list
    for file in sep_fns:
        with open(file, 'r') as my_file:
            for line in my_file:
                local_list1.append(line)  
                
    # Creating a file-like object for use in join_lines
    tempstr = ''.join(local_list1)
    s = io.StringIO(tempstr)    
    join_lines(s, dehyph_stream)
    s.close()
    
# def main():
    # files = list(sys.argv[:-1])
    # outfile = sys.argv[-1]
    # with open(outfile, 'w') as my_outfile:
        # join_pages(files, my_outfile)

    
if __name__ == '__main__':
    main()
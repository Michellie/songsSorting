
"""
  Name: Michelle Arthars
  UPI: mart923
  Purpose: To output k number of longest songs, in descending orders based on the provided list of song and the user input of k.
"""


import sys

""" Merge the divided elements back into an ordered list of songs """
def merge(left, right):
    a_list = []
    # Compare the song durations of the first element of each sub list and merge in descending order 
    while (len(left) != 0) and (len(right) != 0):
        ls = left[0]
        rs = right[0]
        ltime = int(ls[(ls.rfind("&")+ 1) : -1]) #extract left time
        rtime = int(rs[(rs.rfind("&")+ 1) : -1])
        if ltime > rtime:
            a_list.append(left[0])
            left.remove(left[0])
        elif ltime == rtime:
            lt = ls[:(ls.find("&"))] #extract left title
            rt = rs[:(rs.find("&"))]
            min_len = min(len(lt), len(rt))
            # compare and sort titles in alphabetical order for songs with the same duration
            while (len(lt) != 0) and (len(rt) != 0):
                if (ord(lt[0]) < (ord(rt[0]))):
                    a_list.append(left[0])
                    left.remove(left[0])
                    break
                elif (ord(lt[0]) > (ord(rt[0]))):
                    a_list.append(right[0])
                    right.remove(right[0])
                    break
            # if a shorter string has all of its letters matching the other string, display the shorter string first
            if ((len (lt)) - len(rt)) != 0:
                if len(lt) == 0:
                    a_list += left
                else:
                    a_list += right
	    # if both songs have the same duration, title, then compare the composer of each and order in alphabetical ordering
            else: 
                lc = ls[(len(lt) + 1): (ls.rfind("&"))]
                rc = rs[(len(rt) + 1): (rs.rfind("&"))]
                while (len(lc) != 0) and (len(rc) != 0):
                    if (ord(lc[0]) < (ord(rc[0]))):
                        a_list.append(left[0])
                        left.remove(left[0])
                        break
                    elif (ord(lc[0]) > (ord(rc[0]))):
                        a_list.append(right[0])
                        right.remove(right[0])
                        break
                # if a shorter string has all of its letters matching the other string, display the shorter string first
                if len(lc) == 0:
                    a_list += left
                else:
                    a_list += right
        else:
            a_list.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        a_list +=  right
    else:
        a_list += left
    return a_list

""" recursively divide the list in halves """
def mergesort(songs):
    if len(songs) == 0 or len(songs) == 1:
        return songs
    else:
        middle = (len(songs)) // 2
        left =  mergesort(songs[:middle])
        right = mergesort(songs[middle:])
        return merge(left, right)

def main():
    content = sys.stdin.readlines()
    print(content)
    k = int(content[0])
    songs = []
    for i in range (2,len(content)):
        songs.append(content[i])
        i += 1
    s1 = songs[0]
    time1 = s1[(s1.rfind("&")+ 1) : -1]
    sort = mergesort(songs)
    # just incase, number exceed number of songs
    if k > len(sort): 
        k = len(sort)
    for i in range (k):
        print(sort[i][:-1])


main()

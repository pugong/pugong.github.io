# import imghdr
import os
import re
import sys
import traceback

import shutil

# import uuid

from datetime import datetime
# from functools import wraps
# 
POST_DATE_FORMAT = '%Y-%m-%d'



def promote(draft):

    p_path=os.path.realpath('../_posts')
    
    #print p_path

    f = os.path.realpath(draft)
    # return a list of directory names using platform specific separator
    dirlist = f.rsplit(os.sep)

    # check the draft name for a date
    # if you find one, replace it
    # if you don't find one, add it
    dirlist[-1] = re.sub(r'(^\d{4}-\d{2}-\d{2}-)', '', dirlist[-1])
    d = datetime.today()
    d_str = "{0}-".format(d.strftime(POST_DATE_FORMAT))
    dirlist[-1] = d_str + dirlist[-1]

    spath = dirlist[dirlist.index('_drafts')+1:]
    fpath = os.path.join(p_path, *spath)
    bpath = os.path.split(fpath)[0]

    # print spath
    # print fpath
    # print bpath

    # return
    # if the folder path doesn't yet exist, create it recursively
    if not os.path.exists(bpath):
        os.makedirs(bpath)

    if not os.path.exists(fpath):
        shutil.move(f, fpath)


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        '-d', '--draft',
        dest='draft', default=None
    )
    args = parser.parse_args()
    # now = datetime.datetime.now()
    if args.draft:
        # print args.draft

        promote(args.draft)
    else:
        print "please specific the draft file using -d / --draft parameter"

if __name__ == "__main__":
    main()


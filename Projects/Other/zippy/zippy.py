#!/usr/bin/env python2.7

# Libraries to call to
import os, zipfile, libarchive

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

def sevenZip(src, dst):
	for entry in libarchive.create('7z', ['/aa/bb', '/cc/dd'], 'create.7z'):
		print("Adding: %s" % (entry))

def zippy(src, dst):
	print("Do something")
	
def sample_data(type, range):
	print("Do something")
	
zippy("src", "dst")
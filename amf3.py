import os
import sys
import zlib
import json
import pyamf
 
def amfparser(srcpath, n, dstpath):
    fsize = os.path.getsize(srcpath)
    srchandle = open(srcpath, 'rb')
    srchandle.seek(n)
    rdata = srchandle.read(fsize - n)
    decdata = pyamf.decode(zlib.decompressobj().decompress(rdata))
    srchandle.close()
    
    wdata = {}
    dsthandle = open(dstpath, 'w')
    wdata[k] = [elem[k] for elem in decdata for k in elem]
    dsthandle .write(json.dumps(wdata, encoding='utf-8', ensure_ascii=False))
    dsthandle.close()
 
 
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    amfparser('amf3_test_data', 13, 'amf3_test_data_out')

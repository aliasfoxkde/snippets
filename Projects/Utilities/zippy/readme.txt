""" Pseudo Compression Algorithm """

This is experimental code that exploits a potential side effect of compression 
libraries. This is not intended to be a "real world" compression algorithm. 
Zippy is an amazing compression technique but it can only reduce "pattern" 
data and not random datasets. However, unlike an obvious exploit of duplicating
data, all the values are unique (though they may be similiar or paternistic)
and the 'Zippy' exploit handles this particular data better than ZIP or 7Zip.

Benchmarks

128 MB Hexadecimal Sample File

Library     Elapsed Time    Size         % Rate
Zippy       15s             22 KB        99.98%
7zip        30s	            3,391 KB     97.41%
Zip         6s	            32,417 KB    75.27%
None        0s              131,072 KB   0% (N/A)

953 MB Decimal Sample File

Library     Elapsed Time    Size         % Rate
Zippy       49s             1,800 KB     99.82%
7zip        184s            14,775 KB    98.49%
Zip         30s	            215,837 KB   77.99%
None        0s              976,563 KB   0% (N/A)

Notes: The samples used and created are included in zippy/samples but you
       regenerate them using the scripts (Zippy sample files used for size).

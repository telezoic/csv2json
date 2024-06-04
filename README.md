Converts csv data to JSON for the 'Hatches,Matches, Dispatches' map 


Assumes csv structure: 

```
Parents,Child,Location,"""lat""","""lng""",SWS,Date,url,"""Page Number"""
"MCQUIRE, Mr. & Mrs. Henry",Daughter,"Cedar, BC",49.0993,-123.8077,5918767,1890-03-25,https://viurrspace.ca/bitstream/handle/10613/21077/Mar25-1890m.pdf?sequence=4&isAllowed=y#nameddest=1,1
"THATCHER, Mr. & Mrs. F. J.",Son,"Cedar, BC",49.0993,-123.8077,5918767,1893-12-11,https://viurrspace.ca/bitstream/handle/10613/20804/Dec11-1893m.pdf?sequence=4&isAllowed=y#nameddest=1,4
"MILLER, Rev. & Mrs.",Son,"Cedar, BC",49.0993,-123.8077,5918767,1894-05-12,https://viurrspace.ca/bitstream/handle/10613/20994/May12-1894m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"MILLER, Rev. & Mrs. R. G.",Daughter,"Cedar, BC",49.0993,-123.8077,5918767,1895-10-08,https://viurrspace.ca/bitstream/handle/10613/19077/Oct08-1895m.pdf?sequence=4&isAllowed=y#nameddest=1,4
"MILLER, Rev. & Mrs. E. G.",Daughter,"Cedar, BC",49.0993,-123.8077,5918767,1899-01-24,https://viurrspace.ca/bitstream/handle/10613/17426/Jan24-1899m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"HORNE, Mrs. A. G.",Son,"Comox, BC",49.695,-124.8706,5926432,1878-03-16,https://viurrspace.ca/bitstream/handle/10613/21937/Mar16-1878m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"CLIFFE, Mr. & Mrs. S. J.",Son,"Comox, BC",49.695,-124.8706,5926432,1880-08-07,https://viurrspace.ca/bitstream/handle/10613/22236/Aug07-1880m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"PIERCY, Mr. & Mrs. T. H.",Son,"Comox, BC",49.695,-124.8706,5926432,1887-11-26,https://viurrspace.ca/bitstream/handle/10613/22952/Nov26-1887m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"GRANT, Mr. & Mrs. J. J.",Daughter,"Comox, BC",49.695,-124.8706,5926432,1889-02-12,https://viurrspace.ca/bitstream/handle/10613/20674/Feb12-1889m.pdf?sequence=4&isAllowed=y#nameddest=1,4
"HOLMES, Mr. & Mrs. J. B.",Daughter,"Comox, BC",49.695,-124.8706,5926432,1889-02-19,https://viurrspace.ca/bitstream/handle/10613/20676/Feb19-1889m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"CLIFFE, Mrs. S.",Son,"Comox, BC",49.695,-124.8706,5926432,1891-01-09,https://viurrspace.ca/bitstream/handle/10613/21292/Jan09-1891m.pdf?sequence=4&isAllowed=y#nameddest=2,3
"ADAMS, Capt. & Mrs.",Son,"Coupeville Island, WA",48.21982,-122.68628,5791132,1879-04-16,https://viurrspace.ca/bitstream/handle/10613/22005/Apr16-1879m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"ROE, Mr. & Mrs. George H.",Son,"Courtenay, BC",49.68657,-124.9936,5930890,1894-08-16,https://viurrspace.ca/bitstream/handle/10613/19833/Aug16-1894m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"MCLAY, Mr. & Mrs. R",Son,"Cowichan, BC",48.8186,-123.8887,5931136,1878-01-16,https://viurrspace.ca/bitstream/handle/10613/21921/Jan16-1878m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"LOMAS, Mr. & Mrs. W. H.",Daughter,"Cowichan, BC",48.8186,-123.8887,5931136,1884-02-20,https://viurrspace.ca/bitstream/handle/10613/22626/Feb20-1884m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"MEHAN, Mr. & Mrs. John D.",Son,"Cranberry, BC",49.8008,-124.4847,5931605,1892-01-21,https://viurrspace.ca/bitstream/handle/10613/21112/Jan21-1892m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"BATE, Mr. & Mrs. Thomas",Son,"Cumberland, BC",49.6116,-124.9365,5933885,1899-07-03,https://viurrspace.ca/bitstream/handle/10613/16680/Jul03-1899m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"PICKETT, Mr. & Mrs. J.",Son,"Denman Island, BC",49.5257,-124.7676,5937819,1885-08-15,https://viurrspace.ca/bitstream/handle/10613/22813/Aug15-1885m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"CHENEY, Mr. & Mrs. William",Daughter,"Denman Island, BC",49.5257,-124.7676,5937819,1890-05-20,https://viurrspace.ca/bitstream/handle/10613/21090/May20-1890m.pdf?sequence=4&isAllowed=y#nameddest=1,1
"PIERCY, Mr. & Mrs. T. H.",Daughter,"Denman Island, BC",49.5257,-124.7676,5937819,1890-08-05,https://viurrspace.ca/bitstream/handle/10613/21145/Aug05-1890m.pdf?sequence=4&isAllowed=y#nameddest=1,3
"LOAT, Mrs. Christopher",Daughter,"Departure Bay, BC",49.2302,-124.0089,5937950,1878-02-23,https://viurrspace.ca/bitstream/handle/10613/21932/Feb23-1878m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3
"MEILADO, Mr. & Mrs. B.",Son,"Departure Bay, BC",49.2302,-124.0089,5937950,1879-05-17,https://viurrspace.ca/bitstream/handle/10613/22038/May17-1879m.pdf?sequence=4&isAllowed=y#nameddest=Birth1,3 . . . 
```

and converts to 

```
[
    {
        "Name": "MCQUIRE, Mr. & Mrs. Henry",
        "Child": "Daughter",
        "Location": "Cedar, BC",
        "lat": "49.0993",
        "lng": "-123.8077",
        "Date": "1890-03-25",
        "url": "https://viurrspace.ca/bitstream/handle/10613/21077/Mar25-1890m.pdf?sequence=4&isAllowed=y#nameddest=1",
        "PageNumber": "1"
    },
    {
        "Name": "THATCHER, Mr. & Mrs. F. J.",
        "Child": "Son",
        "Location": "Cedar, BC",
        "lat": "49.0993",
        "lng": "-123.8077",
        "Date": "1893-12-11",
        "url": "https://viurrspace.ca/bitstream/handle/10613/20804/Dec11-1893m.pdf?sequence=4&isAllowed=y#nameddest=1",
        "PageNumber": "4"
    },
    {
        "Name": "MILLER, Rev. & Mrs.",
        "Child": "Son",
        "Location": "Cedar, BC",
        "lat": "49.0993",
        "lng": "-123.8077",
        "Date": "1894-05-12",
        "url": "https://viurrspace.ca/bitstream/handle/10613/20994/May12-1894m.pdf?sequence=4&isAllowed=y#nameddest=1",
        "PageNumber": "3"
    },
    {
        "Name": "MILLER, Rev. & Mrs. R. G.",
        "Child": "Daughter",
        "Location": "Cedar, BC",
        "lat": "49.0993",
        "lng": "-123.8077",
        "Date": "1895-10-08",
        "url": "https://viurrspace.ca/bitstream/handle/10613/19077/Oct08-1895m.pdf?sequence=4&isAllowed=y#nameddest=1",
        "PageNumber": "4"
    },
    {
        "Name": "MILLER, Rev. & Mrs. E. G.",
        "Child": "Daughter",
        "Location": "Cedar, BC",
        "lat": "49.0993",
        "lng": "-123.8077",
        "Date": "1899-01-24",
        "url": "https://viurrspace.ca/bitstream/handle/10613/17426/Jan24-1899m.pdf?sequence=4&isAllowed=y#nameddest=1",
        "PageNumber": "3"
    }, . . . 
```

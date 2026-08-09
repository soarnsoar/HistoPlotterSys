[
    ##-----bjet origin == NON Top Bkgs-----##



    ("from_bminus__TTLJ",{
        "procs":["TTLJ_powheg_From"+p+"__HadronB" for p in ["bminus"]],
        "name":"from_bminus__TTLJ",
        "color":3,
        "IsSig":True
    }),

    ("from_bplus__TTLJ",{
        "procs":["TTLJ_powheg_From"+p+"__HadronB" for p in ["bplus"]],
        "name":"from_bplus__TTLJ",
        "color":3,
        "IsSig":True
    }),        



    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]



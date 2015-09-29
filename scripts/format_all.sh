#! /bin/bash
python format_cics_abend.py
python format_cics_axm.py
python format_cics_dfh1.py
python format_cics_dfh2.py
python format_cics_eyua.py
python format_db2msg.py
python format_db2codes.py
python format_mvs.py ../original/iea3m101.txt ../formatted/codes_101.txt
python format_mvs.py ../original/iea3m201.txt ../formatted/codes_201.txt
python format_mvs.py ../original/iea3m301.txt ../formatted/codes_301.txt
python format_mvs.py ../original/iea3m401.txt ../formatted/codes_401.txt
python format_mvs.py ../original/iea3m501.txt ../formatted/codes_501.txt
python format_mvs.py ../original/iea3m601.txt ../formatted/codes_601.txt
python format_mvs.py ../original/iea3m701.txt ../formatted/codes_701.txt
python format_mvs.py ../original/iea3m802.txt ../formatted/codes_802.txt
python format_mvs.py ../original/iea3m902.txt ../formatted/codes_902.txt
python format_mvs.py ../original/iea3ma01.txt ../formatted/codes_a01.txt


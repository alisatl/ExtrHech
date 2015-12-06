REM @ echo off

perl.exe .\src\utf8-to-ISO-8859-1.pl .\data\text.txt > .\temp\text_ISO.txt

C:\FreeLing-2.2\bin\analyzer.EXE -f C:\FreeLing-2.2\bin\es.cfg --outf "tagged" < .\temp\text_ISO.txt > .\temp\text.pos0

python .\src\tagged_back2line_whole_file.py .\temp\text.pos0   >.\data\text.pos

python .\src\fact_extr_regexp4.py .\src\facts_extr.config .\data\text.pos >.\output\text.extr




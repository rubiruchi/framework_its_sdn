#!/bin/bash

#vehicles car0 to car14

cat server_e.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/' | sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_e.txt | grep 5003 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_e.txt | grep 5003 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_etf.txt;  for i in {10..24}; do cat server_etf.txt | grep 200.0.10.1$i > server_etf_car$(echo $i-10|bc)_$1.txt; done; cat server_etf_car?_$1.txt | sort -n > server_etf_car_$1\_tt.txt

cat server_e2.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/' | sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_e2.txt | grep 5004 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_e2.txt | grep 5004 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_e2tf.txt;  for i in {10..24}; do cat server_e2tf.txt | grep 200.0.10.1$i > server_e2tf_car$(echo $i-10|bc)_$1.txt; done; cat server_e2tf_car?_$1.txt | sort -n > server_e2tf_car_$1\_tt.txt

cat server_g.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/' | sed 's/04/4*60/' | sed 's/05/5*60/'|  bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_g.txt | grep 5005 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_g.txt | grep 5005 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_gtf.txt;  for i in {10..24}; do cat server_gtf.txt | grep 200.0.10.1$i > server_gtf_car$(echo $i-10|bc)_$1.txt; done; cat server_gtf_car?_$1.txt | sort -n > server_gtf_car_$1\_tt.txt

cat server_s1.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/' | sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_s1.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_s1.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_s1tf.txt;  for i in {10..24}; do cat server_s1tf.txt | grep 200.0.10.1$i > server_s1tf_car$(echo $i-10|bc)_$1.txt; done

cat server_s2.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/' | sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_s2.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_s2.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_s2tf.txt;  for i in {10..24}; do cat server_s2tf.txt | grep 200.0.10.1$i > server_s2tf_car$(echo $i-10|bc)_$1.txt; done

cat server_s3.txt | grep IP | sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > servert.txt; cat servert.txt | cut -d'.' -f2 > z.txt; cat servert.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/'| sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat servert.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > servertf.txt; cat server_s3.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat server_s3.txt | grep 5002 | grep -v ttl | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste servertf.txt ipo.txt ipd.txt| expand | tr -s ' ' > server_s3tf.txt;  for i in {10..24}; do cat server_s3tf.txt | grep 200.0.10.1$i > server_s3tf_car$(echo $i-10|bc)_$1.txt; done

cat server_s?tf_car?_$1.txt | sort -n > server_stf_car_$1\_tt.txt

for i in {0..14}; do cat car$i.txt | grep IP | grep -v ARP | grep -v ICMP| sed 's/00:0/ 00:0/' | tr -s ' ' | cut -d' ' -f2,9,18 | cut -d')' -f1 | sed 's/,//'|cut -d':' -f2,3 | grep : > cart.txt; cat cart.txt | cut -d'.' -f2 > z.txt; cat cart.txt | cut -d':' -f1 | sed 's/00/0*60/' | sed 's/01/1*60/' | sed 's/02/2*60/' | sed 's/03/3*60/'| sed 's/04/4*60/' | sed 's/05/5*60/'| bc > x.txt; cat cart.txt | cut -d':' -f2 | cut -d'.' -f1 > y.txt; paste x.txt y.txt | expand | tr -s ' ' | tr ' ' '+' | bc > w.txt;  cat z.txt | tr ' ' 'x' >j.txt; paste w.txt j.txt | expand | tr -s ' ' | tr ' ' '.' | tr 'x' ' ' > cartf.txt; echo $i; cat car$i.txt | grep '>' | grep -v ICMP | tr -s ' ' | cut -d':' -f1 | cut -d'.' -f1-4 > ipo.txt; cat car$i.txt | grep '>' | grep -v ICMP | tr -s ' ' | cut -d':' -f1 | cut -d' ' -f4 > ipd.txt; paste cartf.txt ipo.txt ipd.txt| expand | tr -s ' ' > car$(echo $i)tf_$1.txt; done 

for i in $(ls car{7..10}\tf_$1.txt); do rm -f temp1.txt; rm -f temp2.txt; for j in $(cat $i | cut -d'.' -f1); do echo $j+150|bc >> temp1.txt; cat $i | cut -d'.' -f2 > temp2.txt; paste temp1.txt temp2.txt | expand | tr -s ' ' | sed 's/ /./' > $i; done; done

for i in $(ls car{11..14}\tf_$1.txt); do rm -f temp1.txt; rm -f temp2.txt; for j in $(cat $i | cut -d'.' -f1); do echo $j+225|bc >> temp1.txt; cat $i | cut -d'.' -f2 > temp2.txt; paste temp1.txt temp2.txt | expand | tr -s ' ' | sed 's/ /./' > $i; done; done

for i in $(ls car*tf_$1.txt); do for j in {5002..5005}; do cat $i | grep "\.$j" | grep 1498 > $(echo $i | cut -d'.' -f1)_$j.txt; done; done

cat car?tf_$1\_5002.txt | sort -n > cartf_$1\_5002_tt.txt; cat car?tf_$1\_5003.txt | sort -n > cartf_$1\_5003_tt.txt; cat car?tf_$1\_5004.txt | sort -n > cartf_$1\_5004_tt.txt; cat car?tf_$1\_5005.txt | sort -n > cartf_$1\_5005_tt.txt

for i in $(ls ping*); do rm -f s.txt; x=$(cat ping0_s.txt | grep 'from' |cut -d' ' -f1 | head -1); for j in $(cat $i | grep 'from' |cut -d' ' -f1); do echo $x-$j | bc | sed 's/-//' >> s.txt; done; cat $i | grep 'from' | cut -d'=' -f4 | cut -d' ' -f1 > d.txt; paste s.txt d.txt | expand | tr -s ' ' > delay$(echo $i | cut -d'.' -f1 | sed 's/ping//')_$1.txt; done

cat delay?_g_$1.txt |sort -n > delay_g_$1\_tt.txt; cat delay?_e_$1.txt |sort -n > delay_e_$1\_tt.txt; cat delay?_e2_$1.txt |sort -n > delay_e2_$1\_tt.txt; cat delay?_s_$1.txt |sort -n > delay_s_$1\_tt.txt
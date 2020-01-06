#
# dlfjdl. G(7115, 103689). 870 (0.1223) nodes with out-deg > avg deg (29.1), 462 (0.0649) with >2*avg.deg (Mon Jan  6 21:26:12 2020)
#

set title "dlfjdl. G(7115, 103689). 870 (0.1223) nodes with out-deg > avg deg (29.1), 462 (0.0649) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.smdfn.png'
plot 	"outDeg.smdfn.tab" using 1:2 title "" with linespoints pt 6

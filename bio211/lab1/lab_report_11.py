print "\\begin{figure}[h]"
print "\\caption{Differences between resting heart rate and final heart rate}"

# Shell out to python to print our table
from lab_report_1 import latex_table
print latex_table()

print "\\label{fig:table}"
print "\\end{figure}"


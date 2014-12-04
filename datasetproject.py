from scipy.stats.stats import pearsonr

datafile = 'C:\Users\Dr Al-Otaiby\Documents\dataproject\cleandataforproject.csv'

csvfile = open(datafile)

state   = []
highschool = []
bach    = []
advanced  = []
rape =[]
income = []

for each_line in csvfile:
    list_row = each_line.split(',')
    if list_row[0] == 'State':
        continue
    state.append( list_row[0] )
    highschool.append( float(list_row[1]) )
    bach.append( float(list_row[2] ))
    advanced.append(float(list_row[3]))
    income.append( int(list_row[4]) )
    rape.append(float(list_row[5]))

csvfile.close( )

#print state
#print highschool
#print bach
#print income
#print advanced
#print rape
#print ' '


print 'High School', pearsonr(highschool, income)
print 'Bachelor   ', pearsonr(bach, income)
print 'Advanced   ', pearsonr(advanced, income)
print 'Rape and high school ', pearsonr(rape, highschool)
print 'Rape and income ', pearsonr( income,rape )
print 'Bachelor and rape', pearsonr(bach, rape)


  
print '*** End of Program ***'

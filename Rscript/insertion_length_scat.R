chart <- read.csv('../genome_insert_scat_csv.csv', header=TRUE, sep=",")
png('../myfile.png')
plot(chart)
#barplot(as.integer(chart$isize), xlim=c(0,20000), ylim=c(0,28000) , width = 5, border = "dark blue", xlab="Isertion length", ylab="Isertions", names.arg = chart$position, horiz = TRUE, col="grey")
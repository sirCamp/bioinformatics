chart <- read.csv('../kmers.csv', header=TRUE, sep=",")
png('../kmers.png',width = 2000,  height = 600)
barplot(as.integer(chart$quantity), xlim=c(0,900), ylim=c(0,15000) , width = 5, main="Kmers distributions", border = "dark blue", xlab="Kmers", ylab="Quantity", names.arg = chart$kmer, horiz = FALSE, col="grey", las=2)
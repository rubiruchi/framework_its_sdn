tracecar<-read.table(file = 'mininet-wifi/cartf.txt')
traceserver<-read.table(file = 'mininet-wifi/servertf.txt')
names(traceserver)<-c("time", "id", "size")
names(tracecar)<-c("time", "id", "size")
options(digits.secs = 6)
traceserver$time <- as.POSIXlt(traceserver$time, origin = "1987-10-05 11:00:00")
tracecar$time <- as.POSIXlt(tracecar$time, origin = "1987-10-05 11:00:00")
tracecar$size<- tracecar$size*8
traceserver$size<- traceserver$size*8
taxabps1segcar<-aggregate(list(size = tracecar$size), list(segundos = cut(tracecar$time, "1 sec")), sum)
taxabps1segserver<-aggregate(list(size = traceserver$size), list(segundos = cut(traceserver$time, "1 sec")), sum)
taxabps1segcarts<-ts(taxabps1segcar$size, frequency = 1)
taxabps1segserverts<-ts(taxabps1segserver$size, frequency = 1)
#plot(taxabps1segcarts, main="Vehicle transmission (bits/s)", ylab='bits/s', xlab='segundos', col="blue", ylim=c(1e+06,6.5e+06))
plot(taxabps1segcarts[1:300], main="Vehicle transmission (bits/s)", ylab='bits/s', xlab='time(s)', ylim=c(1e+06,7e+06), type = "l", col="blue")
lines(taxabps1segserverts[1:300], main="Server reception (bits/s)", ylab='bits/s', xlab='time(s)', col="red")
legend(240, 2e+06, legend=c("Car transmission", "Server reception"), col=c("blue", "red"), lty=1:2, cex=0.8)

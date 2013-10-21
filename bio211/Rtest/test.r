set.seed(23)
mean.x <- numeric(10000)
for(i in 1:10000){
    x <- rnorm(1000)
    mean.x[i] <- mean(x)
}


# Plotter helper function
avg <- function (data) {
    data <- colMeans(data)
    return(data)
}
plot_data <- function (avg_data, xlab='', ylab='', title='', strip_X=TRUE, x_scale=1.0) {
    # Data should already by average data
    # Get X axis names without the 'X'
    if (strip_X) {
        xlabels = names(avg_data) <- substr(names(avg_data), 2, nchar(names(avg_data)))
    } else {
        xlabels = names(avg_data)
    }
    plot(avg_data, xlab=xlab, ylab=ylab, main=title, xaxt="n")
    axis(1, at=seq(from=1, to=length(xlabels), by=1), labels=xlabels, cex.axis=x_scale)
}

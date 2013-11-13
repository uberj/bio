library(testthat, lib.loc="/home/juber/R/")

the_same <- function (f1, f2) {
    expect_that(f1(), equals(f2()))
}

isequal <- function (a, b) {
    expect_that(a, equals(b))
}


f1 <- function() {
    return('foo');
}

f2 <- function() {
    'foo';
}

f3 <- function() {
    'foo'
}


the_same(f1, f2)
the_same(f2, f3)
the_same(
    function (){
        'baz'
        'bar'
    },
    function (){
        'bar'
    }
)

# Recursion
fib <- function (x){
    if (x <= 1){
        x
    } else {
        fib(x - 1) + fib(x - 2)
    }
}

isequal(fib(20), 6765)

# Closures

outerx1 <- 3
outerf1 <- function () {
    # Closing over a name that is used in a function call is done by reference
    # reference. We know this because the value passed to isequal is going to
    # be the number 4, which is assigned to outer_x1 after this function is
    # declared.
    isequal(outerx1, 4)
}
outerx1 <- 4  # Reassign
outerf1()  # New outer_x is seen during execution of outer_f

outerx2 <- 3
outerf2 <- function () {
    innerx2 <- outerx2  # Definitly passed by reference
    isequal(innerx2, 4)
}
outerx2 <- 4  # Reassign
outerf2()  # New outer_x is seen during execution of outer_f

outerx3 <- 3
outerf3 <- function (x=outerx3) {
    x
}
outerx3 <- 4
isequal(outerf3(), 4)

outerx3 <- 3
outerf3 <- function (x=outerx3) {
    x
}
outerx3 <- 4
isequal(outerf3(), 4)

f1 <- function (x='default param') {
    return(x);
}
x <- 'local assignment'

dontcare <- f1(x)
isequal('local assignment', x)

dontcare <- f1(x='override default with =')
isequal('local assignment', x)

dontcare <- f1(x<-'override default with <-')
isequal('override default with <-', x)

a = 1
b = 2

f <- function(x) {
    isequal(a, 1)  # outerscope values are used
    isequal(b, 2)  # outerscope values are used
    a * x + b
}

g <- function(x) {
    a = 2  # Assignment only applies to this scope
    b = 1  # Assignment only applies to this scope
    f(x)
}

dontcare <- g(2)

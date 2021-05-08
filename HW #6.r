#Create first matrix
matrix.1 <- matrix(c(7,2,9,4,12,13), nrow = 2, ncol = 3)
matrix.1

#Create second matrix
matrix.2 <- matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), nrow = 3, ncol = 4)
matrix.2

#Multiply matrices together
matrix.1%*%matrix.2

#Create data frame
Data_Frame <- data.frame(
    id = c(1,2,3,4,5),
    name = c("Peter", "Amy", "Ryan", "Gary", "Michelle"),
    salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)

#Print data frame
Data_Frame

#Add new department column
New.col.DF <- cbind(Data_Frame, department = c("HR", "sales", "marketing", "legal", "management"))

#Print new department column
New.col.DF

#Extract rows 1,3,5 with columns 2,3 with c function
Data_Frame[c(1,3,5), 2:3]

#Plot bar chart with salary of rows 1,4,5 with name labels. 

barplot(y <- Data_Frame[c(1,4,5),3], 
        names.arg = Data_Frame[c(1,4,5),2],
        main = "Selected  Salaries",
        xlab = "Name",
        ylab = "Salary")

#Plot pie chart with highest, lowest, median salary 
#Find salary statistics
summary(Data_Frame[3])

#Use findings for pie chart  values
#x <- c(515.2, 623.3, 843.2)
x <-  c(min(Data_Frame$salary), median(Data_Frame$salary), 
        max(Data_Frame$salary))

#Create vector of labels
mylabel <- c("Lowest Salary: 515.20","Median Salary: 623.30", 
             "Highest Salary: 843.20")

#Create a vector of colors
colors <- c("blue", "green", "purple")


pie(x, label = mylabel, main = "Salary Statistics", col = colors)

#If-else function
n <- 272

if ((n%%2) == 0) {
    print("Even Number")
    if ((n%%3) == 0) {
        print("and also divisible by 3 and 6")
    } else {
        print("but not divisible by 3 or 6")
    }
} else {
    print("Odd Number")
}



#For-loop (with if-else combined)
#Win game if dice number is even:

dice <- 1:6

for(x in dice) {
    if ((x%%2) == 0) {
        print(paste("The dice number is an even number,", x, "You win!"))
    } else {
        print(paste("The dice number is an odd number,", x, "You lose."))
    }
}



# Python-Challenge

#PyBank/PyPoll

#Final Output

PyBank: To solve this problem i have used the list[] Method. First i did import the given csv file and read the values into csvreader. Inside the for loop i have appended the column values in csv file to two list variables and calculated the row count and total profit amount by increasing the count.
Now i need a condition to calculate my net and average profit loss, and i used if condition logic to calculate the net and average values and append it to another list variable month profit change . Now to find the greatest increase and decrease i had to do max and min on the list variable month profit changes and index on the same list gives me the month info.
Once i have all the values i am using print statements to print the values to terminal and with csvwrite syntax i am using the same print statements to write the values to txt file.

PyPoll: To solve this i used the same list[] method as above, but i had to declare the candidate names in list format in code, rather than reading from csv. Next i and reading the csv file and checking for row count and comparing the index[2] with the candidate list and counting the total votes based on the candidate name in the list. once i have total votes for each candidate i am calculating the percentage based on the total votes for candidate per row count.Next step i am printing the values to the terminal. As a final step to find out the winner using an if condition to determine the winner based on percentage of votes. And finally with csvwrite writing the contents to txt file.
total_number = int(input("Total marks: "))  
failing_number = int(input("Failing number: "))  
score = int(input("Your score: "))

failing_percentage = failing_number / total_number * 100 

score_percentage = score / total_number * 100 

ninety_percent = total_number * 90 / 100

Half_Of_Total = total_number / 2


if ( failing_number > score):
    print("Sorry but you are fail you score: ", str(score_percentage) + "%" , "Out of: ", str(failing_percentage)+"%")


elif (total_number < score):
    print("Dont tell lie you can score more then total number")

elif (ninety_percent <= score):
    print("Excellent use score above 90%. Your score is: " , str(score_percentage) + "%")

elif (Half_Of_Total < score):
    print("Good you score more the 50%. Your score is: " , str(score_percentage) + "%")

else:
    print("You should study hard in order to get good number. Your score is: " , str(score_percentage) + "%")    


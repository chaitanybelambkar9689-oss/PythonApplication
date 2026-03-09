from sklearn.metrics import confusion_matrix # Confusion matrix he  actual answer ani model ne dilele answer mhanjech predicted yana  comapre karun ans dete
def main():
    # 1 : Positive
    # 2 : Negative

    Actual =    [1,0,1,1,1,0,1,0,0,1] 
    Predicted = [1,0,0,1,1,1,1,1,0,1]
    

    print("Actual Data : ",Actual)
    print("Predicted data :",Predicted)

    con_mat = confusion_matrix(Actual,Predicted)
    print(con_mat)
    #[[True negative  false positive] [True Positive  False Negative]]
    #[[2 2][1 5]]
if __name__ == "__main__":
    main()


    #Output : [True negative  false positive]
    #       : [False negative  True Positive]
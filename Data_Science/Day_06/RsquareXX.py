from sklearn.metrics import r2_score
def main():
    Y_actual =[3,4,2,4,5]               #y
    Y_predicted = [3,4,2,4,5]           #yp
     
    r2 = r2_score (Y_actual,Y_predicted)

    print("Actual Values  : Y",Y_actual)
    print("Predicted_Value : Yp",Y_predicted)
    print("R Square Value : ",r2)  #0.237

if __name__ == "__main__":
    main()
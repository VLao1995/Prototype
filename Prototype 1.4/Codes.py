import pandas as pd
from collections import Counter

print("Hello [NAME], I'm IVAA, Your Personal Assistant")
input_value_topic = input("What Can I Do For You Today!?")

if input_value_topic == "Clubbing":
    csv_data = pd.read_csv("Clubbing_Data.csv", sep=",")
    csv_data_df = pd.DataFrame(csv_data)
    input_value_new_target = input("Please Select the Clubs You've Been To!")
    input_value_new_target_similarity = input("Are You Looking For Some Place Similar!")
    new_data_clubbing = []

elif input_value_topic == "Eating":
    csv_data = pd.read_csv("Food_Data.csv", sep=",")
    csv_data_df = pd.DataFrame(csv_data)


input_value_list = []
matches = []
col_counter = 0
number_of_rows = len(csv_data_df)
number_of_cols = len(csv_data_df.columns) - 1

while col_counter < number_of_cols:
    input_value = input((str(csv_data_df.columns.values[col_counter] + "?")))
    if input_value != "stop":
        input_value_list.append(input_value)
    if input_value == "stop":
        break
    row_counter = 0
    for value in csv_data_df.iloc[0:number_of_rows, col_counter]:
        if value == int(input_value):
            matches.append(csv_data_df.iloc[row_counter, -1])
        row_counter += 1
    count = Counter(matches)
    if count.most_common()[0][1] > count.most_common()[1][1]:
        break
    col_counter += 1

count = Counter(matches)
print("PERFECT! Would you Like to Go To", count.most_common()[0], "? ")
SeeMore = input()

if SeeMore == "0":
    print("We also recommend", count.most_common()[1:5])

if input_value_topic == "Clubbing":
    new_data_clubbing.append(input_value_new_target)



    #PROBLEM!!!!
    if input_value_new_target_similarity == "0":
        for i in range(len(input_value_list)):
            if i == "1":
                input_value_list[i] = 0
            if i == "0":
                input_value_list[i] = 1

        new_data_clubbing.append(input_value_list)


    print(new_data_clubbing)
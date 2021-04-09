#! Mifflin st jeor
# 10 * weight(kg) + 6.25 * height - 5 * age + 5

BMR = (
    10 * int(input("body wight: "))
    + 6.25 * int(input("height: "))
    - 5 * int(input("age: "))
    + 5
)

TDEE = BMR * 1.7

# week one and week 2 calorie intake
W1and2 = TDEE * 0.8
W1_Protein = 83 * 1.2
W1_fats = W1and2 * 0.20 / 9
W1_carbs = W1and2 - W1_Protein * 4 + W1_fats * 9 / 4

print(
    f" calorie intake week 1 && 2: {round(W1and2, 2)} \n micro \n  protein: {round(W1_Protein,2)}g \n fats: {round(W1_fats,2)}g \n carbs:{round(W1_carbs,2)}g "
)

week3_4 = W1and2 * 0.9
W2_Protein = 83 * 1.2
W2_fats = week3_4 * 0.20 / 9
W2_carbs = week3_4 - W2_Protein * 4 + W2_fats * 9 / 4

print("+++===+++===+++===+++===+++===+++===+++===+++===+++=== \n")

print(
    f" calorie intake week 3 && 4: {round(week3_4,2)} \n micros \n protein: {round(W2_Protein,2)} \n  fats: {round(W2_fats,2)} \n carbs: {round(W2_carbs,2)} "
)


week5_6 = week3_4 * 0.9
W3_Protein = 83 * 1.2
W3_fats = week5_6 * 0.20 / 9
W3_carbs = week5_6 - W3_Protein * 4 + W3_fats * 9 / 4

print("+++===+++===+++===+++===+++===+++===+++===+++===+++=== \n")

print(
    f" calorie intake week 5 && 6: {round(week5_6,2)} \n micros protein: {round(W3_Protein,2)} \n fats: {round(W3_fats,2)} \n carbs: {round(W3_carbs,2)} "
)
def gallons_to_litres(gallons):
  litres = gallons * 3.785
  return litres

user_input = 0

while user_input >= 0:
    user_input = float(input("montako gallonaa "))

    result = gallons_to_litres(user_input)

    print(result)

print("väärä syöte")


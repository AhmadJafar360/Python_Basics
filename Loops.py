# For Loops
for item in range(5, 10, 2): # Memunculkan nomer sebelum angka 10
 print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# While Loops
i = 1
while i <= 5:
    print('gapopo'*i)
    i = i + 1
print("done")

# Nested Loops
for x in range(4):
   for y in range(3):
      print(f'({x},{y})')

# Challenge
# Nomor = [5, 2, 4, 2, 3]
# for x_press in Nomor:
#    print('x' * x_press)

# Challenge 2
Nomer = [4, 4, 3, 4, 1]
for x_count in Nomer:
   output = '' 
   for count in range(x_count):
      output += 'x'
   print(output)
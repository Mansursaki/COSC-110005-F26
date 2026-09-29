# Auther: Mansur Sakhizadah 
# Date: September 21, 2026 
# Descrption this code will be able to calculate how much ice cream was sold in a ice cream shop in 1 week 

# Output: Identify how much ice cream was sold in 1 week 

# Input: How much scoopes of ice cream was sold each scoope is meassered in 120ml 

# Process: 
# calculate the number of scoopes for each cone size 
# add the scoopes together 
# mutiply each scoope size by 120ml

# pseudo code 
# # START
# INPUT kiddie cones
# INPUT small cones
# INPUT medium cones
# INPUT large cones
# kiddie scoops = kiddie cones * 0.5
# small scoops = small cones * 1
# medium scoops = medium cones * 2
# large scoops = large cones * 3
# total scoops = kiddie scoops + small scoops + medium scoops + large scoops
# total millilitres = total scoops * 120
# OUTPUT total millilitres
# END

kiddie = int(input("how many kiddie scoops were sold"))
small = int(input("how many small scoops were sold "))
medium = int(input("how many medium scoops were sold"))
large = int(input("how many large scoops were sold"))

kiddie_scoops = kiddie * 0.5
small_scoops = small * 1
medium_scoops = medium * 2
large_scoops = large * 3

total_scoops = kiddie_scoops + small_scoops + medium_scoops + large_scoops

total_millilitres = total_scoops * 120

print("Total ice cream sold:", total_millilitres, "mL")





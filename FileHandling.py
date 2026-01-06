# file=open("./file.txt",'r')

# # print(file)

# # content=file.read()
# # content=file.readline()
# # content=file.readline()
# # content=file.readline()
# content=file.readlines()

# print(content[2])

# file.close()


# file=open("./file.txt",'w')

# file.write("Virat Kohli (born 5 November 1988)[a] is an Indian international cricketer and the former all-format captain of the Indian national cricket team.\n He is a right-handed batter and occasional right-arm medium pace bowler.\n Considered one of the greatest all-format batsmen in the history of cricket, he has been nicknamed the King, the Chase Master, and the Run Machine for his skills, records and ability to lead his team to victory.\n Kohli has the most centuries in ODIs and the second-most centuries in international cricket with 84 tons across all formats.\n He is also the leading run-scorer in the Indian Premier League.\n Kohli is the most successful Test captain of India with most wins and 3 consecutive Test mace retainments.\n He is the only batter to earn 900+ rating points across all 3 formats.")

# file.close()

# file=open("./file.txt",'a')

# file.write("\n\nVirat Kohli (born 5 November 1988)[a] is an Indian international cricketer and the former all-format captain of the Indian national cricket team.\n He is a right-handed batter and occasional right-arm medium pace bowler.\n Considered one of the greatest all-format batsmen in the history of cricket, he has been nicknamed the King, the Chase Master, and the Run Machine for his skills, records and ability to lead his team to victory.\n Kohli has the most centuries in ODIs and the second-most centuries in international cricket with 84 tons across all formats.\n He is also the leading run-scorer in the Indian Premier League.\n Kohli is the most successful Test captain of India with most wins and 3 consecutive Test mace retainments.\n He is the only batter to earn 900+ rating points across all 3 formats.")

# file.close()


import os

# print(os.path.exists("./file.txt"))

os.remove('./dummy.csv')
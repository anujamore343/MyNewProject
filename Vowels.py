#write a function to find Vowels in username 
def count_vowels(username):
    vowels = "aeiouAEIOU"
    count = 0
    for char in username:
        if char in vowels:
            count += 1
    return count
username = input("Enter your username: ")
total_vowels = count_vowels(username)
print("Number of vowels in username is:", total_vowels)
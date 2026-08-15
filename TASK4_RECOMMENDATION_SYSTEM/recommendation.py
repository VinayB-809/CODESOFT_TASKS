movies = [{"name": "Baahubali", "genre": "Action"},{"name": "RRR", "genre": "Action"},{"name": "KD: The Devil", "genre": "Action"},{"name": "KGF Chapter 1", "genre": "Action"},{"name": "Salaar", "genre": "Action"},{"name": "Chatrapathi", "genre": "Action"},{"name": "Saaho", "genre": "Action"},{"name": "Dacoit", "genre": "Action"},{"name": "Sardaar Gabbar Singh", "genre": "Action"},{"name": "OG", "genre": "Action"},{"name": "Daaku Maharaaj", "genre": "Action"},{"name": "Rebel", "genre": "Action"},{"name": "Vikram", "genre": "Action"},{"name": "Kaithi", "genre": "Action"},{"name": "Leo", "genre": "Action"},{"name": "Coolie", "genre": "Action"},{"name": "Eega", "genre": "Action"},{"name": "Rangasthalam", "genre": "Action"},{"name": "Pushpa: The Rise", "genre": "Action"},{"name": "Ala Vaikunthapurramuloo", "genre": "Action"},{"name": "Pokiri", "genre": "Action"},{"name": "Okkadu", "genre": "Action"},{"name": "Businessman", "genre": "Action"},{"name": "Janatha Garage", "genre": "Action"},{"name": "Temper", "genre": "Action"},{"name": "Dookudu", "genre": "Action"},{"name": "Mirchi", "genre": "Action"},{"name": "Magadheera", "genre": "Action"},{"name": "Sye", "genre": "Action"},{"name": "Vikramarkudu", "genre": "Action"},{"name": "Sita Ramam", "genre": "Romance"},{"name": "Bommarillu", "genre": "Romance"},{"name": "Darling", "genre": "Romance"},{"name": "Radhe Shyam", "genre": "Romance"},{"name": "Fidaa", "genre": "Romance"},{"name": "Preminchukundam Raa", "genre": "Romance"},{"name": "Ye Maaya Chesave", "genre": "Romance"},{"name": "Majili", "genre": "Romance"},{"name": "Tholi Prema", "genre": "Romance"},{"name": "Kushi", "genre": "Romance"},{"name": "Orange", "genre": "Romance"},
{"name": "Oohalu Gusagusalade", "genre": "Romance"},{"name": "Pelli Choopulu", "genre": "Romance"},{"name": "Geetha Govindam", "genre": "Romance"},{"name": "Yamudiki Mogudu", "genre": "Comedy"},{"name": "Nuvvu Naaku Nachav", "genre": "Comedy"},{"name": "Jathi Ratnalu", "genre": "Comedy"},{"name": "Sankranthiki Vasthunnam", "genre": "Comedy"},{"name": "F2", "genre": "Comedy"},{"name": "F3", "genre": "Comedy"},{"name": "Mana Shankara Vara Prasad Garu", "genre": "Comedy"},{"name": "Jil", "genre": "Comedy"},{"name": "MAD", "genre": "Comedy"},{"name": "Mathu Vadalara", "genre": "Comedy"},{"name": "Pelli Choopulu", "genre": "Comedy"},{"name": "Maryada Ramanna", "genre": "Comedy"},{"name": "Son of Satyamurthy", "genre": "Drama"},{"name": "Jersey", "genre": "Drama"}, {"name": "Mahanati", "genre": "Drama"},{"name": "Sankranthi", "genre": "Drama"},{"name": "Srimanthudu", "genre": "Drama"},  {"name": "Bharat Ane Nenu", "genre": "Drama"},{"name": "Dasara", "genre": "Drama"},{"name": "Devara: Part 1", "genre": "Drama"},{"name": "Middle Class Melodies", "genre": "Drama"},{"name": "Kanchana", "genre": "Horror"},{"name": "Arundhathi", "genre": "Horror"},{"name": "The Raja Saab", "genre": "Horror"},{"name": "Masooda", "genre": "Horror"},{"name": "Prema Katha Chitram", "genre": "Horror"},{"name": "Raju Gari Gadhi", "genre": "Horror"},{"name": "HIT: The Second Case", "genre": "Thriller"},{"name": "HIT: The First Case", "genre": "Thriller"},{"name": "Goodachari", "genre": "Thriller"},{"name": "Evaru", "genre": "Thriller"},{"name": "Agent Sai Srinivasa Athreya", "genre": "Thriller"},{"name": "Karthikeya", "genre": "Thriller"},{"name": "Karthikeya 2", "genre": "Thriller"},{"name": "Brochevarevarura", "genre": "Thriller"},{"name": "Manam", "genre": "Family"},{"name": "Attarintiki Daredi", "genre": "Family"},{"name": "A Aa", "genre": "Family"},{"name": "Shatamanam Bhavati", "genre": "Family"},{"name": "Seethamma Vakitlo Sirimalle Chettu", "genre": "Family"},{"name": "Brindavanam", "genre": "Family"},{"name": "Dhee", "genre": "Family"},{"name": "Bommarillu", "genre": "Family"},{"name": "Malli Malli Idi Rani Roju", "genre": "Family"},{"name": "Nani's Gang Leader", "genre": "Family"}]
lprint()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("     TELUGU MOVIE RECOMMENDATION")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("\nChoose your preferred genre:")
print("1. Action")
print("2. Romance")
print("3. Comedy")
print("4. Drama")
print("5. Horror")
print("6. Thriller")
print("7. Family")
choice = input("\nEnter your choice: ")
if choice == "1":
    preferred_genre = "Action"
elif choice == "2":
    preferred_genre = "Romance"
elif choice == "3":
    preferred_genre = "Comedy"
elif choice == "4":
    preferred_genre = "Drama"
elif choice == "5":
    preferred_genre = "Horror"
elif choice == "6":
    preferred_genre = "Thriller"
elif choice == "7":
    preferred_genre = "Family"
else:
    print("Invalid choice.")
    exit()

print("\nRecommended Movies:")
print("-------------------")

found = False

for movie in movies:
    if movie["genre"] == preferred_genre:
        print("-", movie["name"])
        found = True

if not found:
    print("No movies found.")

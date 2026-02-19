import random

print("🎬 Smart Movie Recommendation System")

name = input("Enter your name: ")
print(f"\nHello {name}! Let's find a movie for you 🍿")

movies = {
    "action": [
        "Avengers", "John Wick", "Mad Max",
        "KGF Chapter 1", "KGF Chapter 2", "War", "Pathaan"
    ],

    "comedy": [
        "Hangover", "The Mask",
        "Hera Pheri", "3 Idiots", "Bhool Bhulaiyaa", "Welcome"
    ],

    "romance": [
        "Titanic", "La La Land",
        "Dilwale Dulhania Le Jayenge", "Kabir Singh", "Yeh Jawaani Hai Deewani"
    ],

    "horror": [
        "The Conjuring", "Insidious",
        "Stree", "Tumbbad", "Raaz"
    ],

    "sci-fi": [
        "Interstellar", "Inception", "The Matrix",
        "Krrish", "Robot (Enthiran)"
    ],

    "thriller": [
        "Se7en", "Shutter Island",
        "Andhadhun", "Drishyam", "Talvar"
    ],

    "drama": [
        "The Shawshank Redemption",
        "Taare Zameen Par", "Dangal", "Chak De India", "Article 15"
    ]
}

while True:
    print("\nAvailable genres:")
    for genre in movies:
        print("-", genre)

    choice = input("\nEnter a genre, type 'random' for surprise, or 'exit' to quit: ").lower()

    if choice == "exit":
        print(f"\nGoodbye {name}! Enjoy your movie time 🎥")
        break

    elif choice == "random":
        genre = random.choice(list(movies.keys()))
        print(f"\n🎲 Random genre selected: {genre}")
        print("Recommended movies:")
        for movie in movies[genre]:
            print("-", movie)

    elif choice in movies:
        print("\nRecommended movies:")
        for movie in movies[choice]:
            print("-", movie)

        another = input("\nWant a random pick from this genre? (yes/no): ").lower()
        if another == "yes":
            print("🎥 Try watching:", random.choice(movies[choice]))

    else:
        print("❌ Genre not found. Please try again.")

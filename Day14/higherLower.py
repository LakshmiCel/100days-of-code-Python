import random
# from peopleDetails import celebrities

celebrities = [
    {
        "name": "Kim Kardashian",
        "age": 43,
        "occupation": "Reality TV Star and Businesswoman",
        "net_worth": 1.2e9,
        "country": "USA",
        "famous_for": "Reality TV and KKW Beauty",
        "instagram_followers": 400000000,
        "twitter_followers": 70000000,
    },
    {
        "name": "Selena Gomez",
        "age": 31,
        "occupation": "Singer and Actress",
        "net_worth": 80e6,
        "country": "USA",
        "famous_for": "Music and acting career",
        "instagram_followers": 400000000,
        "twitter_followers": 65000000,
    },
    {
        "name": "Justin Bieber",
        "age": 29,
        "occupation": "Singer",
        "net_worth": 300e6,
        "country": "Canada",
        "famous_for": "Pop music and global tours",
        "instagram_followers": 300000000,
        "twitter_followers": 120000000,
    },
    {
        "name": "Kanye West",
        "age": 46,
        "occupation": "Rapper and Fashion Designer",
        "net_worth": 2e9,
        "country": "USA",
        "famous_for": "Music and Yeezy brand",
        "instagram_followers": 30000000,
        "twitter_followers": 30000000,
    },
    {
        "name": "Adele",
        "age": 35,
        "occupation": "Singer-Songwriter",
        "net_worth": 220e6,
        "country": "UK",
        "famous_for": "Music and record-breaking albums",
        "instagram_followers": 40000000,
        "twitter_followers": 20000000,
    },
    {
        "name": "Benedict Cumberbatch",
        "age": 47,
        "occupation": "Actor",
        "net_worth": 40e6,
        "country": "UK",
        "famous_for": "Sherlock Holmes and Doctor Strange",
        "instagram_followers": 10000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Rami Malek",
        "age": 42,
        "occupation": "Actor",
        "net_worth": 20e6,
        "country": "USA",
        "famous_for": "Bohemian Rhapsody and Mr. Robot",
        "instagram_followers": 10000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Leonardo DiCaprio",
        "age": 48,
        "occupation": "Actor and Environmental Activist",
        "net_worth": 260e6,
        "country": "USA",
        "famous_for": "Titanic and environmental activism",
        "instagram_followers": 50000000,
        "twitter_followers": 20000000,
    },
    {
        "name": "Jennifer Aniston",
        "age": 54,
        "occupation": "Actress and Producer",
        "net_worth": 320e6,
        "country": "USA",
        "famous_for": "Friends and various films",
        "instagram_followers": 40000000,
        "twitter_followers": 20000000,
    },
    {
        "name": "Robert Pattinson",
        "age": 37,
        "occupation": "Actor",
        "net_worth": 100e6,
        "country": "UK",
        "famous_for": "Twilight series and The Batman",
        "instagram_followers": 20000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Elon Musk",
        "age": 52,
        "occupation": "Entrepreneur",
        "net_worth": 230e9,
        "country": "USA",
        "famous_for": "CEO of SpaceX and Tesla",
        "instagram_followers": 10000000,
        "twitter_followers": 120000000,
    },
    {
        "name": "Taylor Swift",
        "age": 33,
        "occupation": "Singer-Songwriter",
        "net_worth": 400e6,
        "country": "USA",
        "famous_for": "Music and philanthropy",
        "instagram_followers": 200000000,
        "twitter_followers": 90000000,
    },
    {
        "name": "Cristiano Ronaldo",
        "age": 38,
        "occupation": "Professional Footballer",
        "net_worth": 500e6,
        "country": "Portugal",
        "famous_for": "Football and endorsements",
        "instagram_followers": 500000000,
        "twitter_followers": 100000000,
    },
    {
        "name": "Emma Watson",
        "age": 33,
        "occupation": "Actress and Activist",
        "net_worth": 85e6,
        "country": "UK",
        "famous_for": "Harry Potter series and activism",
        "instagram_followers": 60000000,
        "twitter_followers": 30000000,
    },
    {
        "name": "Dwayne Johnson",
        "age": 51,
        "occupation": "Actor and Former Professional Wrestler",
        "net_worth": 320e6,
        "country": "USA",
        "famous_for": "Movies and wrestling career",
        "instagram_followers": 300000000,
        "twitter_followers": 150000000,
    },
    {
        "name": "Beyoncé",
        "age": 42,
        "occupation": "Singer and Actress",
        "net_worth": 500e6,
        "country": "USA",
        "famous_for": "Music and cultural influence",
        "instagram_followers": 300000000,
        "twitter_followers": 20000000,
    },
    {
        "name": "Lionel Messi",
        "age": 36,
        "occupation": "Professional Footballer",
        "net_worth": 600e6,
        "country": "Argentina",
        "famous_for": "Football and endorsements",
        "instagram_followers": 500000000,
        "twitter_followers": 100000000,
    },
    {
        "name": "Ariana Grande",
        "age": 30,
        "occupation": "Singer and Actress",
        "net_worth": 180e6,
        "country": "USA",
        "famous_for": "Music and acting career",
        "instagram_followers": 350000000,
        "twitter_followers": 85000000,
    },
    {
        "name": "Rihanna",
        "age": 35,
        "occupation": "Singer and Businesswoman",
        "net_worth": 1500e6,
        "country": "Barbados",
        "famous_for": "Music and Fenty Beauty",
        "instagram_followers": 150000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Kylie Jenner",
        "age": 26,
        "occupation": "Reality TV Star and Businesswoman",
        "net_worth": 700e6,
        "country": "USA",
        "famous_for": "Kylie Cosmetics and reality TV",
        "instagram_followers": 400000000,
        "twitter_followers": 30000000,
    },
    {
        "name": "Oprah Winfrey",
        "age": 69,
        "occupation": "Media Executive and Philanthropist",
        "net_worth": 3000e6,
        "country": "USA",
        "famous_for": "The Oprah Winfrey Show and philanthropy",
        "instagram_followers": 40000000,
        "twitter_followers": 20000000,
    },
    {
        "name": "Bill Gates",
        "age": 67,
        "occupation": "Business Magnate and Philanthropist",
        "net_worth": 120e9,
        "country": "USA",
        "famous_for": "Co-founder of Microsoft and philanthropy",
        "instagram_followers": 20000000,
        "twitter_followers": 60000000,
    },
    {
        "name": "Mark Zuckerberg",
        "age": 39,
        "occupation": "Co-founder and CEO of Meta Platforms",
        "net_worth": 120e9,
        "country": "USA",
        "famous_for": "Facebook and social media innovations",
        "instagram_followers": 10000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Greta Thunberg",
        "age": 20,
        "occupation": "Environmental Activist",
        "net_worth": 1e6,
        "country": "Sweden",
        "famous_for": "Climate activism",
        "instagram_followers": 1000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Jack Ma",
        "age": 59,
        "occupation": "Business Magnate and Philanthropist",
        "net_worth": 40e9,
        "country": "China",
        "famous_for": "Co-founder of Alibaba Group",
        "instagram_followers": 1000000,
        "twitter_followers": 2000000,
    },
    {
        "name": "Emma Stone",
        "age": 35,
        "occupation": "Actress",
        "net_worth": 40e6,
        "country": "USA",
        "famous_for": "La La Land and other films",
        "instagram_followers": 30000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Keanu Reeves",
        "age": 59,
        "occupation": "Actor",
        "net_worth": 360e6,
        "country": "Canada",
        "famous_for": "The Matrix series and John Wick",
        "instagram_followers": 10000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Gal Gadot",
        "age": 38,
        "occupation": "Actress and Model",
        "net_worth": 300e6,
        "country": "Israel",
        "famous_for": "Wonder Woman",
        "instagram_followers": 10000000,
        "twitter_followers": 3000000,
    },
    {
        "name": "Margot Robbie",
        "age": 33,
        "occupation": "Actress and Producer",
        "net_worth": 50e6,
        "country": "Australia",
        "famous_for": "The Wolf of Wall Street and Harley Quinn",
        "instagram_followers": 30000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Chris Hemsworth",
        "age": 40,
        "occupation": "Actor",
        "net_worth": 130e6,
        "country": "Australia",
        "famous_for": "Thor in the Marvel Cinematic Universe",
        "instagram_followers": 50000000,
        "twitter_followers": 15000000,
    },
    {
        "name": "Natalie Portman",
        "age": 42,
        "occupation": "Actress and Filmmaker",
        "net_worth": 90e6,
        "country": "USA",
        "famous_for": "Black Swan and activism",
        "instagram_followers": 10000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Robert Downey Jr.",
        "age": 58,
        "occupation": "Actor and Producer",
        "net_worth": 300e6,
        "country": "USA",
        "famous_for": "Iron Man and the Marvel Cinematic Universe",
        "instagram_followers": 5000000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Miley Cyrus",
        "age": 31,
        "occupation": "Singer and Actress",
        "net_worth": 160e6,
        "country": "USA",
        "famous_for": "Music and Hannah Montana",
        "instagram_followers": 200000000,
        "twitter_followers": 45000000,
    },
    {
        "name": "Scarlett Johansson",
        "age": 38,
        "occupation": "Actress and Singer",
        "net_worth": 165e6,
        "country": "USA",
        "famous_for": "Black Widow in the Marvel Cinematic Universe",
        "instagram_followers": 20000000,
        "twitter_followers": 10000000,
    },
    {
        "name": "Tom Hanks",
        "age": 67,
        "occupation": "Actor and Filmmaker",
        "net_worth": 400e6,
        "country": "USA",
        "famous_for": "Forrest Gump and Saving Private Ryan",
        "instagram_followers": 20000000,
        "twitter_followers": 5000000,
    },
    {
        "name": "Jennifer Lawrence",
        "age": 33,
        "occupation": "Actress",
        "net_worth": 160e6,
        "country": "USA",
        "famous_for": "The Hunger Games series and Silver Linings Playbook",
        "instagram_followers": 20000000,
        "twitter_followers": 10000000,
    },
]


def display_welcome_message():
    print("Welcome to the Higher or Lower game!")
    print("Try to guess the instagram followers or twitter followers for celebrities.")
    print("You can type 'exit' to quit the game at any time.")

def random_celebrity():
    index = random.randint(0, len(celebrities) - 1)
    return celebrities[index]

def print_celebrity(celebrity):
    print(f"{celebrity['name']} from {celebrity['country']} famous for {celebrity['famous_for']}")
    print(f"Instagram followers: {celebrity['instagram_followers']}")
    print(f"Twitter followers: {celebrity['twitter_followers']}")

def decide_variation():
    should_choose_insta = random.choice([True, False])
    if should_choose_insta:
        return 'instagram_followers'
    else:
        return 'twitter_followers'

score = 0
display_welcome_message()
start = True
while start:
    celebrity1 = random_celebrity()
    celebrity2 = random_celebrity()

    while celebrity1 == celebrity2:
        celebrity2 = random_celebrity()

    # print(f"{celebrity1['name']} from {celebrity1["country"]} famous for{celebrity1["famous_for"]}")
    print_celebrity(celebrity1)
    print_celebrity(celebrity2)
    decide_variations = decide_variation()
    choice = input(f"Which celebrity has more {decide_variations} followers? ({celebrity1["name"]} or {celebrity2["name"]}) /n /n Enter 1 or 2").strip()
    if choice.lower().strip() == 'exit':
        print("Thanks for playing...")
        exit()
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        continue
    if celebrity1[decide_variations] > celebrity2[decide_variations]:
        if choice == '1':
            print(f"Correct! {celebrity1['name']} has more {decide_variations} followers.")
            score += 1
        else:
            print(f"Ooops! {celebrity2['name']} has more {decide_variations} followers.")
            start = False
    else:
        if choice == '2':
            print(f"Correct! {celebrity2['name']} has more {decide_variations} followers.")
            score += 1
        else:
            print(f"Ooops! {celebrity1['name']} has more {decide_variations} followers.")
            start = False
    print(f"Your current score is: {score}")
    
    
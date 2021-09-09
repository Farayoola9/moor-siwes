
print("Welcome to our cinema :)\nChoose the movie of your choice\nMake payment and ensure to collect your sovenuir\nDo not forget to check your center name\n")
print("""
Availble Movies!!!
1. Sugar Rush
2. Justice League
3. The Unholy
""")
cinema_details = {
    "sugar rush" : {
        "movie_time" : "2pm - 4pm",
        "movie_director" : "Sanni Uswat",
        "movie_center" : "Viva",
        "movie_souvenir" : "Popcorn and an orange juice",
        "movie_ticketamount" : "#2000"
        },

    "justice league" : {
        "movie_time" : "9am - 12pm",
        "movie_director" : "Odeh Peter",
        "movie_center" : "Ace mall",
        "movie_souvenir" : "Meat pie with cold stone ice cream",
        "movie_ticketamount" : "#2500"
        },

    "the unholy" : {
        "movie_time" : "9pm - 1am",
        "movie_director" : "Olaniran Elijah",
        "movie_center" : "Ventura",
        "movie_souvenir" : "Biscuits, chicken pie and an apple juice",
        "movie_ticketamount" : "#3500"
        }
}

print("\nThanks for patronizing us\Enjoy your movie\n") 

while True:
    movie_name = input("Enter Movie of your choice: ").lower()
    movie_title = [cinema_details[i] for i in cinema_details if i in movie_name]
    if len (movie_title) > 0:
        
        print(movie_title[0])
        break
    else:
        print("Not Available :(")

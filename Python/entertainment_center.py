import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","Story of a boy","hi","hi")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","Marine on planet","hi","hi")
#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

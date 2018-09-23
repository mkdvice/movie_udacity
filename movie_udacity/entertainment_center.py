import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/Movie_poster_toy_story.jpg/250px-Movie_poster_toy_story.jpg',
                        'https://www.youtube.com/watch?v=ZZv1vki4ou4')
#print(toy_story.storyline)

avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = media.Movie('School of Rock', 'Story line',
                             'https://upload.wikimedia.org/wikipedia/pt/thumb/1/1b/Schoolrockposter.jpg/210px-Schoolrockposter.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille', 'Storyline',
                                'https://upload.wikimedia.org/wikipedia/pt/thumb/8/82/Ratatouille_p%C3%B4ster.jpg/250px-Ratatouille_p%C3%B4ster.jpg',
                                'https://www.youtube.com/watch?v=uVeNEbh3A4U')

hobbit = media.Movie('The Hobbit', 'Storyline',
                     'https://vignette.wikia.nocookie.net/terramedia/images/f/fe/Hobbit_jornadainesperada_46.jpg/revision/latest?cb=20141210190655',
                     'https://www.youtube.com/watch?v=JTSoD4BBCJc')

movies = [toy_story, avatar, school_of_rock, ratatouille, hobbit]
fresh_tomatoes.open_movies_page(movies)
import movie
import fresh_tomatoes

incredible = movie.Movie('The Incredibles',
                         'Forced to adopt a civilian identity and stuck in a white-collar job, Mr Incredible itches to get back into action. When he is lured into a trap by the evil Syndrome, his family contrives to save him.',
                         'https://images-na.ssl-images-amazon.com/images/I/81Q7MV1OgXL._RI_.jpg',
                         'https://www.youtube.com/watch?v=sJCjKQQOqT0')

lincoln = movie.Movie('Lincoln',
                      'Abraham Lincoln uses his powers as the president of the United States of America as he strives to abolish slavery and reunite his country during the Civil War.',
                      'http://www.gstatic.com/tv/thumb/v22vodart/9087990/p9087990_v_v8_ab.jpg',
                      'https://www.youtube.com/watch?v=KJVuqYkI2jQ')

ice_age = movie.Movie('Ice Age',
                      'Manny the mammoth, Sid the loquacious sloth, and Diego the sabre-toothed tiger go on a comical quest to return a human baby back to his father, across a world on the brink of an ice age.',
                      'https://s1.thcdn.com/productimg/0/600/600/53/10665753-1362503719-312140.jpg',
                      'https://www.youtube.com/watch?v=SOFC3h7oZPU')

ratatouille = movie.Movie('Ratatouille',
                          "Remy, a rat, aspires to become a renowned French chef. He doesn't realise that people despise rodents and will never enjoy a meal cooked by him.",
                          'https://media-frontend.tweakwise.com/data/ako/700x700/380707.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')

dark_knight = movie.Movie('The Dark Knight',
                          'With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.',
                          'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
                          'https://www.youtube.com/watch?v=EXeTwQWrcwY')

avenger4 = movie.Movie('Avenger: Infinity War',
                       'Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.',
                       'https://www.canalolympia.com/wp-content/uploads/2018/04/AVENGER-BD.jpg',
                       'https://www.youtube.com/watch?v=6ZfuNTqbHE8&t=18s')

movies_list = [incredible, lincoln, ice_age, ratatouille, dark_knight, avenger4]

# pass array in open_movies_function
fresh_tomatoes.open_movies_page(movies_list)
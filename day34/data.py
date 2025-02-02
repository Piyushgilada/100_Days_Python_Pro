import requests

parameter={'amount':10,'type':'boolean'}
response=requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean',params=parameter)
response.raise_for_status()
data=response.json()
question_data=data['results']

# question_data = [
#     {
#       "type": "boolean",
#       "difficulty": "hard",
#       "category": "Entertainment: Video Games",
#       "question": "In &quot;Minecraft&quot;, gold tools are faster than diamond tools.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "Entertainment: Books",
#       "question": "The book 1984 was published in 1949.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Haggis is traditionally ate on Burns Night.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "Mythology",
#       "question": "According to Greek Mythology, Atlas was an Olympian God.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "History",
#       "question": "The Korean War ended in 1953 without any ceasefire.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "Entertainment: Japanese Anime &amp; Manga",
#       "question": "In the &quot;Melancholy of Haruhi Suzumiya&quot; series, the narrator goes by the nickname Kyon.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Entertainment: Video Games",
#       "question": "In Rocket League, you can play Basketball.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "hard",
#       "category": "General Knowledge",
#       "question": "This is the correct spelling of &quot;Supercalifragilisticexpialidocious&quot;.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "Animals",
#       "question": "&quot;Kamea,&quot; the Gilbertese Islander word for dog, is derived from the English phrase &quot;Come here!&quot;",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "easy",
#       "category": "General Knowledge",
#       "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     }
#   ]
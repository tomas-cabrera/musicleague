import itertools

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator
from scipy.interpolate import CubicSpline

###############################################################################

# Indices
players = [
    "James Carzon",
    "tworandomnames",
    "22733wiag5lbm6rbw3dwf4aja",
    "Steven",
    "Nick King",
    "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability",
    "Rowan",
    "brianmck12",
    "fionajeon",
    "Em Johnson",
    "CyberGrifter",
    "Rinu",
    "Marianna Orth",
    "Andrew Polaski",
]
rounds = [
    "Clowncore",
    "A Rip-Roaring Road Rager",
    "A Midsummer Night's Stream",
    "Songs to Send Your FBI Agent",
    "Dance Dance Evolution!",
    "A Dot in the Shark",
    "Red, White, Black, and Blue",
    "Pub Hubbub",
    "🔥 Songs for Biggest Spleen 🔥",
    "Villain Arc",
    "Undercover Mob",
    "...The Last of the Groomsmaids!",
]

# Scores
dict_scores = dict(zip(players, [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]))
dict_scores["James Carzon"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": np.nan,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 1,
            "brianmck12": 3,
            "fionajeon": 1,
            "Em Johnson": 2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Clowncore"] = {
            "James Carzon": -1,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": 3,
            "brianmck12": 1,
            "fionajeon": 1,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Clowncore"] = {
            "James Carzon": -2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -5,
            "Rowan": -4,
            "brianmck12": -2,
            "fionajeon": 2,
            "Em Johnson": -3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Clowncore"] = {
            "James Carzon": -2,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 6,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 6,
            "Rowan": -1,
            "brianmck12": -3,
            "fionajeon": -2,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Clowncore"] = {
            "James Carzon": 2,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": np.nan,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 4,
            "brianmck12": 3,
            "fionajeon": 3,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Clowncore"] = {
            "James Carzon": 2,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": np.nan,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": np.nan,
            "brianmck12": 2,
            "fionajeon": 3,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Clowncore"] = {
            "James Carzon": 5,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": np.nan,
            "Nick King": -3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": -3,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Clowncore"] = {
            "James Carzon": 5,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": np.nan,
            "Nick King": 5,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 7,
            "brianmck12": 6,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Clowncore"] = {
            "James Carzon": 1,
            "tworandomnames": 5,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": np.nan,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": 0,
            "brianmck12": 0,
            "fionajeon": 5,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Clowncore"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 1,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 5,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": 3,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": 1,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 7,
            "Rowan": 5,
            "brianmck12": 0,
            "fionajeon": 2,
            "Em Johnson": 0,
            "CyberGrifter": 3,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": 5,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 6,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": 0,
            "brianmck12": 0,
            "fionajeon": 1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": -2,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": -2,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": 10,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": -1,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 1,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -2,
            "brianmck12": np.nan,
            "fionajeon": 1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": -2,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": -2,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": np.nan,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 1,
            "Nick King": -1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": 4,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": -3,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": 2,
            "brianmck12": np.nan,
            "fionajeon": -3,
            "Em Johnson": np.nan,
            "CyberGrifter": -5,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": 1,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 2,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": 7,
            "brianmck12": np.nan,
            "fionajeon": 1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["A Rip-Roaring Road Rager"] = {
            "James Carzon": 2,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 3,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": np.nan,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 4,
            "Nick King": 5,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 15,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["A Midsummer Night's Stream"] = {
            "James Carzon": 2,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": -2,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": 7,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["A Midsummer Night's Stream"] = {
            "James Carzon": 4,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": -1,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -3,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["A Midsummer Night's Stream"] = {
            "James Carzon": 2,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": np.nan,
            "Nick King": -1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["A Midsummer Night's Stream"] = {
            "James Carzon": 2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 2,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["A Midsummer Night's Stream"] = {
            "James Carzon": -2,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": -2,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 7,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["A Midsummer Night's Stream"] = {
            "James Carzon": -2,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 4,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": -3,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["A Midsummer Night's Stream"] = {
            "James Carzon": 5,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": 1,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": -3,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["A Midsummer Night's Stream"] = {
            "James Carzon": -1,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 4,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["A Midsummer Night's Stream"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": -2,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 3,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": -2,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": 3,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": 1,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 1,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 7,
            "brianmck12": 2,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": 2,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": np.nan,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": -1,
            "brianmck12": 10,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": -2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": -3,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": -2,
            "brianmck12": -2,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": 3,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 1,
            "Nick King": -1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 4,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": -1,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": 2,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 5,
            "Rowan": np.nan,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": 4,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": 6,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": 5,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 2,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -1,
            "brianmck12": -3,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Songs to Send Your FBI Agent"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": -2,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -1,
            "brianmck12": -4,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Dance Dance Evolution!"] = {
            "James Carzon": -1,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 2,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -1,
            "brianmck12": -1,
            "fionajeon": np.nan,
            "Em Johnson": 5,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Dance Dance Evolution!"] = {
            "James Carzon": -2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 2,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 4,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Dance Dance Evolution!"] = {
            "James Carzon": 1,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 6,
            "Steven": np.nan,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": -1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Dance Dance Evolution!"] = {
            "James Carzon": -2,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": -3,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": 6,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Dance Dance Evolution!"] = {
            "James Carzon": 5,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 3,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 4,
            "brianmck12": 2,
            "fionajeon": np.nan,
            "Em Johnson": 2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Dance Dance Evolution!"] = {
            "James Carzon": 3,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": 5,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": np.nan,
            "brianmck12": 3,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Dance Dance Evolution!"] = {
            "James Carzon": 4,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": 1,
            "Nick King": -3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": -2,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Dance Dance Evolution!"] = {
            "James Carzon": 2,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 2,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -4,
            "Rowan": -1,
            "brianmck12": 8,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Dance Dance Evolution!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 1,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": 6,
            "brianmck12": 1,
            "fionajeon": -1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["A Dot in the Shark"] = {
            "James Carzon": 4,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 1,
            "Nick King": 5,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -3,
            "Rowan": -1,
            "brianmck12": -2,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["A Dot in the Shark"] = {
            "James Carzon": -2,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 1,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": 3,
            "brianmck12": 0,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["A Dot in the Shark"] = {
            "James Carzon": -3,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 4,
            "brianmck12": 6,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["A Dot in the Shark"] = {
            "James Carzon": 1,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 5,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -2,
            "brianmck12": -3,
            "fionajeon": 3,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["A Dot in the Shark"] = {
            "James Carzon": 2,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": -4,
            "Steven": -5,
            "Nick King": -3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 2,
            "brianmck12": 3,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["A Dot in the Shark"] = {
            "James Carzon": 0,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 5,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": np.nan,
            "brianmck12": 2,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["A Dot in the Shark"] = {
            "James Carzon": 5,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": 1,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["A Dot in the Shark"] = {
            "James Carzon": 3,
            "tworandomnames": 5,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 1,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": -1,
            "brianmck12": 3,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["A Dot in the Shark"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Red, White, Black, and Blue"] = {
            "James Carzon": np.nan,
            "tworandomnames": 7,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 2,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": -1,
            "brianmck12": 2,
            "fionajeon": 1,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Red, White, Black, and Blue"] = {
            "James Carzon": 2,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": 3,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 5,
            "brianmck12": 9,
            "fionajeon": 6,
            "Em Johnson": 2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Red, White, Black, and Blue"] = {
            "James Carzon": 4,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 3,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": np.nan,
            "brianmck12": -1,
            "fionajeon": 2,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Red, White, Black, and Blue"] = {
            "James Carzon": -2,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": np.nan,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": 1,
            "brianmck12": 2,
            "fionajeon": 4,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Red, White, Black, and Blue"] = {
            "James Carzon": 1,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": 1,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": 4,
            "brianmck12": -4,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Red, White, Black, and Blue"] = {
            "James Carzon": -2,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": -2,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 4,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Red, White, Black, and Blue"] = {
            "James Carzon": 3,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": 1,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -4,
            "Rowan": np.nan,
            "brianmck12": 0,
            "fionajeon": -3,
            "Em Johnson": -3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Red, White, Black, and Blue"] = {
            "James Carzon": 1,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": 2,
            "Nick King": -3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -2,
            "brianmck12": np.nan,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Red, White, Black, and Blue"] = {
            "James Carzon": 4,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": 3,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Red, White, Black, and Blue"] = {
            "James Carzon": -1,
            "tworandomnames": 0,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": -3,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": -2,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Red, White, Black, and Blue"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Red, White, Black, and Blue"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Red, White, Black, and Blue"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Red, White, Black, and Blue"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Pub Hubbub"] = {
            "James Carzon": np.nan,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": -2,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": np.nan,
            "brianmck12": 5,
            "fionajeon": -1,
            "Em Johnson": 1,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Pub Hubbub"] = {
            "James Carzon": -1,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": 3,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": np.nan,
            "brianmck12": 1,
            "fionajeon": 4,
            "Em Johnson": 2,
            "CyberGrifter": 2,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Pub Hubbub"] = {
            "James Carzon": 2,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 5,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": -1,
            "brianmck12": 1,
            "fionajeon": 1,
            "Em Johnson": 4,
            "CyberGrifter": 2,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Pub Hubbub"] = {
            "James Carzon": 0,
            "tworandomnames": 0,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": 9,
            "brianmck12": 1,
            "fionajeon": 1,
            "Em Johnson": -1,
            "CyberGrifter": 3,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Pub Hubbub"] = {
            "James Carzon": -1,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": 1,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -1,
            "brianmck12": 0,
            "fionajeon": 1,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Pub Hubbub"] = {
            "James Carzon": 1,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 3,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": -1,
            "Em Johnson": 1,
            "CyberGrifter": 2,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Pub Hubbub"] = {
            "James Carzon": 3,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": np.nan,
            "brianmck12": 0,
            "fionajeon": -2,
            "Em Johnson": 1,
            "CyberGrifter": 2,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Pub Hubbub"] = {
            "James Carzon": 4,
            "tworandomnames": 6,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": np.nan,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": 1,
            "Em Johnson": -2,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Pub Hubbub"] = {
            "James Carzon": -1,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": -2,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": np.nan,
            "brianmck12": -5,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": -5,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Pub Hubbub"] = {
            "James Carzon": 5,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 1,
            "Nick King": -1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": 5,
            "brianmck12": 6,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Pub Hubbub"] = {
            "James Carzon": 0,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": -1,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 1,
            "brianmck12": 1,
            "fionajeon": 3,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Pub Hubbub"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Pub Hubbub"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Pub Hubbub"] = {
            "James Carzon": -2,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 2,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": -1,
            "Em Johnson": 2,
            "CyberGrifter": 1,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": -2,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 3,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": 4,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": -3,
            "Nick King": -3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": 6,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": -2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 2,
            "Nick King": 6,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -3,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 4,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": 5,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": np.nan,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 5,
            "Rowan": 0,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": 3,
            "tworandomnames": 7,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": 3,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 5,
            "Rowan": 5,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": -3,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": 3,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -5,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": 1,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": 5,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": -3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": 2,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": 2,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 1,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["🔥 Songs for Biggest Spleen 🔥"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Villain Arc"] = {
            "James Carzon": np.nan,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": -2,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": np.nan,
            "brianmck12": 4,
            "fionajeon": -2,
            "Em Johnson": 2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Villain Arc"] = {
            "James Carzon": -1,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": 1,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": -3,
            "brianmck12": -3,
            "fionajeon": 2,
            "Em Johnson": -1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Villain Arc"] = {
            "James Carzon": 3,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 3,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": 2,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": 1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Villain Arc"] = {
            "James Carzon": 5,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": np.nan,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -3,
            "Rowan": np.nan,
            "brianmck12": 10,
            "fionajeon": -2,
            "Em Johnson": -1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Villain Arc"] = {
            "James Carzon": 0,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 2,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 6,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": -1,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Villain Arc"] = {
            "James Carzon": -2,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": 2,
            "Nick King": -2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -2,
            "brianmck12": 1,
            "fionajeon": np.nan,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Villain Arc"] = {
            "James Carzon": 0,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": -1,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Villain Arc"] = {
            "James Carzon": 4,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -1,
            "Steven": 2,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 0,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Villain Arc"] = {
            "James Carzon": 2,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": -2,
            "Nick King": 2,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 1,
            "Rowan": 1,
            "brianmck12": -2,
            "fionajeon": np.nan,
            "Em Johnson": -2,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Villain Arc"] = {
            "James Carzon": -2,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": 2,
            "Nick King": -1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": 2,
            "brianmck12": np.nan,
            "fionajeon": -1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Villain Arc"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Villain Arc"] = {
            "James Carzon": 1,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": 3,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 4,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": 3,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Villain Arc"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Villain Arc"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": 6,
            "22733wiag5lbm6rbw3dwf4aja": 1,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 8,
            "Rowan": 4,
            "brianmck12": -5,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["Undercover Mob"] = {
            "James Carzon": 7,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -1,
            "brianmck12": 0,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["Undercover Mob"] = {
            "James Carzon": -1,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 0,
            "brianmck12": 0,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["Undercover Mob"] = {
            "James Carzon": -3,
            "tworandomnames": 5,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 11,
            "brianmck12": 0,
            "fionajeon": -1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["Undercover Mob"] = {
            "James Carzon": -1,
            "tworandomnames": 3,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -1,
            "brianmck12": 0,
            "fionajeon": 5,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["Undercover Mob"] = {
            "James Carzon": 0,
            "tworandomnames": -1,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -1,
            "brianmck12": 0,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["Undercover Mob"] = {
            "James Carzon": 6,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 3,
            "Rowan": np.nan,
            "brianmck12": 0,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["Undercover Mob"] = {
            "James Carzon": 2,
            "tworandomnames": 0,
            "22733wiag5lbm6rbw3dwf4aja": 2,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 0,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": 2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["Undercover Mob"] = {
            "James Carzon": 0,
            "tworandomnames": 1,
            "22733wiag5lbm6rbw3dwf4aja": 0,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -1,
            "Rowan": -1,
            "brianmck12": 15,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["Undercover Mob"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["James Carzon"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": -3,
            "Steven": np.nan,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -3,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": 4,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["tworandomnames"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": 4,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": np.nan,
            "Nick King": -5,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 5,
            "Rowan": -1,
            "brianmck12": np.nan,
            "fionajeon": 7,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["22733wiag5lbm6rbw3dwf4aja"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": 4,
            "tworandomnames": 5,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": 1,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 2,
            "brianmck12": np.nan,
            "fionajeon": -3,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Steven"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Nick King"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": 4,
            "tworandomnames": 2,
            "22733wiag5lbm6rbw3dwf4aja": 4,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 4,
            "Rowan": 5,
            "brianmck12": np.nan,
            "fionajeon": -2,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": 3,
            "tworandomnames": -3,
            "22733wiag5lbm6rbw3dwf4aja": 3,
            "Steven": np.nan,
            "Nick King": 4,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": -3,
            "brianmck12": np.nan,
            "fionajeon": 1,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rowan"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": -3,
            "tworandomnames": 4,
            "22733wiag5lbm6rbw3dwf4aja": -2,
            "Steven": np.nan,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": 2,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": 3,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["brianmck12"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["fionajeon"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": -2,
            "tworandomnames": -2,
            "22733wiag5lbm6rbw3dwf4aja": 5,
            "Steven": np.nan,
            "Nick King": 3,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": -2,
            "Rowan": 8,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Em Johnson"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["CyberGrifter"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Rinu"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Marianna Orth"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}
dict_scores["Andrew Polaski"]["...The Last of the Groomsmaids!"] = {
            "James Carzon": np.nan,
            "tworandomnames": np.nan,
            "22733wiag5lbm6rbw3dwf4aja": np.nan,
            "Steven": np.nan,
            "Nick King": np.nan,
            "when questioned should i become a prisoner of war, i am required to give artist, song and album title. i will avoid answering further questions to the utmost of my ability": np.nan,
            "Rowan": np.nan,
            "brianmck12": np.nan,
            "fionajeon": np.nan,
            "Em Johnson": np.nan,
            "CyberGrifter": np.nan,
            "Rinu": np.nan,
            "Marianna Orth": np.nan,
            "Andrew Polaski": np.nan,
}

# Build dataframe
df_multiindex = pd.MultiIndex.from_product([players, rounds])
df_songs = pd.DataFrame(index=df_multiindex)
df_scores = pd.DataFrame(index=df_multiindex, columns=players)
dict_scores = {(p, r): dict_scores[p][r] for p in dict_scores.keys() for r in dict_scores[p].keys()}
df_scores = pd.DataFrame(list(dict_scores.values()), index=pd.MultiIndex.from_tuples(dict_scores.keys()))

# Save and reload
df_scores.to_csv("df_scores.csv")
print(df_scores)
df_scores = pd.read_csv("df_scores.csv", index_col=[0,1])
print(df_scores)

###############################################################################
###############################################################################
########                            Figures                            ########
###############################################################################
###############################################################################

def make_fig_ax(kw_figure={}, kw_subplot={}):
    fig = plt.figure(**kw_figure)
    ax = fig.subplots(**kw_subplot)    
    return fig, ax

# Pick colors
cmap = mpl.cm.gist_rainbow
pcolors = cmap(np.linspace(0, 1, len(players)))
rcolors = cmap(np.linspace(0, 1, len(rounds)))
markers = [
    "o",
    "v",
    "^",
    "<",
    ">",
    "s",
    "p",
    "P",
    "*",
    "H",
    "X",
    "d",
    "1",
    "2",
    "3",
    "4"
]

##############################
###  Roundwise histograms  ###
##############################

def histogram_roundwise(r, df=df_scores, bins=np.arange(-7, 17)):
    """Make a plot stacking the voting distribution histograms for the round for each player

    Parameters
    ----------
    r : _type_
        _description_
    """

    # Setup figure
    fig, ax = make_fig_ax()

    # Iterate over players
    for pi, p in enumerate(df.index.get_level_values(0).unique()):
        # Fetch data
        data = df.loc[p,r].dropna()

        # Continue if there are non-nans
        if len(data) > 0:
            # Generate histogram
            counts, _ = np.histogram(data, bins=bins)

            # Interpolate to make pretty
            cs = CubicSpline(bins[:-1], counts)
            x = np.linspace(min(bins), max(bins), 250)
            y = cs(x)

            # Plot
            ax.plot(
                bins[:-1],
                counts,
                linewidth=0,
                marker=markers[pi],
                color=pcolors[pi],
            )
            ax.plot(
                x,
                y,
                label=p[:9],
                color=pcolors[pi],
            )

    # Format
    ax.legend(loc="upper right", frameon=False)
    ax.set_title(r)
    ax.set_xlim(-5,15)
    ax.set_ylim(-1,5.5)
    ax.set_xlabel("Number of votes")
    
    # Save
    plt.tight_layout()
    fig.savefig(f"plots/histogram_roundwise_{r}.png")
    plt.close()

for r in rounds:
    histogram_roundwise(r)

##############################
### Playerwise histograms  ###
##############################

def histogram_playerwise(p, df=df_scores, bins=np.arange(-7, 17)):
    """Make a plot stacking the voting distribution histograms for the round for each player

    Parameters
    ----------
    p : _type_
        _description_
    """

    # Setup figure
    fig, ax = make_fig_ax()

    # Iterate over rounds 
    for ri, r in enumerate(df.index.get_level_values(1).unique()):
        # Fetch data
        data = df.loc[p,r].dropna()

        # Continue if there are non-nans
        if len(data) > 0:
            # Generate histogram
            counts, _ = np.histogram(data, bins=bins)

            # Interpolate to make pretty
            cs = CubicSpline(bins[:-1], counts)
            x = np.linspace(min(bins), max(bins), 250)
            y = cs(x)

            # Plot
            ax.plot(
                bins[:-1],
                counts,
                linewidth=0,
                marker=markers[ri],
                color=pcolors[ri],
                label=r[:9],
            )
            ax.plot(
                x,
                y,
                color=pcolors[ri],
            )

    # Format
    ax.legend(loc="upper right", frameon=False)
    ax.set_title(p)
    ax.set_xlim(-5,15)
    ax.set_ylim(-1,5.5)
    ax.set_xlabel("Number of votes")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Save
    plt.tight_layout()
    fig.savefig(f"plots/histogram_playerwise_{p}.png")
    plt.close()

for p in players:
    histogram_playerwise(p)

##############################
### Roundwise 2Dhistograms ###
##############################

def histogram2d_roundwise(r, df=df_scores, bins=np.arange(-5.5, 16.5)):
    """Make a plot stacking the voting distribution histograms for the round for each player

    Parameters
    ----------
    r : _type_
        _description_
    """

    # Setup figure
    fig, ax = make_fig_ax()

    # Iterate over players
    arr = []
    for pi, p in enumerate(df.index.get_level_values(0).unique()):
        # Fetch data
        data = df.loc[p,r].dropna()

        # Generate histogram
        counts, _ = np.histogram(data, bins=bins)

        # Append to array
        arr.append(counts)

    # Plot
    im = ax.imshow(arr, cmap="plasma", vmax=5, extent=[-5.5,15.5,0,15])

    # Format
    ax.set_title(r)
    ax.set_xlabel("Number of votes")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_yticks(
        np.arange(len(players)) * 15/14,
        labels=[p[:9] for p in players][::-1],
        ha="right",
        va="bottom",
    )
    cb = ax.figure.colorbar(im) 
    cb.set_label("Counts")
    
    # Save
    plt.tight_layout()
    fig.savefig(f"plots/histogram2d_roundwise_{r}.png")
    plt.close()

for r in rounds:
    histogram2d_roundwise(r)

##############################
###Playerwise 2Dhistograms ###
##############################

def histogram2d_playerwise(p, df=df_scores, bins=np.arange(-5.5, 16.5)):
    """Make a plot stacking the voting distribution histograms for the round for each player

    Parameters
    ----------
    r : _type_
        _description_
    """

    # Setup figure
    fig, ax = make_fig_ax()

    # Iterate over players
    arr = []
    for ri, r in enumerate(df.index.get_level_values(1).unique()):
        # Fetch data
        data = df.loc[p,r].dropna()

        # Generate histogram
        counts, _ = np.histogram(data, bins=bins)

        # Append to array
        arr.append(counts)

    # Plot
    im = ax.imshow(arr, cmap="plasma", vmax=5, extent=[-5.5,15.5,0,15])

    # Format
    ax.set_title(p)
    ax.set_xlabel("Number of votes")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_yticks(
        np.arange(len(rounds)) * 15/12,
        labels=rounds[::-1],
        ha="right",
        va="bottom",
    )
    cb = ax.figure.colorbar(im) 
    cb.set_label("Counts")
    
    # Save
    plt.tight_layout()
    fig.savefig(f"plots/histogram2d_playerwise_{p}.png")
    plt.close()

for p in players:
    histogram2d_playerwise(p)


##############################
###     Extreme voting     ###
##############################

# Prints info by players who received points
for p in players:
    print("\t", p)
    print(df_scores.xs(p, level=0).sum(axis=0))
    print(df_scores.xs(p, level=0).abs().sum(axis=0))
    # print(df_scores.xs(p, level=0).sum(axis=1))
    # print(df_scores.xs(p, level=0).abs().sum(axis=1))
# # Prints info by rounds
# for r in rounds:
#     print("\t", r)
#     print(df_scores.xs(r, level=1).sum(axis=0))
#     print(df_scores.xs(r, level=1).abs().sum(axis=0))
#     print(df_scores.xs(r, level=1).sum(axis=1))
# # Prints info by voting players
# for p in players:
#     print("\t", p)
#     print(df_scores.loc[:,p].sum())
#     print(df_scores.loc[:,p].abs().sum())
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.set_page_config(page_title="NFL Playoff Fantasy 2026", layout="centered")
st.title("🏈 2025-26 NFL Playoff Fantasy Football App")
st.markdown("**Full PPR Scoring | One player/DEF per playoff team**")
st.caption("Roster: 2 QB | 4 RB | 4 WR | 2 TE | 1 K | 1 DEF")

# Updated team rosters as of January 1, 2026
teams = {
    "Buffalo Bills": {
        "QB": ["Josh Allen"],
        "RB": ["James Cook", "Ray Davis", "Ty Johnson"],
        "WR": ["Khalil Shakir", "Amari Cooper", "Keon Coleman", "Curtis Samuel", "Mack Hollins"],
        "TE": ["Dalton Kincaid", "Dawson Knox"],
        "K": ["Tyler Bass"],
        "DEF": "Buffalo Bills DEF"
    },
    "Denver Broncos": {
        "QB": ["Bo Nix"],
        "RB": ["Javonte Williams", "Jaleel McLaughlin", "Audric Estime", "Tyler Badie"],
        "WR": ["Courtland Sutton", "Marvin Mims Jr.", "Troy Franklin", "Devaughn Vele"],
        "TE": ["Greg Dulcich", "Lucas Krull"],
        "K": ["Wil Lutz"],
        "DEF": "Denver Broncos DEF"
    },
    "Houston Texans": {
        "QB": ["C.J. Stroud"],
        "RB": ["Joe Mixon", "Woody Marks", "Dameon Pierce", "Nick Chubb", "Dare Ogunbowale", "Jawhar Jordan"],
        "WR": ["Nico Collins", "Tank Dell", "Robert Woods", "John Metchie III"],
        "TE": ["Dalton Schultz", "Cade Stover", "Brevin Jordan"],
        "K": ["Ka'imi Fairbairn"],
        "DEF": "Houston Texans DEF"
    },
    "Jacksonville Jaguars": {
        "QB": ["Trevor Lawrence"],
        "RB": ["Travis Etienne Jr.", "Tank Bigsby", "D'Ernest Johnson"],
        "WR": ["Brian Thomas Jr.", "Gabe Davis", "Christian Kirk"],
        "TE": ["Evan Engram", "Brenton Strange"],
        "K": ["Cam Little"],
        "DEF": "Jacksonville Jaguars DEF"
    },
    "Los Angeles Chargers": {
        "QB": ["Justin Herbert"],
        "RB": ["J.K. Dobbins", "Gus Edwards", "Hassan Haskins", "Kimani Vidal"],
        "WR": ["Ladd McConkey", "Quentin Johnston", "Joshua Palmer", "DJ Chark"],
        "TE": ["Will Dissly", "Stone Smartt", "Hayden Hurst"],
        "K": ["Cameron Dicker"],
        "DEF": "Los Angeles Chargers DEF"
    },
    "New England Patriots": {
        "QB": ["Drake Maye"],
        "RB": ["Rhamondre Stevenson", "Antonio Gibson"],
        "WR": ["Demario Douglas", "Ja'Lynn Polk", "Kayshon Boutte", "DeMario Douglas"],
        "TE": ["Hunter Henry", "Austin Hooper"],
        "K": ["Joey Slye"],
        "DEF": "New England Patriots DEF"
    },
    "Pittsburgh Steelers": {
        "QB": ["Russell Wilson", "Justin Fields"],
        "RB": ["Najee Harris", "Jaylen Warren", "Cordarrelle Patterson"],
        "WR": ["George Pickens", "Calvin Austin III", "Van Jefferson"],
        "TE": ["Pat Freiermuth", "Darnell Washington"],
        "K": ["Chris Boswell"],
        "DEF": "Pittsburgh Steelers DEF"
    },
    "Chicago Bears": {
        "QB": ["Caleb Williams"],
        "RB": ["D'Andre Swift", "Roschon Johnson", "Travis Homer"],
        "WR": ["DJ Moore", "Rome Odunze", "Keenan Allen"],
        "TE": ["Cole Kmet", "Gerald Everett"],
        "K": ["Cairo Santos"],
        "DEF": "Chicago Bears DEF"
    },
    "Green Bay Packers": {
        "QB": ["Jordan Love"],
        "RB": ["Josh Jacobs", "MarShawn Lloyd", "Emanuel Wilson"],
        "WR": ["Jayden Reed", "Christian Watson", "Romeo Doubs", "Dontayvion Wicks"],
        "TE": ["Tucker Kraft", "Luke Musgrave", "Ben Sims"],
        "K": ["Brandon McManus"],
        "DEF": "Green Bay Packers DEF"
    },
    "Los Angeles Rams": {
        "QB": ["Matthew Stafford"],
        "RB": ["Kyren Williams", "Blake Corum", "Ronnie Rivers"],
        "WR": ["Puka Nacua", "Cooper Kupp", "Demarcus Robinson", "Tut Atwell"],
        "TE": ["Tyler Higbee", "Colby Parkinson", "Davis Allen

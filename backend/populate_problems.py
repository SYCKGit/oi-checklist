import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

fields = ["name", "number", "source", "year", "link"]

raw_problems = [
    ## NOI

    # 2007
    ("Gift", 1, "NOIFINAL", 2007, "https://codebreaker.xyz/problem/gift"),
    
    # 2008
    ("Prime", 1, "NOIFINAL", 2008, "https://codebreaker.xyz/problem/nprime"),
    ("LVM", 2, "NOIFINAL", 2008, "https://codebreaker.xyz/problem/lvm"),
    ("Gecko", 3, "NOIFINAL", 2008, "https://codebreaker.xyz/problem/gecko"),
    ("4sum", 4, "NOIFINAL", 2008, "https://codebreaker.xyz/problem/4sum"),
    ("Rank", 5, "NOIFINAL", 2008, "https://codebreaker.xyz/problem/rank"),
    
    # 2009
    ("Xmas", 1, "NOIFINAL", 2009, "https://codebreaker.xyz/problem/xmas"),
    
    # 2010 Selection Test
    ("Chess Islands", 1, "NOIPRELIM", 2010, "https://codebreaker.xyz/problem/chessislands"),
    ("Triangle Sum", 2, "NOIPRELIM", 2010, "https://codebreaker.xyz/problem/trianglesum"),
    # 2010 Finals
    ("Card", 1, "NOIFINAL", 2010, "https://codebreaker.xyz/problem/card"),
    
    # 2011
    ("Change", 1, "NOIFINAL", 2011, "https://codebreaker.xyz/problem/change"),
    ("Paint", 2, "NOIFINAL", 2011, "https://codebreaker.xyz/problem/paint"),
    ("Tour", 3, "NOIFINAL", 2011, "https://codebreaker.xyz/problem/tour"),
    
    # 2012
    ("Mod Sum", 1, "NOIFINAL", 2012, "https://oj.uz/problem/view/NOI12_modsum"),
    ("Pancake", 2, "NOIFINAL", 2012, "https://oj.uz/problem/view/NOI12_pancake"),
    ("Forensic", 3, "NOIFINAL", 2012, "https://oj.uz/problem/view/NOI12_forensic"),
    ("Walking", 4, "NOIFINAL", 2012, "https://oj.uz/problem/view/NOI12_walking"),
    
    # 2013
    ("Global Warming", 1, "NOIFINAL", 2013, "https://oj.uz/problem/view/NOI13_gw"),
    ("Trucking Diesel", 2, "NOIFINAL", 2013, "https://codebreaker.xyz/problem/diesel"),
    ("Ferries", 3, "NOIFINAL", 2013, "https://oj.uz/problem/view/NOI13_ferries"),
    
    # 2014
    ("Orchard", 1, "NOIFINAL", 2014, "https://oj.uz/problem/view/NOI14_orchard"),
    ("Sightseeing", 2, "NOIFINAL", 2014, "https://oj.uz/problem/view/NOI14_sightseeing"),
    ("CATS", 3, "NOIFINAL", 2014, "https://oj.uz/problem/view/NOI14_cats"),
    ("OBELISK", 4, "NOIFINAL", 2014, "https://oj.uz/problem/view/NOI14_obelisk"),
    
    # 2015
    ("Ask One Get One Free", 1, "NOIFINAL", 2015, "https://codebreaker.xyz/problem/askonegetonefree"),
    ("Sudoku", 2, "NOIFINAL", 2015, "https://codebreaker.xyz/problem/sudoku"),
    ("Radioactive", 3, "NOIFINAL", 2015, "https://codebreaker.xyz/problem/radioactive"),
    ("Banana Farm", 4, "NOIFINAL", 2015, "https://codebreaker.xyz/problem/bananafarm"),
    
    # 2017
    ("Best Place", 1, "NOIFINAL", 2017, "https://oj.uz/problem/view/NOI17_bestplace"),
    ("Roadside Advertisements", 2, "NOIFINAL", 2017, "https://oj.uz/problem/view/NOI17_roadsideadverts"),
    ("Hotspot", 3, "NOIFINAL", 2017, "https://oj.uz/problem/view/NOI17_hotspot"),
    ("RMQ", 4, "NOIFINAL", 2017, "https://oj.uz/problem/view/NOI17_rmq"),
    ("I want to be the very best too!", 5, "NOIFINAL", 2017, "https://oj.uz/problem/view/NOI17_pokemonmaster"),

    # 2018 Preliminary
    ("Snail", 1, "NOIPRELIM", 2018, "https://oj.uz/problem/view/NOI18_snail"),
    ("Knapsack", 2, "NOIPRELIM", 2018, "https://oj.uz/problem/view/NOI18_knapsack"),
    ("Island", 3, "NOIPRELIM", 2018, "https://oj.uz/problem/view/NOI18_island"),
    # 2018 Finals
    ("Collecting Mushrooms", 1, "NOIFINAL", 2018, "https://oj.uz/problem/view/NOI18_collectmushrooms"),
    ("Journey", 2, "NOIFINAL", 2018, "https://oj.uz/problem/view/NOI18_journey"),
    ("Lightning Rod", 3, "NOIFINAL", 2018, "https://oj.uz/problem/view/NOI18_lightningrod"),
    ("City Mapping", 4, "NOIFINAL", 2018, "https://oj.uz/problem/view/NOI18_citymapping"),
    ("Safety", 5, "NOIFINAL", 2018, "https://oj.uz/problem/view/NOI18_safety"),

    # 2019 Preliminary
    ("Palindromic FizzBuzz", 1, "NOIPRELIM", 2019, "https://oj.uz/problem/view/NOI19_palindrome"),
    ("Lost Array", 2, "NOIPRELIM", 2019, "https://oj.uz/problem/view/NOI19_lostarray"),
    ("Experimental Charges", 3, "NOIPRELIM", 2019, "https://oj.uz/problem/view/NOI19_charges"),
    ("Square or Rectangle?", 4, "NOIPRELIM", 2019, "https://oj.uz/problem/view/NOI19_squarerect"),
    # 2019 Finals
    ("Pilot", 1, "NOIFINAL", 2019, "https://oj.uz/problem/view/NOI19_pilot"),
    ("Lasers", 2, "NOIFINAL", 2019, "https://oj.uz/problem/view/NOI19_lasers"),
    ("Feast", 3, "NOIFINAL", 2019, "https://oj.uz/problem/view/NOI19_feast"),
    ("Rigged Roads", 4, "NOIFINAL", 2019, "https://oj.uz/problem/view/NOI19_riggedroads"),
    ("Shuffle", 5, "NOIFINAL", 2019, "https://oj.uz/problem/view/NOI19_shuffle"),

    # 2020 Preliminary
    ("Mountains", 1, "NOIPRELIM", 2020, "https://oj.uz/problem/view/NOI20_mountains"),
    ("Visiting Singapore", 2, "NOIPRELIM", 2020, "https://oj.uz/problem/view/NOI20_visitingsingapore"),
    ("Solar Storm", 3, "NOIPRELIM", 2020, "https://oj.uz/problem/view/NOI20_solarstorm"),

    # 2020 Finals
    ("Labels", 1, "NOIFINAL", 2020, "https://oj.uz/problem/view/NOI20_labels"),
    ("Discharging", 2, "NOIFINAL", 2020, "https://oj.uz/problem/view/NOI20_discharging"),
    ("Progression", 3, "NOIFINAL", 2020, "https://oj.uz/problem/view/NOI20_progression"),
    ("Arcade", 4, "NOIFINAL", 2020, "https://oj.uz/problem/view/NOI20_arcade"),
    ("Aesthetic", 5, "NOIFINAL", 2020, "https://oj.uz/problem/view/NOI20_aesthetic"),

    # 2020 Qualification
    ("Cryptography", 1, "NOIQUAL", 2020, "https://oj.uz/problem/view/NOI20_crypto"),
    ("Fuel Station", 2, "NOIQUAL", 2020, "https://oj.uz/problem/view/NOI20_fuelstation"),
    ("Relay Marathon", 3, "NOIQUAL", 2020, "https://oj.uz/problem/view/NOI20_relaymarathon"),
    ("Firefighting", 4, "NOIQUAL", 2020, "https://oj.uz/problem/view/NOI20_firefighting"),

    # 2021 Finals
    ("Fraud", 1, "NOIFINAL", 2021, "https://codebreaker.xyz/problem/fraud"),
    ("Archaeologist", 2, "NOIFINAL", 2021, "https://codebreaker.xyz/problem/archaeologist"),
    ("Password", 3, "NOIFINAL", 2021, "https://codebreaker.xyz/problem/password"),
    ("Tiles", 4, "NOIFINAL", 2021, "https://codebreaker.xyz/problem/tiles"),
    ("Pond", 5, "NOIFINAL", 2021, "https://codebreaker.xyz/problem/pond"),

    # 2021 Qualification
    ("Competition", 1, "NOIQUAL", 2021, "https://codebreaker.xyz/problem/competition"),
    ("Departure", 2, "NOIQUAL", 2021, "https://codebreaker.xyz/problem/departure"),
    ("Truck", 3, "NOIQUAL", 2021, "https://codebreaker.xyz/problem/truck"),

    # 2022 Finals
    ("Voting City", 1, "NOIFINAL", 2022, "https://oj.uz/problem/view/NOI22_votingcity"),
    ("Gym Badges", 2, "NOIFINAL", 2022, "https://oj.uz/problem/view/NOI22_gymbadges"),
    ("Towers", 3, "NOIFINAL", 2022, "https://oj.uz/problem/view/NOI22_towers"),
    ("Grapevine", 4, "NOIFINAL", 2022, "https://oj.uz/problem/view/NOI22_grapevine"),
    ("Fruits", 5, "NOIFINAL", 2022, "https://oj.uz/problem/view/NOI22_fruits"),

    # 2022 Qualification
    ("L-Board", 1, "NOIQUAL", 2022, "https://codebreaker.xyz/problem/lboard"),
    ("Tree Cutting", 2, "NOIQUAL", 2022, "https://codebreaker.xyz/problem/treecutting"),
    ("Dragonfly", 3, "NOIQUAL", 2022, "https://codebreaker.xyz/problem/dragonfly"),

    # 2023 Qualification
    ("Area", 1, "NOIQUAL", 2023, "https://codebreaker.xyz/problem/area_noi"),
    ("Swords", 2, "NOIQUAL", 2023, "https://codebreaker.xyz/problem/swords"),
    ("Dolls", 3, "NOIQUAL", 2023, "https://codebreaker.xyz/problem/doll_noi"),
    ("Burgers", 4, "NOIQUAL", 2023, "https://codebreaker.xyz/problem/burgers"),
    ("Network", 5, "NOIQUAL", 2023, "https://codebreaker.xyz/problem/network"),

    # 2023 Finals
    ("Topical", 1, "NOIFINAL", 2023, "https://oj.uz/problem/view/NOI23_topical"),
    ("Inspections", 2, "NOIFINAL", 2023, "https://oj.uz/problem/view/NOI23_inspections"),
    ("Airplane", 3, "NOIFINAL", 2023, "https://oj.uz/problem/view/NOI23_airplane"),
    ("Curtains", 4, "NOIFINAL", 2023, "https://oj.uz/problem/view/NOI23_curtains"),
    ("Toxic Gene", 5, "NOIFINAL", 2023, "https://oj.uz/problem/view/NOI23_toxic"),

    # 2024 Finals
    ("Problem Setter", 1, "NOIFINAL", 2024, "https://codebreaker.xyz/problem/problemsetter"),
    ("Shops", 2, "NOIFINAL", 2024, "https://codebreaker.xyz/problem/shops"),
    ("Toxic Gene 2", 3, "NOIFINAL", 2024, "https://codebreaker.xyz/problem/toxic2"),
    ("Coins", 4, "NOIFINAL", 2024, "https://codebreaker.xyz/problem/coin"),
    ("Field", 5, "NOIFINAL", 2024, "https://codebreaker.xyz/problem/field"),

    # 2024 Qualification
    ("Tourist", 1, "NOIQUAL", 2024, "https://codebreaker.xyz/problem/tourist_noi"),
    ("Party", 2, "NOIQUAL", 2024, "https://codebreaker.xyz/problem/party_noi"),
    ("School Photo", 3, "NOIQUAL", 2024, "https://codebreaker.xyz/problem/photo"),
    ("Amusement Park", 4, "NOIQUAL", 2024, "https://codebreaker.xyz/problem/park"),
    ("Explosives", 5, "NOIQUAL", 2024, "https://codebreaker.xyz/problem/explosives"),

    # 2025 Finals
    ("Monsters", 1, "NOIFINAL", 2025, "https://codebreaker.xyz/problem/monsters2"),
    ("Thumper", 2, "NOIFINAL", 2025, "https://codebreaker.xyz/problem/thumper2"),
    ("Reachability", 3, "NOIFINAL", 2025, "https://codebreaker.xyz/problem/reachability2"),
    ("Robots", 4, "NOIFINAL", 2025, "https://codebreaker.xyz/problem/robots2"),
    ("Flooding", 5, "NOIFINAL", 2025, "https://codebreaker.xyz/problem/flooding2"),

    # 2025 Qualification
    ("Train Or Bus", 1, "NOIQUAL", 2025, "https://codebreaker.xyz/problem/trainorbus"),
    ("Ducks And Buttons", 2, "NOIQUAL", 2025, "https://codebreaker.xyz/problem/duckbuttons"),
    ("Snacks", 3, "NOIQUAL", 2025, "https://codebreaker.xyz/problem/snacks"),
    ("Itinerary", 4, "NOIQUAL", 2025, "https://codebreaker.xyz/problem/itinerary"),
    ("Lasers 2", 5, "NOIQUAL", 2025, "https://codebreaker.xyz/problem/lasers2"),

    ## JOISC
    # 2019
    ("Examination", 1, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_examination"),
    ("Naan", 2, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_naan"),
    ("Meetings", 3, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_meetings"),
    ("Two Antennas", 4, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_antennas"),
    ("Two Dishes", 5, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_dishes"),
    ("Two Transportations", 6, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_transportations"),
    ("Designated Cities", 7, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_designated_cities"),
    ("Lamps", 8, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_lamps"),
    ("Bitaro, who Leaps through Time", 9, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_timeleap"),
    ("Cake 3", 10, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_cake3"),
    ("Mergers", 11, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_mergers"),
    ("Minerals", 12, "JOISC", 2019, "https://oj.uz/problem/view/JOI19_minerals"),

    # 2020
    ("Building 4", 1, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_building4"),
    ("Hamburg Steak", 2, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_hamburg"),
    ("Sweeping", 3, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_sweeping"),
    ("Chameleon's Love", 4, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_chameleon"),
    ("Making Friends on Joitter is Fun", 5, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_joitter2"),
    ("Ruins 3", 6, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_ruins3"),
    ("Constellation 3", 7, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_constellation3"),
    ("Harvest", 8, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_harvest"),
    ("Stray Cat", 9, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_stray"),
    ("Capital City", 10, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_capital_city"),
    ("Legendary Dango Maker", 11, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_dango2"),
    ("Treatment Project", 12, "JOISC", 2020, "https://oj.uz/problem/view/JOI20_treatment"),

    # 2021
    ("Aerobatics", 1, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_aerobatics"),
    ("IOI Fever", 2, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_fever"),
    ("Food Court", 3, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_foodcourt"),
    ("Escape Route", 4, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_escape_route"),
    ("Road Construction", 5, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_road_construction"),
    ("Shopping", 6, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_shopping"),
    ("Ancient Machine", 7, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_ancient_machine"),
    ("Bodyguard", 8, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_bodyguard"),
    ("Meetings 2", 9, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_meetings2"),
    ("Event Hopping 2", 10, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_event2"),
    ("Navigation 2", 11, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_navigation2"),
    ("Worst Reporter 4", 12, "JOISC", 2021, "https://oj.uz/problem/view/JOI21_worst_reporter4"),

    # 2022
    ("Jail", 1, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_jail"),
    ("Sightseeing in Kyoto", 2, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_kyoto"),
    ("Misspelling", 3, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_misspelling"),
    ("Copy and Paste 3", 4, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_copypaste3"),
    ("Flights", 5, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_flights"),
    ("Team Contest", 6, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_team"),
    ("Broken Device 2", 7, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_device2"),
    ("Sprinkler", 8, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_sprinkler"),
    ("Ants and Sugar", 9, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_sugar"),
    ("Super Dango Maker", 10, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_dango3"),
    ("Fish 2", 11, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_fish2"),
    ("Reconstruction Project", 12, "JOISC", 2022, "https://oj.uz/problem/view/JOI22_reconstruction"),

    # 2023
    ("Two Currencies", 1, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_currencies"),
    ("Festivals in JOI Kingdom 2", 2, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_festival2"),
    ("Passport", 3, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_passport"),
    ("Council", 5, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_council"),
    ("Mizuyokan 2", 6, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_mizuyokan2"),
    ("Chorus", 7, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_chorus"),
    ("Cookies", 8, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_cookies"),
    ("Tourism", 9, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_tourism"),
    ("Security Guard", 11, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_guard"),
    ("Bitaro's Travel", 12, "JOISC", 2023, "https://oj.uz/problem/view/JOI23_travel"),

    # 2024
    ("Fish 3", 1, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_fish3"),
    ("Ski 2", 2, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_ski2"),
    ("Spy 3", 3, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_spy3"),
    ("Board Game", 4, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_boardgame"),
    ("Tricolor Lights", 5, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_tricolor"),
    ("Growing Vegetables is Fun 5", 6, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_vegetables5"),
    ("Card Collection", 7, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_collection"),
    ("JOI Tour", 8, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_joitour"),
    ("Tower", 9, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_tower"),
    ("Escape Route 2", 10, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_escape2"),
    ("Island Hopping", 11, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_island"),
    ("Table Tennis", 12, "JOISC", 2024, "https://oj.uz/problem/view/JOI24_tabletennis"),

    # 2025
    ("Exhibition 3", 1, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_a"),
    ("Fortune Telling 3", 2, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_b"),
    ("Bitaro's Travel 2", 3, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_c"),
    ("Ambulance", 4, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_d"),
    ("Collecting Stamps 4", 5, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_e"),
    ("Space Thief", 6, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_f"),
    ("Bitaro the Brave 3", 7, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_g"),
    ("Conference", 8, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_h"),
    ("Multi Communication", 9, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_i"),
    ("Circuit 2", 10, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_j"),
    ("Migration Plan", 11, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_k"),
    ("Uiro", 12, "JOISC", 2025, "https://atcoder.jp/contests/joisp2025/tasks/joisp2025_l"),

    ## APIO
    # 2013
    ("Robots", 1, "APIO", 2013, "https://oj.uz/problem/view/APIO13_robots"),
    ("Toll", 2, "APIO", 2013, "https://oj.uz/problem/view/APIO13_toll"),

    # 2014
    ("Palindrome", 1, "APIO", 2014, "https://oj.uz/problem/view/APIO14_palindrome"),
    ("Split the Sequence", 2, "APIO", 2014, "https://oj.uz/problem/view/APIO14_sequence"),
    ("Beads", 3, "APIO", 2014, "https://oj.uz/problem/view/APIO14_beads"),

    # 2015
    ("Bali Sculptures", 1, "APIO", 2015, "https://oj.uz/problem/view/APIO15_sculpture"),
    ("Jakarta Skyscrapers", 2, "APIO", 2015, "https://oj.uz/problem/view/APIO15_skyscraper"),
    ("Palembang Bridges", 3, "APIO", 2015, "https://oj.uz/problem/view/APIO15_bridge"),

    # 2016
    ("Boat", 1, "APIO", 2016, "https://oj.uz/problem/view/APIO16_boat"),
    ("Fireworks", 2, "APIO", 2016, "https://oj.uz/problem/view/APIO16_fireworks"),
    ("Gap", 3, "APIO", 2016, "https://oj.uz/problem/view/APIO16_gap"),

    # 2017
    ("Land of the Rainbow Gold", 1, "APIO", 2017, "https://oj.uz/problem/view/APIO17_rainbow"),
    ("Travelling Merchant", 2, "APIO", 2017, "https://oj.uz/problem/view/APIO17_merchant"),
    ("Koala Game", 3, "APIO", 2017, "https://oj.uz/problem/view/APIO17_koala"),

    # 2018
    ("New Home", 1, "APIO", 2018, "https://oj.uz/problem/view/APIO18_new_home"),
    ("Circle Selection", 2, "APIO", 2018, "https://oj.uz/problem/view/APIO18_circle_selection"),
    ("Duathlon", 3, "APIO", 2018, "https://oj.uz/problem/view/APIO18_duathlon"),

    # 2019
    ("Strange Device", 1, "APIO", 2019, "https://oj.uz/problem/view/APIO19_strange_device"),
    ("Bridges", 2, "APIO", 2019, "https://oj.uz/problem/view/APIO19_bridges"),
    ("Street Lamps", 3, "APIO", 2019, "https://oj.uz/problem/view/APIO19_street_lamps"),

    # 2020
    ("Painting Walls", 1, "APIO", 2020, "https://oj.uz/problem/view/APIO20_paint"),
    ("Swapping Cities", 2, "APIO", 2020, "https://oj.uz/problem/view/APIO20_swap"),
    ("Fun Tour", 3, "APIO", 2020, "https://oj.uz/problem/view/APIO20_fun"),

    # 2021
    ("Hexagonal Territory", 1, "APIO", 2021, "https://oj.uz/problem/view/APIO21_hexagon"),
    ("Rainforest Jumps", 2, "APIO", 2021, "https://oj.uz/problem/view/APIO21_jumps"),
    ("Road Closures", 3, "APIO", 2021, "https://oj.uz/problem/view/APIO21_roads"),

    # 2022
    ("Mars", 1, "APIO", 2022, "https://oj.uz/problem/view/APIO22_mars"),
    ("Game", 2, "APIO", 2022, "https://oj.uz/problem/view/APIO22_game"),
    ("Permutation", 3, "APIO", 2022, "https://oj.uz/problem/view/APIO22_perm"),

    # 2023
    ("Cyberland", 1, "APIO", 2023, "https://oj.uz/problem/view/APIO23_cyberland"),
    ("Sequence", 2, "APIO", 2023, "https://oj.uz/problem/view/APIO23_sequence"),
    ("Alice, Bob, and Circuit", 3, "APIO", 2023, "https://oj.uz/problem/view/APIO23_abc"),

    # 2024
    ("September", 1, "APIO", 2024, "https://oj.uz/problem/view/APIO24_september"),
    ("Train", 2, "APIO", 2024, "https://oj.uz/problem/view/APIO24_train"),
    ("Magic Show", 3, "APIO", 2024, "https://oj.uz/problem/view/APIO24_show"),

    ## INOI
    # 2022
    ("Posting", 1, "INOI", 2022, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2201"),
    ("Conquest", 2, "INOI", 2022, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2202"),
    ("Diocletian", 3, "INOI", 2022, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2203B"),

    # 2023
    ("Planet", 1, "INOI", 2023, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2301"),
    ("Pillars", 2, "INOI", 2023, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2302"),
    ("History", 3, "INOI", 2023, "https://www.codechef.com/practice/course/zco-inoi-problems/INOIPRAC/problems/INOI2303"),

    # 2024
    ("Monsters", 1, "INOI", 2024, "https://codedrills.io/contests/inoi-2024-final/problems/inoi2024-p1---monsters"),
    ("Fertilizer", 2, "INOI", 2024, "https://codedrills.io/contests/inoi-2024-final/problems/inoi2024-p2---fertilizer"),
    ("Trees", 3, "INOI", 2024, "https://codedrills.io/contests/inoi-2024-final/problems/inoi2024-p3---trees"),

    # 2025
    ("Neq Array", 1, "INOI", 2025, "https://icpc.codedrills.io/contests/inoi-2025-main/problems/inoi-2025-p1---neq-array"),
    ("Error of 2", 2, "INOI", 2025, "https://icpc.codedrills.io/contests/inoi-2025-main/problems/inoi-2025-p2---error-of-2"),
    ("Virtual Tree Subsets", 3, "INOI", 2025, "https://icpc.codedrills.io/contests/inoi-2025-main/problems/inoi-2025-p3---virtual-tree-subsets"),

    ## ZCO
    # 2024
    ("Vegetables", 1, "ZCO", 2024, "https://codedrills.io/contests/zco-2024-main/problems/zco2024-p1---vegetables"),
    ("Fruits", 2, "ZCO", 2024, "https://codedrills.io/contests/zco-2024-main/problems/zco2024-p2---fruits"),

    # 2025
    ("River", 1, "ZCO", 2025, "https://codedrills.io/contests/zco-inoi-past-problems/problems/zco2025-p1---river"),
    ("Secret", 2, "ZCO", 2025, "https://codedrills.io/contests/zco-inoi-past-problems/problems/zco2025-p2---secret?tab=overview"),

    ## IOI

    # 2024
    ("Nile", 1, "IOI", 2024, "https://oj.uz/problem/view/IOI24_nile"),
    ("Message", 2, "IOI", 2024, "https://oj.uz/problem/view/IOI24_message"),
    ("Tree", 3, "IOI", 2024, "https://oj.uz/problem/view/IOI24_tree"),
    ("Hieroglyphs", 4, "IOI", 2024, "https://oj.uz/problem/view/IOI24_hieroglyphs"),
    ("Mosaic", 5, "IOI", 2024, "https://oj.uz/problem/view/IOI24_mosaic"),
    ("Sphinx", 6, "IOI", 2024, "https://oj.uz/problem/view/IOI24_sphinx"),

    # 2023
    ("Closing Time", 1, "IOI", 2023, "https://oj.uz/problem/view/IOI23_closing"),
    ("Longest Trip", 2, "IOI", 2023, "https://oj.uz/problem/view/IOI23_longesttrip"),
    ("Soccer Stadium", 3, "IOI", 2023, "https://oj.uz/problem/view/IOI23_soccer"),
    ("Beech Tree", 4, "IOI", 2023, "https://oj.uz/problem/view/IOI23_beechtree"),
    ("Overtaking", 5, "IOI", 2023, "https://oj.uz/problem/view/IOI23_overtaking"),
    ("Robot Contest", 6, "IOI", 2023, "https://oj.uz/problem/view/IOI23_robot"),

    # 2022
    ("Catfish Farm", 1, "IOI", 2022, "https://oj.uz/problem/view/IOI22_fish"),
    ("Prisoner Challenge", 2, "IOI", 2022, "https://oj.uz/problem/view/IOI22_prison"),
    ("Radio Towers", 3, "IOI", 2022, "https://oj.uz/problem/view/IOI22_towers"),
    ("Digital Circuit", 4, "IOI", 2022, "https://oj.uz/problem/view/IOI22_circuit"),
    ("Rarest Insects", 5, "IOI", 2022, "https://oj.uz/problem/view/IOI22_insects"),
    ("Thousands Islands", 6, "IOI", 2022, "https://oj.uz/problem/view/IOI22_islands"),

    # 2021
    ("Distributing Candies", 1, "IOI", 2021, "https://oj.uz/problem/view/IOI21_candies"),
    ("Keys", 2, "IOI", 2021, "https://oj.uz/problem/view/IOI21_keys"),
    ("Fountain Parks", 3, "IOI", 2021, "https://oj.uz/problem/view/IOI21_parks"),
    ("Mutating DNA", 4, "IOI", 2021, "https://oj.uz/problem/view/IOI21_dna"),
    ("Dungeons Game", 5, "IOI", 2021, "https://oj.uz/problem/view/IOI21_dungeons"),
    ("Bit Shift Registers", 6, "IOI", 2021, "https://oj.uz/problem/view/IOI21_registers"),

    # 2020
    ("Comparing Plants", 1, "IOI", 2020, "https://oj.uz/problem/view/IOI20_plants"),
    ("Connecting Supertrees", 2, "IOI", 2020, "https://oj.uz/problem/view/IOI20_supertrees"),
    ("Carnival Tickets", 3, "IOI", 2020, "https://oj.uz/problem/view/IOI20_tickets"),
    ("Packing Biscuits", 4, "IOI", 2020, "https://oj.uz/problem/view/IOI20_biscuits"),
    ("Counting Mushrooms", 5, "IOI", 2020, "https://oj.uz/problem/view/IOI20_mushrooms"),
    ("Stations", 6, "IOI", 2020, "https://oj.uz/problem/view/IOI20_stations"),

    # 2019
    ("Arranging Shoes", 1, "IOI", 2019, "https://oj.uz/problem/view/IOI19_shoes"),
    ("Split the Attractions", 2, "IOI", 2019, "https://oj.uz/problem/view/IOI19_split"),
    ("Rectangles", 3, "IOI", 2019, "https://oj.uz/problem/view/IOI19_rect"),
    ("Broken Line", 4, "IOI", 2019, "https://oj.uz/problem/view/IOI19_line"),
    ("Vision Program", 5, "IOI", 2019, "https://oj.uz/problem/view/IOI19_vision"),
    ("Sky Walking", 6, "IOI", 2019, "https://oj.uz/problem/view/IOI19_walk"),

    # 2018
    ("Combo", 1, "IOI", 2018, "https://oj.uz/problem/view/IOI18_combo"),
    ("Seats", 2, "IOI", 2018, "https://oj.uz/problem/view/IOI18_seats"),
    ("Werewolf", 3, "IOI", 2018, "https://oj.uz/problem/view/IOI18_werewolf"),
    ("Mechanical Doll", 4, "IOI", 2018, "https://oj.uz/problem/view/IOI18_doll"),
    ("Highway Tolls", 5, "IOI", 2018, "https://oj.uz/problem/view/IOI18_highway"),
    ("Meetings", 6, "IOI", 2018, "https://oj.uz/problem/view/IOI18_meetings"),

    # 2017
    ("Nowruz", 1, "IOI", 2017, "https://oj.uz/problem/view/IOI17_nowruz"),
    ("Wiring", 2, "IOI", 2017, "https://oj.uz/problem/view/IOI17_wiring"),
    ("Toy Train", 3, "IOI", 2017, "https://oj.uz/problem/view/IOI17_train"),
    ("The Big Prize", 4, "IOI", 2017, "https://oj.uz/problem/view/IOI17_prize"),
    ("Simurgh", 5, "IOI", 2017, "https://oj.uz/problem/view/IOI17_simurgh"),
    ("Ancient Books", 6, "IOI", 2017, "https://oj.uz/problem/view/IOI17_books"),

    # 2016
    ("Detecting Molecules", 1, "IOI", 2016, "https://oj.uz/problem/view/IOI16_molecules"),
    ("Roller Coaster Railroad", 2, "IOI", 2016, "https://oj.uz/problem/view/IOI16_railroad"),
    ("Shortcut", 3, "IOI", 2016, "https://oj.uz/problem/view/IOI16_shortcut"),
    ("Paint By Numbers", 4, "IOI", 2016, "https://oj.uz/problem/view/IOI16_paint"),
    ("Unscrambling a Messy Bug", 5, "IOI", 2016, "https://oj.uz/problem/view/IOI16_messy"),
    ("Aliens", 6, "IOI", 2016, "https://oj.uz/problem/view/IOI16_aliens"),

    # 2015
    ("Boxes with Souvenirs", 1, "IOI", 2015, "https://oj.uz/problem/view/IOI15_boxes"),
    ("Scales", 2, "IOI", 2015, "https://oj.uz/problem/view/IOI15_scales"),
    ("Teams", 3, "IOI", 2015, "https://oj.uz/problem/view/IOI15_teams"),
    ("Horses", 4, "IOI", 2015, "https://oj.uz/problem/view/IOI15_horses"),
    ("Sorting", 5, "IOI", 2015, "https://oj.uz/problem/view/IOI15_sorting"),
    ("Towns", 6, "IOI", 2015, "https://oj.uz/problem/view/IOI15_towns"),

    # 2014
    ("Rail", 1, "IOI", 2014, "https://oj.uz/problem/view/IOI14_rail"),
    ("Wall", 2, "IOI", 2014, "https://oj.uz/problem/view/IOI14_wall"),
    ("Game", 3, "IOI", 2014, "https://oj.uz/problem/view/IOI14_game"),
    ("Gondola", 4, "IOI", 2014, "https://oj.uz/problem/view/IOI14_gondola"),
    ("Friend", 5, "IOI", 2014, "https://oj.uz/problem/view/IOI14_friend"),
    ("Holiday", 6, "IOI", 2014, "https://oj.uz/problem/view/IOI14_holiday"),

    # 2013
    ("Dreaming", 1, "IOI", 2013, "https://oj.uz/problem/view/IOI13_dreaming"),
    ("Art Class", 2, "IOI", 2013, "https://oj.uz/problem/view/IOI13_artclass"),
    ("Wombats", 3, "IOI", 2013, "https://oj.uz/problem/view/IOI13_wombats"),
    ("Cave", 4, "IOI", 2013, "https://oj.uz/problem/view/IOI13_cave"),
    ("Robots", 5, "IOI", 2013, "https://oj.uz/problem/view/IOI13_robots"),
    ("Game", 6, "IOI", 2013, "https://oj.uz/problem/view/IOI13_game"),

    # 2012
    ("Rings", 2, "IOI", 2012, "https://oj.uz/problem/view/IOI12_rings"),
    ("Scrivener", 3, "IOI", 2012, "https://oj.uz/problem/view/IOI12_scrivener"),
    ("City", 4, "IOI", 2012, "https://oj.uz/problem/view/IOI12_city"),
    ("Supper", 5, "IOI", 2012, "https://oj.uz/problem/view/IOI12_supper"),
    ("Tournament", 6, "IOI", 2012, "https://oj.uz/problem/view/IOI12_tournament"),

    # 2011
    ("Garden", 1, "IOI", 2011, "https://oj.uz/problem/view/IOI11_garden"),
    ("Race", 2, "IOI", 2011, "https://oj.uz/problem/view/IOI11_race"),
    ("Rice Hub", 3, "IOI", 2011, "https://oj.uz/problem/view/IOI11_ricehub"),
    ("Crocodile", 4, "IOI", 2011, "https://oj.uz/problem/view/IOI11_crocodile"),
    ("Elephants", 5, "IOI", 2011, "https://oj.uz/problem/view/IOI11_elephants"),
    ("Parrots", 6, "IOI", 2011, "https://oj.uz/problem/view/IOI11_parrots"),

    ## Since these have 8 problems, I'm temporarily commenting them out (it makes the table look ugly)
    # # 2010
    # ("Cluedo", 1, "IOI", 2010, "https://oj.uz/problem/view/IOI10_cluedo"),
    # ("Hotter Colder", 2, "IOI", 2010, "https://oj.uz/problem/view/IOI10_hottercolder"),
    # ("Quality", 3, "IOI", 2010, "https://oj.uz/problem/view/IOI10_quality"),
    # ("Languages", 4, "IOI", 2010, "https://oj.uz/problem/view/IOI10_languages"),
    # ("Memory", 5, "IOI", 2010, "https://oj.uz/problem/view/IOI10_memory"),
    # ("Traffic", 6, "IOI", 2010, "https://oj.uz/problem/view/IOI10_traffic"),
    # ("Maze", 7, "IOI", 2010, "https://oj.uz/problem/view/IOI10_maze"),
    # ("Saveit", 8, "IOI", 2010, "https://oj.uz/problem/view/IOI10_saveit"),

    # # 2009
    # ("Archery", 1, "IOI", 2009, "https://oj.uz/problem/view/IOI09_archery"),
    # ("Hiring", 2, "IOI", 2009, "https://oj.uz/problem/view/IOI09_hiring"),
    # ("Poi", 3, "IOI", 2009, "https://oj.uz/problem/view/IOI09_poi"),
    # ("Raisins", 4, "IOI", 2009, "https://oj.uz/problem/view/IOI09_raisins"),
    # ("Garage", 5, "IOI", 2009, "https://oj.uz/problem/view/IOI09_garage"),
    # ("Mecho", 6, "IOI", 2009, "https://oj.uz/problem/view/IOI09_mecho"),
    # ("Regions", 7, "IOI", 2009, "https://oj.uz/problem/view/IOI09_regions"),
    # ("Salesman", 8, "IOI", 2009, "https://oj.uz/problem/view/IOI09_salesman"),

    # 2008
    ("Printer", 1, "IOI", 2008, "https://oj.uz/problem/view/IOI08_printer"),
    ("Islands", 2, "IOI", 2008, "https://oj.uz/problem/view/IOI08_islands"),
    ("Fish", 3, "IOI", 2008, "https://oj.uz/problem/view/IOI08_fish"),
    ("Linear Garden", 4, "IOI", 2008, "https://oj.uz/problem/view/IOI08_linear_garden"),
    ("Teleporters", 5, "IOI", 2008, "https://oj.uz/problem/view/IOI08_teleporters"),
    ("Pyramid Base", 6, "IOI", 2008, "https://oj.uz/problem/view/IOI08_pyramid_base"),

    # 2007
    ("Aliens", 1, "IOI", 2007, "https://oj.uz/problem/view/IOI07_aliens"),
    ("Flood", 2, "IOI", 2007, "https://oj.uz/problem/view/IOI07_flood"),
    ("Sails", 3, "IOI", 2007, "https://oj.uz/problem/view/IOI07_sails"),
    ("Miners", 4, "IOI", 2007, "https://oj.uz/problem/view/IOI07_miners"),
    ("Pairs", 5, "IOI", 2007, "https://oj.uz/problem/view/IOI07_pairs"),
    ("Training", 6, "IOI", 2007, "https://oj.uz/problem/view/IOI07_training"),

    ## EGOI

    # 2021
    ("Zeroes", 1, "EGOI", 2021, "https://codeforces.com/gym/103148/problem/A"),
    ("Luna Likes Love", 2, "EGOI", 2021, "https://codeforces.com/gym/103148/problem/B"),
    ("Twin Cookies", 3, "EGOI", 2021, "https://codeforces.com/gym/103148/problem/C"),
    ("Lanterns", 4, "EGOI", 2021, "https://codeforces.com/gym/103148/problem/D"),
    ("Shopping Fever", 5, "EGOI", 2021, "https://codeforces.com/gym/103149/problem/A"),
    ("Railway", 6, "EGOI", 2021, "https://codeforces.com/gym/103149/problem/B"),
    ("Angry Cows", 7, "EGOI", 2021, "https://codeforces.com/gym/103149/problem/C"),
    ("Double Move", 8, "EGOI", 2021, "https://codeforces.com/gym/103149/problem/D"),

    # 2022
    ("SubsetMex", 1, "EGOI", 2022, "https://codeforces.com/gym/104229/problem/A"),
    ("Lego Wall", 2, "EGOI", 2022, "https://codeforces.com/gym/104229/problem/B"),
    ("Social Engineering", 3, "EGOI", 2022, "https://codeforces.com/gym/104229/problem/C"),
    ("Tourists", 4, "EGOI", 2022, "https://codeforces.com/gym/104229/problem/D"),
    ("Data Centers", 5, "EGOI", 2022, "https://codeforces.com/gym/104230/problem/A"),
    ("Superpiece", 6, "EGOI", 2022, "https://codeforces.com/gym/104230/problem/B"),
    ("Toy Design", 7, "EGOI", 2022, "https://codeforces.com/gym/104230/problem/C"),
    ("Chika Wants to Cheat", 8, "EGOI", 2022, "https://codeforces.com/gym/104230/problem/D"),

    # 2023
    ("Inflation", 1, "EGOI", 2023, "https://qoj.ac/contest/1354/problem/7154"),
    ("Padel Prize Pursuit", 2, "EGOI", 2023, "https://qoj.ac/contest/1354/problem/7155"),
    ("Find the Box", 3, "EGOI", 2023, "https://qoj.ac/contest/1354/problem/7156"),
    ("Bikes vs Cars", 4, "EGOI", 2023, "https://qoj.ac/contest/1354/problem/7157"),
    ("Carnival General", 5, "EGOI", 2023, "https://qoj.ac/contest/1355/problem/7158"),
    ("Candy", 6, "EGOI", 2023, "https://qoj.ac/contest/1355/problem/7159"),
    ("Sopsug", 7, "EGOI", 2023, "https://qoj.ac/contest/1355/problem/7160"),
    ("Guessing Game", 8, "EGOI", 2023, "https://qoj.ac/contest/1355/problem/7161"),

    # 2024
    ("Infinite Race", 1, "EGOI", 2024, "http://oj.uz/problem/view/EGOI24_infiniterace2"),
    ("Bouquet", 2, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_bouquet"),
    ("Team Coding", 3, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_teamcoding"),
    ("Garden Decorations", 4, "EGOI", 2024, "https://qoj.ac/contest/1764/problem/9185"),
    ("Circle Passing", 5, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_circlepassing"),
    ("Bikeparking", 6, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_bikeparking"),
    ("Light Bulbs", 7, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_lightbulbs"),
    ("Make Them Meet", 8, "EGOI", 2024, "https://oj.uz/problem/view/EGOI24_makethemmeet"),

    ## IOITC
    # 2023
    ("Grid Construction", 1, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/GridConstruction/statements/EN"),
    ("Colorful Cycles", 2, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/ColorfulCycles/statements/EN"),
    ("LIS", 3, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/LIS/statements/EN"),
    ("Reversed Inversions", 4, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/ReversedInversions/statements/EN"),
    ("Sole Occupancy", 5, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/SoleOccupancy/statements/EN"),
    ("Tournament", 6, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/Tournament/statements/EN"),
    ("Yet Another Tree Problem", 7, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/YetAnotherTreeProblem/statements/EN"),
    ("Cookies", 8, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/Cookies/statements/EN"),
    ("Tree Matching", 9, "IOITC", 2023, "http://cms.iarcs.org.in:8888/tasks/TreeMatching/statements/EN"),

    # 2022
    ("Median Communication", 9, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/MedianCommunication/statements/EN"),
    ("Add Subtract Equalize", 8, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/AddSubtractEqualize/statements/EN"),
    ("Tree Interval Queries", 7, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/TreeIntervalQueries/statements/EN"),
    ("Inversions", 6, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/Inversions/statements/EN"),
    ("Tree Coverage", 5, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/TreeCoverage/statements/EN"),
    ("Array Splitting", 4, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/ArraySplitting/statements/EN"),
    ("Manhattan Matching", 3, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/ManhattanMatching/statements/EN"),
    ("Isolable Queries", 2, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/IsolableQueries/statements/EN"),
    ("Binary String Happiness", 1, "IOITC", 2022, "http://cms.iarcs.org.in:8888/tasks/BinaryStringHappiness/statements/EN"),

    # 2021
    ("Edge Subsets", 9, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/EdgeSubsets/statements/EN"),
    ("Graph Count", 8, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/GraphCount/statements/EN"),
    ("Hidden Cell", 7, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/HiddenCell/statements/EN"),
    ("Crew Reunion", 6, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/CrewReunion/statements/EN"),
    ("Interactive MST", 5, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/InteractiveMST/statements/EN"),
    ("Similar Arrays", 4, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/SimilarArrays/statements/EN"),
    ("Island Hopping", 3, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/IslandHopping/statements/EN"),
    ("Odd Sum Partition", 2, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/OddSumPartition/statements/EN"),
    ("Tokens On A Tree", 1, "IOITC", 2021, "http://cms.iarcs.org.in:8888/tasks/TokensOnATree/statements/EN"),

    # 2020
    ("Beautiful Trees", 9, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/BeautifulTrees/statements/EN"),
    ("The Social Gathering", 8, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/TheSocialGathering/statements/EN"),
    ("Hidden Vertex", 7, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/HiddenVertex/statements/EN"),
    ("Almost Shortest Paths", 6, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/AlmostShortestPaths/statements/EN"),
    ("Buildings", 5, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/Buildings/statements/EN"),
    ("Pairing Trees", 4, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/PairingTrees/statements/EN"),
    ("Counting Intervals", 3, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/CountingIntervals/statements/EN"),
    ("Paint It Black", 2, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/PaintItBlack/statements/EN"),
    ("Removing Leaves", 1, "IOITC", 2020, "http://cms.iarcs.org.in:8888/tasks/RemovingLeaves/statements/EN"),

    # 2019
    ("Breaking Trees", 8, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/BreakingTrees/statements/EN"),
    ("Labelled Tree", 7, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/LabelledTree/statements/EN"),
    ("Equal Length Paths", 6, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/EqualLengthPaths/statements/EN"),
    ("Increasing Chains", 5, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/IncreasingChains/statements/EN"),
    ("Tree Profit", 4, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/TreeProfit/statements/EN"),
    ("Diverse Subarrays", 3, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/DiverseSubarrays/statements/EN"),
    ("Figure 8", 2, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/Figure8/statements/EN"),
    ("Make Acyclic", 1, "IOITC", 2019, "http://cms.iarcs.org.in:8888/tasks/MakeAcyclic/statements/EN"),

    # 2018
    ("Increasing Means", 9, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/IncreasingMeans/statements/EN"),
    ("TwoGoodWalks", 8, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/TwoGoodWalks/statements/EN"),
    ("Add Rotate XOR", 7, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/AddRotateXOR/statements/EN"),
    ("Changing Numbers", 6, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/ChangingNumbers/statements/EN"),
    ("Coin Denominations", 5, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/CoinDenominations/statements/EN"),
    ("Exact Walks", 4, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/ExactWalks/statements/EN"),
    ("Cycles And Colorings", 3, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/CyclesAndColorings/statements/EN"),
    ("K Perfect Matchings", 2, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/KPerfectMatchings/statements/EN"),
    ("Circular Intervals", 1, "IOITC", 2018, "http://cms.iarcs.org.in:8888/tasks/CircularIntervals/statements/EN"),

    # 2017
    ("Smoothness", 9, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/Smoothness/statements/EN"),
    ("Walled Inversions", 8, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/WalledInversions/statements/EN"),
    ("Painting Tree", 7, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/PaintingTree/statements/EN"),
    ("Evolutionary Trees", 6, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/EvolutionaryTrees/statements/EN"),
    ("Collecting Coins", 5, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/CollectingCoins/statements/EN"),
    ("Check SCC", 4, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/CheckSCC/statements/EN"),
    ("Graph LIS", 3, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/GraphLIS/statements/EN"),
    ("Subarray Medians", 2, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/SubarrayMedians/statements/EN"),
    ("Convex Hull Count", 1, "IOITC", 2017, "http://cms.iarcs.org.in:8888/tasks/ConvexHullCount/statements/EN"),

    ## JOIFR
    # 2025
    ("Grid Coloring", 1, "JOIFR", 2025, "https://atcoder.jp/contests/joi2025ho/tasks/joi2025ho_a"),
    ("Bitaro the Brave 2", 2, "JOIFR", 2025, "https://atcoder.jp/contests/joi2025ho/tasks/joi2025ho_b"),
    ("Mi Teleférico", 3, "JOIFR", 2025, "https://atcoder.jp/contests/joi2025ho/tasks/joi2025ho_c"),
    ("Just Long Neckties 2", 4, "JOIFR", 2025, "https://atcoder.jp/contests/joi2025ho/tasks/joi2025ho_d"),
    ("Post Office", 5, "JOIFR", 2025, "https://atcoder.jp/contests/joi2025ho/tasks/joi2025ho_e"),

    # 2024
    ("Room Temperature", 1, "JOIFR", 2024, "https://oj.uz/problem/view/JOI24_ho_t1"),
    ("Construction Project 2", 3, "JOIFR", 2024, "https://oj.uz/problem/view/JOI24_ho_t3"),
    ("Marathon Race 2", 2, "JOIFR", 2024, "https://oj.uz/problem/view/JOI24_ho_t2"),
    ("Gift Exchange", 4, "JOIFR", 2024, "https://oj.uz/problem/view/JOI24_ho_t4"),
    ("Road Service 2", 5, "JOIFR", 2024, "https://oj.uz/problem/view/JOI24_ho_t5"),

    # 2023
    ("Stone Arranging 2", 1, "JOIFR", 2023, "https://oj.uz/problem/view/JOI23_ho_t1"),
    ("Advertisement 2", 2, "JOIFR", 2023, "https://oj.uz/problem/view/JOI23_ho_t2"),
    ("Maze", 3, "JOIFR", 2023, "https://oj.uz/problem/view/JOI23_ho_t3"),
    ("Cat Exercise", 4, "JOIFR", 2023, "https://oj.uz/problem/view/JOI23_ho_t4"),
    ("Modern Machine", 5, "JOIFR", 2023, "https://oj.uz/problem/view/JOI23_ho_t5"),

    # 2022
    ("Intercastellar", 1, "JOIFR", 2022, "https://oj.uz/problem/view/JOI22_ho_t1"),
    ("Self Study", 2, "JOIFR", 2022, "https://oj.uz/problem/view/JOI22_ho_t2"),
    ("Let's Win the Election", 3, "JOIFR", 2022, "https://oj.uz/problem/view/JOI22_ho_t3"),
    ("Railway Trip 2", 4, "JOIFR", 2022, "https://oj.uz/problem/view/JOI22_ho_t4"),
    ("Sandcastle 2", 5, "JOIFR", 2022, "https://oj.uz/problem/view/JOI22_ho_t5"),

    # 2021
    ("Growing Vegetables is Fun 4", 1, "JOIFR", 2021, "https://oj.uz/problem/view/JOI21_ho_t1"),
    ("Snowball", 2, "JOIFR", 2021, "https://oj.uz/problem/view/JOI21_ho_t2"),
    ("Group Photo", 3, "JOIFR", 2021, "https://oj.uz/problem/view/JOI21_ho_t3"),
    ("Robot", 4, "JOIFR", 2021, "https://oj.uz/problem/view/JOI21_ho_t4"),
    ("Dungeon 3", 5, "JOIFR", 2021, "https://oj.uz/problem/view/JOI21_ho_t5"),

    # 2020
    ("Just Long Neckties", 1, "JOIFR", 2020, "https://oj.uz/problem/view/JOI20_ho_t1"),
    ("JJOOII 2", 2, "JOIFR", 2020, "https://oj.uz/problem/view/JOI20_ho_t2"),
    ("Collecting Stamps 3", 3, "JOIFR", 2020, "https://oj.uz/problem/view/JOI20_ho_t3"),
    ("Olympic Bus", 4, "JOIFR", 2020, "https://oj.uz/problem/view/JOI20_ho_t4"),
    ("Fire", 5, "JOIFR", 2020, "https://oj.uz/problem/view/JOI20_ho_t5"),

    # 2019
    ("Bitaro the Brave", 1, "JOIFR", 2019, "https://oj.uz/problem/view/JOI19_ho_t1"),
    ("Exhibition", 2, "JOIFR", 2019, "https://oj.uz/problem/view/JOI19_ho_t2"),
    ("Growing Vegetable is Fun 3", 3, "JOIFR", 2019, "https://oj.uz/problem/view/JOI19_ho_t3"),
    ("Coin Collecting", 4, "JOIFR", 2019, "https://oj.uz/problem/view/JOI19_ho_t4"),
    ("Unique Cities", 5, "JOIFR", 2019, "https://oj.uz/problem/view/JOI19_ho_t5"),

    # 2018
    ("Stove", 1, "JOIFR", 2018, "https://oj.uz/problem/view/JOI18_stove"),
    ("Art Exhibition", 2, "JOIFR", 2018, "https://oj.uz/problem/view/JOI18_art"),
    ("Dango Maker", 3, "JOIFR", 2018, "https://oj.uz/problem/view/JOI18_dango_maker"),
    ("Commuter Pass", 4, "JOIFR", 2018, "https://oj.uz/problem/view/JOI18_commuter_pass"),
    ("Snake Escaping", 5, "JOIFR", 2018, "https://oj.uz/problem/view/JOI18_snake_escaping"),

    # 2017
    ("Foehn Phenomena", 1, "JOIFR", 2017, "https://oj.uz/problem/view/JOI17_foehn_phenomena"),
    ("Semiexpress", 2, "JOIFR", 2017, "https://oj.uz/problem/view/JOI17_semiexpress"),
    ("The Kingdom of JOIOI", 3, "JOIFR", 2017, "https://oj.uz/problem/view/JOI17_joioi"),
    ("Soccer", 4, "JOIFR", 2017, "https://oj.uz/problem/view/JOI17_soccer"),
    ("Rope", 5, "JOIFR", 2017, "https://oj.uz/problem/view/JOI17_rope"),

    ## POI
    # 2019
    ("Renovation", 1, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/xNjwUvwdHQoQTFBrmyG8vD1O/site/?key=statement"),
    ("Auto Racing", 2, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/S8phA644ooC9arh6FhXzvbiH/site/?key=statement"),
    ("Globetrotter Congress", 3, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/bS_effBgQtuS7NXJA_dn7Ogm/site/?key=statement"),
    ("Long Travels", 4, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/QHh99tBu4p9FMsFohv4da7S7/site/?key=statement"),
    ("Game of Divisors", 5, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/k4iPPyQbhkKRE3kLi6zjUbWz/site/?key=statement"),
    ("Ornithologist", 6, "POI", 2019, "https://szkopul.edu.pl/problemset/problem/3QSA66sDeX0fi-Ry_gX1WXhy/site/?key=statement"),

    # 2018
    ("Complete Numbers", 1, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/GfNdWdsmfgHxoByl0ETuZW9c/site/?key=statement"),
    ("Fence", 2, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/guoc36QCEe4q47qruYB7HBV-/site/?key=statement"),
    ("Triinformathlon", 3, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/URPMk7vthz60i1J3MT3XbIIO/site/?key=statement"),
    ("Two Long Candy Sticks", 4, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/Kmofhbw9cTx06gSZg-C5MiBU/site/?key=statement"),
    ("Taxis", 5, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/pxbqUTPy3IuPDul9FdT2_Sth/site/?key=statement"),
    ("Polynomial", 6, "POI", 2018, "https://szkopul.edu.pl/problemset/problem/9JvSAnyf5d1FlPAEXEdUAtCz/site/?key=statement"),

    # 2017
    ("Midas", 1, "POI", 2017, "https://szkopul.edu.pl/problemset/problem/wrTmzO9-dzEbLtsRUCdMV2_W/site/?key=statement"),
    ("Grades", 2, "POI", 2017, "https://szkopul.edu.pl/problemset/problem/0KG8REkSLNnY5sVkm7Aei_R7/site/?key=statement"),
    ("Panini", 3, "POI", 2017, "https://szkopul.edu.pl/problemset/problem/w-dbshXVyRol4LIT9jeP-bNn/site/?key=statement"),
    ("Cook", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/9NFtPM59qGWa7wdn570ifuP0/site/?key=statement"),
    ("Crossroads of Parity", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/-7cqC3RrH4e-Ar7DWy4GKzLv/site/?key=statement"),

    # 2016
    ("Messenger", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Mk-9GNDtSal6h_8T4n9Ezq9M/site/?key=statement"),
    ("Diligent Johny", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/_cVmDXXn2TjF0dF1rW6eazA0/site/?key=statement"),
    ("Hedge", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/dABzva_j1-BvzKMsyxkuRoue/site/?key=statement"),
    ("Club Members", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/3Kqkgeapr-W-MBprNjUDGICL/site/?key=statement"),
    ("Amusing Journeys", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/YY6-3ua-C1rt7q-97laWc0UP/site/?key=statement"),
    ("Parade", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/1QaUWE_ePAmitZjgAszOVD1U/site/?key=statement"),

    # 2015
    ("Car Washes", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/kYVp05sX8lzHWNwn93xjcYwH/site/?key=statement"),
    ("Direction Signs", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/4roJ2TqCXhLN6ftK2jiWKlO9/site/?key=statement"),
    ("Trous de Loup", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/07Q0fFk7fU2TmGr6wpPeDCZj/site/?key=statement"),
    ("Kolekcjoner Bajtemonów", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/i_8o_TvZ2QA9MWo4h1PglK0H/site/?key=statement"),
    ("Highway Modernization", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/z0rincXf7fi157ycO_Sl0bCb/site/?key=statement"),
    ("Trips", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/zKf5Ua8okcS0jngsrTgKVM9L/site/?key=statement"),

    # 2014
    ("Around the World", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/hogW-qBD1uDPGDS4jTohYMwc/site/?key=statement"),
    ("Ant Colony", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/J5f8YHtUsaMdtOdfx0QoHKe0/site/?key=statement"),
    ("Turystyka", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/QGvPmh3HPUW0aZHn6EZuV-l1/site/?key=statement"),
    ("Solar Lamps", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/GBNhbXwWhoCD5GHjNFAm_pOJ/site/?key=statement"),
    ("Solar Panels", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/hzKdkq0maus68ExIKeHyERTJ/site/?key=statement"),
    ("Freight", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/tbAODT0mS1ZwmNfteVw6W8JZ/site/?key=statement"),

    # 2013
    ("Bytecomputer", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/3GXkVUEnWNZRn2C2VpX2uKmq/site/?key=statement"),
    ("Gdzie jest jedynka?", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/2TMZ0x-MC86QBBwLrqDfUVVd/site/?key=statement"),
    ("Colorful Chain", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/MAWN1VdLdXO29VvrVYuYxQyw/site/?key=statement"),
    ("Maze", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/TE77UNYEUxsFcrRxYRPc99na/site/?key=statement"),
    ("Laser", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/50NNSYZSygWhYhYv77iwZYP7/site/?key=statement"),
    ("Polarization", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/vG3DC9--8cjl4sPNwjBj9ag6/site/?key=statement"),

    # 2012
    ("Licytacja", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/deIZtcberd8cAXH64zlIq0wC/site/?key=statement"),
    ("Salaries", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/4nwnYqhu2gE6dB5aJUCiltnu/site/?key=statement"),
    ("Leveling Ground", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/ba-ep4dx0P4_GYxLz15iJVVm/site/?key=statement"),
    ("Bezpieczeństwo minimalistyczne", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/aSbIC_LB4H-CGMYPEVue5jFw/site/?key=statement"),
    ("Warehouse Store", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/hbT9J8hl2Xw1zWGJBsXN9aic/site/?key=statement"),
    ("Prefixsuffix", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/oFbHZH1QYy8yYlyN9AezBIZb/site/?key=statement"),

    # 2011
    ("Impreza", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/PCtteC6gKwc2ZikW8nUZzfyh/site/?key=statement"),
    ("Inspekcja", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/bLHHUzy1-byoiJSbilgpI6Dc/site/?key=statement"),
    ("Periodicity", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/FoRguPpW1-czheh8UD_LniGy/site/?key=statement"),
    ("Meteors", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/czzVm7v3I58TnPHzBgWiyELT/site/?key=statement"),
    ("Sticks", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/iqmKYlJL1Oz_sPCgi1BLqKRx/site/?key=statement"),
    ("Programming Contest", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/V5GPagFaNYlHkVBoXtHbbAxX/site/?key=statement"),

    # 2010
    ("The Minima Game", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/zGq2aLbEYfP96wuSl8SSYSGs/site/?key=statement"),
    ("Lamp", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/EncjSFKUGONaUWytbsYk6cSz/site/?key=statement"),
    ("Frog", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/VdGoo4AEt68ZDztfDsJ34iiP/site/?key=statement"),
    ("Ones", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/SYv6VGnZ_7dhrf9WwAJgWBk_/site/?key=statement"),
    ("Bridges", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/BKM4bb6_C3OZsScdRxzaed8N/site/?key=statement"),
    ("Pilots", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/4ZH1h7Wr18Yb7B0L7ym_Km0L/site/?key=statement"),

    # 2009
    ("Words 2", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/B6cy6tLhdE36fraSbG8Wl2_m/site/?key=statement"),
    ("Words", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/2_ADV6xog8RC2Gk3RVQaGQGI/site/?key=statement"),
    ("Tablice", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/_i0PmDyArk7mCW0eUJJzEVOA/site/?key=statement"),
    ("Island", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/6OBIhkGGyfsXCmGFAAe_JW2Y/site/?key=statement"),
    ("The Code", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/hAWG6xh9ehn2gjGUvkJ6qJmv/site/?key=statement"),
    ("Poszukiwania", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/IA0ujQ8R_JJmiyM9GAdxxfun/site/?key=statement"),

    # 2008
    ("Plot Purchase", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/KUCDVoRoWc5kQbNZPUrY5eYO/site/?key=statement"),
    ("Subdivision of Kingdom", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/a-E26wgLFqHZJv98qc9jQe2E/site/?key=statement"),
    ("Triangles", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/oFbVh8iOGlqNYUUueTt5V9N4/site/?key=statement"),
    ("Permutation", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/YQSokeBN7xK7z8KccTxjfeDk/site/?key=statement"),
    ("Stacja", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/7Pd1uIyue3oHambW1v-ADJDN/site/?key=statement"),

    # 2007
    ("Gas Pipelines", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/dPgIN7IwQ8JfKdyk3zTpUMiu/site/?key=statement"),
    ("Weights", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/h_QPStxSmfEHuL2h_I5Qpa29/site/?key=statement"),
    ("Egzamin na prawo jazdy", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/nLSrpyeJ1JnFGbBORYVVavIQ/site/?key=statement"),
    ("Klocki", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/dzRn8XS_ypGMFV-bqZLgBBB5/site/?key=statement"),
    ("Quaternary Balance", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/yAp_TKw6g0VUWE2TJfzia9y0/site/?key=statement"),

    # 2006
    ("Aesthetic Text", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/WPdj4dv7QzWPuqWA9FJi55k5/site/?key=statement"),
    ("Crystals", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/yR-PeT6cqju4_0heF5rfDbdJ/site/?key=statement"),
    ("Teddies", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/rjT2toimgFwJAHEb_-Lm75qm/site/?key=statement"),
    ("Palindromy", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/HZe8i5clz3sEyDRgoC0sYTaH/site/?key=statement"),
    ("Sophie", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Igfr_XfXWhPW-td_1TuZvWm1/site/?key=statement"),

    # 2005
    ("Special Forces", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Cyqv1x7xJRdcwj24GKoOZyl3/site/?key=statement"),
    ("Two Parties", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/VTgYcRFl4Fj0Z1o-SqFyaaD1/site/?key=statement"),
    ("Double-Row", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/TcT3eHfPGmUV2NmvzqyvVn9e/site/?key=statement"),
    ("The Bus", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/YBrY12KT6hTbgYrqwXhH3soW/site/?key=statement"),
    ("Mirror Trap", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/fNjmmASbl-0BUyNIqwXSwbyn/site/?key=statement"),
    ("Dextrogyrate Camel", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Ycgy3PbuMUIf8Cz2RdFpRCe4/site/?key=statement"),

    # 2004
    ("East-West", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/-Y8_7SoJ1a_l2Z5fBEgT71Fw/site/?key=statement"),
    ("The Islands", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/wPNHEHvCW-eLTl0dHA35gXfH/site/?key=statement"),
    ("C-Algae", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/mjS3vRIqO5DliMOK5FBq6Nn6/site/?key=statement"),
    ("Maximal Orders of Permutations", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/yGPiTBXT10gXduxMfkfZ93ix/site/?key=statement"),
    ("Misie-Patysie", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/8oUmi6G8bsCV8a3A6vhlV11O/site/?key=statement"),

    # 2003
    ("Treasure", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/7595YZE4SyxcB5Gx2JeLcVBH/site/?key=statement"),
    ("Sums", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/ROXsaseQWYR11jbNvCgM19Er/site/?key=statement"),
    ("Crystal", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/7JdjnsBuXMIYVUyiYNWmHUw_/site/?key=statement"),
    ("Monkeys", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/kd-sEDS37q_Q8vr-RjxBhw4p/site/?key=statement"),
    ("Shuffle", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/YKe-ENVFmXXLDpPXxKvhmB5Y/site/?key=statement"),

    # 2002
    ("Skiers", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/PUVCH73E4h3hU8UPiJqvvLmQ/site/?key=statement"),
    ("Balance", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/rM5z02XMy26GufAAAC03fjcB/site/?key=statement"),
    ("B-Smooth Numbers", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/VBw12Ev-eDIXnziDWIE9jqVX/site/?key=statement"),
    ("Brackets", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/7LNEawgnHXLp1Vi7uVyfgEW4/site/?key=statement"),
    ("Cipher", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/cBNmbxNBhgroqh5J3-bDmd7J/site/?key=statement"),

    # 2001
    ("Necklaces", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/xcfpiyLfEPRoh8rcD4TIEQPA/site/?key=statement"),
    ("Zwiedzanie miasta", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/rWYE5XwIo1j6GRd_Js7Jfv3U/site/?key=statement"),
    ("Bank", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/9LUSHZ-Xg-KBMNhZTJDajImi/site/?key=statement"),
    ("Goldmine", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/TYf8i2qvrGI0l8QHEYJXO5dG/site/?key=statement"),
    ("Chain", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/ePvi3FkYcJy9JsKUhJkEtFE_/site/?key=statement"),

    # 2000
    ("Jajka", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/hBOvw6FB18J-Rk7wPkcK-5_u/site/?key=statement"),
    ("P-Broken-Line", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/J9tLam0o-cxTbv4l-hIyG-jT/site/?key=statement"),
    ("Agents", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/5ngwR2pw5IQsTAOKQL3qFgjm/site/?key=statement"),
    ("Repetitions", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Ls-r_-OqMaX1vAEQJjyIdT5_/site/?key=statement"),
    ("Promotion", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/VD_bKhKPiYjm8uq-R8O1r88h/site/?key=statement"),

    # 1999
    ("Store-Keeper", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/i7RSA7WlQYQzXFjBLHIW5J3_/site/?key=statement"),
    ("Map", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/eM1NxQFB_0iFuv6hjK8VjaMz/site/?key=statement"),
    ("Altars", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/JR1lB-gdjNHcT5j3mtNRFhLa/site/?key=statement"),
    ("Primitivus", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/cNZAVjRjIqK6zEkU9pJsk-T5/site/?key=statement"),
    ("Water", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/VSHBP4X_iVq6D-6GZ3hLMW8u/site/?key=statement"),

    # 1998
    ("ATMs", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/6wWvqL0ucOaCSwAp9kf5wjK3/site/?key=statement"),
    ("Chase", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/u-kIHVk5n2hFoKGo7iA2ckWM/site/?key=statement"),
    ("The Lightest Language", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/9-tYuiHpeLAJBtw2vDdNgWbh/site/?key=statement"),
    ("Gra Ulama", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/si6uepnYG6tvH4BK2MHrgvbe/site/?key=statement"),
    ("Flat Broken Lines", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/pjxjyqtJe53guchEg4CnhvFN/site/?key=statement"),
    ("Rectangles", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/Pi-gX_dH2TzvdxTc74KjdHLo/site/?key=statement"),

    # 1997
    ("Canoes", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/qcEpw4SfiiE9VBmBrUz2LgW3/site/?key=statement"),
    ("The Number of n-k-Special Sets", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/tvDsyvSww77IiecR5AKcASbM/site/?key=statement"),
    ("Monochromatic Triangles", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/UU2Uj-barjiONnRxd9aEVoDj/site/?key=statement"),
    ("Ali Baba", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/kxtvaAcrnyJEN57F2bwEr4_1/site/?key=statement"),
    ("Lecture Halls Reservations", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/ex8U04OQav3BWcaH7wCtK-_b/site/?key=statement"),
    ("Skok w bok", 1, "POI", 2000, "https://szkopul.edu.pl/problemset/problem/WyYC56d39shbxS0QYZe8WqQI/site/?key=statement"),
]

problems = [dict(zip(fields, p)) for p in raw_problems]

db_path = os.getenv("DATABASE_PATH", "database.db")  # fallback to "database.db" if not set
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Clear existing problems
cur.execute("DELETE FROM problems")

for p in problems:
    cur.execute('''
        INSERT INTO problems (name, number, source, year, link)
        VALUES (?, ?, ?, ?, ?)
    ''', (p["name"], p["number"], p["source"], p["year"], p["link"]))

conn.commit()
conn.close()

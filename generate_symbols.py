"""
Generate a comprehensive Unicode symbols database.
This creates a properly-encoded JSON file with thousands of symbols.
"""
import json
import os

categories = []

# ============================================================
# 1. EMOJIS - Smileys & People
# ============================================================
emojis_smileys = {
    "id": "smileys",
    "name": "Smileys & Emotion",
    "icon": "\U0001F600",
    "symbols": []
}

smiley_data = [
    (0x1F600, "Grinning Face"),
    (0x1F601, "Beaming Face with Smiling Eyes"),
    (0x1F602, "Face with Tears of Joy"),
    (0x1F603, "Grinning Face with Big Eyes"),
    (0x1F604, "Grinning Face with Smiling Eyes"),
    (0x1F605, "Grinning Face with Sweat"),
    (0x1F606, "Grinning Squinting Face"),
    (0x1F607, "Smiling Face with Halo"),
    (0x1F608, "Smiling Face with Horns"),
    (0x1F609, "Winking Face"),
    (0x1F60A, "Smiling Face with Smiling Eyes"),
    (0x1F60B, "Face Savoring Food"),
    (0x1F60C, "Relieved Face"),
    (0x1F60D, "Smiling Face with Heart-Eyes"),
    (0x1F60E, "Smiling Face with Sunglasses"),
    (0x1F60F, "Smirking Face"),
    (0x1F610, "Neutral Face"),
    (0x1F611, "Expressionless Face"),
    (0x1F612, "Unamused Face"),
    (0x1F613, "Downcast Face with Sweat"),
    (0x1F614, "Pensive Face"),
    (0x1F615, "Confused Face"),
    (0x1F616, "Confounded Face"),
    (0x1F617, "Kissing Face"),
    (0x1F618, "Face Blowing a Kiss"),
    (0x1F619, "Kissing Face with Smiling Eyes"),
    (0x1F61A, "Kissing Face with Closed Eyes"),
    (0x1F61B, "Face with Tongue"),
    (0x1F61C, "Winking Face with Tongue"),
    (0x1F61D, "Squinting Face with Tongue"),
    (0x1F61E, "Disappointed Face"),
    (0x1F61F, "Worried Face"),
    (0x1F620, "Angry Face"),
    (0x1F621, "Pouting Face"),
    (0x1F622, "Crying Face"),
    (0x1F623, "Persevering Face"),
    (0x1F624, "Face with Steam From Nose"),
    (0x1F625, "Sad but Relieved Face"),
    (0x1F626, "Frowning Face with Open Mouth"),
    (0x1F627, "Anguished Face"),
    (0x1F628, "Fearful Face"),
    (0x1F629, "Weary Face"),
    (0x1F62A, "Sleepy Face"),
    (0x1F62B, "Tired Face"),
    (0x1F62C, "Grimacing Face"),
    (0x1F62D, "Loudly Crying Face"),
    (0x1F62E, "Face with Open Mouth"),
    (0x1F62F, "Hushed Face"),
    (0x1F630, "Anxious Face with Sweat"),
    (0x1F631, "Face Screaming in Fear"),
    (0x1F632, "Astonished Face"),
    (0x1F633, "Flushed Face"),
    (0x1F634, "Sleeping Face"),
    (0x1F635, "Face with Crossed-Out Eyes"),
    (0x1F636, "Face Without Mouth"),
    (0x1F637, "Face with Medical Mask"),
    (0x1F641, "Slightly Frowning Face"),
    (0x1F642, "Slightly Smiling Face"),
    (0x1F643, "Upside-Down Face"),
    (0x1F644, "Face with Rolling Eyes"),
    (0x1F910, "Zipper-Mouth Face"),
    (0x1F911, "Money-Mouth Face"),
    (0x1F912, "Face with Thermometer"),
    (0x1F913, "Nerd Face"),
    (0x1F914, "Thinking Face"),
    (0x1F915, "Face with Head-Bandage"),
    (0x1F916, "Robot"),
    (0x1F917, "Hugging Face"),
    (0x1F920, "Cowboy Hat Face"),
    (0x1F921, "Clown Face"),
    (0x1F922, "Nauseated Face"),
    (0x1F923, "Rolling on the Floor Laughing"),
    (0x1F924, "Drooling Face"),
    (0x1F925, "Lying Face"),
    (0x1F927, "Sneezing Face"),
    (0x1F928, "Face with Raised Eyebrow"),
    (0x1F929, "Star-Struck"),
    (0x1F92A, "Zany Face"),
    (0x1F92B, "Shushing Face"),
    (0x1F92C, "Face with Symbols on Mouth"),
    (0x1F92D, "Face with Hand Over Mouth"),
    (0x1F92E, "Face Vomiting"),
    (0x1F92F, "Exploding Head"),
    (0x1F970, "Smiling Face with Hearts"),
    (0x1F971, "Yawning Face"),
    (0x1F973, "Partying Face"),
    (0x1F974, "Woozy Face"),
    (0x1F975, "Hot Face"),
    (0x1F976, "Cold Face"),
    (0x1F97A, "Pleading Face"),
    (0x1F9D0, "Face with Monocle"),
    (0x1FAE0, "Melting Face"),
    (0x1FAE1, "Saluting Face"),
    (0x1FAE2, "Face with Open Eyes and Hand Over Mouth"),
    (0x1FAE3, "Face with Peeking Eye"),
    (0x1FAE4, "Face with Diagonal Mouth"),
    (0x1FAE5, "Dotted Line Face"),
    (0x263A, "Smiling Face"),
    (0x2639, "Frowning Face"),
]

for code, name in smiley_data:
    ch = chr(code)
    emojis_smileys["symbols"].append({
        "char": ch,
        "name": name,
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

categories.append(emojis_smileys)

# ============================================================
# 2. HEARTS & LOVE
# ============================================================
hearts = {
    "id": "hearts",
    "name": "Hearts & Love",
    "icon": "\u2764",
    "symbols": []
}

heart_data = [
    (0x2764, "Red Heart"),
    (0x1F493, "Beating Heart"),
    (0x1F494, "Broken Heart"),
    (0x1F495, "Two Hearts"),
    (0x1F496, "Sparkling Heart"),
    (0x1F497, "Growing Heart"),
    (0x1F498, "Heart with Arrow"),
    (0x1F499, "Blue Heart"),
    (0x1F49A, "Green Heart"),
    (0x1F49B, "Yellow Heart"),
    (0x1F49C, "Purple Heart"),
    (0x1F49D, "Heart with Ribbon"),
    (0x1F49E, "Revolving Hearts"),
    (0x1F49F, "Heart Decoration"),
    (0x1F5A4, "Black Heart"),
    (0x1F90D, "White Heart"),
    (0x1F90E, "Brown Heart"),
    (0x1F9E1, "Orange Heart"),
    (0x2763, "Heavy Heart Exclamation"),
    (0x2661, "White Heart Suit"),
    (0x2665, "Black Heart Suit"),
    (0x1F48B, "Kiss Mark"),
    (0x1F48C, "Love Letter"),
    (0x1F48D, "Ring"),
    (0x1F48E, "Gem Stone"),
    (0x1F48F, "Kiss"),
    (0x1F490, "Bouquet"),
    (0x1F491, "Couple with Heart"),
    (0x1F492, "Wedding"),
    (0x1F339, "Rose"),
    (0x1F33A, "Hibiscus"),
    (0x1F33B, "Sunflower"),
    (0x1F33C, "Blossom"),
    (0x1F337, "Tulip"),
    (0x1F940, "Wilted Flower"),
    (0x2618, "Shamrock"),
    (0x2740, "White Florette"),
    (0x2741, "Eight Petalled Outlined Black Florette"),
    (0x2742, "Six Petalled Black and White Florette"),
    (0x2743, "Heavy Four Balloon-Spoked Asterisk"),
    (0x273F, "Black Florette"),
]

for code, name in heart_data:
    ch = chr(code)
    hearts["symbols"].append({
        "char": ch,
        "name": name,
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

categories.append(hearts)

# ============================================================
# 3. HAND GESTURES & PEOPLE
# ============================================================
hands = {
    "id": "hands",
    "name": "Hands & Gestures",
    "icon": "\U0001F44D",
    "symbols": []
}

hand_data = [
    (0x1F44D, "Thumbs Up"),
    (0x1F44E, "Thumbs Down"),
    (0x1F44F, "Clapping Hands"),
    (0x1F450, "Open Hands"),
    (0x1F44A, "Oncoming Fist"),
    (0x1F44B, "Waving Hand"),
    (0x1F44C, "OK Hand"),
    (0x1F446, "Backhand Index Pointing Up"),
    (0x1F447, "Backhand Index Pointing Down"),
    (0x1F448, "Backhand Index Pointing Left"),
    (0x1F449, "Backhand Index Pointing Right"),
    (0x1F4AA, "Flexed Biceps"),
    (0x1F440, "Eyes"),
    (0x1F441, "Eye"),
    (0x1F442, "Ear"),
    (0x1F443, "Nose"),
    (0x1F444, "Mouth"),
    (0x1F445, "Tongue"),
    (0x1F590, "Hand with Fingers Splayed"),
    (0x1F596, "Vulcan Salute"),
    (0x1F64C, "Raising Hands"),
    (0x1F64F, "Folded Hands"),
    (0x1F91A, "Raised Back of Hand"),
    (0x1F91B, "Left-Facing Fist"),
    (0x1F91C, "Right-Facing Fist"),
    (0x1F91D, "Handshake"),
    (0x1F91E, "Crossed Fingers"),
    (0x1F91F, "Love-You Gesture"),
    (0x1F918, "Sign of the Horns"),
    (0x1F919, "Call Me Hand"),
    (0x1F930, "Pregnant Woman"),
    (0x1F934, "Prince"),
    (0x1F935, "Person in Tuxedo"),
    (0x1F936, "Mrs. Claus"),
    (0x1F937, "Person Shrugging"),
    (0x1F938, "Person Cartwheeling"),
    (0x1F64B, "Person Raising Hand"),
    (0x1F64D, "Person Frowning"),
    (0x1F64E, "Person Pouting"),
    (0x1F647, "Person Bowing"),
    (0x1F926, "Person Facepalming"),
    (0x270A, "Raised Fist"),
    (0x270B, "Raised Hand"),
    (0x270C, "Victory Hand"),
    (0x270D, "Writing Hand"),
    (0x261D, "Index Pointing Up"),
]

for code, name in hand_data:
    ch = chr(code)
    hands["symbols"].append({
        "char": ch,
        "name": name,
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

categories.append(hands)

# ============================================================
# 4. ANIMALS & NATURE
# ============================================================
animals = {
    "id": "animals",
    "name": "Animals & Nature",
    "icon": "\U0001F43E",
    "symbols": []
}

animal_data = [
    (0x1F400, "Rat"), (0x1F401, "Mouse"), (0x1F402, "Ox"), (0x1F403, "Water Buffalo"),
    (0x1F404, "Cow"), (0x1F405, "Tiger"), (0x1F406, "Leopard"), (0x1F407, "Rabbit"),
    (0x1F408, "Cat"), (0x1F409, "Dragon"), (0x1F40A, "Crocodile"), (0x1F40B, "Whale"),
    (0x1F40C, "Snail"), (0x1F40D, "Snake"), (0x1F40E, "Horse"), (0x1F40F, "Ram"),
    (0x1F410, "Goat"), (0x1F411, "Ewe"), (0x1F412, "Monkey"), (0x1F413, "Rooster"),
    (0x1F414, "Chicken"), (0x1F415, "Dog"), (0x1F416, "Pig"), (0x1F417, "Boar"),
    (0x1F418, "Elephant"), (0x1F419, "Octopus"), (0x1F41A, "Spiral Shell"),
    (0x1F41B, "Bug"), (0x1F41C, "Ant"), (0x1F41D, "Honeybee"), (0x1F41E, "Lady Beetle"),
    (0x1F41F, "Fish"), (0x1F420, "Tropical Fish"), (0x1F421, "Blowfish"),
    (0x1F422, "Turtle"), (0x1F423, "Hatching Chick"), (0x1F424, "Baby Chick"),
    (0x1F425, "Front-Facing Baby Chick"), (0x1F426, "Bird"), (0x1F427, "Penguin"),
    (0x1F428, "Koala"), (0x1F429, "Poodle"), (0x1F42A, "Camel"), (0x1F42B, "Two-Hump Camel"),
    (0x1F42C, "Dolphin"), (0x1F42D, "Mouse Face"), (0x1F42E, "Cow Face"),
    (0x1F42F, "Tiger Face"), (0x1F430, "Rabbit Face"), (0x1F431, "Cat Face"),
    (0x1F432, "Dragon Face"), (0x1F433, "Spouting Whale"), (0x1F434, "Horse Face"),
    (0x1F435, "Monkey Face"), (0x1F436, "Dog Face"), (0x1F437, "Pig Face"),
    (0x1F438, "Frog"), (0x1F439, "Hamster"), (0x1F43A, "Wolf"),
    (0x1F43B, "Bear"), (0x1F43C, "Panda"), (0x1F43D, "Pig Nose"),
    (0x1F43E, "Paw Prints"), (0x1F43F, "Chipmunk"),
    (0x1F981, "Lion"), (0x1F982, "Scorpion"), (0x1F983, "Turkey"),
    (0x1F984, "Unicorn"), (0x1F985, "Eagle"), (0x1F986, "Duck"),
    (0x1F987, "Bat"), (0x1F988, "Shark"), (0x1F989, "Owl"),
    (0x1F98A, "Fox"), (0x1F98B, "Butterfly"), (0x1F98C, "Deer"),
    (0x1F98D, "Gorilla"), (0x1F98E, "Lizard"), (0x1F98F, "Rhinoceros"),
    (0x1F990, "Shrimp"), (0x1F991, "Squid"), (0x1F992, "Giraffe"),
    (0x1F993, "Zebra"), (0x1F994, "Hedgehog"), (0x1F995, "Sauropod"),
    (0x1F996, "T-Rex"), (0x1F997, "Cricket"), (0x1F998, "Kangaroo"),
    (0x1F999, "Llama"), (0x1F99A, "Peacock"), (0x1F99B, "Hippopotamus"),
    (0x1F99C, "Parrot"), (0x1F99D, "Raccoon"), (0x1F99E, "Lobster"),
    (0x1F99F, "Mosquito"), (0x1F9A0, "Microbe"), (0x1F9A1, "Badger"),
    (0x1F9A2, "Swan"), (0x1F9A5, "Sloth"), (0x1F9A6, "Otter"),
    (0x1F9A7, "Orangutan"), (0x1F9A8, "Skunk"), (0x1F9A9, "Flamingo"),
    (0x1F9AB, "Beaver"), (0x1F9AC, "Bison"), (0x1F9AD, "Seal"),
    # Nature
    (0x1F331, "Seedling"), (0x1F332, "Evergreen Tree"), (0x1F333, "Deciduous Tree"),
    (0x1F334, "Palm Tree"), (0x1F335, "Cactus"), (0x1F33E, "Sheaf of Rice"),
    (0x1F33F, "Herb"), (0x1F340, "Four Leaf Clover"), (0x1F341, "Maple Leaf"),
    (0x1F342, "Fallen Leaf"), (0x1F343, "Leaf Fluttering in Wind"),
    (0x1F344, "Mushroom"), (0x1F490, "Bouquet"),
    (0x2618, "Shamrock"),
]

for code, name in animal_data:
    ch = chr(code)
    animals["symbols"].append({
        "char": ch,
        "name": name,
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

categories.append(animals)

# ============================================================
# 5. ARROWS (comprehensive)
# ============================================================
arrows = {
    "id": "arrows",
    "name": "Arrows",
    "icon": "\u2192",
    "symbols": []
}

arrow_data = [
    # Basic arrows
    (0x2190, "Leftwards Arrow"), (0x2191, "Upwards Arrow"),
    (0x2192, "Rightwards Arrow"), (0x2193, "Downwards Arrow"),
    (0x2194, "Left Right Arrow"), (0x2195, "Up Down Arrow"),
    (0x2196, "North West Arrow"), (0x2197, "North East Arrow"),
    (0x2198, "South East Arrow"), (0x2199, "South West Arrow"),
    (0x219A, "Leftwards Arrow with Stroke"), (0x219B, "Rightwards Arrow with Stroke"),
    (0x219C, "Leftwards Wave Arrow"), (0x219D, "Rightwards Wave Arrow"),
    (0x219E, "Leftwards Two Headed Arrow"), (0x219F, "Upwards Two Headed Arrow"),
    (0x21A0, "Rightwards Two Headed Arrow"), (0x21A1, "Downwards Two Headed Arrow"),
    (0x21A2, "Leftwards Arrow with Tail"), (0x21A3, "Rightwards Arrow with Tail"),
    (0x21A4, "Leftwards Arrow from Bar"), (0x21A5, "Upwards Arrow from Bar"),
    (0x21A6, "Rightwards Arrow from Bar"), (0x21A7, "Downwards Arrow from Bar"),
    (0x21A8, "Up Down Arrow with Base"),
    (0x21A9, "Leftwards Arrow with Hook"), (0x21AA, "Rightwards Arrow with Hook"),
    (0x21AB, "Leftwards Arrow with Loop"), (0x21AC, "Rightwards Arrow with Loop"),
    (0x21AD, "Left Right Wave Arrow"), (0x21AE, "Left Right Arrow with Stroke"),
    (0x21AF, "Downwards Zigzag Arrow"),
    (0x21B0, "Upwards Arrow with Tip Leftwards"), (0x21B1, "Upwards Arrow with Tip Rightwards"),
    (0x21B2, "Downwards Arrow with Tip Leftwards"), (0x21B3, "Downwards Arrow with Tip Rightwards"),
    (0x21B4, "Rightwards Arrow with Corner Downwards"), (0x21B5, "Downwards Arrow with Corner Leftwards"),
    (0x21B6, "Anticlockwise Top Semicircle Arrow"), (0x21B7, "Clockwise Top Semicircle Arrow"),
    (0x21B8, "North West Arrow to Long Bar"), (0x21B9, "Leftwards Arrow to Bar over Rightwards Arrow to Bar"),
    (0x21BA, "Anticlockwise Open Circle Arrow"), (0x21BB, "Clockwise Open Circle Arrow"),
    (0x21BC, "Leftwards Harpoon with Barb Upwards"), (0x21BD, "Leftwards Harpoon with Barb Downwards"),
    (0x21BE, "Upwards Harpoon with Barb Rightwards"), (0x21BF, "Upwards Harpoon with Barb Leftwards"),
    (0x21C0, "Rightwards Harpoon with Barb Upwards"), (0x21C1, "Rightwards Harpoon with Barb Downwards"),
    (0x21C2, "Downwards Harpoon with Barb Rightwards"), (0x21C3, "Downwards Harpoon with Barb Leftwards"),
    (0x21C4, "Rightwards Arrow over Leftwards Arrow"), (0x21C5, "Upwards Arrow Leftwards of Downwards Arrow"),
    (0x21C6, "Leftwards Arrow over Rightwards Arrow"), (0x21C7, "Leftwards Paired Arrows"),
    (0x21C8, "Upwards Paired Arrows"), (0x21C9, "Rightwards Paired Arrows"),
    (0x21CA, "Downwards Paired Arrows"),
    # Double arrows
    (0x21D0, "Leftwards Double Arrow"), (0x21D1, "Upwards Double Arrow"),
    (0x21D2, "Rightwards Double Arrow"), (0x21D3, "Downwards Double Arrow"),
    (0x21D4, "Left Right Double Arrow"), (0x21D5, "Up Down Double Arrow"),
    (0x21D6, "North West Double Arrow"), (0x21D7, "North East Double Arrow"),
    (0x21D8, "South East Double Arrow"), (0x21D9, "South West Double Arrow"),
    (0x21DA, "Leftwards Triple Arrow"), (0x21DB, "Rightwards Triple Arrow"),
    (0x21DC, "Leftwards Squiggle Arrow"), (0x21DD, "Rightwards Squiggle Arrow"),
    (0x21E0, "Leftwards Dashed Arrow"), (0x21E1, "Upwards Dashed Arrow"),
    (0x21E2, "Rightwards Dashed Arrow"), (0x21E3, "Downwards Dashed Arrow"),
    (0x21E4, "Leftwards Arrow to Bar"), (0x21E5, "Rightwards Arrow to Bar"),
    (0x21E6, "Leftwards White Arrow"), (0x21E7, "Upwards White Arrow"),
    (0x21E8, "Rightwards White Arrow"), (0x21E9, "Downwards White Arrow"),
    # Dingbat arrows
    (0x2794, "Heavy Wide-Headed Rightwards Arrow"),
    (0x2799, "Heavy Rightwards Arrow"),
    (0x279A, "Heavy Rightwards Arrow with Tail"),
    (0x279B, "Drafting Point Rightwards Arrow"),
    (0x279C, "Heavy Round-Tipped Rightwards Arrow"),
    (0x279D, "Triangle-Headed Rightwards Arrow"),
    (0x279E, "Heavy Triangle-Headed Rightwards Arrow"),
    (0x279F, "Dashed Triangle-Headed Rightwards Arrow"),
    (0x27A0, "Heavy Dashed Triangle-Headed Rightwards Arrow"),
    (0x27A1, "Black Rightwards Arrow"),
    (0x27A2, "Three-D Top-Lighted Rightwards Arrowhead"),
    (0x27A3, "Three-D Bottom-Lighted Rightwards Arrowhead"),
    (0x27A4, "Black Rightwards Arrowhead"),
    (0x27B2, "Circled Heavy White Rightwards Arrow"),
    # Block arrows
    (0x2B05, "Leftwards Black Arrow"), (0x2B06, "Upwards Black Arrow"),
    (0x2B07, "Downwards Black Arrow"), (0x2B08, "North East Black Arrow"),
    (0x2B09, "North West Black Arrow"), (0x2B0A, "South East Black Arrow"),
    (0x2B0B, "South West Black Arrow"),
    (0x27F0, "Upwards Quadruple Arrow"), (0x27F1, "Downwards Quadruple Arrow"),
    (0x27F2, "Anticlockwise Gapped Circle Arrow"), (0x27F3, "Clockwise Gapped Circle Arrow"),
    (0x27F5, "Long Leftwards Arrow"), (0x27F6, "Long Rightwards Arrow"),
    (0x27F7, "Long Left Right Arrow"), (0x27F8, "Long Leftwards Double Arrow"),
    (0x27F9, "Long Rightwards Double Arrow"), (0x27FA, "Long Left Right Double Arrow"),
    (0x21F5, "Downwards Arrow Leftwards of Upwards Arrow"),
]

for code, name in arrow_data:
    try:
        ch = chr(code)
        arrows["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})
    except: pass

categories.append(arrows)

# ============================================================
# 6. MATH SYMBOLS (comprehensive)
# ============================================================
math = {
    "id": "math",
    "name": "Math Symbols",
    "icon": "\u2211",
    "symbols": []
}

math_data = [
    (0x002B, "Plus Sign"), (0x2212, "Minus Sign"), (0x00D7, "Multiplication Sign"),
    (0x00F7, "Division Sign"), (0x003D, "Equals Sign"), (0x2260, "Not Equal To"),
    (0x2248, "Almost Equal To"), (0x2261, "Identical To"), (0x2264, "Less-Than or Equal To"),
    (0x2265, "Greater-Than or Equal To"), (0x003C, "Less-Than Sign"), (0x003E, "Greater-Than Sign"),
    (0x00B1, "Plus-Minus Sign"), (0x2213, "Minus-or-Plus Sign"),
    (0x221E, "Infinity"), (0x221A, "Square Root"), (0x221B, "Cube Root"), (0x221C, "Fourth Root"),
    (0x2211, "N-Ary Summation"), (0x220F, "N-Ary Product"), (0x2210, "N-Ary Coproduct"),
    (0x222B, "Integral"), (0x222C, "Double Integral"), (0x222D, "Triple Integral"),
    (0x222E, "Contour Integral"), (0x222F, "Surface Integral"), (0x2230, "Volume Integral"),
    (0x2202, "Partial Differential"), (0x2207, "Nabla"),
    (0x2200, "For All"), (0x2203, "There Exists"), (0x2204, "There Does Not Exist"),
    (0x2205, "Empty Set"), (0x2208, "Element Of"), (0x2209, "Not an Element Of"),
    (0x220A, "Small Element Of"), (0x220B, "Contains as Member"), (0x220C, "Does Not Contain"),
    (0x222A, "Union"), (0x2229, "Intersection"),
    (0x2282, "Subset Of"), (0x2283, "Superset Of"), (0x2284, "Not a Subset Of"),
    (0x2285, "Not a Superset Of"), (0x2286, "Subset of or Equal To"),
    (0x2287, "Superset of or Equal To"), (0x228A, "Subset with Not Equal To"),
    (0x228B, "Superset with Not Equal To"),
    (0x2227, "Logical And"), (0x2228, "Logical Or"), (0x00AC, "Not Sign"),
    (0x2295, "Circled Plus"), (0x2296, "Circled Minus"), (0x2297, "Circled Times"),
    (0x2298, "Circled Division Slash"), (0x2299, "Circled Dot"),
    (0x22A5, "Up Tack (Perpendicular)"), (0x22A4, "Down Tack"),
    (0x2220, "Angle"), (0x2221, "Measured Angle"), (0x2222, "Spherical Angle"),
    (0x221F, "Right Angle"), (0x00B0, "Degree Sign"),
    (0x221D, "Proportional To"), (0x2234, "Therefore"), (0x2235, "Because"),
    (0x223C, "Tilde Operator"), (0x2243, "Asymptotically Equal To"),
    (0x2245, "Approximately Equal To"), (0x2247, "Neither Approximately nor Actually Equal To"),
    (0x224D, "Equivalent To"), (0x2250, "Approaches the Limit"),
    (0x2254, "Colon Equals"), (0x2255, "Equals Colon"),
    (0x226A, "Much Less-Than"), (0x226B, "Much Greater-Than"),
    (0x2270, "Neither Less-Than nor Equal To"), (0x2271, "Neither Greater-Than nor Equal To"),
    (0x22C5, "Dot Operator"), (0x22C6, "Star Operator"),
    (0x00B7, "Middle Dot"), (0x2217, "Asterisk Operator"),
    (0x2218, "Ring Operator"), (0x2219, "Bullet Operator"),
    # Greek letters
    (0x03B1, "Alpha"), (0x03B2, "Beta"), (0x03B3, "Gamma"), (0x03B4, "Delta"),
    (0x03B5, "Epsilon"), (0x03B6, "Zeta"), (0x03B7, "Eta"), (0x03B8, "Theta"),
    (0x03B9, "Iota"), (0x03BA, "Kappa"), (0x03BB, "Lambda"), (0x03BC, "Mu"),
    (0x03BD, "Nu"), (0x03BE, "Xi"), (0x03BF, "Omicron"), (0x03C0, "Pi"),
    (0x03C1, "Rho"), (0x03C3, "Sigma"), (0x03C4, "Tau"), (0x03C5, "Upsilon"),
    (0x03C6, "Phi"), (0x03C7, "Chi"), (0x03C8, "Psi"), (0x03C9, "Omega"),
    (0x0391, "Capital Alpha"), (0x0392, "Capital Beta"), (0x0393, "Capital Gamma"),
    (0x0394, "Capital Delta"), (0x0395, "Capital Epsilon"), (0x0396, "Capital Zeta"),
    (0x0397, "Capital Eta"), (0x0398, "Capital Theta"), (0x0399, "Capital Iota"),
    (0x039A, "Capital Kappa"), (0x039B, "Capital Lambda"), (0x039C, "Capital Mu"),
    (0x039D, "Capital Nu"), (0x039E, "Capital Xi"), (0x039F, "Capital Omicron"),
    (0x03A0, "Capital Pi"), (0x03A1, "Capital Rho"), (0x03A3, "Capital Sigma"),
    (0x03A4, "Capital Tau"), (0x03A5, "Capital Upsilon"), (0x03A6, "Capital Phi"),
    (0x03A7, "Capital Chi"), (0x03A8, "Capital Psi"), (0x03A9, "Capital Omega"),
    # Subscripts and superscripts
    (0x00B2, "Superscript Two"), (0x00B3, "Superscript Three"), (0x00B9, "Superscript One"),
    (0x2070, "Superscript Zero"), (0x2074, "Superscript Four"), (0x2075, "Superscript Five"),
    (0x2076, "Superscript Six"), (0x2077, "Superscript Seven"), (0x2078, "Superscript Eight"),
    (0x2079, "Superscript Nine"), (0x207A, "Superscript Plus"), (0x207B, "Superscript Minus"),
    (0x2080, "Subscript Zero"), (0x2081, "Subscript One"), (0x2082, "Subscript Two"),
    (0x2083, "Subscript Three"), (0x2084, "Subscript Four"), (0x2085, "Subscript Five"),
    (0x2086, "Subscript Six"), (0x2087, "Subscript Seven"), (0x2088, "Subscript Eight"),
    (0x2089, "Subscript Nine"), (0x208A, "Subscript Plus"), (0x208B, "Subscript Minus"),
    # Number forms
    (0x00BC, "Fraction One Quarter"), (0x00BD, "Fraction One Half"), (0x00BE, "Fraction Three Quarters"),
    (0x2150, "Fraction One Seventh"), (0x2151, "Fraction One Ninth"), (0x2152, "Fraction One Tenth"),
    (0x2153, "Fraction One Third"), (0x2154, "Fraction Two Thirds"),
    (0x2155, "Fraction One Fifth"), (0x2156, "Fraction Two Fifths"),
    (0x2157, "Fraction Three Fifths"), (0x2158, "Fraction Four Fifths"),
    (0x2159, "Fraction One Sixth"), (0x215A, "Fraction Five Sixths"),
    (0x215B, "Fraction One Eighth"), (0x215C, "Fraction Three Eighths"),
    (0x215D, "Fraction Five Eighths"), (0x215E, "Fraction Seven Eighths"),
    (0x2030, "Per Mille Sign"), (0x2031, "Per Ten Thousand Sign"),
    (0x2032, "Prime"), (0x2033, "Double Prime"), (0x2034, "Triple Prime"),
]

for code, name in math_data:
    ch = chr(code)
    math["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(math)

# ============================================================
# 7. CURRENCY SYMBOLS
# ============================================================
currency = {
    "id": "currency",
    "name": "Currency Symbols",
    "icon": "$",
    "symbols": []
}

currency_data = [
    (0x0024, "Dollar Sign"), (0x00A2, "Cent Sign"), (0x00A3, "Pound Sign"),
    (0x00A4, "Currency Sign"), (0x00A5, "Yen Sign"), (0x058F, "Armenian Dram"),
    (0x060B, "Afghani Sign"), (0x09F3, "Bengali Rupee Sign"),
    (0x0BF9, "Tamil Rupee Sign"), (0x0E3F, "Thai Baht Sign"),
    (0x17DB, "Khmer Currency Symbol"),
    (0x20A0, "Euro-Currency Sign"), (0x20A1, "Colon Sign"), (0x20A2, "Cruzeiro Sign"),
    (0x20A3, "French Franc Sign"), (0x20A4, "Lira Sign"), (0x20A5, "Mill Sign"),
    (0x20A6, "Naira Sign"), (0x20A7, "Peseta Sign"), (0x20A8, "Rupee Sign"),
    (0x20A9, "Won Sign"), (0x20AA, "New Sheqel Sign"), (0x20AB, "Dong Sign"),
    (0x20AC, "Euro Sign"), (0x20AD, "Kip Sign"), (0x20AE, "Tugrik Sign"),
    (0x20AF, "Drachma Sign"), (0x20B0, "German Penny Sign"), (0x20B1, "Peso Sign"),
    (0x20B2, "Guarani Sign"), (0x20B3, "Austral Sign"), (0x20B4, "Hryvnia Sign"),
    (0x20B5, "Cedi Sign"), (0x20B6, "Livre Tournois Sign"), (0x20B7, "Spesmilo Sign"),
    (0x20B8, "Tenge Sign"), (0x20B9, "Indian Rupee Sign"), (0x20BA, "Turkish Lira Sign"),
    (0x20BB, "Nordic Mark Sign"), (0x20BC, "Manat Sign"), (0x20BD, "Ruble Sign"),
    (0x20BE, "Lari Sign"), (0x20BF, "Bitcoin Sign"),
    (0xFDFC, "Rial Sign"),
]

for code, name in currency_data:
    ch = chr(code)
    currency["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(currency)

# ============================================================
# 8. PUNCTUATION & TYPOGRAPHY
# ============================================================
punctuation = {
    "id": "punctuation",
    "name": "Punctuation & Typography",
    "icon": "\u00B6",
    "symbols": []
}

punct_data = [
    (0x2014, "Em Dash"), (0x2013, "En Dash"), (0x2012, "Figure Dash"),
    (0x2015, "Horizontal Bar"), (0x2026, "Horizontal Ellipsis"),
    (0x2022, "Bullet"), (0x2023, "Triangular Bullet"), (0x2043, "Hyphen Bullet"),
    (0x00B7, "Middle Dot"), (0x00B6, "Pilcrow Sign"), (0x00A7, "Section Sign"),
    (0x2020, "Dagger"), (0x2021, "Double Dagger"),
    (0x00A9, "Copyright Sign"), (0x00AE, "Registered Sign"), (0x2122, "Trade Mark Sign"),
    (0x2120, "Service Mark"),
    (0x00AB, "Left Double Angle Quotation Mark"), (0x00BB, "Right Double Angle Quotation Mark"),
    (0x2018, "Left Single Quotation Mark"), (0x2019, "Right Single Quotation Mark"),
    (0x201A, "Single Low-9 Quotation Mark"), (0x201B, "Single High-Reversed-9 Quotation Mark"),
    (0x201C, "Left Double Quotation Mark"), (0x201D, "Right Double Quotation Mark"),
    (0x201E, "Double Low-9 Quotation Mark"), (0x201F, "Double High-Reversed-9 Quotation Mark"),
    (0x2039, "Single Left Angle Quotation Mark"), (0x203A, "Single Right Angle Quotation Mark"),
    (0x00A1, "Inverted Exclamation Mark"), (0x00BF, "Inverted Question Mark"),
    (0x203D, "Interrobang"), (0x2042, "Asterism"), (0x2116, "Numero Sign"),
    (0x204A, "Tironian Et Sign"), (0x204B, "Reversed Pilcrow Sign"),
    (0x203B, "Reference Mark"), (0x2040, "Character Tie"),
    (0x2010, "Hyphen"), (0x2011, "Non-Breaking Hyphen"),
    (0x2016, "Double Vertical Line"), (0x2017, "Double Low Line"),
    (0x2024, "One Dot Leader"), (0x2025, "Two Dot Leader"),
    (0x2027, "Hyphenation Point"), (0x2032, "Prime"), (0x2033, "Double Prime"),
    (0x2035, "Reversed Prime"), (0x2036, "Reversed Double Prime"),
    (0x2038, "Caret"), (0x203E, "Overline"),
    (0x00A0, "No-Break Space"), (0x00AD, "Soft Hyphen"),
    (0x2044, "Fraction Slash"), (0x204E, "Low Asterisk"),
    (0x2052, "Commercial Minus Sign"),
    (0x2053, "Swung Dash"), (0x2057, "Quadruple Prime"),
]

for code, name in punct_data:
    ch = chr(code)
    punctuation["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(punctuation)

# ============================================================
# 9. SHAPES & GEOMETRIC
# ============================================================
shapes = {
    "id": "shapes",
    "name": "Shapes & Geometric",
    "icon": "\u25A0",
    "symbols": []
}

shape_data = [
    (0x25A0, "Black Square"), (0x25A1, "White Square"),
    (0x25A2, "White Square with Rounded Corners"), (0x25A3, "White Square Containing Small Black Square"),
    (0x25AA, "Black Small Square"), (0x25AB, "White Small Square"),
    (0x25AC, "Black Rectangle"), (0x25AD, "White Rectangle"),
    (0x25B2, "Black Up-Pointing Triangle"), (0x25B3, "White Up-Pointing Triangle"),
    (0x25B4, "Black Up-Pointing Small Triangle"), (0x25B5, "White Up-Pointing Small Triangle"),
    (0x25B6, "Black Right-Pointing Triangle"), (0x25B7, "White Right-Pointing Triangle"),
    (0x25BA, "Black Right-Pointing Pointer"), (0x25BB, "White Right-Pointing Pointer"),
    (0x25BC, "Black Down-Pointing Triangle"), (0x25BD, "White Down-Pointing Triangle"),
    (0x25C0, "Black Left-Pointing Triangle"), (0x25C1, "White Left-Pointing Triangle"),
    (0x25C4, "Black Left-Pointing Pointer"), (0x25C5, "White Left-Pointing Pointer"),
    (0x25C6, "Black Diamond"), (0x25C7, "White Diamond"),
    (0x25C8, "White Diamond Containing Small Black Diamond"),
    (0x25C9, "Fisheye"), (0x25CA, "Lozenge"),
    (0x25CB, "White Circle"), (0x25CC, "Dotted Circle"),
    (0x25CF, "Black Circle"), (0x25CE, "Bullseye"),
    (0x25D0, "Circle with Left Half Black"), (0x25D1, "Circle with Right Half Black"),
    (0x25D2, "Circle with Lower Half Black"), (0x25D3, "Circle with Upper Half Black"),
    (0x25D4, "Circle with Upper Right Quadrant Black"),
    (0x25D5, "Circle with All but Upper Left Quadrant Black"),
    (0x25D8, "Inverse Bullet"), (0x25D9, "Inverse White Circle"),
    (0x25E2, "Black Lower Right Triangle"), (0x25E3, "Black Lower Left Triangle"),
    (0x25E4, "Black Upper Left Triangle"), (0x25E5, "Black Upper Right Triangle"),
    (0x25EF, "Large Circle"),
    (0x2605, "Black Star"), (0x2606, "White Star"),
    (0x2726, "Black Four Pointed Star"), (0x2727, "White Four Pointed Star"),
    (0x2729, "Stress Outlined White Star"),
    (0x272A, "Circled White Star"), (0x272B, "Open Centre Black Star"),
    (0x272C, "Black Centre White Star"), (0x272D, "Outlined Black Star"),
    (0x272E, "Heavy Outlined Black Star"), (0x272F, "Pinwheel Star"),
    (0x2730, "Shadowed White Star"), (0x2731, "Heavy Asterisk"),
    (0x2732, "Open Centre Asterisk"), (0x2733, "Eight Spoked Asterisk"),
    (0x2734, "Eight Pointed Black Star"), (0x2735, "Eight Pointed Pinwheel Star"),
    (0x2736, "Six Pointed Black Star"), (0x2737, "Eight Pointed Rectilinear Black Star"),
    (0x2738, "Heavy Eight Pointed Rectilinear Black Star"),
    (0x2739, "Twelve Pointed Black Star"),
    (0x273A, "Sixteen Pointed Asterisk"), (0x2756, "Black Diamond Minus White X"),
    (0x2B1A, "Dotted Square"), (0x2B1B, "Black Large Square"), (0x2B1C, "White Large Square"),
    (0x2B50, "White Medium Star"), (0x2B55, "Heavy Large Circle"),
    # Card suits
    (0x2660, "Black Spade Suit"), (0x2661, "White Heart Suit"),
    (0x2662, "White Diamond Suit"), (0x2663, "Black Club Suit"),
    (0x2664, "White Spade Suit"), (0x2665, "Black Heart Suit"),
    (0x2666, "Black Diamond Suit"), (0x2667, "White Club Suit"),
    # Dice
    (0x2680, "Die Face-1"), (0x2681, "Die Face-2"), (0x2682, "Die Face-3"),
    (0x2683, "Die Face-4"), (0x2684, "Die Face-5"), (0x2685, "Die Face-6"),
    # Check marks
    (0x2713, "Check Mark"), (0x2714, "Heavy Check Mark"),
    (0x2715, "Multiplication X"), (0x2716, "Heavy Multiplication X"),
    (0x2717, "Ballot X"), (0x2718, "Heavy Ballot X"),
    (0x271A, "Heavy Greek Cross"), (0x271B, "Open Centre Cross"),
    (0x271C, "Heavy Open Centre Cross"),
    # Music
    (0x2669, "Quarter Note"), (0x266A, "Eighth Note"),
    (0x266B, "Beamed Eighth Notes"), (0x266C, "Beamed Sixteenth Notes"),
    (0x266D, "Music Flat Sign"), (0x266E, "Music Natural Sign"), (0x266F, "Music Sharp Sign"),
    # Misc
    (0x25EF, "Large Circle"),
    (0x2744, "Snowflake"), (0x2745, "Tight Trifoliate Snowflake"), (0x2746, "Heavy Chevron Snowflake"),
    (0x2747, "Sparkle"), (0x2748, "Heavy Sparkle"),
    (0x274B, "Heavy Eight Teardrop-Spoked Propeller Asterisk"),
    (0x274C, "Cross Mark"), (0x274E, "Cross Mark with Shadow"),
    (0x275B, "Heavy Single Turned Comma Quotation Mark"),
    (0x275C, "Heavy Single Comma Quotation Mark"),
    (0x275D, "Heavy Double Turned Comma Quotation Mark"),
    (0x275E, "Heavy Double Comma Quotation Mark"),
]

for code, name in shape_data:
    ch = chr(code)
    shapes["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(shapes)

# ============================================================
# 10. TECHNICAL & MISCELLANEOUS
# ============================================================
technical = {
    "id": "technical",
    "name": "Technical & Miscellaneous",
    "icon": "\u2318",
    "symbols": []
}

tech_data = [
    (0x2318, "Command Key"), (0x2325, "Option Key"), (0x21E7, "Shift Key"),
    (0x2303, "Control Key"), (0x238B, "Escape Key"), (0x23CE, "Return Symbol"),
    (0x232B, "Erase to the Left (Delete)"), (0x21E5, "Tab Key"),
    (0x21EA, "Caps Lock"), (0x2328, "Keyboard"), (0x2423, "Open Box (Space)"),
    (0x2326, "Erase to the Right"), (0x21DE, "Page Up"), (0x21DF, "Page Down"),
    # Weather / Astro
    (0x2600, "Black Sun with Rays"), (0x2601, "Cloud"), (0x2602, "Umbrella"),
    (0x2603, "Snowman"), (0x2604, "Comet"), (0x2605, "Black Star"), (0x2606, "White Star"),
    (0x2607, "Lightning"), (0x2608, "Thunderstorm"),
    (0x260E, "Black Telephone"), (0x260F, "White Telephone"),
    (0x2610, "Ballot Box"), (0x2611, "Ballot Box with Check"), (0x2612, "Ballot Box with X"),
    # Zodiac
    (0x2648, "Aries"), (0x2649, "Taurus"), (0x264A, "Gemini"), (0x264B, "Cancer"),
    (0x264C, "Leo"), (0x264D, "Virgo"), (0x264E, "Libra"), (0x264F, "Scorpio"),
    (0x2650, "Sagittarius"), (0x2651, "Capricorn"), (0x2652, "Aquarius"), (0x2653, "Pisces"),
    # Planets
    (0x2609, "Sun"), (0x263D, "First Quarter Moon"), (0x263E, "Last Quarter Moon"),
    (0x2640, "Female Sign"), (0x2642, "Male Sign"),
    # Symbols
    (0x262E, "Peace Symbol"), (0x262F, "Yin Yang"),
    (0x2622, "Radioactive Sign"), (0x2623, "Biohazard Sign"),
    (0x2624, "Caduceus"), (0x2625, "Ankh"),
    (0x2626, "Orthodox Cross"), (0x2627, "Chi Rho"),
    (0x2628, "Cross of Lorraine"), (0x2629, "Cross of Jerusalem"),
    (0x262A, "Star and Crescent"), (0x262B, "Farsi Symbol"),
    (0x262C, "Adi Shakti"), (0x262D, "Hammer and Sickle"),
    (0x2638, "Wheel of Dharma"), (0x2721, "Star of David"),
    (0x271D, "Latin Cross"), (0x2720, "Maltese Cross"),
    # Warning / misc
    (0x26A0, "Warning Sign"), (0x26A1, "High Voltage Sign"),
    (0x2699, "Gear"), (0x269B, "Atom Symbol"), (0x269C, "Fleur-de-lis"),
    (0x2696, "Scales"), (0x2694, "Crossed Swords"),
    (0x2690, "White Flag"), (0x2691, "Black Flag"),
    (0x267B, "Recycling Symbol"), (0x267F, "Wheelchair Symbol"),
    (0x2695, "Staff of Aesculapius"), (0x2698, "Flower"),
    (0x269A, "Staff of Hermes"),
    (0x2709, "Envelope"), (0x270E, "Lower Right Pencil"),
    (0x270F, "Pencil"), (0x2710, "Upper Right Pencil"),
    (0x2711, "White Nib"), (0x2712, "Black Nib"),
    (0x2702, "Black Scissors"), (0x2704, "White Scissors"),
    (0x2615, "Hot Beverage"), (0x231A, "Watch"), (0x231B, "Hourglass"),
    (0x2614, "Umbrella with Rain Drops"), (0x2618, "Shamrock"),
    (0x261D, "White Up Pointing Index"),
    (0x2620, "Skull and Crossbones"), (0x2621, "Caution Sign"),
    (0x26AA, "Medium White Circle"), (0x26AB, "Medium Black Circle"),
    (0x26BD, "Soccer Ball"), (0x26BE, "Baseball"),
    (0x26C4, "Snowman without Snow"),  (0x26C5, "Sun Behind Cloud"),
    (0x26CE, "Ophiuchus"), (0x26D4, "No Entry"),
    (0x26EA, "Church"), (0x26F2, "Fountain"), (0x26F3, "Flag in Hole"),
    (0x26F5, "Sailboat"), (0x26FA, "Tent"), (0x26FD, "Fuel Pump"),
]

for code, name in tech_data:
    ch = chr(code)
    technical["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(technical)

# ============================================================
# 11. BOX DRAWING & BLOCKS
# ============================================================
box_drawing = {
    "id": "box-drawing",
    "name": "Box Drawing & Blocks",
    "icon": "\u250C",
    "symbols": []
}

# Box drawing chars U+2500 - U+257F
box_names = {
    0x2500: "Light Horizontal", 0x2501: "Heavy Horizontal",
    0x2502: "Light Vertical", 0x2503: "Heavy Vertical",
    0x2504: "Light Triple Dash Horizontal", 0x2505: "Heavy Triple Dash Horizontal",
    0x2506: "Light Triple Dash Vertical", 0x2507: "Heavy Triple Dash Vertical",
    0x2508: "Light Quadruple Dash Horizontal", 0x2509: "Heavy Quadruple Dash Horizontal",
    0x250A: "Light Quadruple Dash Vertical", 0x250B: "Heavy Quadruple Dash Vertical",
    0x250C: "Light Down and Right", 0x250D: "Down Light and Right Heavy",
    0x250E: "Down Heavy and Right Light", 0x250F: "Heavy Down and Right",
    0x2510: "Light Down and Left", 0x2511: "Down Light and Left Heavy",
    0x2512: "Down Heavy and Left Light", 0x2513: "Heavy Down and Left",
    0x2514: "Light Up and Right", 0x2515: "Up Light and Right Heavy",
    0x2516: "Up Heavy and Right Light", 0x2517: "Heavy Up and Right",
    0x2518: "Light Up and Left", 0x2519: "Up Light and Left Heavy",
    0x251A: "Up Heavy and Left Light", 0x251B: "Heavy Up and Left",
    0x251C: "Light Vertical and Right", 0x2524: "Light Vertical and Left",
    0x252C: "Light Down and Horizontal", 0x2534: "Light Up and Horizontal",
    0x253C: "Light Vertical and Horizontal",
    0x2550: "Double Horizontal", 0x2551: "Double Vertical",
    0x2552: "Down Single and Right Double", 0x2553: "Down Double and Right Single",
    0x2554: "Double Down and Right", 0x2555: "Down Single and Left Double",
    0x2556: "Down Double and Left Single", 0x2557: "Double Down and Left",
    0x2558: "Up Single and Right Double", 0x2559: "Up Double and Right Single",
    0x255A: "Double Up and Right", 0x255B: "Up Single and Left Double",
    0x255C: "Up Double and Left Single", 0x255D: "Double Up and Left",
    0x255E: "Vertical Single and Right Double", 0x255F: "Vertical Double and Right Single",
    0x2560: "Double Vertical and Right", 0x2561: "Vertical Single and Left Double",
    0x2562: "Vertical Double and Left Single", 0x2563: "Double Vertical and Left",
    0x2564: "Down Single and Horizontal Double", 0x2565: "Down Double and Horizontal Single",
    0x2566: "Double Down and Horizontal", 0x2567: "Up Single and Horizontal Double",
    0x2568: "Up Double and Horizontal Single", 0x2569: "Double Up and Horizontal",
    0x256A: "Vertical Single and Horizontal Double",
    0x256B: "Vertical Double and Horizontal Single",
    0x256C: "Double Vertical and Horizontal",
}

for code, name in sorted(box_names.items()):
    ch = chr(code)
    box_drawing["symbols"].append({"char": ch, "name": f"Box Drawings {name}", "unicode": f"U+{code:04X}", "html": f"&#{code};"})

# Block elements
block_data = [
    (0x2580, "Upper Half Block"), (0x2581, "Lower One Eighth Block"),
    (0x2582, "Lower One Quarter Block"), (0x2583, "Lower Three Eighths Block"),
    (0x2584, "Lower Half Block"), (0x2585, "Lower Five Eighths Block"),
    (0x2586, "Lower Three Quarters Block"), (0x2587, "Lower Seven Eighths Block"),
    (0x2588, "Full Block"), (0x2589, "Left Seven Eighths Block"),
    (0x258A, "Left Three Quarters Block"), (0x258B, "Left Five Eighths Block"),
    (0x258C, "Left Half Block"), (0x258D, "Left Three Eighths Block"),
    (0x258E, "Left One Quarter Block"), (0x258F, "Left One Eighth Block"),
    (0x2590, "Right Half Block"),
    (0x2591, "Light Shade"), (0x2592, "Medium Shade"), (0x2593, "Dark Shade"),
    (0x2594, "Upper One Eighth Block"), (0x2595, "Right One Eighth Block"),
]

for code, name in block_data:
    ch = chr(code)
    box_drawing["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(box_drawing)

# ============================================================
# 12. EMOJI OBJECTS & ACTIVITIES
# ============================================================
objects = {
    "id": "objects",
    "name": "Objects & Activities",
    "icon": "\U0001F3AF",
    "symbols": []
}

obj_data = [
    (0x1F4A1, "Light Bulb"), (0x1F4A2, "Anger Symbol"), (0x1F4A3, "Bomb"),
    (0x1F4A4, "Zzz"), (0x1F4A5, "Collision"), (0x1F4A6, "Sweat Droplets"),
    (0x1F4A7, "Droplet"), (0x1F4A8, "Dashing Away"), (0x1F4A9, "Pile of Poo"),
    (0x1F4AA, "Flexed Biceps"), (0x1F4AB, "Dizzy"), (0x1F4AC, "Speech Balloon"),
    (0x1F4AD, "Thought Balloon"), (0x1F4AE, "White Flower"), (0x1F4AF, "Hundred Points"),
    (0x1F4B0, "Money Bag"), (0x1F4B1, "Currency Exchange"), (0x1F4B2, "Heavy Dollar Sign"),
    (0x1F4B3, "Credit Card"), (0x1F4B4, "Yen Banknote"), (0x1F4B5, "Dollar Banknote"),
    (0x1F4B8, "Money with Wings"), (0x1F4BB, "Laptop"), (0x1F4BC, "Briefcase"),
    (0x1F4BD, "Computer Disk"), (0x1F4BE, "Floppy Disk"), (0x1F4BF, "Optical Disk"),
    (0x1F4C0, "DVD"), (0x1F4C1, "File Folder"), (0x1F4C2, "Open File Folder"),
    (0x1F4C3, "Page with Curl"), (0x1F4C4, "Page Facing Up"), (0x1F4C5, "Calendar"),
    (0x1F4CB, "Clipboard"), (0x1F4CC, "Pushpin"), (0x1F4CD, "Round Pushpin"),
    (0x1F4CE, "Paperclip"), (0x1F4CF, "Straight Ruler"), (0x1F4D0, "Triangular Ruler"),
    (0x1F4D1, "Bookmark Tabs"), (0x1F4D2, "Ledger"), (0x1F4D3, "Notebook"),
    (0x1F4D4, "Notebook with Decorative Cover"), (0x1F4D5, "Closed Book"),
    (0x1F4D6, "Open Book"), (0x1F4D7, "Green Book"), (0x1F4D8, "Blue Book"),
    (0x1F4D9, "Orange Book"), (0x1F4DA, "Books"), (0x1F4DB, "Name Badge"),
    (0x1F4DC, "Scroll"), (0x1F4DD, "Memo"), (0x1F4DE, "Telephone Receiver"),
    (0x1F4DF, "Pager"), (0x1F4E0, "Fax Machine"), (0x1F4E1, "Satellite Antenna"),
    (0x1F4E2, "Loudspeaker"), (0x1F4E3, "Megaphone"), (0x1F4E4, "Outbox Tray"),
    (0x1F4E5, "Inbox Tray"), (0x1F4E6, "Package"), (0x1F4E7, "E-Mail"),
    (0x1F4E8, "Incoming Envelope"), (0x1F4E9, "Envelope with Arrow"),
    (0x1F4EA, "Closed Mailbox with Lowered Flag"), (0x1F4EB, "Closed Mailbox with Raised Flag"),
    (0x1F4F0, "Newspaper"), (0x1F4F1, "Mobile Phone"), (0x1F4F2, "Mobile Phone with Arrow"),
    (0x1F4F7, "Camera"), (0x1F4F9, "Video Camera"), (0x1F4FA, "Television"),
    (0x1F4FB, "Radio"), (0x1F4FC, "Videocassette"),
    (0x1F525, "Fire"), (0x1F526, "Flashlight"), (0x1F527, "Wrench"),
    (0x1F528, "Hammer"), (0x1F529, "Nut and Bolt"), (0x1F52A, "Kitchen Knife"),
    (0x1F52B, "Pistol"), (0x1F52C, "Microscope"), (0x1F52D, "Telescope"),
    (0x1F52E, "Crystal Ball"), (0x1F52F, "Six Pointed Star with Middle Dot"),
    (0x1F530, "Japanese Symbol for Beginner"),
    (0x1F3A8, "Artist Palette"), (0x1F3AC, "Clapper Board"), (0x1F3AD, "Performing Arts"),
    (0x1F3AE, "Video Game"), (0x1F3AF, "Bullseye"), (0x1F3B0, "Slot Machine"),
    (0x1F3B1, "Pool 8 Ball"), (0x1F3B2, "Game Die"), (0x1F3B3, "Bowling"),
    (0x1F3B4, "Flower Playing Cards"), (0x1F3B5, "Musical Note"),
    (0x1F3B6, "Musical Notes"), (0x1F3B7, "Saxophone"), (0x1F3B8, "Guitar"),
    (0x1F3B9, "Musical Keyboard"), (0x1F3BA, "Trumpet"), (0x1F3BB, "Violin"),
    (0x1F3BC, "Musical Score"),
    (0x1F389, "Party Popper"), (0x1F38A, "Confetti Ball"),
    (0x1F38B, "Tanabata Tree"), (0x1F38C, "Crossed Flags"),
    (0x1F38D, "Pine Decoration"), (0x1F38E, "Japanese Dolls"),
    (0x1F38F, "Carp Streamer"), (0x1F390, "Wind Chime"),
    (0x1F391, "Moon Viewing Ceremony"), (0x1F380, "Ribbon"),
    (0x1F381, "Wrapped Gift"), (0x1F382, "Birthday Cake"),
    (0x1F383, "Jack-O-Lantern"), (0x1F384, "Christmas Tree"),
    (0x1F386, "Fireworks"), (0x1F387, "Sparkler"),
    (0x1F388, "Balloon"),
    (0x2B50, "Star"), (0x1F31F, "Glowing Star"), (0x2728, "Sparkles"),
    # Food
    (0x1F34E, "Red Apple"), (0x1F34F, "Green Apple"), (0x1F34A, "Tangerine"),
    (0x1F34B, "Lemon"), (0x1F34C, "Banana"), (0x1F34D, "Pineapple"),
    (0x1F347, "Grapes"), (0x1F348, "Melon"), (0x1F349, "Watermelon"),
    (0x1F350, "Pear"), (0x1F351, "Peach"), (0x1F352, "Cherries"),
    (0x1F353, "Strawberry"), (0x1F345, "Tomato"), (0x1F346, "Eggplant"),
    (0x1F354, "Hamburger"), (0x1F355, "Pizza"), (0x1F356, "Meat on Bone"),
    (0x1F357, "Poultry Leg"), (0x1F35E, "Bread"), (0x1F35F, "French Fries"),
    (0x1F363, "Sushi"), (0x1F36A, "Cookie"), (0x1F36B, "Chocolate Bar"),
    (0x1F36C, "Candy"), (0x1F36D, "Lollipop"), (0x1F36E, "Custard"),
    (0x1F370, "Shortcake"), (0x1F377, "Wine Glass"), (0x1F378, "Cocktail Glass"),
    (0x1F379, "Tropical Drink"), (0x1F37A, "Beer Mug"), (0x1F37B, "Clinking Beer Mugs"),
    (0x2615, "Hot Beverage"),
]

for code, name in obj_data:
    ch = chr(code)
    objects["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(objects)

# ============================================================
# 13. TRAVEL & PLACES
# ============================================================
travel = {
    "id": "travel",
    "name": "Travel & Places",
    "icon": "\U0001F30D",
    "symbols": []
}

travel_data = [
    (0x1F30D, "Globe Europe-Africa"), (0x1F30E, "Globe Americas"),
    (0x1F30F, "Globe Asia-Australia"), (0x1F310, "Globe with Meridians"),
    (0x1F311, "New Moon"), (0x1F312, "Waxing Crescent Moon"),
    (0x1F313, "First Quarter Moon"), (0x1F314, "Waxing Gibbous Moon"),
    (0x1F315, "Full Moon"), (0x1F316, "Waning Gibbous Moon"),
    (0x1F317, "Last Quarter Moon"), (0x1F318, "Waning Crescent Moon"),
    (0x1F319, "Crescent Moon"), (0x1F31A, "New Moon Face"),
    (0x1F31B, "First Quarter Moon Face"), (0x1F31C, "Last Quarter Moon Face"),
    (0x1F31D, "Full Moon Face"), (0x1F31E, "Sun with Face"),
    (0x1F320, "Shooting Star"), (0x1F308, "Rainbow"),
    (0x26C5, "Sun Behind Cloud"), (0x1F324, "Sun Behind Small Cloud"),
    (0x1F325, "Sun Behind Large Cloud"), (0x1F326, "Sun Behind Rain Cloud"),
    (0x1F327, "Cloud with Rain"), (0x1F328, "Cloud with Snow"),
    (0x1F329, "Cloud with Lightning"), (0x1F32A, "Tornado"),
    (0x1F32B, "Fog"), (0x1F32C, "Wind Face"),
    (0x1F3D4, "Snow-Capped Mountain"), (0x1F3D5, "Camping"),
    (0x1F3D6, "Beach with Umbrella"), (0x1F3D7, "Building Construction"),
    (0x1F3D8, "Houses"), (0x1F3D9, "Cityscape"),
    (0x1F3DA, "Derelict House"), (0x1F3DB, "Classical Building"),
    (0x1F3DC, "Desert"), (0x1F3DD, "Desert Island"),
    (0x1F3DE, "National Park"), (0x1F3DF, "Stadium"),
    (0x1F3E0, "House"), (0x1F3E1, "House with Garden"),
    (0x1F3E2, "Office Building"), (0x1F3E3, "Japanese Post Office"),
    (0x1F3E5, "Hospital"), (0x1F3E6, "Bank"),
    (0x1F3E8, "Hotel"), (0x1F3EA, "Convenience Store"),
    (0x1F3EB, "School"), (0x1F3EC, "Department Store"),
    (0x1F3ED, "Factory"), (0x1F3EF, "Japanese Castle"),
    (0x1F3F0, "Castle"),
    # Vehicles
    (0x1F680, "Rocket"), (0x1F681, "Helicopter"), (0x1F682, "Locomotive"),
    (0x1F683, "Railway Car"), (0x1F684, "High-Speed Train"),
    (0x1F685, "Bullet Train"), (0x1F686, "Train"),
    (0x1F687, "Metro"), (0x1F688, "Light Rail"),
    (0x1F689, "Station"), (0x1F68C, "Bus"),
    (0x1F690, "Minibus"), (0x1F691, "Ambulance"),
    (0x1F692, "Fire Engine"), (0x1F693, "Police Car"),
    (0x1F695, "Taxi"), (0x1F697, "Automobile"),
    (0x1F699, "Sport Utility Vehicle"), (0x1F69A, "Delivery Truck"),
    (0x1F69B, "Articulated Lorry"), (0x1F69C, "Tractor"),
    (0x1F6A2, "Ship"), (0x1F6A4, "Speedboat"),
    (0x1F6A5, "Horizontal Traffic Light"), (0x1F6A6, "Vertical Traffic Light"),
    (0x1F6A7, "Construction"), (0x1F6A8, "Police Car Light"),
    (0x1F6B2, "Bicycle"), (0x1F6F3, "Passenger Ship"),
    (0x1F6F4, "Kick Scooter"), (0x1F6F5, "Motor Scooter"),
    (0x1F6F6, "Canoe"), (0x1F6F7, "Sled"),
    (0x1F6F8, "Flying Saucer"), (0x1F6F9, "Skateboard"),
    (0x1F6FA, "Auto Rickshaw"), (0x2708, "Airplane"),
    (0x26F5, "Sailboat"), (0x26FD, "Fuel Pump"),
]

for code, name in travel_data:
    ch = chr(code)
    travel["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(travel)

# ============================================================
# 14. FLAGS & COUNTRY
# ============================================================
flags = {
    "id": "flags",
    "name": "Flags & Symbols",
    "icon": "\U0001F3F3",
    "symbols": []
}

flag_data = [
    (0x1F3F3, "White Flag"), (0x1F3F4, "Black Flag"),
    (0x1F3C1, "Chequered Flag"), (0x1F6A9, "Triangular Flag"),
    (0x1F38C, "Crossed Flags"),
    # Warning signs
    (0x26A0, "Warning"), (0x26D4, "No Entry"), (0x26AB, "Black Circle"),
    (0x26AA, "White Circle"), (0x1F6AB, "Prohibited"),
    (0x1F6B3, "No Bicycles"), (0x1F6AD, "No Smoking"),
    (0x1F6AE, "Litter in Bin Sign"), (0x1F6AF, "No Littering"),
    (0x1F6B0, "Potable Water"), (0x1F6B1, "Non-Potable Water"),
    (0x1F6B7, "No Pedestrians"), (0x1F6B8, "Children Crossing"),
    (0x1F6B9, "Mens Symbol"), (0x1F6BA, "Womens Symbol"),
    (0x1F6BB, "Restroom"), (0x1F6BC, "Baby Symbol"),
    (0x1F6BE, "Water Closet"), (0x1F6C2, "Passport Control"),
    (0x1F6C3, "Customs"), (0x1F6C4, "Baggage Claim"),
    (0x1F6C5, "Left Luggage"),
    # CJK symbols
    (0x1F250, "Japanese Bargain Button"), (0x1F251, "Japanese Acceptable Button"),
    (0x1F004, "Mahjong Red Dragon"), (0x1F0CF, "Joker"),
    (0x3030, "Wavy Dash"), (0x303D, "Part Alternation Mark"),
    (0x2B55, "Heavy Large Circle"), (0x2B1B, "Black Large Square"),
    (0x2B1C, "White Large Square"),
    (0x1F534, "Red Circle"), (0x1F535, "Blue Circle"),
    (0x1F536, "Large Orange Diamond"), (0x1F537, "Large Blue Diamond"),
    (0x1F538, "Small Orange Diamond"), (0x1F539, "Small Blue Diamond"),
    (0x1F53A, "Red Triangle Pointed Up"), (0x1F53B, "Red Triangle Pointed Down"),
    (0x1F4A0, "Diamond with a Dot"),
    (0x1F518, "Radio Button"), (0x1F519, "Back Arrow"),
    (0x1F51A, "End Arrow"), (0x1F51B, "On! Arrow"),
    (0x1F51C, "Soon Arrow"), (0x1F51D, "Top Arrow"),
]

for code, name in flag_data:
    ch = chr(code)
    flags["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(flags)

# ============================================================
# 15. LETTERLIKE SYMBOLS
# ============================================================
letterlike = {
    "id": "letterlike",
    "name": "Letterlike & Number Forms",
    "icon": "\u2115",
    "symbols": []
}

letter_data = [
    (0x2100, "Account Of"), (0x2101, "Addressed to the Subject"),
    (0x2102, "Double-Struck Capital C"), (0x2103, "Degree Celsius"),
    (0x2104, "Centre Line Symbol"), (0x2105, "Care Of"),
    (0x2106, "Cada Una"), (0x2107, "Euler Constant"),
    (0x2108, "Scruple"), (0x2109, "Degree Fahrenheit"),
    (0x210A, "Script Small G"), (0x210B, "Script Capital H"),
    (0x210C, "Black-Letter Capital H"), (0x210D, "Double-Struck Capital H"),
    (0x210E, "Planck Constant"), (0x210F, "Planck Constant over Two Pi"),
    (0x2110, "Script Capital I"), (0x2111, "Black-Letter Capital I"),
    (0x2112, "Script Capital L"), (0x2113, "Script Small L"),
    (0x2115, "Double-Struck Capital N"), (0x2116, "Numero Sign"),
    (0x2117, "Sound Recording Copyright"), (0x2118, "Weierstrass Elliptic Function"),
    (0x2119, "Double-Struck Capital P"), (0x211A, "Double-Struck Capital Q"),
    (0x211B, "Script Capital R"), (0x211C, "Black-Letter Capital R"),
    (0x211D, "Double-Struck Capital R"), (0x211E, "Prescription Take"),
    (0x2124, "Double-Struck Capital Z"),
    (0x2126, "Ohm Sign"), (0x2127, "Inverted Ohm Sign"),
    (0x2128, "Black-Letter Capital Z"), (0x2129, "Turned Greek Small Letter Iota"),
    (0x212A, "Kelvin Sign"), (0x212B, "Angstrom Sign"),
    (0x212C, "Script Capital B"), (0x212D, "Black-Letter Capital C"),
    (0x212F, "Script Small E"), (0x2130, "Script Capital E"),
    (0x2131, "Script Capital F"), (0x2133, "Script Capital M"),
    (0x2134, "Script Small O"), (0x2135, "Alef Symbol"),
    (0x2136, "Bet Symbol"), (0x2137, "Gimel Symbol"), (0x2138, "Dalet Symbol"),
    (0x2139, "Information Source"),
    # Roman numerals
    (0x2160, "Roman Numeral One"), (0x2161, "Roman Numeral Two"),
    (0x2162, "Roman Numeral Three"), (0x2163, "Roman Numeral Four"),
    (0x2164, "Roman Numeral Five"), (0x2165, "Roman Numeral Six"),
    (0x2166, "Roman Numeral Seven"), (0x2167, "Roman Numeral Eight"),
    (0x2168, "Roman Numeral Nine"), (0x2169, "Roman Numeral Ten"),
    (0x216A, "Roman Numeral Eleven"), (0x216B, "Roman Numeral Twelve"),
    (0x216C, "Roman Numeral Fifty"), (0x216D, "Roman Numeral One Hundred"),
    (0x216E, "Roman Numeral Five Hundred"), (0x216F, "Roman Numeral One Thousand"),
    # Small roman
    (0x2170, "Small Roman Numeral One"), (0x2171, "Small Roman Numeral Two"),
    (0x2172, "Small Roman Numeral Three"), (0x2173, "Small Roman Numeral Four"),
    (0x2174, "Small Roman Numeral Five"), (0x2175, "Small Roman Numeral Six"),
    (0x2176, "Small Roman Numeral Seven"), (0x2177, "Small Roman Numeral Eight"),
    (0x2178, "Small Roman Numeral Nine"), (0x2179, "Small Roman Numeral Ten"),
    # Enclosed alphanumerics
    (0x24B6, "Circled Latin Capital Letter A"), (0x24B7, "Circled Latin Capital Letter B"),
    (0x24B8, "Circled Latin Capital Letter C"), (0x24B9, "Circled Latin Capital Letter D"),
    (0x24BA, "Circled Latin Capital Letter E"),
    (0x24C1, "Circled Latin Capital Letter L"),
    (0x24C4, "Circled Latin Capital Letter O"),
    (0x24C8, "Circled Latin Capital Letter S"),
    (0x24D0, "Circled Latin Small Letter A"), (0x24D1, "Circled Latin Small Letter B"),
    (0x24D2, "Circled Latin Small Letter C"),
    # Circled numbers
    (0x2460, "Circled Digit One"), (0x2461, "Circled Digit Two"),
    (0x2462, "Circled Digit Three"), (0x2463, "Circled Digit Four"),
    (0x2464, "Circled Digit Five"), (0x2465, "Circled Digit Six"),
    (0x2466, "Circled Digit Seven"), (0x2467, "Circled Digit Eight"),
    (0x2468, "Circled Digit Nine"), (0x2469, "Circled Number Ten"),
    (0x246A, "Circled Number Eleven"), (0x246B, "Circled Number Twelve"),
    (0x246C, "Circled Number Thirteen"), (0x246D, "Circled Number Fourteen"),
    (0x246E, "Circled Number Fifteen"), (0x246F, "Circled Number Sixteen"),
    (0x2470, "Circled Number Seventeen"), (0x2471, "Circled Number Eighteen"),
    (0x2472, "Circled Number Nineteen"), (0x2473, "Circled Number Twenty"),
]

for code, name in letter_data:
    ch = chr(code)
    letterlike["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(letterlike)

# ============================================================
# 16. BRAILLE PATTERNS
# ============================================================
braille = {
    "id": "braille",
    "name": "Braille Patterns",
    "icon": "\u2803",
    "symbols": []
}

braille_names = [
    "Blank", "Dots-1", "Dots-2", "Dots-12", "Dots-3", "Dots-13", "Dots-23", "Dots-123",
    "Dots-4", "Dots-14", "Dots-24", "Dots-124", "Dots-34", "Dots-134", "Dots-234", "Dots-1234",
    "Dots-5", "Dots-15", "Dots-25", "Dots-125", "Dots-35", "Dots-135", "Dots-235", "Dots-1235",
    "Dots-45", "Dots-145", "Dots-245", "Dots-1245", "Dots-345", "Dots-1345", "Dots-2345", "Dots-12345",
    "Dots-6", "Dots-16", "Dots-26", "Dots-126", "Dots-36", "Dots-136", "Dots-236", "Dots-1236",
    "Dots-46", "Dots-146", "Dots-246", "Dots-1246", "Dots-346", "Dots-1346", "Dots-2346", "Dots-12346",
    "Dots-56", "Dots-156", "Dots-256", "Dots-1256", "Dots-356", "Dots-1356", "Dots-2356", "Dots-12356",
    "Dots-456", "Dots-1456", "Dots-2456", "Dots-12456", "Dots-3456", "Dots-13456", "Dots-23456", "Dots-123456",
]

for i, name in enumerate(braille_names):
    code = 0x2800 + i
    ch = chr(code)
    braille["symbols"].append({
        "char": ch,
        "name": f"Braille Pattern {name}",
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

categories.append(braille)

# ============================================================
# 17. DINGBATS & ORNAMENTS
# ============================================================
dingbats = {
    "id": "dingbats",
    "name": "Dingbats & Ornaments",
    "icon": "\u2766",
    "symbols": []
}

ding_data = [
    (0x2701, "Upper Blade Scissors"), (0x2702, "Black Scissors"),
    (0x2703, "Lower Blade Scissors"), (0x2704, "White Scissors"),
    (0x2706, "Telephone Location Sign"), (0x2707, "Tape Drive"),
    (0x2708, "Airplane"), (0x2709, "Envelope"),
    (0x270C, "Victory Hand"), (0x270D, "Writing Hand"),
    (0x270E, "Lower Right Pencil"), (0x270F, "Pencil"),
    (0x2710, "Upper Right Pencil"), (0x2711, "White Nib"),
    (0x2712, "Black Nib"),
    (0x2740, "White Florette"), (0x2741, "Eight Petalled Black Florette"),
    (0x2742, "Six Petalled Black and White Florette"),
    (0x2743, "Heavy Four Balloon-Spoked Asterisk"),
    (0x2744, "Snowflake"), (0x2745, "Tight Trifoliate Snowflake"),
    (0x2746, "Heavy Chevron Snowflake"),
    (0x2747, "Sparkle"), (0x2748, "Heavy Sparkle"),
    (0x2749, "Balloon-Spoked Asterisk"),
    (0x274A, "Eight Teardrop-Spoked Propeller Asterisk"),
    (0x274B, "Heavy Eight Teardrop-Spoked Propeller Asterisk"),
    (0x2750, "Upper Right Drop-Shadowed White Square"),
    (0x2751, "Lower Right Shadowed White Square"),
    (0x2752, "Upper Right Shadowed White Square"),
    (0x2756, "Black Diamond Minus White X"),
    (0x2758, "Light Vertical Bar"), (0x2759, "Medium Vertical Bar"),
    (0x275A, "Heavy Vertical Bar"),
    (0x2761, "Curved Stem Paragraph Sign Ornament"),
    (0x2762, "Heavy Exclamation Mark Ornament"),
    (0x2763, "Heavy Heart Exclamation Mark Ornament"),
    (0x2764, "Heavy Black Heart"),
    (0x2765, "Rotated Heavy Black Heart Bullet"),
    (0x2766, "Floral Heart"), (0x2767, "Rotated Floral Heart Bullet"),
    (0x2776, "Dingbat Negative Circled Digit One"),
    (0x2777, "Dingbat Negative Circled Digit Two"),
    (0x2778, "Dingbat Negative Circled Digit Three"),
    (0x2779, "Dingbat Negative Circled Digit Four"),
    (0x277A, "Dingbat Negative Circled Digit Five"),
    (0x277B, "Dingbat Negative Circled Digit Six"),
    (0x277C, "Dingbat Negative Circled Digit Seven"),
    (0x277D, "Dingbat Negative Circled Digit Eight"),
    (0x277E, "Dingbat Negative Circled Digit Nine"),
    (0x277F, "Dingbat Negative Circled Number Ten"),
    (0x2780, "Dingbat Circled Sans-Serif Digit One"),
    (0x2781, "Dingbat Circled Sans-Serif Digit Two"),
    (0x2782, "Dingbat Circled Sans-Serif Digit Three"),
    (0x2783, "Dingbat Circled Sans-Serif Digit Four"),
    (0x2784, "Dingbat Circled Sans-Serif Digit Five"),
    (0x2785, "Dingbat Circled Sans-Serif Digit Six"),
    (0x2786, "Dingbat Circled Sans-Serif Digit Seven"),
    (0x2787, "Dingbat Circled Sans-Serif Digit Eight"),
    (0x2788, "Dingbat Circled Sans-Serif Digit Nine"),
    (0x2789, "Dingbat Circled Sans-Serif Number Ten"),
    (0x278A, "Dingbat Negative Circled Sans-Serif Digit One"),
    (0x278B, "Dingbat Negative Circled Sans-Serif Digit Two"),
    (0x278C, "Dingbat Negative Circled Sans-Serif Digit Three"),
    (0x278D, "Dingbat Negative Circled Sans-Serif Digit Four"),
    (0x278E, "Dingbat Negative Circled Sans-Serif Digit Five"),
    (0x278F, "Dingbat Negative Circled Sans-Serif Digit Six"),
    (0x2790, "Dingbat Negative Circled Sans-Serif Digit Seven"),
    (0x2791, "Dingbat Negative Circled Sans-Serif Digit Eight"),
    (0x2792, "Dingbat Negative Circled Sans-Serif Digit Nine"),
    (0x2793, "Dingbat Negative Circled Sans-Serif Number Ten"),
]

for code, name in ding_data:
    ch = chr(code)
    dingbats["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(dingbats)

# ============================================================
# 18. LATIN EXTENDED & ACCENTED
# ============================================================
latin = {
    "id": "latin",
    "name": "Latin Extended & Accented",
    "icon": "\u00C9",
    "symbols": []
}

latin_data = [
    (0x00C0, "A with Grave"), (0x00C1, "A with Acute"), (0x00C2, "A with Circumflex"),
    (0x00C3, "A with Tilde"), (0x00C4, "A with Diaeresis"), (0x00C5, "A with Ring Above"),
    (0x00C6, "AE Ligature"), (0x00C7, "C with Cedilla"),
    (0x00C8, "E with Grave"), (0x00C9, "E with Acute"),
    (0x00CA, "E with Circumflex"), (0x00CB, "E with Diaeresis"),
    (0x00CC, "I with Grave"), (0x00CD, "I with Acute"),
    (0x00CE, "I with Circumflex"), (0x00CF, "I with Diaeresis"),
    (0x00D0, "Eth"), (0x00D1, "N with Tilde"),
    (0x00D2, "O with Grave"), (0x00D3, "O with Acute"),
    (0x00D4, "O with Circumflex"), (0x00D5, "O with Tilde"),
    (0x00D6, "O with Diaeresis"), (0x00D8, "O with Stroke"),
    (0x00D9, "U with Grave"), (0x00DA, "U with Acute"),
    (0x00DB, "U with Circumflex"), (0x00DC, "U with Diaeresis"),
    (0x00DD, "Y with Acute"), (0x00DE, "Thorn"),
    (0x00DF, "Sharp S (Eszett)"),
    (0x00E0, "a with Grave"), (0x00E1, "a with Acute"),
    (0x00E2, "a with Circumflex"), (0x00E3, "a with Tilde"),
    (0x00E4, "a with Diaeresis"), (0x00E5, "a with Ring Above"),
    (0x00E6, "ae Ligature"), (0x00E7, "c with Cedilla"),
    (0x00E8, "e with Grave"), (0x00E9, "e with Acute"),
    (0x00EA, "e with Circumflex"), (0x00EB, "e with Diaeresis"),
    (0x00EC, "i with Grave"), (0x00ED, "i with Acute"),
    (0x00EE, "i with Circumflex"), (0x00EF, "i with Diaeresis"),
    (0x00F0, "eth"), (0x00F1, "n with Tilde"),
    (0x00F2, "o with Grave"), (0x00F3, "o with Acute"),
    (0x00F4, "o with Circumflex"), (0x00F5, "o with Tilde"),
    (0x00F6, "o with Diaeresis"), (0x00F8, "o with Stroke"),
    (0x00F9, "u with Grave"), (0x00FA, "u with Acute"),
    (0x00FB, "u with Circumflex"), (0x00FC, "u with Diaeresis"),
    (0x00FD, "y with Acute"), (0x00FE, "thorn"),
    (0x00FF, "y with Diaeresis"),
    (0x0100, "A with Macron"), (0x0101, "a with Macron"),
    (0x0102, "A with Breve"), (0x0103, "a with Breve"),
    (0x0104, "A with Ogonek"), (0x0105, "a with Ogonek"),
    (0x0106, "C with Acute"), (0x0107, "c with Acute"),
    (0x0108, "C with Circumflex"), (0x0109, "c with Circumflex"),
    (0x010C, "C with Caron"), (0x010D, "c with Caron"),
    (0x010E, "D with Caron"), (0x010F, "d with Caron"),
    (0x0110, "D with Stroke"), (0x0111, "d with Stroke"),
    (0x0112, "E with Macron"), (0x0113, "e with Macron"),
    (0x0118, "E with Ogonek"), (0x0119, "e with Ogonek"),
    (0x011A, "E with Caron"), (0x011B, "e with Caron"),
    (0x011E, "G with Breve"), (0x011F, "g with Breve"),
    (0x0130, "I with Dot Above"), (0x0131, "Dotless i"),
    (0x0141, "L with Stroke"), (0x0142, "l with Stroke"),
    (0x0143, "N with Acute"), (0x0144, "n with Acute"),
    (0x0147, "N with Caron"), (0x0148, "n with Caron"),
    (0x014C, "O with Macron"), (0x014D, "o with Macron"),
    (0x0150, "O with Double Acute"), (0x0151, "o with Double Acute"),
    (0x0152, "OE Ligature"), (0x0153, "oe Ligature"),
    (0x0158, "R with Caron"), (0x0159, "r with Caron"),
    (0x015A, "S with Acute"), (0x015B, "s with Acute"),
    (0x015E, "S with Cedilla"), (0x015F, "s with Cedilla"),
    (0x0160, "S with Caron"), (0x0161, "s with Caron"),
    (0x0162, "T with Cedilla"), (0x0163, "t with Cedilla"),
    (0x0164, "T with Caron"), (0x0165, "t with Caron"),
    (0x016E, "U with Ring Above"), (0x016F, "u with Ring Above"),
    (0x0170, "U with Double Acute"), (0x0171, "u with Double Acute"),
    (0x0178, "Y with Diaeresis"), (0x0179, "Z with Acute"), (0x017A, "z with Acute"),
    (0x017B, "Z with Dot Above"), (0x017C, "z with Dot Above"),
    (0x017D, "Z with Caron"), (0x017E, "z with Caron"),
    # IPA
    (0x0259, "Schwa"), (0x025B, "Open E"), (0x0254, "Open O"),
    (0x0283, "Esh"), (0x0292, "Ezh"), (0x014B, "Eng"),
    (0x0252, "Turned Alpha"), (0x0250, "Turned a"),
]

for code, name in latin_data:
    ch = chr(code)
    latin["symbols"].append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

categories.append(latin)

# ============================================================
# BUILD AND SAVE
# ============================================================
data = {"categories": categories}

# Count total
total = sum(len(c["symbols"]) for c in categories)
print(f"Total categories: {len(categories)}")
for c in categories:
    print(f"  {c['id']}: {len(c['symbols'])} symbols")
print(f"Total symbols: {total}")

# Write website JSON
out_path = os.path.join("website", "data", "symbols.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"\nWritten to {out_path} ({os.path.getsize(out_path)} bytes)")

# Write chrome extension JS
ext_path = os.path.join("chrome-extension", "symbols.js")
with open(ext_path, "w", encoding="utf-8") as f:
    f.write("const SYMBOLS_DATA = ")
    json.dump(data, f, ensure_ascii=False)
    f.write(";")
print(f"Written to {ext_path} ({os.path.getsize(ext_path)} bytes)")

# Validate
with open(out_path, "r", encoding="utf-8") as f:
    test = json.load(f)
print(f"\nValidation: JSON is valid with {sum(len(c['symbols']) for c in test['categories'])} symbols")

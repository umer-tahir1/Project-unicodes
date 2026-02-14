"""
Comprehensive Unicode Symbol Database Generator v2
Generates 5000+ symbols across 25+ categories covering virtually every useful Unicode block.
"""
import json, os, unicodedata

categories = []

def add_range(syms, start, end, prefix="", filter_fn=None):
    """Add all named characters in a Unicode range."""
    for code in range(start, end + 1):
        ch = chr(code)
        try:
            name = unicodedata.name(ch)
        except ValueError:
            continue
        if filter_fn and not filter_fn(name):
            continue
        syms.append({
            "char": ch,
            "name": (prefix + " " if prefix else "") + name.title(),
            "unicode": f"U+{code:04X}",
            "html": f"&#{code};"
        })

def add_list(syms, data):
    """Add from a list of (code, name) tuples."""
    for code, name in data:
        ch = chr(code)
        syms.append({"char": ch, "name": name, "unicode": f"U+{code:04X}", "html": f"&#{code};"})

# ============================================================
# 1. SMILEYS & EMOTION (Comprehensive)
# ============================================================
cat = {"id": "smileys", "name": "Smileys & Emotion", "icon": "\U0001F600", "symbols": []}
smiley_codes = [
    (0x1F600, "Grinning Face"), (0x1F601, "Beaming Face with Smiling Eyes"),
    (0x1F602, "Face with Tears of Joy"), (0x1F603, "Grinning Face with Big Eyes"),
    (0x1F604, "Grinning Face with Smiling Eyes"), (0x1F605, "Grinning Face with Sweat"),
    (0x1F606, "Grinning Squinting Face"), (0x1F607, "Smiling Face with Halo"),
    (0x1F608, "Smiling Face with Horns"), (0x1F609, "Winking Face"),
    (0x1F60A, "Smiling Face with Smiling Eyes"), (0x1F60B, "Face Savoring Food"),
    (0x1F60C, "Relieved Face"), (0x1F60D, "Smiling Face with Heart-Eyes"),
    (0x1F60E, "Smiling Face with Sunglasses"), (0x1F60F, "Smirking Face"),
    (0x1F610, "Neutral Face"), (0x1F611, "Expressionless Face"),
    (0x1F612, "Unamused Face"), (0x1F613, "Downcast Face with Sweat"),
    (0x1F614, "Pensive Face"), (0x1F615, "Confused Face"),
    (0x1F616, "Confounded Face"), (0x1F617, "Kissing Face"),
    (0x1F618, "Face Blowing a Kiss"), (0x1F619, "Kissing Face with Smiling Eyes"),
    (0x1F61A, "Kissing Face with Closed Eyes"), (0x1F61B, "Face with Tongue"),
    (0x1F61C, "Winking Face with Tongue"), (0x1F61D, "Squinting Face with Tongue"),
    (0x1F61E, "Disappointed Face"), (0x1F61F, "Worried Face"),
    (0x1F620, "Angry Face"), (0x1F621, "Pouting Face"),
    (0x1F622, "Crying Face"), (0x1F623, "Persevering Face"),
    (0x1F624, "Face with Steam From Nose"), (0x1F625, "Sad but Relieved Face"),
    (0x1F626, "Frowning Face with Open Mouth"), (0x1F627, "Anguished Face"),
    (0x1F628, "Fearful Face"), (0x1F629, "Weary Face"),
    (0x1F62A, "Sleepy Face"), (0x1F62B, "Tired Face"),
    (0x1F62C, "Grimacing Face"), (0x1F62D, "Loudly Crying Face"),
    (0x1F62E, "Face with Open Mouth"), (0x1F62F, "Hushed Face"),
    (0x1F630, "Anxious Face with Sweat"), (0x1F631, "Face Screaming in Fear"),
    (0x1F632, "Astonished Face"), (0x1F633, "Flushed Face"),
    (0x1F634, "Sleeping Face"), (0x1F635, "Face with Crossed-Out Eyes"),
    (0x1F636, "Face Without Mouth"), (0x1F637, "Face with Medical Mask"),
    (0x1F638, "Grinning Cat"), (0x1F639, "Cat with Tears of Joy"),
    (0x1F63A, "Grinning Cat with Smiling Eyes"), (0x1F63B, "Smiling Cat with Heart-Eyes"),
    (0x1F63C, "Cat with Wry Smile"), (0x1F63D, "Kissing Cat"),
    (0x1F63E, "Pouting Cat"), (0x1F63F, "Crying Cat"),
    (0x1F640, "Weary Cat"), (0x1F641, "Slightly Frowning Face"),
    (0x1F642, "Slightly Smiling Face"), (0x1F643, "Upside-Down Face"),
    (0x1F644, "Face with Rolling Eyes"),
    (0x1F910, "Zipper-Mouth Face"), (0x1F911, "Money-Mouth Face"),
    (0x1F912, "Face with Thermometer"), (0x1F913, "Nerd Face"),
    (0x1F914, "Thinking Face"), (0x1F915, "Face with Head-Bandage"),
    (0x1F916, "Robot"), (0x1F917, "Hugging Face"),
    (0x1F920, "Cowboy Hat Face"), (0x1F921, "Clown Face"),
    (0x1F922, "Nauseated Face"), (0x1F923, "Rolling on the Floor Laughing"),
    (0x1F924, "Drooling Face"), (0x1F925, "Lying Face"),
    (0x1F927, "Sneezing Face"), (0x1F928, "Face with Raised Eyebrow"),
    (0x1F929, "Star-Struck"), (0x1F92A, "Zany Face"),
    (0x1F92B, "Shushing Face"), (0x1F92C, "Face with Symbols on Mouth"),
    (0x1F92D, "Face with Hand Over Mouth"), (0x1F92E, "Face Vomiting"),
    (0x1F92F, "Exploding Head"), (0x1F970, "Smiling Face with Hearts"),
    (0x1F971, "Yawning Face"), (0x1F973, "Partying Face"),
    (0x1F974, "Woozy Face"), (0x1F975, "Hot Face"),
    (0x1F976, "Cold Face"), (0x1F977, "Ninja"),
    (0x1F978, "Disguised Face"), (0x1F979, "Face Holding Back Tears"),
    (0x1F97A, "Pleading Face"), (0x1F9D0, "Face with Monocle"),
    (0x1FAE0, "Melting Face"), (0x1FAE1, "Saluting Face"),
    (0x1FAE2, "Face with Open Eyes and Hand Over Mouth"),
    (0x1FAE3, "Face with Peeking Eye"), (0x1FAE4, "Face with Diagonal Mouth"),
    (0x1FAE5, "Dotted Line Face"), (0x1FAE6, "Biting Lip"),
    (0x1FAE7, "Bubbles"), (0x1FAE8, "Shaking Face"),
    (0x263A, "Smiling Face"), (0x2639, "Frowning Face"),
    (0x1F47B, "Ghost"), (0x1F47D, "Alien"), (0x1F47E, "Alien Monster"),
    (0x1F47F, "Angry Face with Horns"), (0x1F480, "Skull"),
    (0x1F4A9, "Pile of Poo"), (0x1F479, "Ogre"), (0x1F47A, "Goblin"),
    (0x1F47C, "Baby Angel"), (0x1F383, "Jack-O-Lantern"),
    (0x2620, "Skull and Crossbones"),
    (0x1F648, "See-No-Evil Monkey"), (0x1F649, "Hear-No-Evil Monkey"), (0x1F64A, "Speak-No-Evil Monkey"),
    (0x1F4A2, "Anger Symbol"), (0x1F4A3, "Bomb"), (0x1F4A4, "Zzz"),
    (0x1F4A5, "Collision"), (0x1F4A6, "Sweat Droplets"), (0x1F4A7, "Droplet"),
    (0x1F4A8, "Dashing Away"), (0x1F4AB, "Dizzy"), (0x1F4AC, "Speech Balloon"),
    (0x1F4AD, "Thought Balloon"), (0x1F4AE, "White Flower"), (0x1F4AF, "Hundred Points"),
    (0x1F573, "Hole"), (0x1F5E8, "Left Speech Bubble"),
]
add_list(cat["symbols"], smiley_codes)
categories.append(cat)

# ============================================================
# 2. HEARTS & LOVE
# ============================================================
cat = {"id": "hearts", "name": "Hearts & Love", "icon": "\u2764", "symbols": []}
add_list(cat["symbols"], [
    (0x2764, "Red Heart"), (0x1F493, "Beating Heart"), (0x1F494, "Broken Heart"),
    (0x1F495, "Two Hearts"), (0x1F496, "Sparkling Heart"), (0x1F497, "Growing Heart"),
    (0x1F498, "Heart with Arrow"), (0x1F499, "Blue Heart"), (0x1F49A, "Green Heart"),
    (0x1F49B, "Yellow Heart"), (0x1F49C, "Purple Heart"), (0x1F49D, "Heart with Ribbon"),
    (0x1F49E, "Revolving Hearts"), (0x1F49F, "Heart Decoration"),
    (0x1F5A4, "Black Heart"), (0x1F90D, "White Heart"), (0x1F90E, "Brown Heart"),
    (0x1F9E1, "Orange Heart"), (0x2763, "Heavy Heart Exclamation"),
    (0x2661, "White Heart Suit"), (0x2665, "Black Heart Suit"),
    (0x2766, "Floral Heart"), (0x2767, "Rotated Floral Heart Bullet"),
    (0x2765, "Rotated Heavy Black Heart Bullet"),
    (0x1FA75, "Light Blue Heart"), (0x1FA76, "Grey Heart"), (0x1FA77, "Pink Heart"),
    (0x1F48B, "Kiss Mark"), (0x1F48C, "Love Letter"), (0x1F48D, "Ring"),
    (0x1F48E, "Gem Stone"), (0x1F48F, "Kiss"), (0x1F490, "Bouquet"),
    (0x1F491, "Couple with Heart"), (0x1F492, "Wedding"),
    (0x1F339, "Rose"), (0x1F33A, "Hibiscus"), (0x1F33B, "Sunflower"),
    (0x1F33C, "Blossom"), (0x1F337, "Tulip"), (0x1F940, "Wilted Flower"),
    (0x1FAB7, "Lotus"), (0x1F338, "Cherry Blossom"),
    (0x2618, "Shamrock"), (0x2740, "White Florette"), (0x273F, "Black Florette"),
    (0x2741, "Eight Petalled Outlined Black Florette"),
    (0x2742, "Six Petalled Black and White Florette"),
])
categories.append(cat)

# ============================================================
# 3. HANDS & BODY
# ============================================================
cat = {"id": "hands", "name": "Hands & Body", "icon": "\U0001F44D", "symbols": []}
add_list(cat["symbols"], [
    (0x1F44D, "Thumbs Up"), (0x1F44E, "Thumbs Down"), (0x1F44F, "Clapping Hands"),
    (0x1F450, "Open Hands"), (0x1F44A, "Oncoming Fist"), (0x1F44B, "Waving Hand"),
    (0x1F44C, "OK Hand"), (0x1F446, "Pointing Up"), (0x1F447, "Pointing Down"),
    (0x1F448, "Pointing Left"), (0x1F449, "Pointing Right"),
    (0x1F4AA, "Flexed Biceps"), (0x1F440, "Eyes"), (0x1F441, "Eye"),
    (0x1F442, "Ear"), (0x1F443, "Nose"), (0x1F444, "Mouth"), (0x1F445, "Tongue"),
    (0x1F590, "Hand with Fingers Splayed"), (0x1F596, "Vulcan Salute"),
    (0x1F64C, "Raising Hands"), (0x1F64F, "Folded Hands"),
    (0x1F91A, "Raised Back of Hand"), (0x1F91B, "Left-Facing Fist"),
    (0x1F91C, "Right-Facing Fist"), (0x1F91D, "Handshake"),
    (0x1F91E, "Crossed Fingers"), (0x1F91F, "Love-You Gesture"),
    (0x1F918, "Sign of the Horns"), (0x1F919, "Call Me Hand"),
    (0x1F90C, "Pinched Fingers"), (0x1F90F, "Pinching Hand"),
    (0x1FAF0, "Hand with Index Finger and Thumb Crossed"),
    (0x1FAF1, "Rightwards Hand"), (0x1FAF2, "Leftwards Hand"),
    (0x1FAF3, "Palm Down Hand"), (0x1FAF4, "Palm Up Hand"),
    (0x1FAF5, "Index Pointing at the Viewer"), (0x1FAF6, "Heart Hands"),
    (0x1FAF7, "Leftwards Pushing Hand"), (0x1FAF8, "Rightwards Pushing Hand"),
    (0x1F9B5, "Leg"), (0x1F9B6, "Foot"), (0x1F9B4, "Bone"),
    (0x1F9B7, "Tooth"), (0x1F9BB, "Ear with Hearing Aid"),
    (0x1F9E0, "Brain"), (0x1FAC0, "Anatomical Heart"), (0x1FAC1, "Lungs"),
    (0x1F9B0, "Red Hair"), (0x1F9B1, "Curly Hair"), (0x1F9B2, "Bald"),
    (0x1F9B3, "White Hair"),
    (0x270A, "Raised Fist"), (0x270B, "Raised Hand"), (0x270C, "Victory Hand"),
    (0x270D, "Writing Hand"), (0x261D, "Index Pointing Up"),
    (0x1F930, "Pregnant Woman"), (0x1F931, "Breast-Feeding"),
    (0x1F934, "Prince"), (0x1F935, "Person in Tuxedo"),
    (0x1F936, "Mrs. Claus"), (0x1F937, "Person Shrugging"),
    (0x1F938, "Person Cartwheeling"), (0x1F64B, "Person Raising Hand"),
    (0x1F647, "Person Bowing"), (0x1F926, "Person Facepalming"),
    (0x1F46E, "Police Officer"), (0x1F477, "Construction Worker"),
    (0x1F482, "Guard"), (0x1F575, "Detective"), (0x1F468, "Man"),
    (0x1F469, "Woman"), (0x1F474, "Old Man"), (0x1F475, "Old Woman"),
    (0x1F466, "Boy"), (0x1F467, "Girl"), (0x1F476, "Baby"),
    (0x1F385, "Santa Claus"), (0x1F478, "Princess"),
    (0x1F9D1, "Person"), (0x1F9D2, "Child"), (0x1F9D3, "Older Person"),
    (0x1F9D4, "Person with Beard"), (0x1F9D5, "Person with Headscarf"),
    (0x1F9D9, "Mage"), (0x1F9DA, "Fairy"), (0x1F9DB, "Vampire"),
    (0x1F9DC, "Merperson"), (0x1F9DD, "Elf"), (0x1F9DE, "Genie"),
    (0x1F9DF, "Zombie"), (0x1F9D6, "Person in Steamy Room"),
    (0x1F9D7, "Person Climbing"), (0x1F9D8, "Person in Lotus Position"),
    (0x1F6B6, "Person Walking"), (0x1F3C3, "Person Running"),
    (0x1F483, "Woman Dancing"), (0x1F57A, "Man Dancing"),
    (0x1F46F, "People with Bunny Ears"), (0x1F9CF, "Deaf Person"),
    (0x1F9CE, "Person Kneeling"), (0x1F6B9, "Men's Room"),
    (0x1F6BA, "Women's Room"), (0x1F6BB, "Restroom"),
])
categories.append(cat)

# ============================================================
# 4. ANIMALS & NATURE (comprehensive)
# ============================================================
cat = {"id": "animals", "name": "Animals & Nature", "icon": "\U0001F43E", "symbols": []}
# All animal face/body emojis
add_range(cat["symbols"], 0x1F400, 0x1F43F)
add_range(cat["symbols"], 0x1F980, 0x1F9AD)
# Nature
add_list(cat["symbols"], [
    (0x1F331, "Seedling"), (0x1F332, "Evergreen Tree"), (0x1F333, "Deciduous Tree"),
    (0x1F334, "Palm Tree"), (0x1F335, "Cactus"), (0x1F33E, "Sheaf of Rice"),
    (0x1F33F, "Herb"), (0x1F340, "Four Leaf Clover"), (0x1F341, "Maple Leaf"),
    (0x1F342, "Fallen Leaf"), (0x1F343, "Leaf Fluttering in Wind"),
    (0x1F344, "Mushroom"), (0x1F33D, "Ear of Corn"),
    (0x1FAB4, "Potted Plant"), (0x1FAB5, "Wood"), (0x1FAB6, "Feather"),
    (0x1FAB7, "Lotus"), (0x1FAB8, "Coral"), (0x1FABB, "Hyacinth"),
    (0x1FAB9, "Empty Nest"), (0x1FABA, "Nest with Eggs"),
    (0x1FAB0, "Fly"), (0x1FAB1, "Worm"), (0x1FAB2, "Beetle"),
    (0x1FAB3, "Cockroach"), (0x1FABC, "Jellyfish"),
    (0x1F577, "Spider"), (0x1F578, "Spider Web"),
    (0x1F54A, "Dove"), (0x1F426, "Bird"), (0x1F985, "Eagle"),
    (0x1F9A4, "Dodo"), (0x1F9A3, "Mammoth"),
    (0x1F9AE, "Guide Dog"), (0x1F9AF, "White Cane"),
    (0x1F415, "Dog"), (0x1F408, "Cat"), (0x1F40E, "Horse"),
])
categories.append(cat)

# ============================================================
# 5. FOOD & DRINK (NEW - comprehensive)
# ============================================================
cat = {"id": "food", "name": "Food & Drink", "icon": "\U0001F354", "symbols": []}
add_list(cat["symbols"], [
    (0x1F34E, "Red Apple"), (0x1F34F, "Green Apple"), (0x1F34A, "Tangerine"),
    (0x1F34B, "Lemon"), (0x1F34C, "Banana"), (0x1F34D, "Pineapple"),
    (0x1F96D, "Mango"), (0x1F347, "Grapes"), (0x1F348, "Melon"),
    (0x1F349, "Watermelon"), (0x1F350, "Pear"), (0x1F351, "Peach"),
    (0x1F352, "Cherries"), (0x1F353, "Strawberry"), (0x1FAD0, "Blueberries"),
    (0x1F95D, "Kiwi Fruit"), (0x1F965, "Coconut"),
    (0x1F345, "Tomato"), (0x1F346, "Eggplant"), (0x1F336, "Hot Pepper"),
    (0x1F33D, "Ear of Corn"), (0x1F955, "Carrot"), (0x1F954, "Potato"),
    (0x1F360, "Roasted Sweet Potato"), (0x1F9C5, "Onion"), (0x1F9C4, "Garlic"),
    (0x1FAD1, "Bell Pepper"), (0x1FAD2, "Olive"), (0x1F96C, "Leafy Green"),
    (0x1F966, "Broccoli"), (0x1F344, "Mushroom"), (0x1F95C, "Peanuts"),
    (0x1FAD8, "Beans"), (0x1FAD7, "Pouring Liquid"),
    (0x1F35E, "Bread"), (0x1F950, "Croissant"), (0x1FAD3, "Flatbread"),
    (0x1F96F, "Bagel"), (0x1F95E, "Pancakes"), (0x1F9C7, "Waffle"),
    (0x1F9C0, "Cheese Wedge"), (0x1F356, "Meat on Bone"), (0x1F357, "Poultry Leg"),
    (0x1F969, "Cut of Meat"), (0x1F953, "Bacon"), (0x1F354, "Hamburger"),
    (0x1F35F, "French Fries"), (0x1F355, "Pizza"), (0x1F32D, "Hot Dog"),
    (0x1F96A, "Sandwich"), (0x1F32E, "Taco"), (0x1F32F, "Burrito"),
    (0x1FAD4, "Tamale"), (0x1F959, "Stuffed Flatbread"), (0x1F9C6, "Falafel"),
    (0x1F95A, "Egg"), (0x1F373, "Cooking"), (0x1F958, "Shallow Pan of Food"),
    (0x1F372, "Pot of Food"), (0x1FAD5, "Fondue"), (0x1F963, "Bowl with Spoon"),
    (0x1F957, "Green Salad"), (0x1F37F, "Popcorn"), (0x1F9C8, "Butter"),
    (0x1F9C2, "Salt"), (0x1F96B, "Canned Food"),
    (0x1F371, "Bento Box"), (0x1F358, "Rice Cracker"), (0x1F359, "Rice Ball"),
    (0x1F35A, "Cooked Rice"), (0x1F35B, "Curry Rice"), (0x1F35C, "Steaming Bowl"),
    (0x1F35D, "Spaghetti"), (0x1F360, "Roasted Sweet Potato"),
    (0x1F362, "Oden"), (0x1F363, "Sushi"), (0x1F364, "Fried Shrimp"),
    (0x1F365, "Fish Cake"), (0x1F96E, "Moon Cake"), (0x1F361, "Dango"),
    (0x1F95F, "Dumpling"), (0x1F960, "Fortune Cookie"),
    (0x1F961, "Takeout Box"), (0x1F366, "Soft Ice Cream"),
    (0x1F367, "Shaved Ice"), (0x1F368, "Ice Cream"),
    (0x1F369, "Doughnut"), (0x1F36A, "Cookie"), (0x1F382, "Birthday Cake"),
    (0x1F370, "Shortcake"), (0x1F9C1, "Cupcake"), (0x1F967, "Pie"),
    (0x1F36B, "Chocolate Bar"), (0x1F36C, "Candy"), (0x1F36D, "Lollipop"),
    (0x1F36E, "Custard"), (0x1F36F, "Honey Pot"),
    (0x1F37C, "Baby Bottle"), (0x1F95B, "Glass of Milk"),
    (0x2615, "Hot Beverage"), (0x1FAD6, "Teapot"),
    (0x1F375, "Teacup Without Handle"), (0x1F376, "Sake"),
    (0x1F37E, "Bottle with Popping Cork"), (0x1F377, "Wine Glass"),
    (0x1F378, "Cocktail Glass"), (0x1F379, "Tropical Drink"),
    (0x1F37A, "Beer Mug"), (0x1F37B, "Clinking Beer Mugs"),
    (0x1F942, "Clinking Glasses"), (0x1F943, "Tumbler Glass"),
    (0x1FAD9, "Jar"), (0x1F964, "Cup with Straw"), (0x1F9CB, "Bubble Tea"),
    (0x1F9C3, "Beverage Box"), (0x1F9C9, "Mate"), (0x1F9CA, "Ice"),
    (0x1F962, "Chopsticks"), (0x1F37D, "Fork and Knife with Plate"),
    (0x1F374, "Fork and Knife"), (0x1F944, "Spoon"), (0x1F52A, "Kitchen Knife"),
    (0x1FAD3, "Flatbread"),
])
categories.append(cat)

# ============================================================
# 6. SPORTS & ACTIVITIES (NEW)
# ============================================================
cat = {"id": "sports", "name": "Sports & Activities", "icon": "\u26BD", "symbols": []}
add_list(cat["symbols"], [
    (0x26BD, "Soccer Ball"), (0x26BE, "Baseball"), (0x1F3C0, "Basketball"),
    (0x1F3D0, "Volleyball"), (0x1F3C8, "American Football"),
    (0x1F3C9, "Rugby Football"), (0x1F3BE, "Tennis"),
    (0x1F94F, "Flying Disc"), (0x1F3B3, "Bowling"), (0x1F3CF, "Cricket Game"),
    (0x1F3D1, "Field Hockey"), (0x1F3D2, "Ice Hockey"), (0x1F94D, "Lacrosse"),
    (0x1F3D3, "Ping Pong"), (0x1F3F8, "Badminton"), (0x1F94A, "Boxing Glove"),
    (0x1F94B, "Martial Arts Uniform"), (0x1F945, "Goal Net"),
    (0x26F3, "Flag in Hole"), (0x26F8, "Ice Skate"), (0x1F3A3, "Fishing Pole"),
    (0x1F93F, "Diving Mask"), (0x1F3BD, "Running Shirt"),
    (0x1F3BF, "Skis"), (0x1F6F7, "Sled"), (0x1F94C, "Curling Stone"),
    (0x1F3AF, "Bullseye"), (0x1F3B1, "Pool 8 Ball"),
    (0x1F3AE, "Video Game"), (0x1F579, "Joystick"), (0x1F3B2, "Game Die"),
    (0x1F9E9, "Puzzle Piece"), (0x1F9F8, "Teddy Bear"), (0x1FA80, "Yo-Yo"),
    (0x1FA81, "Kite"), (0x1FA86, "Nesting Dolls"),
    (0x265F, "Chess Pawn"), (0x2657, "White Chess Queen"),
    (0x2654, "White Chess King"), (0x2655, "White Chess Queen"),
    (0x2656, "White Chess Bishop"), (0x2658, "White Chess Knight"),
    (0x2659, "White Chess Pawn"), (0x265A, "Black Chess King"),
    (0x265B, "Black Chess Queen"), (0x265C, "Black Chess Rook"),
    (0x265D, "Black Chess Bishop"), (0x265E, "Black Chess Knight"),
    (0x1F3C6, "Trophy"), (0x1F3C5, "Sports Medal"), (0x1F947, "1st Place Medal"),
    (0x1F948, "2nd Place Medal"), (0x1F949, "3rd Place Medal"),
    (0x1F396, "Military Medal"), (0x1F397, "Reminder Ribbon"),
    (0x1F3A0, "Carousel Horse"), (0x1F3A1, "Ferris Wheel"),
    (0x1F3A2, "Roller Coaster"), (0x1F3AA, "Circus Tent"),
    (0x1F3A4, "Microphone"), (0x1F3A5, "Movie Camera"),
    (0x1F3A6, "Cinema"), (0x1F3A7, "Headphone"),
    (0x1F3A8, "Artist Palette"), (0x1F3A9, "Top Hat"),
    (0x1F3AB, "Ticket"), (0x1F3AC, "Clapper Board"),
    (0x1F3AD, "Performing Arts"),
    # Music
    (0x1F3B5, "Musical Note"), (0x1F3B6, "Musical Notes"),
    (0x1F3B7, "Saxophone"), (0x1F3B8, "Guitar"),
    (0x1F3B9, "Musical Keyboard"), (0x1F3BA, "Trumpet"),
    (0x1F3BB, "Violin"), (0x1F3BC, "Musical Score"),
    (0x1FA95, "Banjo"), (0x1FA97, "Accordion"), (0x1FA98, "Long Drum"),
    (0x1F941, "Drum"), (0x1FA87, "Maracas"), (0x1FA88, "Flute"),
    (0x1F6F9, "Skateboard"), (0x1F6FC, "Roller Skate"),
    (0x1F3CB, "Person Lifting Weights"), (0x1F3CC, "Person Golfing"),
    (0x1F3CA, "Person Swimming"), (0x1F3C4, "Person Surfing"),
    (0x1F3C7, "Horse Racing"), (0x1F6B4, "Person Biking"),
    (0x1F93A, "Person Fencing"), (0x1F93C, "People Wrestling"),
    (0x1F93D, "Person Playing Water Polo"),
    (0x1F93E, "Person Playing Handball"),
    (0x1F938, "Person Cartwheeling"),
])
categories.append(cat)

# ============================================================
# 7. TRAVEL & VEHICLES
# ============================================================
cat = {"id": "travel", "name": "Travel & Transport", "icon": "\U0001F30D", "symbols": []}
add_list(cat["symbols"], [
    (0x1F30D, "Globe Europe-Africa"), (0x1F30E, "Globe Americas"),
    (0x1F30F, "Globe Asia-Australia"), (0x1F310, "Globe with Meridians"),
    (0x1F5FA, "World Map"), (0x1F9ED, "Compass"),
    # Moon phases
    (0x1F311, "New Moon"), (0x1F312, "Waxing Crescent Moon"),
    (0x1F313, "First Quarter Moon"), (0x1F314, "Waxing Gibbous Moon"),
    (0x1F315, "Full Moon"), (0x1F316, "Waning Gibbous Moon"),
    (0x1F317, "Last Quarter Moon"), (0x1F318, "Waning Crescent Moon"),
    (0x1F319, "Crescent Moon"), (0x1F31A, "New Moon Face"),
    (0x1F31B, "First Quarter Moon Face"), (0x1F31C, "Last Quarter Moon Face"),
    (0x1F31D, "Full Moon Face"), (0x1F31E, "Sun with Face"),
    (0x1F320, "Shooting Star"), (0x2B50, "Star"), (0x1F31F, "Glowing Star"),
    (0x2728, "Sparkles"), (0x1F308, "Rainbow"),
    # Weather
    (0x2600, "Sun"), (0x26C5, "Sun Behind Cloud"),
    (0x1F324, "Sun Behind Small Cloud"), (0x1F325, "Sun Behind Large Cloud"),
    (0x1F326, "Sun Behind Rain Cloud"), (0x1F327, "Cloud with Rain"),
    (0x1F328, "Cloud with Snow"), (0x1F329, "Cloud with Lightning"),
    (0x1F32A, "Tornado"), (0x1F32B, "Fog"), (0x1F32C, "Wind Face"),
    (0x2601, "Cloud"), (0x2602, "Umbrella"), (0x2614, "Umbrella with Rain"),
    (0x26C4, "Snowman"), (0x2603, "Snowman with Snow"),
    (0x2604, "Comet"), (0x26A1, "High Voltage"),
    # Places
    (0x1F3D4, "Snow-Capped Mountain"), (0x1F3D5, "Camping"),
    (0x1F3D6, "Beach with Umbrella"), (0x1F3D7, "Building Construction"),
    (0x1F3D8, "Houses"), (0x1F3D9, "Cityscape"), (0x1F3DA, "Derelict House"),
    (0x1F3DB, "Classical Building"), (0x1F3DC, "Desert"),
    (0x1F3DD, "Desert Island"), (0x1F3DE, "National Park"),
    (0x1F3DF, "Stadium"), (0x1F3E0, "House"), (0x1F3E1, "House with Garden"),
    (0x1F3E2, "Office Building"), (0x1F3E3, "Japanese Post Office"),
    (0x1F3E5, "Hospital"), (0x1F3E6, "Bank"), (0x1F3E8, "Hotel"),
    (0x1F3EA, "Convenience Store"), (0x1F3EB, "School"),
    (0x1F3EC, "Department Store"), (0x1F3ED, "Factory"),
    (0x1F3EF, "Japanese Castle"), (0x1F3F0, "Castle"),
    (0x1F54C, "Mosque"), (0x1F54D, "Synagogue"), (0x1F6D5, "Hindu Temple"),
    (0x26EA, "Church"), (0x26F2, "Fountain"), (0x26FA, "Tent"),
    (0x1F5FB, "Mount Fuji"), (0x1F5FC, "Tokyo Tower"),
    (0x1F5FD, "Statue of Liberty"), (0x1F5FE, "Map of Japan"),
    (0x1F5FF, "Moyai"),
    # Vehicles
    (0x1F680, "Rocket"), (0x1F681, "Helicopter"), (0x1F682, "Locomotive"),
    (0x1F683, "Railway Car"), (0x1F684, "High-Speed Train"),
    (0x1F685, "Bullet Train"), (0x1F686, "Train"), (0x1F687, "Metro"),
    (0x1F688, "Light Rail"), (0x1F689, "Station"), (0x1F68C, "Bus"),
    (0x1F690, "Minibus"), (0x1F691, "Ambulance"), (0x1F692, "Fire Engine"),
    (0x1F693, "Police Car"), (0x1F695, "Taxi"), (0x1F697, "Automobile"),
    (0x1F699, "Sport Utility Vehicle"), (0x1F69A, "Delivery Truck"),
    (0x1F69B, "Articulated Lorry"), (0x1F69C, "Tractor"),
    (0x1F6A2, "Ship"), (0x1F6A4, "Speedboat"), (0x1F6F3, "Passenger Ship"),
    (0x1F6F4, "Kick Scooter"), (0x1F6F5, "Motor Scooter"),
    (0x1F6F6, "Canoe"), (0x1F6F8, "Flying Saucer"),
    (0x1F6FA, "Auto Rickshaw"), (0x1F6FB, "Pickup Truck"),
    (0x1F6A5, "Horizontal Traffic Light"), (0x1F6A6, "Vertical Traffic Light"),
    (0x1F6A7, "Construction"), (0x1F6A8, "Police Car Light"),
    (0x1F6B2, "Bicycle"), (0x1F6E9, "Small Airplane"),
    (0x1F6EB, "Airplane Departure"), (0x1F6EC, "Airplane Arrival"),
    (0x1F6F0, "Satellite"), (0x2708, "Airplane"),
    (0x26F5, "Sailboat"), (0x26FD, "Fuel Pump"),
    (0x1F6E2, "Oil Drum"), (0x1F6E3, "Motorway"), (0x1F6E4, "Railway Track"),
    (0x1F6E5, "Motor Boat"), (0x1F6F1, "Cable Car"),
    (0x1F6A0, "Mountain Cableway"), (0x1F6A1, "Aerial Tramway"),
    (0x1F6A9, "Triangular Flag"),
    (0x1F9F3, "Luggage"), (0x1FA9E, "Mirror"),
])
categories.append(cat)

# ============================================================
# 8. OBJECTS & TECHNOLOGY (Comprehensive)
# ============================================================
cat = {"id": "objects", "name": "Objects & Technology", "icon": "\U0001F4BB", "symbols": []}
add_list(cat["symbols"], [
    # Tech devices
    (0x1F4BB, "Laptop"), (0x1F5A5, "Desktop Computer"), (0x1F5A8, "Printer"),
    (0x2328, "Keyboard"), (0x1F5B1, "Computer Mouse"), (0x1F5B2, "Trackball"),
    (0x1F4BD, "Computer Disk"), (0x1F4BE, "Floppy Disk"), (0x1F4BF, "Optical Disk"),
    (0x1F4C0, "DVD"), (0x1F4F1, "Mobile Phone"), (0x1F4F2, "Mobile Phone with Arrow"),
    (0x260E, "Telephone"), (0x1F4DE, "Telephone Receiver"),
    (0x1F4DF, "Pager"), (0x1F4E0, "Fax Machine"),
    (0x1F50B, "Battery"), (0x1F50C, "Electric Plug"), (0x1FAAB, "Low Battery"),
    (0x1F4F7, "Camera"), (0x1F4F8, "Camera with Flash"),
    (0x1F4F9, "Video Camera"), (0x1F4FA, "Television"), (0x1F4FB, "Radio"),
    (0x1F4FC, "Videocassette"), (0x1F399, "Studio Microphone"),
    (0x1F39A, "Level Slider"), (0x1F39B, "Control Knobs"),
    (0x1F4E1, "Satellite Antenna"), (0x1F9EE, "Abacus"),
    # Light & electrical
    (0x1F4A1, "Light Bulb"), (0x1F526, "Flashlight"), (0x1F56F, "Candle"),
    (0x1FA94, "Diya Lamp"),
    # Office
    (0x1F4B0, "Money Bag"), (0x1F4B3, "Credit Card"), (0x1F4B8, "Money with Wings"),
    (0x1F4B5, "Dollar Banknote"), (0x1F4B4, "Yen Banknote"),
    (0x1F4B6, "Euro Banknote"), (0x1F4B7, "Pound Banknote"),
    (0x1F4B1, "Currency Exchange"), (0x1F4B2, "Heavy Dollar Sign"),
    (0x1F4BC, "Briefcase"), (0x1F4C1, "File Folder"),
    (0x1F4C2, "Open File Folder"), (0x1F4C3, "Page with Curl"),
    (0x1F4C4, "Page Facing Up"), (0x1F4C5, "Calendar"),
    (0x1F4C6, "Tear-Off Calendar"), (0x1F5D3, "Spiral Calendar"),
    (0x1F4C7, "Card Index"), (0x1F4C8, "Chart Increasing"),
    (0x1F4C9, "Chart Decreasing"), (0x1F4CA, "Bar Chart"),
    (0x1F4CB, "Clipboard"), (0x1F4CC, "Pushpin"), (0x1F4CD, "Round Pushpin"),
    (0x1F4CE, "Paperclip"), (0x1F587, "Linked Paperclips"),
    (0x1F4CF, "Straight Ruler"), (0x1F4D0, "Triangular Ruler"),
    (0x1F4D1, "Bookmark Tabs"), (0x1F4D2, "Ledger"),
    (0x1F4D3, "Notebook"), (0x1F4D4, "Notebook with Decorative Cover"),
    (0x1F4D5, "Closed Book"), (0x1F4D6, "Open Book"),
    (0x1F4D7, "Green Book"), (0x1F4D8, "Blue Book"),
    (0x1F4D9, "Orange Book"), (0x1F4DA, "Books"),
    (0x1F4DB, "Name Badge"), (0x1F4DC, "Scroll"),
    (0x1F4DD, "Memo"), (0x1F4F0, "Newspaper"),
    (0x1F5DE, "Rolled-Up Newspaper"), (0x1F516, "Bookmark"),
    (0x1F3F7, "Label"),
    # Writing
    (0x270F, "Pencil"), (0x2712, "Black Nib"), (0x1F58A, "Pen"),
    (0x1F58B, "Fountain Pen"), (0x1F58C, "Paintbrush"), (0x1F58D, "Crayon"),
    # Mail
    (0x2709, "Envelope"), (0x1F4E2, "Loudspeaker"), (0x1F4E3, "Megaphone"),
    (0x1F4E4, "Outbox Tray"), (0x1F4E5, "Inbox Tray"), (0x1F4E6, "Package"),
    (0x1F4E7, "E-Mail"), (0x1F4E8, "Incoming Envelope"),
    (0x1F4E9, "Envelope with Arrow"), (0x1F4EA, "Closed Mailbox Low Flag"),
    (0x1F4EB, "Closed Mailbox Raised Flag"), (0x1F4EC, "Open Mailbox Raised Flag"),
    (0x1F4ED, "Open Mailbox Low Flag"), (0x1F4EE, "Postbox"),
    (0x1F4EF, "Postal Horn"),
    # Tools
    (0x1F527, "Wrench"), (0x1F528, "Hammer"), (0x1F529, "Nut and Bolt"),
    (0x1F6E0, "Hammer and Wrench"), (0x1F6E1, "Shield"),
    (0x2692, "Hammer and Pick"), (0x2699, "Gear"),
    (0x26CF, "Pick"), (0x26D1, "Helmet with White Cross"),
    (0x26D3, "Chains"), (0x1F5DC, "Clamp"),
    (0x1FA93, "Axe"), (0x1FA9A, "Carpentry Saw"),
    (0x1FA9B, "Screwdriver"), (0x1FA9C, "Ladder"),
    (0x1FA9D, "Hook"), (0x1FA9F, "Window"),
    (0x1FAA0, "Plunger"), (0x1FAA1, "Sewing Needle"),
    (0x1FAA2, "Knot"), (0x1F9F0, "Toolbox"),
    (0x1F9F2, "Magnet"), (0x1F9EA, "Test Tube"), (0x1F9EB, "Petri Dish"),
    (0x1F9EC, "DNA"), (0x1F52C, "Microscope"), (0x1F52D, "Telescope"),
    (0x1F52E, "Crystal Ball"),
    # Locks
    (0x1F510, "Closed Lock with Key"), (0x1F511, "Key"),
    (0x1F512, "Locked"), (0x1F513, "Unlocked"),
    (0x1F5DD, "Old Key"),
    # Household
    (0x1F6AA, "Door"), (0x1FA91, "Chair"), (0x1F6CF, "Bed"),
    (0x1F6CB, "Couch and Lamp"), (0x1F6BD, "Toilet"),
    (0x1F6BF, "Shower"), (0x1F6C1, "Bathtub"),
    (0x1FA92, "Razor"), (0x1F9F4, "Lotion Bottle"), (0x1F9F5, "Thread"),
    (0x1F9F6, "Yarn"), (0x1F9F7, "Safety Pin"), (0x1F9F9, "Broom"),
    (0x1F9FA, "Basket"), (0x1F9FB, "Roll of Paper"),
    (0x1F9FC, "Soap"), (0x1F9FD, "Sponge"),
    (0x1F9EF, "Fire Extinguisher"),
    (0x1FA83, "Boomerang"), (0x1FA84, "Magic Wand"),
    (0x1FA85, "Pinata"),
    # Clothing
    (0x1F451, "Crown"), (0x1F452, "Woman's Hat"), (0x1F453, "Glasses"),
    (0x1F454, "Necktie"), (0x1F455, "T-Shirt"), (0x1F456, "Jeans"),
    (0x1F457, "Dress"), (0x1F458, "Kimono"), (0x1F459, "Bikini"),
    (0x1F45A, "Woman's Clothes"), (0x1F45B, "Purse"), (0x1F45C, "Handbag"),
    (0x1F45D, "Clutch Bag"), (0x1F45E, "Man's Shoe"), (0x1F45F, "Running Shoe"),
    (0x1F460, "High-Heeled Shoe"), (0x1F461, "Woman's Sandal"),
    (0x1F462, "Woman's Boot"), (0x1F97B, "Sari"),
    (0x1F97C, "Lab Coat"), (0x1F97D, "Goggles"),
    (0x1F97E, "Hiking Boot"), (0x1F97F, "Flat Shoe"),
    (0x1F9E2, "Billed Cap"), (0x1F9E3, "Scarf"),
    (0x1F9E4, "Gloves"), (0x1F9E5, "Coat"), (0x1F9E6, "Socks"),
    (0x1F9BA, "Safety Vest"), (0x1FA71, "One-Piece Swimsuit"),
    (0x1FA72, "Briefs"), (0x1FA73, "Shorts"),
    (0x1FA74, "Thong Sandal"),
    (0x1F576, "Dark Sunglasses"), (0x1F392, "Backpack"),
    (0x1F393, "Graduation Cap"),
    (0x1F484, "Lipstick"), (0x1F485, "Nail Polish"),
    (0x1F48E, "Gem Stone"), (0x1F48D, "Ring"),
    (0x1F9AF, "White Cane"), (0x1FA7C, "Crutch"),
    (0x1FA7A, "Stethoscope"), (0x1FA7B, "X-Ray"),
    # Celebrations
    (0x1F389, "Party Popper"), (0x1F38A, "Confetti Ball"),
    (0x1F38B, "Tanabata Tree"), (0x1F38C, "Crossed Flags"),
    (0x1F38D, "Pine Decoration"), (0x1F38E, "Japanese Dolls"),
    (0x1F38F, "Carp Streamer"), (0x1F390, "Wind Chime"),
    (0x1F391, "Moon Viewing Ceremony"), (0x1F380, "Ribbon"),
    (0x1F381, "Wrapped Gift"), (0x1F382, "Birthday Cake"),
    (0x1F383, "Jack-O-Lantern"), (0x1F384, "Christmas Tree"),
    (0x1F386, "Fireworks"), (0x1F387, "Sparkler"),
    (0x1F388, "Balloon"), (0x1F9E7, "Red Envelope"),
    (0x1F9E8, "Firecracker"), (0x1FAA9, "Mirror Ball"),
])
categories.append(cat)

# ============================================================
# 9. FLAGS (NEW - Country flags via Regional Indicators + misc)
# ============================================================
cat = {"id": "flags", "name": "Flags", "icon": "\U0001F3F3", "symbols": []}
# Regional Indicator Symbols (individual letters A-Z)
for i in range(26):
    code = 0x1F1E6 + i
    letter = chr(ord('A') + i)
    cat["symbols"].append({
        "char": chr(code),
        "name": f"Regional Indicator Symbol Letter {letter}",
        "unicode": f"U+{code:04X}",
        "html": f"&#{code};"
    })

# Country flags as two-letter regional indicator pairs
country_flags = [
    ("US", "United States"), ("GB", "United Kingdom"), ("CA", "Canada"),
    ("AU", "Australia"), ("DE", "Germany"), ("FR", "France"),
    ("IT", "Italy"), ("ES", "Spain"), ("PT", "Portugal"),
    ("BR", "Brazil"), ("MX", "Mexico"), ("AR", "Argentina"),
    ("CO", "Colombia"), ("CL", "Chile"), ("PE", "Peru"),
    ("IN", "India"), ("PK", "Pakistan"), ("BD", "Bangladesh"),
    ("CN", "China"), ("JP", "Japan"), ("KR", "South Korea"),
    ("TW", "Taiwan"), ("TH", "Thailand"), ("VN", "Vietnam"),
    ("ID", "Indonesia"), ("MY", "Malaysia"), ("PH", "Philippines"),
    ("SG", "Singapore"), ("RU", "Russia"), ("UA", "Ukraine"),
    ("PL", "Poland"), ("NL", "Netherlands"), ("BE", "Belgium"),
    ("SE", "Sweden"), ("NO", "Norway"), ("DK", "Denmark"),
    ("FI", "Finland"), ("CH", "Switzerland"), ("AT", "Austria"),
    ("IE", "Ireland"), ("GR", "Greece"), ("TR", "Turkey"),
    ("EG", "Egypt"), ("ZA", "South Africa"), ("NG", "Nigeria"),
    ("KE", "Kenya"), ("GH", "Ghana"), ("ET", "Ethiopia"),
    ("MA", "Morocco"), ("TZ", "Tanzania"),
    ("SA", "Saudi Arabia"), ("AE", "United Arab Emirates"),
    ("QA", "Qatar"), ("KW", "Kuwait"), ("IL", "Israel"),
    ("JO", "Jordan"), ("LB", "Lebanon"), ("IQ", "Iraq"),
    ("IR", "Iran"), ("AF", "Afghanistan"),
    ("NZ", "New Zealand"), ("FJ", "Fiji"),
    ("CU", "Cuba"), ("JM", "Jamaica"), ("HT", "Haiti"),
    ("DO", "Dominican Republic"), ("PR", "Puerto Rico"),
    ("IS", "Iceland"), ("LU", "Luxembourg"),
    ("CZ", "Czech Republic"), ("SK", "Slovakia"),
    ("HU", "Hungary"), ("RO", "Romania"), ("BG", "Bulgaria"),
    ("HR", "Croatia"), ("RS", "Serbia"), ("BA", "Bosnia"),
    ("SI", "Slovenia"), ("LT", "Lithuania"), ("LV", "Latvia"),
    ("EE", "Estonia"), ("GE", "Georgia"),
    ("AM", "Armenia"), ("AZ", "Azerbaijan"),
    ("KZ", "Kazakhstan"), ("UZ", "Uzbekistan"),
    ("NP", "Nepal"), ("LK", "Sri Lanka"), ("MM", "Myanmar"),
    ("KH", "Cambodia"), ("LA", "Laos"), ("MN", "Mongolia"),
    ("HK", "Hong Kong"), ("MO", "Macao"),
    ("PA", "Panama"), ("CR", "Costa Rica"), ("GT", "Guatemala"),
    ("EC", "Ecuador"), ("VE", "Venezuela"), ("BO", "Bolivia"),
    ("PY", "Paraguay"), ("UY", "Uruguay"),
    ("DZ", "Algeria"), ("TN", "Tunisia"), ("LY", "Libya"),
    ("SD", "Sudan"), ("CM", "Cameroon"), ("CD", "Congo"),
    ("AO", "Angola"), ("MZ", "Mozambique"),
    ("MG", "Madagascar"), ("ZW", "Zimbabwe"),
    ("EU", "European Union"),
]

for code2, name in country_flags:
    c1 = 0x1F1E6 + (ord(code2[0]) - ord('A'))
    c2 = 0x1F1E6 + (ord(code2[1]) - ord('A'))
    ch = chr(c1) + chr(c2)
    cat["symbols"].append({
        "char": ch,
        "name": f"Flag: {name} ({code2})",
        "unicode": f"U+{c1:04X} U+{c2:04X}",
        "html": f"&#{c1};&#{c2};"
    })

# Misc flags
add_list(cat["symbols"], [
    (0x1F3F3, "White Flag"), (0x1F3F4, "Black Flag"),
    (0x1F3C1, "Chequered Flag"), (0x1F6A9, "Triangular Flag"),
    (0x1F38C, "Crossed Flags"),
])
categories.append(cat)

# ============================================================
# 10. ARROWS (Complete Unicode Arrows block)
# ============================================================
cat = {"id": "arrows", "name": "Arrows", "icon": "\u2192", "symbols": []}
# Arrows block U+2190–U+21FF
add_range(cat["symbols"], 0x2190, 0x21FF)
# Supplemental Arrows-A U+27F0–U+27FF
add_range(cat["symbols"], 0x27F0, 0x27FF)
# Supplemental Arrows-B U+2900–U+297F
add_range(cat["symbols"], 0x2900, 0x297F)
# Dingbat arrows
add_list(cat["symbols"], [
    (0x2794, "Heavy Wide-Headed Rightwards Arrow"),
    (0x27A1, "Black Rightwards Arrow"),
    (0x2B05, "Leftwards Black Arrow"), (0x2B06, "Upwards Black Arrow"),
    (0x2B07, "Downwards Black Arrow"), (0x2B08, "North East Black Arrow"),
    (0x2B09, "North West Black Arrow"), (0x2B0A, "South East Black Arrow"),
    (0x2B0B, "South West Black Arrow"),
])
categories.append(cat)

# ============================================================
# 11. MATH SYMBOLS (Complete)
# ============================================================
cat = {"id": "math", "name": "Mathematics", "icon": "\u2211", "symbols": []}
# Mathematical Operators U+2200–U+22FF
add_range(cat["symbols"], 0x2200, 0x22FF)
# Supplemental Mathematical Operators U+2A00–U+2AFF
add_range(cat["symbols"], 0x2A00, 0x2AFF)
# Miscellaneous Mathematical Symbols-A U+27C0–U+27EF
add_range(cat["symbols"], 0x27C0, 0x27EF)
# Miscellaneous Mathematical Symbols-B U+2980–U+29FF
add_range(cat["symbols"], 0x2980, 0x29FF)
# Common math extras
add_list(cat["symbols"], [
    (0x002B, "Plus Sign"), (0x00D7, "Multiplication Sign"), (0x00F7, "Division Sign"),
    (0x003D, "Equals Sign"), (0x00B1, "Plus-Minus Sign"), (0x00B0, "Degree Sign"),
    (0x00B7, "Middle Dot"), (0x00AC, "Not Sign"),
    (0x00BC, "Fraction One Quarter"), (0x00BD, "Fraction One Half"),
    (0x00BE, "Fraction Three Quarters"),
])
categories.append(cat)

# ============================================================
# 12. GREEK & COPTIC (Full block)
# ============================================================
cat = {"id": "greek", "name": "Greek & Coptic", "icon": "\u03A9", "symbols": []}
add_range(cat["symbols"], 0x0370, 0x03FF)
# Greek Extended
add_range(cat["symbols"], 0x1F00, 0x1FFF)
categories.append(cat)

# ============================================================
# 13. CYRILLIC
# ============================================================
cat = {"id": "cyrillic", "name": "Cyrillic", "icon": "\u0414", "symbols": []}
add_range(cat["symbols"], 0x0400, 0x04FF)
categories.append(cat)

# ============================================================
# 14. ARABIC
# ============================================================
cat = {"id": "arabic", "name": "Arabic", "icon": "\u0639", "symbols": []}
add_range(cat["symbols"], 0x0600, 0x06FF)
categories.append(cat)

# ============================================================
# 15. DEVANAGARI (Hindi)
# ============================================================
cat = {"id": "devanagari", "name": "Devanagari (Hindi)", "icon": "\u0905", "symbols": []}
add_range(cat["symbols"], 0x0900, 0x097F)
categories.append(cat)

# ============================================================
# 16. CJK SYMBOLS & IDEOGRAPHS (common)
# ============================================================
cat = {"id": "cjk", "name": "CJK & Japanese", "icon": "\u4E00", "symbols": []}
# CJK Symbols and Punctuation
add_range(cat["symbols"], 0x3000, 0x303F)
# Hiragana
add_range(cat["symbols"], 0x3040, 0x309F)
# Katakana
add_range(cat["symbols"], 0x30A0, 0x30FF)
# CJK Unified Ideographs (first 200 most common)
common_cjk = [
    (0x4E00, "One"), (0x4E8C, "Two"), (0x4E09, "Three"), (0x56DB, "Four"),
    (0x4E94, "Five"), (0x516D, "Six"), (0x4E03, "Seven"), (0x516B, "Eight"),
    (0x4E5D, "Nine"), (0x5341, "Ten"), (0x767E, "Hundred"), (0x5343, "Thousand"),
    (0x4E07, "Ten Thousand"), (0x5146, "Trillion"),
    (0x5927, "Big"), (0x5C0F, "Small"), (0x4E2D, "Middle"), (0x4E0A, "Up"),
    (0x4E0B, "Down"), (0x5DE6, "Left"), (0x53F3, "Right"),
    (0x65E5, "Day/Sun"), (0x6708, "Month/Moon"), (0x5E74, "Year"),
    (0x6642, "Time"), (0x4EBA, "Person"), (0x5973, "Woman"), (0x7537, "Man"),
    (0x5B50, "Child"), (0x7236, "Father"), (0x6BCD, "Mother"),
    (0x5148, "First"), (0x751F, "Life/Birth"), (0x5B66, "Study"),
    (0x6821, "School"), (0x56FD, "Country"), (0x5C71, "Mountain"),
    (0x5DDD, "River"), (0x6D77, "Sea"), (0x7A7A, "Sky/Empty"),
    (0x82B1, "Flower"), (0x96E8, "Rain"), (0x98A8, "Wind"),
    (0x706B, "Fire"), (0x6C34, "Water"), (0x571F, "Earth"),
    (0x91D1, "Gold/Metal"), (0x6728, "Tree/Wood"),
    (0x77F3, "Stone"), (0x7530, "Rice Field"), (0x529B, "Power"),
    (0x6C17, "Spirit"), (0x5FC3, "Heart"), (0x624B, "Hand"),
    (0x8DB3, "Foot"), (0x76EE, "Eye"), (0x8033, "Ear"),
    (0x53E3, "Mouth"), (0x9B5A, "Fish"), (0x9CE5, "Bird"),
    (0x72AC, "Dog"), (0x732B, "Cat"), (0x99AC, "Horse"),
    (0x725B, "Cow"), (0x7F8A, "Sheep"), (0x8C5A, "Pig"),
    (0x866B, "Insect"), (0x7AF9, "Bamboo"), (0x7C73, "Rice"),
    (0x8336, "Tea"), (0x9152, "Sake/Alcohol"), (0x8089, "Meat"),
    (0x98DF, "Food/Eat"), (0x98F2, "Drink"),
    (0x611B, "Love"), (0x5922, "Dream"), (0x5E78, "Happiness"),
    (0x798F, "Fortune/Luck"), (0x5BFF, "Longevity"),
    (0x5FB3, "Virtue"), (0x4FE1, "Trust"), (0x7F8E, "Beauty"),
    (0x548C, "Peace/Harmony"), (0x5149, "Light"),
    (0x95C7, "Darkness"), (0x6B7B, "Death"), (0x547D, "Life/Fate"),
    (0x6226, "War"), (0x5263, "Sword"), (0x9F8D, "Dragon"),
    (0x864E, "Tiger"), (0x9B3C, "Demon"), (0x795E, "God/Spirit"),
    (0x4ECF, "Buddha"), (0x5929, "Heaven"), (0x5730, "Earth/Ground"),
    (0x738B, "King"), (0x7687, "Emperor"), (0x59EB, "Princess"),
    (0x6B66, "Martial"), (0x5FCD, "Endure/Ninja"),
]
for code, name in common_cjk:
    cat["symbols"].append({"char": chr(code), "name": f"CJK: {name}", "unicode": f"U+{code:04X}", "html": f"&#{code};"})
categories.append(cat)

# ============================================================
# 17. CURRENCY SYMBOLS (Complete block)
# ============================================================
cat = {"id": "currency", "name": "Currency Symbols", "icon": "$", "symbols": []}
add_list(cat["symbols"], [
    (0x0024, "Dollar Sign"), (0x00A2, "Cent Sign"), (0x00A3, "Pound Sign"),
    (0x00A4, "Currency Sign"), (0x00A5, "Yen Sign"),
])
add_range(cat["symbols"], 0x20A0, 0x20CF)
add_list(cat["symbols"], [
    (0x058F, "Armenian Dram"), (0x060B, "Afghani Sign"),
    (0x09F3, "Bengali Rupee"), (0x0BF9, "Tamil Rupee"),
    (0x0E3F, "Thai Baht"), (0x17DB, "Khmer Currency Symbol"),
    (0xFDFC, "Rial Sign"),
])
categories.append(cat)

# ============================================================
# 18. PUNCTUATION & TYPOGRAPHY
# ============================================================
cat = {"id": "punctuation", "name": "Punctuation & Typography", "icon": "\u00B6", "symbols": []}
# General Punctuation U+2000–U+206F
add_range(cat["symbols"], 0x2010, 0x205E)
# Supplemental Punctuation
add_range(cat["symbols"], 0x2E00, 0x2E4F)
add_list(cat["symbols"], [
    (0x00A1, "Inverted Exclamation Mark"), (0x00AB, "Left Double Angle Quotation"),
    (0x00BB, "Right Double Angle Quotation"), (0x00BF, "Inverted Question Mark"),
    (0x00A7, "Section Sign"), (0x00A9, "Copyright Sign"),
    (0x00AE, "Registered Sign"), (0x00B6, "Pilcrow Sign"),
])
categories.append(cat)

# ============================================================
# 19. SHAPES & GEOMETRIC (Complete blocks)
# ============================================================
cat = {"id": "shapes", "name": "Shapes & Geometric", "icon": "\u25A0", "symbols": []}
# Geometric Shapes U+25A0–U+25FF
add_range(cat["symbols"], 0x25A0, 0x25FF)
# Miscellaneous Symbols U+2600–U+26FF (many shapes/symbols here)
add_range(cat["symbols"], 0x2600, 0x26FF)
# Dingbats U+2700–U+27BF
add_range(cat["symbols"], 0x2700, 0x27BF)
# Geometric Shapes Extended U+1F780–U+1F7FF
add_range(cat["symbols"], 0x1F780, 0x1F7FF)
categories.append(cat)

# ============================================================
# 20. BOX DRAWING & BLOCKS (Complete blocks)
# ============================================================
cat = {"id": "box-drawing", "name": "Box Drawing & Blocks", "icon": "\u250C", "symbols": []}
add_range(cat["symbols"], 0x2500, 0x257F)  # Box Drawing
add_range(cat["symbols"], 0x2580, 0x259F)  # Block Elements
categories.append(cat)

# ============================================================
# 21. LETTERLIKE & NUMBER FORMS
# ============================================================
cat = {"id": "letterlike", "name": "Letterlike & Numbers", "icon": "\u2115", "symbols": []}
# Letterlike Symbols
add_range(cat["symbols"], 0x2100, 0x214F)
# Number Forms
add_range(cat["symbols"], 0x2150, 0x218F)
# Enclosed Alphanumerics
add_range(cat["symbols"], 0x2460, 0x24FF)
# Enclosed Alphanumeric Supplement
add_range(cat["symbols"], 0x1F100, 0x1F1FF)
# Superscripts and Subscripts
add_range(cat["symbols"], 0x2070, 0x209F)
categories.append(cat)

# ============================================================
# 22. BRAILLE PATTERNS (Full block)
# ============================================================
cat = {"id": "braille", "name": "Braille Patterns", "icon": "\u2803", "symbols": []}
add_range(cat["symbols"], 0x2800, 0x28FF)
categories.append(cat)

# ============================================================
# 23. MUSICAL & PLAYING CARDS
# ============================================================
cat = {"id": "music-cards", "name": "Music, Cards & Games", "icon": "\u2669", "symbols": []}
# Musical Symbols
add_list(cat["symbols"], [
    (0x2669, "Quarter Note"), (0x266A, "Eighth Note"),
    (0x266B, "Beamed Eighth Notes"), (0x266C, "Beamed Sixteenth Notes"),
    (0x266D, "Music Flat Sign"), (0x266E, "Music Natural Sign"),
    (0x266F, "Music Sharp Sign"),
])
# Musical Symbols block
add_range(cat["symbols"], 0x1D100, 0x1D1FF)
# Playing Cards
add_range(cat["symbols"], 0x1F0A0, 0x1F0FF)
# Domino Tiles
add_range(cat["symbols"], 0x1F030, 0x1F09F)
# Mahjong Tiles
add_range(cat["symbols"], 0x1F000, 0x1F02F)
# Dice
add_list(cat["symbols"], [
    (0x2680, "Die Face-1"), (0x2681, "Die Face-2"), (0x2682, "Die Face-3"),
    (0x2683, "Die Face-4"), (0x2684, "Die Face-5"), (0x2685, "Die Face-6"),
])
categories.append(cat)

# ============================================================
# 24. LATIN EXTENDED & IPA
# ============================================================
cat = {"id": "latin", "name": "Latin Extended & IPA", "icon": "\u00C9", "symbols": []}
# Latin-1 Supplement (accented chars)
add_range(cat["symbols"], 0x00C0, 0x00FF)
# Latin Extended-A
add_range(cat["symbols"], 0x0100, 0x017F)
# Latin Extended-B (selection)
add_range(cat["symbols"], 0x0180, 0x024F)
# IPA Extensions
add_range(cat["symbols"], 0x0250, 0x02AF)
# Spacing Modifier Letters
add_range(cat["symbols"], 0x02B0, 0x02FF)
categories.append(cat)

# ============================================================
# 25. ZODIAC, SYMBOLS & RELIGION
# ============================================================
cat = {"id": "symbols-misc", "name": "Symbols & Signs", "icon": "\u262F", "symbols": []}
add_list(cat["symbols"], [
    # Zodiac
    (0x2648, "Aries"), (0x2649, "Taurus"), (0x264A, "Gemini"), (0x264B, "Cancer"),
    (0x264C, "Leo"), (0x264D, "Virgo"), (0x264E, "Libra"), (0x264F, "Scorpio"),
    (0x2650, "Sagittarius"), (0x2651, "Capricorn"), (0x2652, "Aquarius"), (0x2653, "Pisces"),
    (0x26CE, "Ophiuchus"),
    # Planets
    (0x2609, "Sun"), (0x263D, "First Quarter Moon"), (0x263E, "Last Quarter Moon"),
    (0x2640, "Female Sign (Venus)"), (0x2642, "Male Sign (Mars)"),
    (0x263F, "Mercury"), (0x2643, "Jupiter"), (0x2644, "Saturn"),
    (0x2645, "Uranus"), (0x2646, "Neptune"), (0x2647, "Pluto"),
    # Religious / spiritual
    (0x262E, "Peace Symbol"), (0x262F, "Yin Yang"),
    (0x2622, "Radioactive Sign"), (0x2623, "Biohazard Sign"),
    (0x2624, "Caduceus"), (0x2625, "Ankh"),
    (0x2626, "Orthodox Cross"), (0x2627, "Chi Rho"),
    (0x2628, "Cross of Lorraine"), (0x2629, "Cross of Jerusalem"),
    (0x262A, "Star and Crescent"), (0x262C, "Adi Shakti"),
    (0x262D, "Hammer and Sickle"), (0x2638, "Wheel of Dharma"),
    (0x2721, "Star of David"), (0x271D, "Latin Cross"),
    (0x2720, "Maltese Cross"), (0x2719, "Outlined Greek Cross"),
    (0x271A, "Heavy Greek Cross"), (0x271B, "Open Centre Cross"),
    (0x2630, "Trigram for Heaven"), (0x2631, "Trigram for Lake"),
    (0x2632, "Trigram for Fire"), (0x2633, "Trigram for Thunder"),
    (0x2634, "Trigram for Wind"), (0x2635, "Trigram for Water"),
    (0x2636, "Trigram for Mountain"), (0x2637, "Trigram for Earth"),
    # Misc warning / signs
    (0x26A0, "Warning Sign"), (0x26A1, "High Voltage"),
    (0x2699, "Gear"), (0x269B, "Atom Symbol"), (0x269C, "Fleur-de-lis"),
    (0x2696, "Balance Scale"), (0x2694, "Crossed Swords"),
    (0x2695, "Staff of Aesculapius"), (0x269A, "Staff of Hermes"),
    (0x267B, "Recycling Symbol"), (0x267F, "Wheelchair Symbol"),
    (0x267E, "Permanent Paper Sign (Infinity)"),
    (0x2690, "White Flag"), (0x2691, "Black Flag"),
    (0x2698, "Flower"), (0x26B0, "Coffin"), (0x26B1, "Funeral Urn"),
    # Ballot / check
    (0x2610, "Ballot Box"), (0x2611, "Ballot Box with Check"),
    (0x2612, "Ballot Box with X"),
    (0x2713, "Check Mark"), (0x2714, "Heavy Check Mark"),
    (0x2715, "Multiplication X"), (0x2716, "Heavy Multiplication X"),
    (0x2717, "Ballot X"), (0x2718, "Heavy Ballot X"),
    # Computer/keyboard
    (0x2318, "Command Key (Place of Interest)"), (0x2325, "Option Key"),
    (0x21E7, "Shift Key (Upwards White Arrow)"), (0x2303, "Control (Up Arrowhead)"),
    (0x238B, "Escape (Broken Circle with Northwest Arrow)"),
    (0x23CE, "Return Symbol"), (0x232B, "Erase to the Left"),
    (0x2326, "Erase to the Right"), (0x21E5, "Tab Key (Rightwards Arrow to Bar)"),
    (0x21EA, "Caps Lock"), (0x2423, "Open Box (Space)"),
    (0x21DE, "Page Up"), (0x21DF, "Page Down"),
    (0x23CF, "Eject Symbol"), (0x23F4, "Black Left-Pointing Double Triangle"),
    (0x23F5, "Black Right-Pointing Double Triangle (Fast Forward)"),
    (0x23F6, "Black Up-Pointing Double Triangle"),
    (0x23F7, "Black Down-Pointing Double Triangle"),
    (0x23F8, "Double Vertical Bar (Pause)"),
    (0x23F9, "Black Square for Stop"), (0x23FA, "Black Circle for Record"),
    (0x23F0, "Alarm Clock"), (0x23F1, "Stopwatch"), (0x23F2, "Timer Clock"),
    (0x23F3, "Hourglass with Flowing Sand"), (0x231A, "Watch"), (0x231B, "Hourglass"),
    (0x23EB, "Black Up-Pointing Double Triangle"),
    (0x23EC, "Black Down-Pointing Double Triangle"),
    (0x23ED, "Black Right-Pointing Double Triangle with Bar"),
    (0x23EE, "Black Left-Pointing Double Triangle with Bar"),
    # Gender
    (0x26A2, "Doubled Female Sign"), (0x26A3, "Doubled Male Sign"),
    (0x26A4, "Interlocked Female and Male Sign"),
    (0x26A5, "Male and Female Sign"), (0x26A6, "Male with Stroke Sign"),
    (0x26A7, "Male with Stroke and Male and Female Sign"),
    (0x26B2, "Neuter"),
    # Info symbols
    (0x2139, "Information Source"),
    (0x24C2, "Circled Latin Capital Letter M (Metro)"),
    (0x1F17E, "O Button (Blood Type)"),
    (0x1F17F, "P Button (Parking)"),
    (0x1F170, "A Button (Blood Type)"),
    (0x1F171, "B Button (Blood Type)"),
    (0x1F18E, "AB Button (Blood Type)"),
    (0x1F191, "CL Button"), (0x1F192, "Cool Button"),
    (0x1F193, "Free Button"), (0x1F194, "ID Button"),
    (0x1F195, "New Button"), (0x1F196, "NG Button"),
    (0x1F197, "OK Button"), (0x1F198, "SOS Button"),
    (0x1F199, "Up! Button"), (0x1F19A, "VS Button"),
    (0x1F201, "Japanese Here Button"), (0x1F202, "Japanese Service Charge Button"),
    (0x1F21A, "Japanese Free of Charge Button"),
    (0x1F22F, "Japanese Reserved Button"),
    (0x1F232, "Japanese Prohibited Button"),
    (0x1F233, "Japanese Vacancy Button"),
    (0x1F234, "Japanese Passing Grade Button"),
    (0x1F235, "Japanese No Vacancy Button"),
    (0x1F236, "Japanese Not Free of Charge Button"),
    (0x1F237, "Japanese Monthly Amount Button"),
    (0x1F238, "Japanese Application Button"),
    (0x1F239, "Japanese Discount Button"),
    (0x1F23A, "Japanese Open for Business Button"),
    (0x1F250, "Japanese Bargain Button"),
    (0x1F251, "Japanese Acceptable Button"),
    # Number signs
    (0x0023, "Number Sign"), (0x002A, "Asterisk"),
    (0x1F51F, "Keycap Digit Ten"),
    (0x1F520, "Input Latin Uppercase"), (0x1F521, "Input Latin Lowercase"),
    (0x1F522, "Input Numbers"), (0x1F523, "Input Symbols"),
    (0x1F524, "Input Latin Letters"),
])
categories.append(cat)

# ============================================================
# 26. EMOTICONS & MISCELLANEOUS PICTOGRAPHS
# ============================================================
cat = {"id": "pictographs", "name": "Pictographs & Emoticons", "icon": "\U0001F300", "symbols": []}
# Misc Symbols and Pictographs U+1F300–U+1F5FF
# Just do a range - this covers TONS of emojis
add_range(cat["symbols"], 0x1F300, 0x1F320)  # Weather, sky
add_range(cat["symbols"], 0x1F32D, 0x1F335)  # Food & plants
add_range(cat["symbols"], 0x1F3A0, 0x1F3FA)  # Activity & sports
add_range(cat["symbols"], 0x1F4A0, 0x1F4FD)  # Objects
add_range(cat["symbols"], 0x1F500, 0x1F579)  # Media & controls
add_range(cat["symbols"], 0x1F5A0, 0x1F5FF)  # Misc
add_range(cat["symbols"], 0x1F600, 0x1F64F)  # Emoticons (faces + gestures)
add_range(cat["symbols"], 0x1F680, 0x1F6FF)  # Transport & map
add_range(cat["symbols"], 0x1F900, 0x1F9FF)  # Supplemental symbols
add_range(cat["symbols"], 0x1FA00, 0x1FA6F)  # Chess, etc
add_range(cat["symbols"], 0x1FA70, 0x1FAFF)  # Extended-A
categories.append(cat)


# ============================================================
# BUILD AND SAVE
# ============================================================
data = {"categories": categories}

total = sum(len(c["symbols"]) for c in categories)
print(f"\n{'='*50}")
print(f"UNICODE SYMBOL DATABASE v2")
print(f"{'='*50}")
print(f"Total categories: {len(categories)}")
for c in categories:
    print(f"  {c['name']:35s} {len(c['symbols']):>5} symbols")
print(f"{'='*50}")
print(f"TOTAL SYMBOLS: {total}")
print(f"{'='*50}")

# Write website JSON
os.makedirs(os.path.join("website", "data"), exist_ok=True)
out_path = os.path.join("website", "data", "symbols.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"\nWebsite JSON: {out_path} ({os.path.getsize(out_path):,} bytes)")

# Write chrome extension JS
ext_path = os.path.join("chrome-extension", "symbols.js")
with open(ext_path, "w", encoding="utf-8") as f:
    f.write("const SYMBOLS_DATA = ")
    json.dump(data, f, ensure_ascii=False)
    f.write(";")
print(f"Extension JS: {ext_path} ({os.path.getsize(ext_path):,} bytes)")

# Validate
with open(out_path, "r", encoding="utf-8") as f:
    test = json.load(f)
total_v = sum(len(c["symbols"]) for c in test["categories"])
print(f"\nValidation: JSON is VALID with {total_v} symbols across {len(test['categories'])} categories")

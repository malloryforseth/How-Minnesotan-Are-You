topic_prompt = "\nHello! Thanks for playing my game: How Minnesotan Are You? "\
"A quiz about the...uh, charms...of Minnesota culture. \n\nPlease select a "\
"quiz topic by typing it in. Possible choices are: vocabulary, social "\
"niceties, or tundra survival.\n\n"

unexpected_response = "\nSorry, we couldn't match your response to any of the "\
"options for this question. Please start the game again.\n"

def select_topic():
    """prompts user to choose a topic for the game. Outputs topic confirmation
    msg or error msg."""
    user_topic = raw_input(topic_prompt).lower()
    expected_responses = ['vocabulary', 'social niceties', 'tundra survival']
    assert user_topic in expected_responses, unexpected_response
    if user_topic in expected_responses:
        print "\nYou've chosen " + user_topic + "!"
        return user_topic

hints_prompt = "\nYou will get 4 chances to guess the correct answer for each "\
"blank. You now must choose whether or not to receive hints. If you choose "\
"'yes', following your second wrong guess for any blank, you will receive a "\
"hint giving you the first letter of the answer to that blank. Would you like "\
"to receive hints? Type yes or no.\n\n"

yes_hints = "\nAlrighty, I got your back! You will get 4 guesses per blank, "\
"and will receive hints following two wrong guesses for any blank.\n"

no_hints = "\nI like your confidence! You will get 4 guesses per blank, and "\
"we'll do this round without hints.\n"

def select_hints():
    """prompts user to choose whether or not to receive hints during the game.
    Prints confirmation msg or error msg & returns T/F."""
    user_hints = raw_input(hints_prompt).lower()
    assert user_hints == "yes" or user_hints == "no", unexpected_response
    if user_hints == "yes":
        print yes_hints
        return True
    else:
        print no_hints
        return False

def get_quiz_and_answers(topic, quiz_list):
    """takes user topic choice and list with quiz texts as input,
    outputs list containing quiz text and answers for the chosen topic."""
    for element in quiz_list:
        if element[0] == topic:
            quiz_and_answers = [element[1], element[2]]
            return quiz_and_answers


quiz_list = [["vocabulary","You just arrived at a party and the host asks if "\
"you'd like a drink. In place of 'yes', a true Minnesotan would say, 'You "\
"___1___!' Whoa! The drink is a tad stronger than you had bargained for. Use "\
"the Minnesota go-to exclamation - '___2___!' to express your surprise, "\
"between coughs. Need a fizzy chaser to wash it down? Better know what to ask "\
"for! It's called ___3___ around these parts. Dying for the recipe for that "\
"delicious, bubbly, oven-baked medley dish from the party buffet table? Don't "\
"disgrace the chef with the 'c' word. We don't care what you fancy pants call it, us salt of the earth folks know it as ___4___. Respect.", ["betcha",
"uffda", "pop", "hotdish"]], ["social niceties","First, it's important to "\
"understand that the number one topic of conversation in Minnesota is the "\
"___1___. Always. Get used to talking about it at length. Every day. In both "\
"seasons (winter and road construction). Second, you must know that "\
"Minnesotans will go to great lengths to avoid conflict. Do not break this "\
"unspoken social contract. Find something unpleasant, off-putting, "\
"disturbing, even downright repulsive? Say, 'Well, that's... ___2___.' We'll "\
" get the message. Some call it passive agressive, we prefer Minnesota "\
"___3___. Finally, let go of any hope of a quick escape from conversations or "\
"social engagements. Unless you want to leave everyone wondering what they've "\
"done to so deeply offend you, you must adopt the Minnesota long ___4___. "\
"Something about the lingering makes us feel secure. Like we must really like "\
"each other. Since we can never be sure what other Minnesotans *really* "\
"think,  a little lingering assurance goes a long way. Give yourself at least "\
"5 minutes to hang up the phone and a good 15 to 20 minutes to be out the "\
"door, and you'll stay in good graces.", ["weather", "different", "nice",
"goodbye"]],["tundra survival","Your little wallet-sized ice scraper sure is "\
"cute, but it's time to quit playing if you hope to survive a winter in the "\
"tundra. The best tool to clean snow from your car is a push ___1___. Hit up "\
"a hardware store and invest, stat. If you think our 10,000 lakes are only "\
"for summertime fun, you are mistaken. Grab a case of beer and a pint of "\
"minnows - you don't really *get* Minnesota until you've spent a day ___2___ "\
"in a shanty. Never fret, you'll warm up once the sun has gone down at the "\
"local watering hole. While you're there, be sure to participate in our "\
"charity gambling traditions by buying a ticket or twenty to the ___3___ "\
"raffle. Gambling, raw steak, a good cause - what's not to love? After 4 or 5 "\
"months of car sweeping, ___2___  and ___3___ raffles, you better believe "\
 "you'll be celebrating the arrival of spring. It's March, and the "\
 "thermometer just hit a whopping 40 degrees. Show your excitement like a "\
 "Minnesotan by busting those ___4___ out of the closet first thing. Who cares if there's still snow on the ground? You feel so...free.", ["broom",
 "ice fishing", "meat", "shorts"]]]

blanks = ["___1___", "___2___", "___3___", "___4___"]

correct_response_q123 = "\nCorrect answer! Nice work! Onwards!\n"

correct_final_q = "\nYou betcha! You answered all of the questions correctly! "\
"Certified Minnesotan! (And if not, they'll never know.) Thanks for playing!\n"

incorrect_try_again = "\nSorry, that is incorrect. Give it another shot!"

incorrect_hint = "\nSorry that is incorrect. How about a hint? The first "\
"letter of the answer is: "

game_over = "\nSorry, that is incorrect and you're out of guesses. Game over!"\
" :( Maybe you can search out a Minnesotan friend to help you along? We're "\
"real nice people, don'tcha know?! \n"


def guesses_remaining(attempt_count):
    """Takes attempt number as input.
    Outputs text informing user of number of guesses remaining."""
    number = 4 - attempt_count
    print number
    return " You've got " + str(number) + " guesses remaining.\n"


def respond_correct_answer(blank_count):
    """Takes blank_count as input.
    Outputs the appropriate game response to a correct answer for that blank."""
    if blank_count == 4:
        return correct_final_q
    else:
        return correct_response_q123


def respond_incorrect_answer(attempt_count, answers, blank_count, hints):
    """Takes attempt_count, answers, blank_count, and hints as input.
    Outputs appropriate game reponse to an incorrect answer for that blank,
    attempt number, and choice of hints."""
    if attempt_count == 4:
        return game_over
    if hints == True and attempt_count == 2:
        return (incorrect_hint + answers[blank_count-1][0] + "." + guesses_remaining(attempt_count))
    return incorrect_try_again + guesses_remaining(attempt_count)


def check_user_answer(quiz, answers, blanks, blank_count):
    """Takes quiz, answers, blanks, and blank_count as input.
    Prompts user for answer for that quiz and blank_count.
    Tests to see if user answer is correct, returns T/F."""
    user_answer = raw_input("The current paragraph reads as such:\n\n" + quiz +
    "\n\nWhat should be substituted for" + blanks[blank_count-1] + "?\n\n")
    correct_answer = answers[blank_count-1]
    if user_answer == correct_answer:
        return True
    else:
        return False


def run_quiz(quiz, answers, blanks, hints):
    # NOTE FOR REVIEWER: I struggled a bit to explain what this does, which
    # probably means it's not very well-written code, but I arrived here via
    # much tinkering and IT WORKS (!) so I don't really want to touch it
    # anymore, but I very much look forward to your input on ways to improve.

    """Takes unfilled quiz text, list of quiz answers, list of unfilled blanks
    in the quiz, and user choice to receive hints or not as input.
    For each blank, prompts user to fill in blank, tests to see if answer is
    correct, and provides the appropriate response depending on correctness,
    blank number, choice of hints, and attempt number."""
    blank_count = 1
    for i in blanks:
        attempt_count = 1
        while attempt_count <= 4:
            if check_user_answer(quiz, answers, blanks, blank_count) == True:
                print respond_correct_answer(blank_count)
                quiz = quiz.replace(blanks[blank_count - 1], answers[blank_count-1])
                if blank_count != 4:
                    blank_count = blank_count + 1
                    attempt_count = 1
                else:
                    return
            else:
                print respond_incorrect_answer(attempt_count, answers, blank_count, hints)
                attempt_count = attempt_count + 1
        return
    return


def play_game(quiz_list, blanks):
    """Takes two lists as input - one containing unfilled quiz text and
    answers, and the other a list of the blanks in the quiz text.
    Prompts user to select topic and choose whether or not to receive hints.
    Defines lists of quiz and answers according to user topic selection.
    Prompts user to type 'go' to begin and runs run_quiz function."""
    topic = select_topic()
    hints = select_hints()
    quiz = get_quiz_and_answers(topic, quiz_list)[0]
    answers = get_quiz_and_answers(topic, quiz_list)[1]
    if raw_input("Type 'go' to begin!\n\n").lower() == "go":
        run_quiz(quiz, answers, blanks, hints)


play_game(quiz_list, blanks)

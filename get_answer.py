import warnings
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from transformers import pipeline
import os
import random

list1 = [
"Let your thoughts flow with journaling fun!",
"Dive into therapy, it's like a brain spa!",
"Scream it out like you're in a movie scene!",
"Sink into serenity with a marathon bath!",
"Say 'bye' to screens like a tech ninja!",
"Box away stress like a champ!",
"Let thoughts marinate like a gourmet dish!",
"Tears are like emotional confetti, let them fall!",
"Snuggle into sleep like a cozy burrito!",
"Netflix and chill - the ultimate relaxation recipe!",
"Meditation: finding zen or just daydreaming?",
"Lazy days: the ultimate superpower!",
"Unplug and recharge like a digital phoenix!",
"Celebrate your quirks like it's a party for one!"
]

list2 = [
"Reach out to a friend for a virtual hug!",
"Blast your favorite song like you're at a concert!",
"Doodle and color like a kid on a sugar rush!",
"Revive old friendships like a reunion party!",
"Squeeze a stress ball like a superhero in training!",
"Netflix and chill: the sequel!",
"Unplug and reset like a digital magician!",
"Bathe away stress like a spa day at home!",
"Screen time boundaries: challenge accepted!",
"Box away stress like a champ in training!",
"Absorb thoughts like a sponge in a brainstorm!",
"Shop 'til you drop like a retail therapy pro!",
"Indulge in your favorite dish like it's a gourmet feast!",
"Get lost in a book like a literary explorer!",
"Smile like you're on a sitcom set!",
"Meditation: find inner peace or just take a nap?",
"Cook up a storm like a culinary artist!",
"Connect with furry friends like a pet whisperer!"
]

list3 = [
"Reach out and hug a friend for a dose of comfort!",
"Blast your jam like you're the DJ of your life!",
"Color outside the lines like it's a masterpiece!",
"Rekindle friendships like you're reigniting fireworks!",
"Squeeze a stress ball like it owes you money!",
"Netflix marathon: the sequel!",
"Unplug and reboot like a tech-savvy guru!",
"Soak in bubbles like you're in a relaxation commercial!",
"Screen time rules: challenge accepted!",
"Boxing session: stress relief or audition for Rocky?",
"Absorb thoughts like a sponge in a brainstorm!",
"Retail therapy: because you're worth it!",
"Indulge in a feast fit for a king!",
"Get lost in a book like it's a literary labyrinth!",
"Smile like you're on a happiness mission!",
"Meditation: find your inner calm or just take a nap?",
"Cook up a storm like a culinary wizard!",
"Connect with furry pals like you're a pet whisperer!"
]

list4 = [
"Walk it out like you're strolling on sunshine!",
"Blast your anthem like it's your victory song!",
"Relax in nature's embrace like a zen master!",
"Color outside the lines like an artistic rebel!",
"Netflix marathon: the sequel!",
"Unplug and recharge like a digital nomad!",
"Karaoke night: unleash your inner rockstar!",
"Revive old bonds like reuniting with long-lost pals!",
"Absorb thoughts like a sponge in a brainstorm!",
"Bathe in bubbles like you're in a relaxation spa!",
"Squeeze stress away like a tension-taming pro!",
"Retail therapy: because shopping is cardio for the soul!",
"Indulge in a feast like it's a royal banquet!",
"Escape reality like you're diving into a literary adventure!",
"Smile like it's contagious - Captain Holt approved!",
"Game night: may the best player win!",
"Declutter your mind like tidying up a messy room!",
"Digital detox: unplug and unwind like a tech guru!",
"Cook up creativity like a master chef in the making!"
]


list5 = [
"Step into action like you're on a mission!",
"Rock out to your anthem like it's your personal concert!",
"Absorb thoughts like a sponge in a brainstorm!",
"Find peace in nature's embrace like a park guru!",
"Feast on your favorite dish like it's a gourmet delight!",
"Game on: board game night with friends!",
"Bathe in bubbles like you're in a relaxation sanctuary!",
"Netflix marathon: the ultimate escape!",
"Karaoke showdown: unleash your inner diva!",
"Score goals like a sports superstar!",
"Retail therapy: because every purchase is a victory!",
"Connect with furry pals like you're in a pet paradise!",
"Digital detox: unplug and unwind like a tech wizard!",
"Puzzle time: challenge your brain with fun twists!",
"Declutter for clarity like organizing a mental masterpiece!",
"Run like you're chasing your dreams!",
"Adventure awaits: explore like a fearless explorer!",
"Escape into a book like it's a literary journey!",
"Cook up creativity like a kitchen magician!"
]

list6 = [
"Expand your social circle: make friends like it's a party!",
"Find zen in nature's embrace like a park enthusiast!",
"Dance like nobody's watching to your favorite beat!",
"Rock out: become a music maestro!",
"Unplug and recharge: digital detox time!",
"Absorb thoughts like a sponge in a brainstorm!",
"Bathe in bubbles: stress relief deluxe!",
"Karaoke night: unleash your inner rockstar!",
"Sprinkle kindness like confetti with a random act!",
"Play your favorite sport: victory awaits!",
"Netflix marathon: the ultimate escape!",
"Learn something new: become a skillful master!",
"Retail therapy: because you deserve it!",
"Puzzle time: exercise your brain with fun challenges!",
"Run like the wind: chase your dreams!",
"Adventure awaits: explore like a fearless explorer!"
]

list7 = [
"Expand your social circle: make friends like it's a social safari!",
"Sing your heart out: let your voice be your superhero!",
"Dance like nobody's watching to your favorite beat!",
"Absorb thoughts like a sponge in a brainstorm!",
"Unplug and recharge: digital detox time!",
"Become a musical maestro: play an instrument!",
"Netflix marathon: the ultimate escape!",
"Bathe in bubbles: stress relief deluxe!",
"Learn something new: become a skillful master!",
"Play your favorite sport: victory awaits!",
"Retail therapy: because you're worth it!",
"Karaoke night: unleash your inner rockstar!",
"Write a letter to your future self: time travel with words!",
"Let go of burdens: forgiveness is freedom!",
"Bonjour! Learn a new language: become a polyglot!",
"Spread joy: gift someone a smile with a meaningful gift!",
"Run like the wind: chase your dreams!",
"Recharge with sleep: snooze like a sleep champion!",
"Sprinkle kindness like confetti with a random act!",
"Nourish your body: feast on balanced meals!",
"Adventure awaits: explore like a fearless explorer!",
"Dream big: envision future adventures!",
"Plan for peace: organize for tranquility!",
"Share compliments: spread sunshine with kind words!"
]



list8 = [
"Journal your journey: write your heart out!",
"Sing like you're the star of your own show!",
"Dance to your own beat: groove like nobody's watching!",
"Movie marathon: get lost in cinematic adventures!",
"Absorb thoughts like a sponge in a brainstorm!",
"Unplug and recharge: digital detox time!",
"Become a musical maestro: play an instrument!",
"Karaoke night: unleash your inner rockstar!",
"Learn something new: expand your horizons!",
"Bathe in bubbles: indulge in a relaxation retreat!",
"Let go and forgive: release burdens like balloons!",
"Give thanks: gratitude is the key to happiness!",
"Write a letter to your future self: time-travel with words!",
"Spread joy: share meaningful gifts with loved ones!",
"Bonjour! Learn a new language: embrace linguistic adventures!",
"Run like the wind: chase your dreams with every step!",
"Recharge with sleep: snooze like a sleep champion!",
"Adventure awaits: explore new horizons!",
"Sprinkle kindness like confetti with random acts!",
"Nourish your body: feast on meals that fuel your soul!",
"Dream big: envision adventures yet to unfold!",
"Plan ahead: organize for peace of mind!",
"Share compliments: spread positivity with kind words!",
"Celebrate your uniqueness: you're one of a kind!"
]


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    return score

def display_activities(compound):
    if compound<-0.75:
        return list1
    elif compound<-0.50:
        return list2
    elif compound<-0.25:
        return list3
    elif compound<0:
        return list4
    elif compound<0.25:
        return list5
    elif compound<0.50:
        return list6
    elif compound<0.75:
        return list7
    else:
        return list8


def get_answer(answers):
    
    warnings.filterwarnings("ignore")
    random_number = random.randint(1000, 9999)

    sent_answers = answers[0] + answers[1]
    
    #FINDING THE POLARITY SCORE
    
    ss = sentiment_analyse(sent_answers)
    #neg,neu,pos,compound
    emotions=[]
    scores=[]
    for key, value in ss.items():
        answers.append(value)
        emotions.append(key)
        scores.append(value)

    if ss["compound"]<=-0.25:
        final_emotion="neg"
    elif ss["compound"]>=0.25:
        final_emotion="pos"
    else:
        final_emotion="neu"

    answers.append(final_emotion)
    activity_list = display_activities(ss["compound"])

    #PLOT 

    fig=plt.figure(figsize=(8,6))

    plt.barh(emotions,scores,color="plum",label=emotions)
    plt.title("Sentiment Intensity Plot",color="darkslategray",fontsize=20)
    plt.ylabel("Sentiment",color="darkslategray",fontsize=14)
    plt.xlabel("Intensity",color="darkslategray",fontsize=14)
    for i in range(len(scores)):
        plt.text(scores[i]//2,i , scores[i], ha = 'center',color="black",fontsize=12)
    plt.xlim(-1,1)
    plt.xticks(color="darkslategray")
    plt.yticks(color="darkslategray")

    fig.tight_layout()
    
    [os.remove('static/Website_Images/' + file) for file in os.listdir('static/Website_Images/') if file.startswith("graph")]

    # Save the new graph
    result_file = f'static/Website_Images/graph{random_number}.png'
    plt.savefig(result_file)
    plt.close()

    # SAVING INPUT IN A CSV FILE
    filename = "responses.csv"
            
    # Check if the file exists
    file_exists = False
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            file_exists = bool(next(reader, None))
    except FileNotFoundError:
        pass

    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["q1","q2","tm","pa","sl","neg","neu","pos","com","fe"])
        writer.writerow(answers)
    
    return activity_list , result_file

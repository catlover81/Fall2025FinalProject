label start:

    play music home fadein 0.5

    scene black

    #INCLUDE POPUP THAT HAS THE DATE + TIME

    #December 27, 7:00 AM

    "The polychromatic television screen shows me another reminder of my failures."

    scene news with dissolve

    tv "Notorious phantom thief Selene strikes again, this time pouncing on the \“Madam Fleurette,\” a relic of a wedding long past for a to-be princess of the ancient kingdom of Izoria."

    "I have been trailing the phantom thief Selene for weeks on end, sacrificing sleep and nights out with my friends and colleagues in favor of late nights at the station archives and early mornings at my desk, musing over file after file after file."
    
    tv "The dress was once an heirloom within the Izoria royal family before they were overthrown by a neighboring kingdom, ending their reign."
    
    tv "It was later unearthed and sold to an anthropologist, where it cycled through many owners before landing in the hands of renowned dressmaker Klarika Erdei."
    
    "But this thief is elusive, and they don't leave me any clues. Any leads whatsoever can practically guarantee their arrest and a chance to prove myself a worthy detective."

    "Just like my father would have wanted."

    tv "The Oaksborough Police Department's investigation is still underway. Detective Kova says that while information regarding Selene's identity cannot be disclosed at the time, he and the rest of his team are doing everything they can to catch them."

    scene klmorning with dissolve

    #show tobias serious

    tk serious "Ugh… good job Tobias… that's just another fancy way of saying \“we haven't gotten anywhere.\” People are definitely going to realize that you haven't made any progress in weeks!"

    anon "Woof!"

    "I look down at my leg and see my Bernese Mountain puppy, Lilith, sitting patiently and smiling at me, like she's trying to cheer me up."

    "And it works. I could never stay too upset with her by my side."

    "I shut off the television. It only serves to dampen my mood."

    tk happy "I'm doing just fine, sweetie, I promise."

    dog "Ruff!"

    "Lilith glances over at the clock, reminding me that I only had thirty minutes left to get ready." 
    
    "The chances of me being late for work are low, but I wasn't about to risk it by sitting around and watching the television."

    "I get up from the table, get dressed, pack my bag full of case files and documents, and head to the bathroom one last time to comb my hair and give myself one last spritz of cologne."

    scene lookingood with dissolve

    "Looking good."

    scene frontdoormorning with dissolve

    tk smiley "I'm leaving, Lilith!"

    dog "Woof! Woof woof!"

    "It's always hard to say goodbye to Lilith in the morning, especially when she has a habit of sticking her nose through the crack in the door to try and stop me."

    tk "Who's a good girl? Are you a good girl?"

    dog "Woof!"

    "I assume that means \'yes\'"

    "And I make sure to give her plenty of belly rubs before I go."

    tk base "See you soon!"

    stop music fadeout 0.5

    play sound park fadein 0.5

    scene sidewalkmorning with dissolve

    tk pensive "Should I get coffee today? Hmm..."

    tk base "Sure, why not?"

    "I briskly walk down the street to Titania's Cafe, my favorite place to get coffee in the morning."

    "To be honest, I couldn't care less about the coffee. I could get coffee from anywhere, really. What I was really there for was the barista who made it for me."

    scene cafe with dissolve

    stop sound fadeout 0.5

    play music cafe fadein 1.0

    "I compose myself before I pull the door open, the aroma of coffee beans and freshly baked pastries lulling me inside."

    "A voice interjects to bring me back to reality."

    scene toot with dissolve

    anon "Oh, Detective! Hello!"

    tk smiley "Hey, Tamaki."

    "This is Naoya Tamaki, the cutest, friendliest, most considerate guy I've ever met."

    "He has great posture and exceptional customer service and negotiation skills. And did I mention he was cute?"

    scene cafe with dissolve
    show naoya happy
    nt "Oh, please, detective, we're on a first name basis now, aren't we?"
    show naoya base
    tk blush "Right! Sorry."
    show naoya happy
    nt "No worries. The usual?"

    menu:
        "Yes, please":
            $ good_end_counters += 10
            $ usual_choice = True
            show naoya base
            tk smiley "I'll have the usual, thanks."
            show naoya happy
            nt "Coming right up!"
        "I'll try something else":
            $ good_end_counters += 5
            $ usual_choice = False
            tk smiley "I actually wanted to see what the house espresso was like."
            show naoya serious
            nt "Oh, are you sure?"
            tk smiley "Yeah, I'll give it a try."
            show naoya happy
            nt "Okay, coming right up!"

    hide naoya happy
    "Naoya walks away and I take a seat by the window."

    "I have a bit of time to look over more of the files I stayed up until 2 AM reading."

    "I take out a crisp manila folder and open it. Inside are the contents of an interrogation transcript."

    scene dantefile

    "Psst... person playing... you can read the file by hovering over and clicking parts of the file!"
    play music looking fadein 0.5
    jump file1

label continuation4:

    "I guess I'm done here."

    scene cafe with dissolve
    play music cafe fadein 0.5
    hide screen dantefile
    show naoya serious
    nt "Are those MORE case files?"
    
    tk serious "Gah!"
    show naoya concern
    nt "Oh, sorry! Did I scare you?"
    
    tk blush "A bit, haha..."
    show naoya concern
    nt "Are you... getting enough sleep, detective?"
    
    menu:
        "Lie":
            $ good_end_counters = good_end_counters - 1
            tk smiley "Yeah, I am! You just caught me off guard, is all."
            show naoya concern
            nt "Is that true?"
            
            tk blush "Yeah."
        "Tell the truth":
            $ good_end_counters += 1
            show naoya concern
            tk sad "To be honest, I haven't gotten a good sleep since I took up this case."
            show naoya concern
            nt "You poor thing... you need to give yourself a break every now and then!"
            tk smiley "I know, but this case is such a huge opportunity for me! I can't stop now."
    
    show naoya concern
    nt "Every time you come in, I see you working so hard, detective."

    tk blush "Well, yeah. My dad was a detective, so I feel I owe it to him to become a great detective and make him proud."

    tk smiley "Besides, this thief isn't going to catch themself."
    show naoya cheeky
    nt "I'm sure your dad appreciates all your efforts."

    "I wouldn't know. He died in action when I was still a teenager in highschool. I never got to hear how proud of me he was."
    show naoya cheeky
    nt "Oh! And here's your coffee order. Careful, it's hot."
    jump coffee_order

label coffee_order:
    if usual_choice == True:
        jump usual_order
    elif usual_choice == False:
        jump new_order       
label usual_order:
    show naoya cheeky
    nt "Your usual: A hot mocha latte with whipped cream and enough sugar to kill an elephant and so much chocolate that-"

    tk blush "That it doesn't even taste like coffee anymore, I know."
    show naoya concern
    nt "I'm surprised a big guy like you takes his coffee with this much sugar..."

    tk "Are you judging me based on my coffee order?"
    show naoya blush
    nt "Well, you're plenty sweet already. I don't see why you need any more."

    tk "O-oh."

    "Naoya winks and I can feel myself turning red. I hide my stupid grind behind my hand and clear my throat awkwardly."
    show naoya smiley
    nt "Enjoy!"

    tk smiley "Thanks."
    hide naoya smiley
    "I take a sip of my overly sweet mocha latte. Its overbearing chocolate taste is enough to wash away any sleepiness that still remained in my body from last night."

    "It tastes great, as usual."

    jump continuation1
label new_order:
    show naoya cheeky
    nt "One house espresso, freshly pressed."

    tk smiley "Thank you."
    
    nt "Enjoy!"
    hide naoya smiley
    "I have a feeling Naoya wanted to say more, but he returned to behind the counter."

    "I take a sip of the house espresso. It's strong, nothing like my usual mocha with a truckload of sugar and chocolate."

    "But it wakes me right up and I feel energized enough to get through the rest of my day."

    "I don't really like the bitter flavor, but I won't let it go to waste. I wouldn't be ordering it again, though."

    jump continuation1

label continuation1:

    "I down the last few sips of my coffee and start packing up my file folders."

    "When I go to return my cup, Naoya is busy taking another customer's order. My eyes meet his as I start to head towards the door to leave, and it seems as if he scrambles to get something."

    "Just as I'm about to open the door, I hear his voice call out to me."
    
    nt "Detective, wait!"

    "I turn to find Naoya running up to me with a brown paper bag in his hands. He stops, holds it in front of him, and shakes it a little."
    show naoya smiley
    nt "Here."

    "I take the paper bag. This isn't the first time Naoya has given me a pastry on the house."

    tk blush "Thanks! What is it?"

    nt "It's a muffin. On the house."

    tk "Aw, another treat for little old me? What did I do to deserve this?"
    show naoya cheeky
    nt "Who knows...?"

    tk smiley "Seriously though, Tamaki, you can't just keep giving me pastries because I'm a regular and you like me-"

    "Naoya gives me a playful nudge, and I can swear there's a faint tint of red on his cheeks."
    show naoya blush
    nt "Who said anything about liking you!? And enough referring to me by my last name! We're so past that!"
    show naoya shy
    tk "Haha. Thanks, Naoya, I'll see you soon."
    hide naoya shy
    scene sidewalkmorning with dissolve

    stop music fadeout 0.5

    play sound park fadein 1.0

    "I wave him goodbye as I leave, and while I can't see him as I walk down the sidewalk, I hear him call out to me as clear as day."

    nt "Once you catch this thief, call me! I'll give them a good punch for making you work so hard!"

    tk "That's not necessary, but sure!"

    nt "See you soon!"

    scene officemorning with dissolve

    play sound office fadein 1.0

    # December 27, 9:00 AM

    "After greeting my colleagues and hanging my coat up, I take a seat at my desk to look over some more information."

    "Despite Selene not leaving many traces behind I still have a short stack of files to get through."

    "Just five more things in this pile. Then I can take a small break before moving onto another batch."

    # ENTER JOURNAL MECHANIC

    "I take a deep breath, turning to face the stack of files at the corner of my desk."

    "I reach over to take one when suddenly..."
    show julia happy
    anon "Detective Kova, good morning!"
    show julia base
    "I look up from my  files and see a familiar beaming face."

    "Julia Schmidt: a veterinary major exchange students from Germany with a minor in journalism. She always visits me in the morning before her classes."
    "She says it's for a \"journalism project,\" but all she really wants to do is chat. If it were at a different time, I wouldn't mind it."

    tk happy "Hey, Julia."
    show julia happy
    js "What is popping, fam?"
    show julia base
    tk base "..."
    show julia surprise
    js "Aw come on! Don't you understand your own American slang?"
    show julia base
    "Of course I do. I'm just trying to not to laugh as she says it in a horrible Southern accent."

    tk serious "I'm just gonna eat this."
    show julia surprise
    js "Hm?"
    show julia upset
    js "AH!"
    show julia base
    "Julia yelps and I nearly drop the muffin that Naoya gave me."

    tk "What?"
    show julia surprise
    js "{i}Oh mein Gott!{/i} It's a muffin! {i}Schrippen!{/i} A muffin!"

    "Oh boy..."

    tk "Yeah... it's a muffin. So what?"
    show julia happy
    js "You got it from that barista you keep seeing for coffee in the morning!"
    show julia base
    tk blush "Okay, yeah, Naoya gave me a muffin \"on the house.\" So what? He's just exercising good customer service."
    show julia happy
    js "Well, allow me to pull up some facts!"

    "Julia produces a small notebook from her pocket and flips through some pages before clearing her throat."
    show julia surprise
    js "November 3, Naoya gives you a slice of pumpkin loaf \"on the house.\""

    js "November 14, Naoya gave you a slice of a chestnut tart \"on the house.\""

    js "November 23, Naoya gives you a marshmallow cookie \"on the house-\""

    tk serious "How long have you been-"
    show julia upset
    js "{i}Warte!{/i} I'm not done!"
    show julia surprise
    js "A journalist always knows where the big story is! Ahem!"

    js "November 30, Naoya gives you a batch of {i}katzenzunge-{/i} er... cat-tongue cookies, which aren't even on the menu by the way!"

    js "And now, December 27, he has given you a blueberry muffin. Ergo...?"

    menu:
        "Answer her question":
            $ good_end_counters += 10
            tk serious "Ergo, he sees a hardworking detective and wants to be nice and gives him a few baked goods every now and then."
            show julia upset
            js "No!"
        "Change the topic":
            $ good_end_counters += 3
            tk serious "This is ridiculous. How long have you been documenting this?"
            js "Since I met you, so... October!"
            show julia upset
            js "Hold on, don't change the subject!"
    show julia surprise
    js "Detective Kova, you expect me to believe that Naoya gives baked goods to one random detective because he wants to be nice?"

    tk blush "Why else?"
    show julia upset
    js "Why else- he LIKES you!"

    tk serious "No he doesn't!"

    "Julia screams into her hands and starts pacing the room, much to my embarrassment as some of the officers peek into the room at the sound of her outburst."

    "In all reality, I have an inkling that Naoya is interested in me, but I don't have any time to entertain the idea."
    
    js "Okay, listen here-"
    show julia upset at slightleft
    show leonel serious at slightright
    anon "Julia, please don't distract my detective while he's working!"

    "I look up from my muffin to see Chief Leonel Vasquez walking in."

    tk serious "Chief!"
    show julia base
    show leonel happy
    lv "Ah, no need to be so tense, Kova. I'm just here for a chat."
    show leonel serious
    lv "Julia, could you leave us for a moment?"
    show julia base
    js "Yeah, totally!"
    hide julia base
    show leonel base at centerpos
    "Julia skips out of the room and waves me and the chief goodbye."

    "Chief of Police Leonel Vasquez was practically family to me. He was a fresh graduate of the academy when my father was a detective, and he had a bit of a friendly rivalry with him."

    "I think he feels some sort of responsibility towards me since I'm my father's son."

    "He pulls up a chair from an empty desk and groans as he lowers himself onto it. The room is silent as he takes a sip of coffee from his mug before setting it down."
    show leonel serious
    lv "Eugh... the coffee they make here sucks. Any more and I might land in the hospital."
    show leonel happy
    lv "You get your coffee at some fancy place, don't you Kova?"
    show leonel base
    tk smiley "Yeah, at Titania's Cafe. The pastries there are pretty good too."

    lv "The pastries you keep getting from that cute barista Julia keeps teasing you about, right?"

    tk blush "Y-yeah, I guess."

    "I see the faint beginnings of a grin on the chief's face and he gives me a very firm pat on the shoulder."

    tk smiley "What did you want to chat about, chief?"
    show leonel serious
    lv "Well, I was going to ask about the case, but..."

    tk base "..."
    
    lv "I can see you're already bending over backwards trying to figure it out."

    tk serious "I can talk about the case!"

    lv "No, Kova, I want to know about something else."
    show leonel worry
    lv "Are you getting enough sleep? Taking breaks? Relaxing? It seems that every time I see you you're always working, even during your scheduled breaks."

    "At times like these, it almost seems like Chief Vasquez is trying to act like my dad."

    menu:
        "Lie":
            $ good_end_counters = good_end_counters - 3
            tk serious "Of course I am!"
            show leonel serious
            lv "Hm..."
            tk "Chief..."
            show leonel happy
            lv "Well, it's not like I can follow you home and check... that would be considered stalking."
        "Tell the truth":
            $ good_end_counters += 5
            tk sad "The investigation is taking up a lot of my time, chief. I haven't been taking too many breaks."
            show leonel worry
            lv "Seriously? How many hours of sleep have you gotten?"
            tk serious "Like twelve!"
            show leonel serious
            lv "Twelve hours of sleep last night or twelve hours of sleep for the whole week?"
            tk sad "...Next question."

    show leonel serious
    lv "I'm telling you this now, Kova. If you don't slow down, you're going to end up dead before we even get to catch Selene."

    lv "You need to take breaks. Walk your dog, go to the mall, talk nonsense with Julia outside of work, visit that barista you like more often and ask him out!"

    tk serious "Chief!"

    lv "I'm serious. I can't have my best detective getting sick from overwork. Promise me you'll at least take a break within the next 3 days. Y'know... on your birthday?"

    "Oh... right. My birthday is in three days... on December 30th. I had been so preoccupied with the case that I completely forgot."

    menu:
        "Tell him you will take a break":
            tk serious "I will."
            lv "Promise?"
            tk "Promise."
            show leonel happy
            lv "Good."
            tk smiley "But until then, I'll work hard and make you and my dad proud."
        "The case takes priority":
            $ good_end_counters = good_end_counters - 3
            tk sad "If I have enough time..."
            show leonel worry
            lv "Detective."
            tk serious "Chief, I just know that if I do well on this case, my dad would be so proud of me! Please. I can handle it, I promise."

    "I see Chief Vasquez's face soften at the mention of my father."
    show leonel happy
    lv "...That you will."
    show leonel base
    "Chief Vasquez gives me a smile and another firm pat on my shoulder."
    show leonel happy
    lv "Keep up the good work."

    tk smiley "I will!"
    hide leonel happy
    "Chief Vasquez bids me farewell, takes his mug, and leaves the room. I turn back to my corkboard, with pictures and post it notes plastered and pinned all over it." 
    
    "For a split second, I feel my head spin."

    tk sad "Agh-!"

    "Chief Vasquez was right. Maybe I have been going at it pretty hard recently."

    "Should I take a small break?"

    menu:
        "Take a break.":
            $ good_end_counters += 5
            "I finish off the last bit of my muffin and decide to chat with someone for a bit."
            "Who should I chat with?"
            jump hangout_event
        "Push through.":
            $ good_end_counters = good_end_counters - 3
            tk serious "I can't quit now!"
            "I grit my teeth and slap myself in the face to refocus myself on the task at hand and start to add new information to me corkboard."
            jump interrogating

    #December 27, 2:00 PM

label interrogating:

    scene black with dissolve

    stop music fadeout 0.5

    "As per my duties as a detective, I go to interrogate a witness who came in contact with Selene."

    "Normally, I'd assign other officers to do this process and they'll bring me the interrogation transcript afterwards, but incidentally, no one was available or willing to ask this witness any questions."

    "So, I stepped up and took the job instead."

    scene interrogation with dissolve

    play sound bleh fadein 0.5

    "I step into the interrogation room to find a very poised older lady sitting cross-legged in the chair. As I walk around to sit in the chair across from her, I notice her arms are crossed and on her face was a very stern and annoyed expression."
    show klarika serious
    anon "I've been sitting here for almost 45 minutes."
    show klarika base
    "I take a peek at her witness file and my eyes widen as I recognize her name: Klarika Erdei. She was the dressmaker that Selene stole the “Madam Fleurette” wedding dress from. It made sense that she was so annoyed."
    show klarika talk
    ke "I already told most of the information I'm about to tell you to other officers. I don't see why an interrogation is necessary."
    show klarika base
    tk smiley "So sorry, Ms. Erdei. We do need this conversation on file. It's easier to reference a piece of paper with all the information on it rather than rely on hearsay from word of mouth."
    show klarika serious
    ke "None of what I'm saying is hearsay!"
    show klarika base
    tk happy "Right! Of course. What I meant to say was once everything you say is recorded, it'll make it easier for us to keep track of your testimony and connect it to the other evidence we have."
    show klarika talk
    ke "Yeah, fine. Could we make this quick, please? I had to push 3 VIP clients' appointments because of this, and if I keep them waiting, they'll all be extremely upset with me."
    show klarika base
    tk pensive "Alright, Ms. Klarika Erdei, my name is Detective Tobias Kova with the Oaksborough Police Department. This interrogation will be recorded and I will be taking notes, okay? This is regarding the recent heist at your residence involving Selene and the \"Madam Fleurette\""

    "What should I ask her first?"

    jump interrogate_klarika

label interrogate_klarika:
    menu:
        "Ask her how she knew Selene" if interrogate1 == False:
            $ interrogate1 = True
            tk pensive "You're a dressmaker, correct?"
            show klarika talk
            ke "Only one of the best. I specialize in bridal attire."
            show klarika base
            tk "How did you come to know Selene before the heist?"
            show klarika talk
            ke "They made an appointment with me for consultation and measurements. I made the mistake of showing them my collection so they could get some inspiration."
            show klarika base
            tk "And where was the \"Madam Fleurette\" before it was taken?"
            show klarika talk
            ke "I had it locked in a glass case that would set off an alarm when broken into or opened without my biometrics."
            show klarika base
            tk base "I see."
            jump interrogate_klarika
        "Ask for her alibi" if interrogate2 == False:
            $ interrogate2 = True
            tk pensive "On the evening of the heist, where were you and what were you doing?"
            show klarika talk
            ke "Once I had gotten Selene's calling card saying that they would be stealing the dress, I had it moved to my basement and set some guards to keep watch."
            ke "I went to bed, thinking that the dress would be safe, but when I woke up the next morning, the two guards were knocked out and the dress was gone."
            show klarika base
            tk serious "Are the guards okay? Any injuries?"
            show klarika serious
            ke "How am I supposed to know?"
            show klarika base
            jump interrogate_klarika
        "Ask about Selene's appearance." if interrogate3 == False:
            $ interrogate3 = True
            tk pensive "Do you remember anything about Selene's appearance?"
            show klarika talk
            ke "That's the funny thing. I remember taking their measurements, recommending fabric colors based on their complexion, and even recommending makeup brands that wouldn't transfer easily as to not get their dress dirty. But it seems like as soon as I shook their hand to seal the dea, I blacked out and forgot everything about them."
            show klarika base
            tk "I thought so. That seems to be the common answer amongst all the witnesses and victims."
            show klarika serious
            ke "If that was the case, why even bother asking me!?"
            jump interrogate_klarika   

    show klarika base
    "I can tell that Klarika is getting irritated, and I'm running low on steam myself. Dealing with someone this pompous is exhausting. I totally understand if my fellow officers chose not to talk to her because of that. I could call the investigation here, or I could press for more information."
    
    menu:
        "Press for more information":
            $ good_end_counters = good_end_counters - 3
            tk happy "Thank you for your cooperation thus far, Ms. Erdei. I do have some more requests to make, if that's okay."
            show klarika serious
            ke "What happened to making this quick? Fine. What do you want?"
            show klarika base
            tk pensive "You said you took Selene's measurements and you discussed things like their complexion, right?"
            show klarika talk
            ke "Yes. I keep all that information in my pocket notepad."
            show klarika base
            tk "Could you give that notepad to my officers? There could be some crucial information in there."
            show klarika serious
            ke "What a ridiculous request! All of my clients' measurements are in that notepad. I can't just give you the whole thing!"
            show klarika base
            tk "Then, uh, how about a photocopy of just the page with Selene's measurements?"
            show klarika talk
            ke "Fine. Will that be all?"
        "Finish up":
            pass
    
    show klarika base
    tk pensive "I believe those are all the questions I have for you today. Thank you for your time today, Ms. Erdei. An officer will be here shortly to escort you out."
    play sound bleh
    "She hums in satisfaction, staying still as I clean up my papers and head towards the door."
    show klarika serious
    ke "Actually, I'd like to ask you a question."
    show klarika base
    tk base "Hm? Yes?"
    show klarika serious
    ke "How long have you been on this case, detective?"
    show klarika base
    tk pensive "Since September, ma'am."
    show klarika serious
    ke "So you're telling me it's been 3 months, you still haven't made an arrest, and they haven't gotten the FBI or CIA involved?"
    show klarika base
    tk sad "Uh-"
    show klarika serious
    ke "They still have you, a local detective and his officers, in charge of capturing a thief that is capable of getting past intricate security systems and wiping people's memory with some supernatural ability?"

    ke "For weeks, there have only been reports of Selene's heists on the news. Many of my friends are worried that they are going to be targeted next! Doesn't that sound terrifying?"
    show klarika base
    tk "I understand your concern ma'am, but-"
    show klarika serious
    ke "No, listen. I'm going to be frank here, detective. You are obviously not cut out for a case as big as this, so I'm going to give a piece of advice."

    ke "You need to quit. Hand this case over to the FBI or at least someone more capable."

    ke "Or, if you're so stubborn that you feel the need to stay on this case, you better be ready to die finding this thief. Those are the best chances you have if you want to get Selene behind bars."
    show klarika base
    "I can feel my blood boil, and I clench my fist a little too hard and crumple one of the files. What does this condescending, filthy rich dressmaker know about my motivations!? Or my sacrifices!? Or my past!?"

    "I take a deep breath and try not to show my disappointment. I compose myself and turn away from her."

    tk serious "Thank you for your input, Ms. Erdei. Now, if you'll excuse me."
    hide klarika base
    #December 27, 5:00 PM
    stop sound fadeout 0.5
    scene black with dissolve
    
    "I try to keep a brave face when I get back to the office, but for the rest of the day, I kept getting distracted by what Klarika said to me about being on the Selene case. Chief Vasquez seemed to notice because he barred me from staying any amount of overtime and told me to go straight home."

    "I begrudgingly obliged, got my coat, and bid everyone at the office good night."

    scene frontdoornight with dissolve
    play sound night fadein 0.5
    "After stopping to get some takeout for dinner, I get home around 6:00 PM. My keys serve as an indicator for my arrival, and Lilith wastes no time running toward the front door and jumping to greet me."

    dog "Woof! Woof woof!"

    tk smiley "Hey, sweetie girl! Did you miss me?"

    dog "Ruff! Woof woof!"

    "I am eventually overpowered and forced to sit on the ground as Lilith continues to pounce on me. She eventually calms and settles into my lap, looking up at me and smiling."

    tk sad "Today was rough. I got told that my efforts werenlt making any progress with the case and that I should just quit."

    "Lilith looks up at me, still smiling. I don't know what I'm thinking, talking to my dog as if she can understand me."

    "Though, I guess it's better than nothing."

    tk "I mean, how ridiculous is that? I'm on this case because I'm a detective, and it's my job to solve it! I'm not going to quit."

    tk "I have to keep working. I have to keep looking for more clues. I need to catch this thief. I need to. Or else…"

    "I look up at the dresser near my front door. Hanging just above it is a picture frame. I reach over to pull it off its hook and hold it in my hand."
    stop sound fadeout 0.5
    play music sad fadein 0.5
    scene nostalgia

    "It's a picture of my dad standing next to me at a school culture festival talent show. He left work early at the police department just to see me and spend time with me, something that he didn't do too often."
    
    "While he loved me and my family, I had a feeling that he always loved his work as a detective more."

    "Every night at dinner, I'd always ask him about his investigations, and he'd go off on a tangent about crimes and suspects and the whole legal process behind his work."
    
    "He always seemed so happy to talk about his job, which is probably why I followed in his footsteps."

    "But..."

    "I think deep down inside me, I only became a detective because I wanted him to spend more time with me. I wanted him to ramble on about me as much as he rambled on about his cases." 
    
    "I thought that maybe if I became a detective, I'd see my dad more. But... I never got to..."

    tk "I just wanted to make him proud of me..."

    tk "I feel like I'm failing, Lilith… I'm failing this case… and I'm failing my dad... If he were here right now, he'd be so disappointed in me. I don't know what to do anymore! It's all so overwhelming."

    scene frontdoornight with dissolve
    stop music fadeout 0.5
    play sound night fadein 0.5
    tk base "..."

    "I look at Lilith, almost expecting an answer. As usual, she sits and stares at me with that usual happy smile. I take a deep breath and wipe my tears."

    tk happy "You must be starving. Let's get us some food, yeah?"

    #December 27, 8:00 PM

    scene klnight with dissolve

    "After a meal of chicken and broccoli with rice (and a mix of dry kibble and wet food for Lilith) as well as a long, steamy shower, I find myself sitting on the couch, with Lilith sitting to my left and some files that I brought home from the station to my right."

    "My mind wanders back to what Ms. Erdei said about me earlier today and, instincitvely, I start reaching for the papers."

    "A jolt of pain shoots through my head for just a second, then fades."

    "That was weird... but..."

    "I could... keep going..."

    menu:
        "Look through the files":
            $ good_end_counters = good_end_counters - 2
            tk serious "I have to keep looking. I can't prove Ms. Erdei right."
            "I take another manila file from my bag. Inside is a horrible photocopy of Klarika's work notes, courtesy of one of the guards."
            scene klarikafile
            play music looking fadein 0.5
            stop sound fadeout 0.5
            jump file2
        "Take a break.":
            $ good_end_counters += 5
            tk sad "That headache can't be good..."
            "I think... more than anything, my dad would want me to stay healthy."
            "I turn to Lilith and, immediately, she goes to fetch her rope tug toy and holds one end in her mouth, wagging her tail expectantly."
            "I take the other end and play tug with her for a bit, then when she's a little more tuckered out, she curls up next to me and we watch a movie for the remainder of the night."

label continuation5:
    
    "I guess I'm done here."
    
    scene klnight

    "Once I find myself unable to fight my drowsiness, I get up, brush my teeth, say good night to Lilith, and go to bed."

    #December 28, 7:00 AM

    stop sound fadeout 0.5
    play music home fadein 0.5

    scene bedroom with dissolve

    "I wake up tangled in my bedsheets; I didn't get a fulfilling amount of sleep, but there's nothing I can do about it now that it's morning."

    "Lilith is at the food of my bed, and as soon as she notices that I'm awake, she barks and leaps up into my arms."

    tk relaxed  "Oof! You don't seem much like a puppy anymore, sweetie!"

    tk "You certainly don't weigh as much as you did when you were a month old."

    dog "Ruff!"

    "Yesterday seemed like such a blur, but one thing is for certain: I'm not going to let what Ms. Erdei said get to me. I had my time to be upset, and I can either prove her wrong or forget she ever said anything and continue on with my life."

    "But first..."

    tk home  "Let's get us some breakfast."

    scene klmorning with dissolve

    "I get up and fill Lilith's food bowl with some kibble and wet food, as well as half a freshly boiled egg as a treat."

    "I had heard somewhere that they were good for a dog's digestive health and fur, and I had one last egg lying in my fridge that I hadn't used yet."

    "After I have a semi-fulfilling breakfast of leftovers and the other half of the boiled egg I made, I head to the bathroom to finish getting ready."

    scene lookingood with dissolve

    "I get dressed, pack my bag, brush my teeth and spruce up my appearance a little more."

    "I reach up and run a hand through my hair. The red and brown strands spill through my fingers. A sense of nostalgia rushes through me."

    tk happy "I can't wait for this to grow out again. Then, I can rock that cool red ponytail I've always wanted!"

    tk "Why did I ever cut it in the first place...? Eh, whatever."

    "I brush my hair into a neat half-ponytail and spritz on some cologne."

    "Still looking pretty good, if I do say so myself."

    scene frontdoormorning with dissolve

    tk smiley "I'm leaving, Lilith!"

    dog "Ruff!"

    tk "You'll be good and guard the house while I'm gone, right? I'm counting on you!"

    dog "Woof!"

    tk "I'll see you soon!"

    scene sidewalkmorning with dissolve
    stop music fadeout 0.5
    play sound park fadein 0.5
    "Despite getting to bed at a reasonable time last night (something that I haven't been able to do as of recent), I still feel somewhat exhausted."

    "I have a bit of time before I technically have to clock in for work. Should I get to the office early or go to the cafe and see Naoya again?"

    menu:
        "Get to work early!":
            $ good_end_counters = good_end_counters - 3
            $ earlyBird = True
            "I decide to save my money for today and head to work early." 
            "As I walk down the sidewalk past Titania's Cafe, someone walks out the cafe door and runs face-first into my chest. They seemed to be on the shorter side, and they were wearing an oversized black hoodie that obscured their face."
            tk serious "Woah!"
            "The person doesn't utter any apology and simply takes off in the other direction. I stood there, dumbfounded, as I watched them bolt down the sidewalk."
            tk base "That was weird..."
            "I take one last glance at the cafe door and make my way down the street to the police department."
            scene officemorning with dissolve
            stop sound fadeout 0.5
            play sound office fadein 0.5
            "I greet my colleagues a good morning, finding comfort in seeing that they are equally as sleepy as I am. I take a seat at my desk and reach for another file folder, sighing heavily. I set it down in front of me, open it up, and start scanning the contents."
            play music looking fadein 0.5
            jump file3
        "Pay Naoya a visit!":
            $ good_end_counters += 5
            $ onTime = True
            "I decide to energize myself with a cup of coffee while I skimmed through more evidence."
            "I stop right in front of Titania's Cafe and just as I am about to open the door, someone walks out the cafe door and runs face-first into my chest. They seemed to be on the shorter side, and they were wearing an oversized black hoodie that obscured their face."
            tk serious "Woah!"
            "The person doesn't utter any apology and simply takes off in the other direction. I stood there, dumbfounded, as I watched them bolt down the sidewalk."
            tk base "That was weird..."
            jump cafe_day2

label cafe_day2:

    scene cafe with dissolve
    stop sound fadeout 0.5
    play music cafe fadein 0.5
    show naoya happy
    nt "Welcome in, detective! I'll be with you in just a second!"
    show naoya base
    tk happy "No problem!"

    "I wait patiently while Naoya finishes up cleaning a few mugs and hanging them up on some hooks on the back wall. He then approached the cash register with a notepad and a smile."
    show naoya cheeky
    nt "Thanks for waiting. Should I make you your usual, or do you want to try something else?"
    show naoya base
    tk blush "I'll have my usual, thanks."
    show naoya happy
    nt "You got it. Take a seat and I'll bring it out to you soon."
    show naoya base
    "I pay my tab and take my usual seat by the window, In a few minutes, Naoya brings me a fresh, hot mug of my usual coffee order."
    show naoya cheeky
    nt "Here you are, your hot mocha latte with enough sugar to-"

    tk happy "Yeah, yeah, enough sugar to kill an elephant and so much chocolate that it doesn't even taste like coffee anymore, I get it."
    show naoya smiley
    nt "A ridiculously sweet cup of coffee for a sweetheart detective such as yourself."

    tk blush "Oh my goodness-"

    "I hide my face in my hands and shoo at Naoya as he laughs. He doesn't leave, and as I take a peek through my fingers, I realize that the cafe is a little slow this morning."

    "It's a perfect time to strike up a conversation or catch up on some work."

    menu:
        "Make small talk with Naoya.":
            $ good_end_counters += 5
            tk smiley "Are you up to chat a little bit, Naoya?"
            show naoya cheeky
            nt "Hm... sure, why not?"
            "Naoya takes a seat next across from me and rests his head in his hands."
            nt "There is something I wanted to know about you."
            tk happy "What is it?"
            show naoya concern
            nt "What do you do outside of work?"
            tk pensive "Well, uh... I take care of a dog? Her name is Lilith. She's a 7 month old Burnese Mountain puppy."
            show naoya cheeky
            nt "Aw, how cute! I didn't peg you as a dog person... or a pet person at all, actually."
            tk happy "What!? Why? What's wrong with me?"
            nt "W-well... you're huge."
            tk blush "Yeah. I am considerably taller than most people my age. Six feet and two inches, to be exact."
            show naoya concern
            nt "Okay, you don't have to rub it in my face."
            tk "How tall are you, Naoya?"
            nt "..."
            nt "No point lying about it... I'm five feet and four inches."
            tk "That's... shorter than average."
            show naoya shy
            nt "I'm a perfectly average height back home!"
            tk "I'm not going to doubt that-"
            show naoya cheeky
            nt "No, but seriously. You are huge. Not just height-wise. You're like... bulked up."
            tk happy "What does that have to do with me owning a dog?"
            show naoya smiley
            nt "Nothing! Just- the irony of it! Big guy, cute tiny puppy"
            tk "She's not that tiny. Burnese Mountain dogs can get up to 100 pounds in weight and 30 inches in height."
            show naoya shy
            nt "That's like half my size!"
            tk smiley "Pfft- haha!"
            show naoya blush
            nt "No need to laugh about it..."
            tk blush "Sorry- sorry."
            show naoya shy
            nt "...does she eat whipped cream?"
            tk pensive "I don't think she's ever had whipped cream. Is it safe?"
            show naoya smiley
            nt "Yeah! Totally! Bring her around some time and I'll give her a bit."
            tk happy "That's sweet of you. I'll definitely bring her one of these days."
            show naoya cheeky
            nt "Sounds good. I better get back to work or people might say I'm slacking off."
            tk smiley "Yeah, thanks for chatting!"
            show naoya happy
            nt "Mhm!"
            hide naoya happy
            "Naoya gets up from the chair and pushes it in, waving me goodbye before returning to behind the coutnter."
            "That was nice."
            jump continuation2
        "Read up on more files.":
            hide naoya smiley
            $ good_end_counters = good_end_counters - 2
            stop music fadeout 0.5
            play music looking fadein 0.5
            jump file3
            # FILE AND JOURNAL MECHANICS
    
label continuation2:
    stop music fadeout 0.5
    play music cafe fadein 0.5
    "I guess I'm done here."

    scene cafe with dissolve
    
    "After finishing my coffee, I return my cup at the counter and start packing my things to leave. Once again, Naoya calls out to stop me and rushes up with yet another brown paper bag."
    show naoya base
    tk happy "Thanks, what is it this time?"
    show naoya happy
    nt "A Danish pastry."
    show naoya base
    tk smiley "Ooh, thanks."
    show naoya serious
    nt "Ah- detective- er, Tobias."
    show naoya base
    tk base "Hm?"
    show naoya serious
    nt "Please. Take it easy."
    show naoya base
    tk happy "Ah- yeah- um, thanks, Naoya. I'll see you tomorrow."
    hide naoya base
    "I wave Naoya goodbye and make my way to the Oaksborough Police Department."

    jump ontime

label earlybird:

    "I guess I'm done here."
    stop music fadeout 0.5
    scene officemorning with dissolve
    play sound office fadein 0.5
    "I look up from my files at the sound of Julia's rambunctious voice. I watch her walk into the office and she meets my eyes, somewhat surprised to see me."
    show julia base at slightleft
    show romeo base at slightright
    "Trailing behind her was a bespectacled person about her height, with bright yellow eyes that had the beginnings of eyebags and hair that was styled almost like an owl's head. They shuffled nervously and stared down at the floor as Julia spoke."
    show julia surprise
    js "Detective! You're here early!"
    show julia base
    tk happy "Ah- yeah. I decided to come early and get a headstart on some more files."

    "The stranger's eyes flickered over to look at the pile of files and my corkboard, and for a moment they seemed interested."
    show julia surprise
    js "Eh!? So no pastry today?"

    tk base "Nope, sorry."
    show julia upset
    js "{i}Sccchhhade!{/i} C'mon detective, we had a streak going!"

    tk "You. You had a streak going."

    tk happy "Anyways, are you going to introduce me to your friend?"
    show julia surprise
    js "Oh, right!"

    jump meet_romeo

label ontime:
    stop sound fadeout 0.5
    stop music fadeout 0.5
    scene officemorning with dissolve
    play sound office fadein 0.5
    show julia base at slightleft
    show romeo base at slightright
    "I walk into the office, greeting my colleagues and spotting Julia's bright red hair immediately."

    "She stood next to my desk and made small talk with a stranger who had bright yellow eyes and a hairstyle that made them look a bit like an owl. They shuffled their feet, looking down at the floor."

    "Ocassionally, their eyes would flicker up to look at Julia, but also at the files on on my desk."

    tk smiley "Julia!"
    show julia surprise
    "At the sound of her name, Julia looked over at me and beamed. The stranger also looked in my direction, albeit a little more nervously."

    js "Detective!"

    "Julia runs up to me and it almost looks like she's about to give me a hug, but she fakes out and snatches the paper bag from my hand instead."

    tk happy "Hey!"
    show julia base
    "She peeks inside, then looks up at me with a sneaky grin. She hands me the bag and then takes out her notepad, no doubt scribbling down the date, time, and the Danish pastry Naoya gave me."
    show julia happy
    js "As I said, a good journalist always knows where the big story is!"

    tk base "Yeah... okay."

    tk "You didn't have to snatch it out of my hands, though."
    show julia base
    js "Sorry!"

    "I made my way to my desk, and when I catch the stranger staring up at me, they avert their eyes and scramble to get out of my way. As I sit down, Julia clears her throat, gesturing to her friend."

    js "Allow me to introduce you, detective!"

    jump meet_romeo

label meet_romeo:
    play sound office fadein  0.5
    show julia happy
    js "This is Romeo Ryder, the new archivist! They're kinda shy, but they're very good at their job, I assure you. We became friends just this morning!"
    show julia base
    show romeo shy
    rr "H-hey."
    show julia base
    show romeo base
    js "Aw, Romeo, no need to be nervous! Detective Kova is very kind!"
    
    tk smiley "I don't bite, I promise."
    show romeo shy
    rr "Ah, um, okay."
    show julia happy
    show romeo base
    js "That's the spirit! I have a feeling you two will be seeing each other a lot, so I'll leave you two to get acquainted!"
    show julia base
    show romeo surprise
    rr "Ah, J-julia!"
    hide julia base
    "And just like that, Julia skipped out of the office, leaving poor Romeo sweating and stuttering."
    show romeo base at centerpos
    "I have a feeling Romeo isn't the best at small talk. It's best for me to get to know the archivist, seeing as they are the person that I'll be getting most of my information from."

    jump ask_romeo

label ask_romeo:
    
    menu:
        "Compliment their outfit" if question1 == False:
            $ question1 = True
            show romeo base
            tk happy "I like your boots."
            show romeo shy
            rr "Ah- um, thank you. I like your- uh shirt... tie."
            show romeo base
            tk "Oh, thanks. Um, do you always wear gloves?"
            show romeo shy
            rr "Um, yeah. So I can handle things- the files and stuff- with care. I can't get my fingerprints on anything or stuff."
            show romeo base
            tk base "Uh, yeah. That makes sense."
            jump ask_romeo
        "Compliment their hair" if question2 == False:
            $ question2 = True
            show romeo base
            tk happy "You have an interesting hairstyle. Looks kinda like an owl."
            show romeo shy
            rr "It's just m-my bedhead."
            show romeo base
            tk base "Oh."
            show romeo shy
            rr "...your hair is red."
            show romeo base
            tk blush "Yeah, but only the bottom of it, which is why I tie my hair up."
            show romeo shy
            rr "C-cool, yeah..."
            show romeo base
            jump ask_romeo
        "Ask about their job." if question3 == False:
            $ question3 = True
            show romeo base
            tk smiley "So, like Julia said, I'll probably be seeing you around a lot. What exactly is it that you do?"
            show romeo shy
            rr "I organize the files, give them to officers, make sure they're in good condition..."
            show romeo base
            tk happy "Yeah? Do you have a favorite case?"
            show romeo surprise
            "Romeo's eyes suddenly lit up and they make direct eye contact with me. They started shaking excitedly and their voice got much louder."
            show romeo happy
            rr "I love the Selene cases! They're all so intersting! Reading up on all the heists and how and where they were pulled off are so... magical!"
            "Their enthusiasm startles me, but I'm glad I got them talking."
            tk smiley "That's great! I'm actually the detective in charge of the Selene cases."
            rr "Oh, I know. Though, I've been following Selene's cases since before you were in charge. Ever since the first heist..."
            tk happy "That was more than 8 months ago!"
            rr "Back when Selene was still considered a petty thief..."
            rr "Did you know that one of the first heists was reported to take place in a museum safehouse? But! It actually took place in broad daylight!"
            rr "The artifact, an old Chinese pipa engraved with the names of two lovers, was hidden away in a restricted area. The museum had locked it down tightly, but didn't anticipate that someone would actually avoid all the guards, turn off security, and steal a giant instrument without being caught!"
            rr "To be fair, this was before Selene started sending calling cards, so the museum authorities couldn't do anything to prepare, but come on! It's a giant, delicate, musical instrument!"
            rr "The museum staff must have been so embarrassed that they let something so big get stolen that they asked the police to report something else to the papers! But, of course, the truth is always listed in the files."
            tk pensive "Ah... that's interesting..."
            rr "Right!? By the way, I heard there was supposed to be an auction held at the Ivory Auction house tonight. The items there are probably worth a lot of money..."
            rr "Maybe Selene will send a calling card out right in the middle of the proceedings!"
            tk base "Uh huh..."
            show romeo surprise
            rr "Ah! S-sorry- I must have rambled for long- too long... sorry..."
            show romeo shy
            tk happy "That's... okay."
            show romeo base
            jump ask_romeo

    show romeo shy
    rr "I'm just gonna- I'll have to- I'm off- I'm gonna go find Julia now. Um... if you need me, I'll be he- the- a-around."
    hide romeo shy
    "Romeo turned and skittered out of the room hastily."

    tk "They were certainly... interesting."

    "I turned to the rest of my files that were sitting on my desk. I'll definitely run into Romeo again sooner or later when I return these to them. Best get started now..."

    tk "I'll probably have to stay overtime tonight..."

    "I picked up another file and began my search for information again."

    jump auction_night

label auction_night:
    stop sound fadeout 0.5
    scene black with dissolve
    
    "Later that night..." # DIFFERENT COLOR

    # December 28, 8:00 PM

    scene ivory hallway with dissolve
    play sound footsteps fadein 0.5
    "The sound of two pairs of footsteps echoed down the hallway, a pair of pink, three-inch platform heels and a pair of worn, scuffed, black dress shoes. Two young figures waltzed confidently down the hallway, ignoring the perplexed stares of the much older attendees peppered throughout the building."
    show evie base at slightleft
    show theo base at slightright
    "A young woman in a frilly outfit walked happily alongside a taller man in a formal suit. The young man was much more tense than the young woman, and he clutched a calculator and a notepad in his hands, pressing a few buttons as she rambled."
    show evie happy
    anon "Isn't this so exciting, Theo? Your first auction! And I have my eye on one specific item specifically!"
    show evie base
    "The young woman locked her arm onto the young man's- Theo's. He cleared his throat and looked down at his calculator and notes."
    show theo concern
    tp "Yes, but don't get too excited Evie. You wouldn't want to end up bidding too high."
    show evie happy
    show theo base
    ei "I know, I know. This isn't my first auction! I'll be fine!"
    show evie base
    show theo concern
    tp "Okay... I just don't want you to be made a fool of in front of all these older men."
    show evie happy
    show theo base
    ei "I don't fear all the older attendees, {i}mon chou.{/i} They should be scared of me! I could technically bid high on every item here!"
    show evie base
    show theo concern
    tp "Please don't, that's like my worst nightmare. I will fail my accounting course if you actually do that. No bachelor's degree for me."
    show evie happy
    show theo base
    ei "I won't! I won't! Promise."
    show evie base
    show theo serious
    tp "Good."
    show evie happy
    show theo base
    ei "But... I could?"
    show evie base
    show theo serious
    tp "Let's just... go find our seats."
    show evie happy
    show theo base
    ei "{i}Ja!{/i} Let's!"

    scene auctionlight with dissolve
    play sound audience fadein 0.5
    show evie base at slightleft
    show theo base at slightright
    "Evie and Theo walked into the main auction hall and looked for the seats with their names on them. On each seat was a pamphlet listing all of the items up for auction."

    "Evie took off looking for her seat, and Theo followed shortly after, keeping an eye open for his seat as well."
    show evie serious
    ei "\"Ilhe,\" \"Ilhe...\" where is my chair?"
    show evie base
    show theo serious
    tk "Evie! Over here!"

    "Evie jogged over to Theo and he gestured to two chairs positioned right next to each other. They read \"Theo Ponce de Leon,\" and \"Evie Ilhe\" respectively."

    "On Evie's chair, there was a numbered paddle right on top of the pamphlet, the instrument she would use to bid on the auction items."
    show evie happy
    show theo base
    ei "Great! Thanks, {i}mon chou!{/i}"
    show evie base
    show theo base
    tp "N-no problem."

    "The two of them took their seats, and slowly but surely, the rest of the attendees filed into the room, slowly filling the hall with chatter."

    "As some older adults sat next to Evie and Theo, they donned a stunned expression at the two of them, no doubt surprised that people their age were attending."
    show evie happy
    ei "Good evening!"
    show evie base
    "Evie waved to the people sitting near her, and she got some awkward waves back."

    "While they waited, Theo looked over his notes and Evie leafed through the pamphlet. When she got to a certain page, her eyes lit up."

    "She grabbed Theo's arm and pointed excitedly at the picture of the item."
    show evie happy
    ei "Theo! Theo, look! Look, this is it! The one I've been looking for! Isn't it just gorgeous?"
    show evie base
    "Theo peeked over at the pamphlet. Evie was pointing at a beautiful wood-carved music box that was made during a time of religious persecution by a father for his two children, who were daughters of a religious convent."

    "It contained an original composition that one of the daughters wrote. Rumors say that it survived multiple building collapses, house fires, and had no evidence of water damage."

    "According to legend, whoever owned this music box heard it play before something tragic happened. It was considered both a good luck charm and a cursed artifact."
    show theo concern
    tp "That one? Really?"
    show theo base
    show evie serious
    ei "Why? What's wrong with it?"
    show evie base
    show theo concern
    tp "Nothing... good luck, Evie."
    show evie happy
    show theo base
    ei "I can't wait!"
    show evie base
    
    "Shortly after, the auction went into full-swing. Artifact after priceless artifact was brought out, and the auctioneer rambled number after obscenely large number."

    "Rounds of applause erupted after each item was sold, and people started to grow suspicious of Evie as she sat, straight-faced and serious, not moving her numbered paddle."
    show evie serious
    guy "Our next is item is the \"Sister's Lullaby,\" a music box from the 1700s. Bidding starts at $15,000! Do I hear $15,000?"

    yall "$15,000!"
    
    yall "$16,000!"

    "Theo looked over at Evie, who now sat upright and closed her eyes, listening intently."

    "She seemed to be waiting for the right moment."

    guy "$16,000! $16,000!"

    yall "$17,000!"

    yall "$18,000!"

    yall "$19,000!"

    yall "$19,500!"

    yall "$19,750!"

    "Suddenly, Evie threw her paddle in the air."
    show evie upset
    ei "$25,000!"
    show evie serious
    "The other ateendees looked at her, shocked, and Theo hummed proudly. Evie sat back a little, smirking. In her mind, she doubted that anyone would bid any higher."

    guy "$25,000! $25,000!"

    yall "$27,000!"
    
    "Evie looked around, staring indignantly at the person who currently had their paddle up. Without hesitating, she placed another."
    show evie upset
    ei "$27,500!"
    show evie serious
    yall "$28,500!"

    "Irritated, she slammed her hand down and shouted."
    show evie upset
    ei "$32,000!"
    show evie serious
    "Theo coughed a little at the number, and at this point, everyone was looking at Evie as if she was crazy."

    guy "$32,000! Going once, going twice... sold to 364 for $32,000!"
    show evie happy
    ei "YESSSSSS!!!"

    "The rest of the room gave their applause and Evie grabbed Theo by the shoulders and shook him aggressively."

    "He sighed, looking down at his notes. He wasn't expecting her to go over $30,000, but it wasn't a terrible amount, especially for someone who runs as much on instinct as she does."

    #December 28, 11:00 PM
    hide evie happy
    stop sound fadeout 0.5
    scene manor outside night with dissolve
    play sound night fadein 0.5
    
    "Evie loaded her prize into her car after the auction. It started raining on the way home, and Evie couldn't help but be lulled, falling asleep on Theo's shoulder. When she awoke at her front door, she and Theo carried the music box carefully up the stairs to her room."

    scene evieroomnight with dissolve
    show evie base at slightleft
    show theo base at slightright
    "They opened the box and unwrapped the protective covering, setting it on the mantle above the fireplace in Evie's room."
    show evie happy
    ei "It's perfect."
    show evie base
    "While Evie swooned at her new treasure, Theo stared right at her."
    show theo concern
    tp "Yeah..."
    show evie happy
    show theo base
    ei "Okay! I'm gonna get ready for bed. I'm exhausted."
    show evie base
    show theo concern
    tp "Okay, I'll leave you to it, then. Good night, Evie."
    show evie happy
    show theo base
    ei "Good night!"
    show evie base at centerpos
    hide theo base
    "Evie sat down at her vanity and began removing her accessories and combing through her hair."

    "The sound of rain outside her room was hard enough to mask the sound of someone unlatching the window and crawling inside."

    "As Evie hummed happily, a calling card seemed to flutter down from the sky and land right in front of her. She picked it up and she recognized the picture of the opera mask in the corner immediately. She read the text with shaky hands."

    "\"This heartfelt work of grief and remembrance shall soon be put into deserving hands.\""

    "Panicked, Evie's head whipped around to look at her fireplace, and she sighed in relief when she saw that the music box was still there."
    show evie concern
    ei "THEO! WE MIGHT HAVE A PROBLEM!"
    hide evie concern
    "Meanwhile..."
    stop sound fadeout 0.5
    scene black with dissolve

    anon "...tective... Detective..."

    anon "Detective..."

    "Who... who's calling me?"

    anon "Detective!"

    "Someone whisper-shouts my name, and I open my eyes to find..."

    scene officenight with dissolve
    play sound night fadein 0.5
    show julia concern at slightleft
    show romeo base at slightright
    "Romeo and Julia look down at me, their eyes are full of worry. They seemed taken aback once I opened my eyes. No doubt that my face looks horrible right now."

    js "Detective, maybe you should go home..."

    tk "Julia? What time is-"

    "The clock at the front of the room read \"11:00\" on the dot."

    tk sad "Wha- what are you and Romeo doing here? It's so late."
    show julia surprise
    js "I could say the same to you!"
    show julia concern
    js "Romeo called me. They were worried about you."
    show romeo shy
    rr "I stayed late to um... organize more files. You... fell asleep. I just finished up."
    show julia concern
    show romeo base
    js "Detective, isn't it your birthday in two days?"

    tk "How do you know that?"

    js "I overheard Chief Vasquez mention it yesterday... I didn't mean to eavesdrop- it's just-"

    js "Shouldn't you take a break?"

    tk "I can't... I still have things to read..."
    show romeo concern
    rr "I can... help summarize that. I've read every Selene case file front to back... I can sa- tell you- like, whatever's in each file."
    show romeo surprise
    rr "B-but for now, you should take a break, Detective Kova."
    show julia upset
    show romeo base
    js "Please! You're exhausted!"
    show julia base
    "No doubt. I decided to stay an hour or two after my usual clock-out time and an hour became 6. Why didn't anyone come to wake me up?"

    "I didn't have any time to think about it now."

    tk "Okay, okay. I'll go home."
    show julia upset
    js "Good. And leave all those files here! No bringing work with you!"
    show romeo shy
    show julia concern
    rr "I'll um... email you the information you need by- to you by tonight."
    
    "It's nice knowing that I have people who care about me. I was so focused on making my dad proud that I forgot I have to make them proud too."

    tk happy "Thanks, guys. I'll see you tomorrow."
    show julia base
    js "Yeah, good night detective."
    show romeo shy
    rr "Good- uh- good night."
    show romeo base
    show julia concern
    "I grab my coat, pack my bag and leave the office."

    js "..."

    rr "..."
    show julia surprise
    js "He's gone, right?"
    show romeo shy
    rr "Yeah.."

    js "Everything is in order, right?"

    rr "Definitely."
    show julia base
    js "Heh... I can't wait to see the look on his face..."
    hide julia base
    hide romeo shy
    stop sound fadeout 0.5
    scene frontdoornight with dissolve
    play sound night fadein 0.5
    tk sad "Lilith... I'm home..."

    dog "Woof!"

    "I closed my front door and slid down onto the floor. I let out a heavy sigh and pat Lilith's head."

    "My cellphone vibrated in my pocket, and when I took it out to take a look, I saw a barrage of emails from Romeo summarizing the last three Selene files I needed to read about."

    "I felt relieved, but also a little betrayed. I wish I had found out all this information on my own."

    "At the bottom of one of those emails was a little post script that read \" REST WELL DETECTIVE!!! I'LL SEE YOU TOMORROW!!! - Julia.\" I couldn't help but laugh a little when I saw it."

    tk happy "My friends are amazing, Lilith."

    dog "Ruff!"

    tk smiley "You too, Lilith. Of course you are."

    "I reach down to embrace her and close my eyes."

    tk happy "I'm so lucky I have you guys..."

    "After a meal of leftovers and a shower, I sat down and reached into my bag, pulling out some files I had secretly brought home. Romeo was nice enough to summarize the files that I needed to read from my last batch. I guess I instinctively started on my next batch of files."

    tk base "I know Julia said I should take a break, but... I already took a break yesterday, so... maybe it should be okay if I start reading up again?"

    menu:
        "Keep your promise.":
            $ good_end_counters += 5
            "Julia would be devastated if she learned that I did work outside of work hours."
            tk happy "It's already so late. I guess I should go to sleep now so I get up on time tomorrow."
            dog "Woof!"
            "Lilith seems to agree with me, barking quietly and then yawning."
            tk "You're right, sweetie. I'll go to bed."
            "I lean over to kiss her on her head before going to the bathroom to brush my teeth, get dressed, and go to bed."
            scene black with dissolve
            jump day3
        "One more wouldn't hurt.":
            $ good_end_counters = good_end_counters - 3
            "Lilith looks up at me with an almost worried expression. I pat her on the head and turn back to the manila folder in my hand."
            "As I open up the folder, another jolt of pain shoots through my head."
            tk sad "Ack-!"
            "It doesn't fade away like usual, but instead, subdues into a constant, annoying, pulsing feeling in my temples."
            dog "Woof?"
            tk happy "I-I'm fine, sweetie."
            "I shake my head and try to keep the pain in the back of my mind. The case takes priority."
            play music looking fadein 0.5
            jump file4

label late_night:
    "I guess I'm done here."

    scene klnight with dissolve
    play sound night fadein 0.5
    "The headache still hasn't gone away..."

    "Maybe I should have taken a break..."

    "Lilith is still laying next to me, fighting sleep as she waited for me to finish."

    "I sigh, petting her on the head and guiding her to her bed before I got ready for bed myself."

    jump day3

label day3:
    stop sound fadeout 0.5
    scene black with dissolve

    "{i}Tobias.{/i}"

    "Who... is calling me?"

    "{i}Tobias, the case...{/i}"

    "The... case..."

    if good_end_counters < 30:

        "{i}You're hurting yourself.{/i}"

        "This is about Selene, isn't it...? I'm getting close..."

        anon "You're doing too much. It'll only hurt in the end."

        anon "Don't make the same mistake I did."

        anon "Save yourself."

        "That voice..."

        "D-dad!?"

        scene bedroom with dissolve

        "My eyes shoot open, and I wake up with an excruciating headache."

        tk relaxed "Uh-ugh-!"

        tk home "..."

        scene bedroom with dissolve

        tk "What- what the heck...?"

        "Lilith scrambles to comfort me, and I reach for some painkillers in my nightstand drawer. I shake two into my palm and swallow them quickly."

        "I'm well aware they won't work right away, but it's better than nothing."

        tk relaxed "Haah..."

        tk "That dream... that was my dad's voice..."

        dog "Woof?"

        tk home "Lilith.. I have a feeling today is going to be a very interesting day."

        "I got up from my bed and finish the rest of my routine- feeding myself and Lilith, getting dressed and packing my bag. Once again, I go to my bathroom and look at myself in the mirror as I'm reaching for my comb and cologne."

        scene finalsweek with dissolve

        "Did... did I always look so tired?"

        jump continuation3

    if good_end_counters >= 30:

        "{i}You're so close.{/i}"

        "I know... I practically only need people of interest."

        anon "The truth might be surprising, but... you've come so far. With your career and your friends."

        anon "I'm so proud of you."

        "That voice..."

        "Dad!"

        scene bedroom with dissolve

        "My eyes shoot open, and I don't realize it at first, but I'm crying."

        tk relaxed "Uh..."

        "Lilith jumps up onto my bed to greet me \"good morning,\" and I wipe my tears and hold her close."

        tk home "That dream... that was my dad's voice..."

        dog "Woof?"

        tk relaxed "Lilith.. I have a feeling today is going to be a very interesting day."

        "I got up from my bed and finish the rest of my routine- feeding myself and Lilith, getting dressed and packing my bag. Once again, I go to my bathroom and look at myself in the mirror as I'm reaching for my comb and cologne."

        scene likehim with dissolve

        "For the first time in a long time, I see myself. Really see myself. I'm standing a little taller and my eyes are a little brighter."

        "I look like my dad."

        jump continuation3

label continuation3:

    scene frontdoormorning with dissolve

    "Once I finish sprucing myself up, I say goodbye to Lilith at the front door and make my way down the sidewalk."

    scene sidewalkmorning with dissolve
    play sound park fadein 0.5

    "I pass in front of Titania's Cafe before doubling back and contemplating whether or not I should go in. Just then, I got a message from Chief Vasquez- which is weird because I don't recall giving him my number and he has stated multiple times that he is not a text person."

    "The message says, \"We need you, for a site  investigation. Nothing. tooserious but if you coud get here asap… thanks. Here's the addres: - Chief Leonel Vasquez,\" and below it was an address to someone's house, I assume."

    "He said it wasn't serious, so I think I'm free to be a little late, so I could stop for a little coffee. It shouldn't take too long."

    "I open the door and enter the cafe."

    scene cafe with dissolve
    stop sound fadeout 0.5
    play music cafe fadein 0.5
    show naoya happy
    nt "Detective, hey! Took you long enough. I watched you stand outside the cafe door for a good while, haha!"
    show naoya base
    tk blush "You were watching me!? Ugh… I'm so embarrassed…"
    show naoya happy
    nt "Nothing to be embarrassed about. The usual?"
    show naoya base
    tk happy "Yes, please."
    show naoya happy
    nt "Coming right up!"
    show naoya base
    "This time, I took a seat next to the counter and watched Naoya work. I noticed one of his hands was ungloved and his palm had a decently sized bandage on it."

    tk base "Did you get hurt, Naoya?"
    show naoya happy
    nt "Hm? Oh, yeah. I cut myself when I was baking earlier. It's just a scratch though! I'm fine."
    show naoya base
    "Naoya must have noticed that I was worried because he came up to me and poked my forehead."
    show naoya serious
    nt "Stop frowning! I said I'm fine, silly. I'll be healed soon. Here…"
    show naoya base
    "Naoya handed me my usual coffee order."
    show naoya cheeky
    nt "Should I go on my spiel or should I let you drink your liquid saccharin in peace?"

    tk smiley "Oh, spare me, great sovereign of coffee! I'm already suffering enough trying to catch this thief!"

    nt "Hm, you're right. I'll spare you since tomorrow is such a special day."

    "I was about to question him but he turned away from me and went to grab something. He came back with a small cardstock box and pushed it in front of me. He leaned on the counter and looked at me expectantly."

    tk blush "What's this?"
    show naoya smiley
    nt "Why don't you open it and find out?"

    "I did as he said, and inside the box was a small cake with the words, \"Happy Birthday\" written in red frosting on top."

    tk smiley "Oh, my goodness, thanks! Is this why you said you would spare me? Because my birthday is tomorrow?"
    show naoya smiley
    nt "Mhm! That's not the only thing in there."

    "He tapped the underside of the box's lid, and there was a small note taped there. I took it out and unfolded it, and I started reading. It read…"

    "\"Thank you for your hard work and your continued and enthusiastic patronage. Here's a little something for you, detective.\""

    "And at the bottom of the note was Naoya's signature and a postscript that had nothing but a set of numbers."

    tk pensive "Naoya, what are these numbers?"
    show naoya concern
    nt "Oh, detective, don't make me say it!"

    tk base "..."

    nt "..."
    show naoya blush
    nt "It's… my number…"

    "Naoya hid his blushing face behind his hands, and I could feel my face getting just as red. Naoya Tamaki just gave me his number. He gave me his number. His number and a birthday present. He gave them to me."

    "I could cry."
    show naoya shy
    nt "Someone told me that it was your birthday on the 30th yesterday. I thought maybe we could hang out and celebrate? Get a snack? A drink? Go to your… um… your place? Or mine? A-anything's fine, really."

    tk blush "Ah, um… yeah. That- I'd like that. A lot."
    show naoya smiley
    nt "Great, um… it's a date, then?"

    tk "Y-yeah!"
    show naoya cheeky
    nt "Cool."
    hide naoya cheeky
    "As soon as I finished my coffee and bid Naoya farewell at the door, I broke into a run and went straight to the police department."
    stop sound fadeout 0.5
    scene officemorning with dissolve
    stop music fadeout 0.5
    play sound office fadein 0.5
    show julia concern at slightleft
    show romeo base at slightright
    "I ran into the office and found Julia and Romeo talking. They seemed worried to see me at first, but I went up to them and pushed the note and cake in Julia's face."
    show julia surprise
    js "Detective- what?"

    tk smiley "Look!"
    show romeo shy
    rr "Huh?"
    show julia surprise

    "Julia and Romeo scanned the contents of the note, and as soon as they got to the bottom, both of their eyes widened."
    
    js  "{i}Oh mein Gott!{/i} Is that-!?"
    show romeo surprise
    rr "It's his number…!"

    "The two of them shared a look and pumped their fists in victory. The three of us squealed in excitement, drawing the attention of irritated coworkers passing by. For the first time in a long time, I felt a little bit of my stress fizzle away into nothingness."
    hide romeo surprise
    hide julia surprise
    # December 29, 9:15 AM
    stop sound fadeout 0.5
    scene manor outside morning with dissolve
    play sound park fadein 0.5
    "I didn't have much time to celebrate with Julia and Romeo- I had a car to catch. I was driven all the way to the Ilhe manor, the site of the investigation. As I drove up the driveway, I noticed a faint trail of footsteps leading to the side of the building. They disappeared from my sight as the car rolled up next to the front gate, and someone knocked on the car's window, grabbing my attention."
    show theo serious
    anon "Detective? Is that you?"
    show theo base
    "I exit the car and thank the officer driving, locking eyes with a tired young man in a black suit and short, black hair. I shake hands with him and he sighs, introducing himself to me as best he can."
    show theo serious
    tp "I'm Theo Ponce de Leon. Thanks for coming. Evie has been so panicked since she received that calling card from Selene last night. I had to stay with her in her room just for her to get a good night's sleep."
    show theo base
    tk serious "I see. Why didn't you call the police office sooner?"
    show theo serious
    tp "Evie insisted that she wanted to get her \"beauty sleep\" first, and that she would call first thing in the morning. I didn't have the heart to tell her that her decision was dangerous, because- well, nevermind."
    show theo base
    tk pensive "I see…"

    "I sense a hint of protectiveness and… love, probably."

    tk serious "Could you lead me inside? I'd like to inspect the room and ask Evie a few questions."
    show theo serious
    tp "S-sure. This way."

    "Theo led me to the front door and we stood awkwardly in the front entrance as he rang the doorbell to be let back in."
    show theo serious
    tp "It takes a while for the door to be opened."
    show theo base
    tk happy "No problem."

    "Maybe I should ask Theo a few question while we wait."

    menu:
        "Stay silent.":
            tk base "..."
            tp "..."
            tk "..."
            tp "..."
            "The door clicks and Theo gestures for me to go inside first. He then guides me up the stairs to Evie's room."


        "Make small talk.":
            $ good_end_counters += 5
            tk happy "You have an interesting accent, Theo."
            show theo serious
            tp "Ah, yes. I'm a transfer student from Spain. Other than English, I speak Spanish and- with my parents- African French."
            show theo base
            tk pensive "Wow, two romance languages. That's amazing."
            tk "Also, I can't help but notice you have a slight limp. Did you injure yourself?"
            show theo serious
            tp "Oh, I was trying not to make it so obvious. I do have a slight injury on my foot. I got it at fencing practice."
            show theo base
            tk happy "You're a fencer?"
            show theo serious
            tp "Yes. I also dabble in recreational swordfighting."
            show theo base
            tk pensive "...with real metal swords?"
            show theo serious
            tp "Yes."
            show theo base
            tk happy "Huh. Impressive."
            "Theo seems stoic, but I can see the beginnings of a smile on his face."
            show theo serious
            tp "Thank you."
            show theo base
            "The door clicks and Theo gestures for me to go inside first. He then guides me up the stairs to Evie's room."
    stop sound fadeout 0.5
    scene evieroommorning with dissolve
    play sound bleh fadein 0.5
    "Evie was talking to Chief Vasquez by the time we got to her room. Theo gave me the green light to look around while the two of them finished up their conversation, and I pulled on my gloves and started my search."

    jump investigate

label investigate:
    menu:
        "Check the windows." if check_window == False:
            $ check_window = True
            "The windows were latched shut. Tight. All except for one, and there was a small amount of dried blood on the latch. I tried to collect it with a cotton swab, but it only scraped off the latch, not sticking."
            jump investigate
        "Check the music box." if check_box == False:
            $ check_box = True
            "I gently picked up the music box and looked at it on all sides. It seemed unharmed, and there wasn't any outward evidence of any sort of tracker. I set it back down gently."
            jump investigate
        "Check the vanity." if check_vanity == False:
            $ check_vanity = True
            "Evie's vanity was spotless. Not even a hair in sight. I suppose that's what you should expect when you have constant cleaning service. Other than the usual jewelry boxes, taped photos of her friends and family, and skincare products, nothing seems out of the ordinary."
            jump investigate

    scene evieroommorning
    show evie concern at slightleft
    show leonel base at slightright
    "As soon as I finish my search, Chief Vasquez calls me over to introduce myself to Evie. She seems fidgety and tense, and the fact that I tower over her doesn't seem to calm her down one bit."
    show leonel serious
    lv "Miss Evie, this is Detective Tobias Kova. He's currently in charge of the Selene cases. Detective Kova, this is Evie Ilhe. She's a relationship psychologist renowned for her work as a very successful matchmaker."
    show leonel base
    ei "Ah, um, hello, detective."
    
    tk smiley "It's nice to meet you, Miss Evie."
    show leonel serious
    lv "I'm sure you have questions, so I'll leave you two to it. I'll try and see if there's any information on the security systems."
    
    ei "Yeah, thanks…"
    hide leonel serious
    show evie concern at centerpos
    "Evie was quick to delve into what happened last night, including her escapades in Ivory Auction Hall- how she herself put an over thirty thousand value on the music box and how the calling card seemed to appear out of nowhere."

    ei "I've been so panicked and- and- I don't know what- I don't want to bother Theo cause it feels like I'm relying on him way too much- I mean, I want to do this on my own-"

    tk serious "Slow down, Evie. You did good by contacting us."

    "Though, it probably would have been better if you contacted us sooner."

    ei "What should I do?"

    tk pensive "Well, for one, it would help if you gave us that calling card you received last night. And as for the music box… how about you move it to a more secure location? Like in a basement or a windowless, locked room?"

    ei "Okay… I'll try. My father usually knows what to do in situations like this, but he's always away on business so that makes me the master of the house while he's away… It's really overwhelming sometimes."

    tk happy "Just you? What about your other family?"

    ei "I'm an only child and my mother… she died on the front lines as an army medic."

    tk sad "I'm so sorry."

    ei "It's okay! It was a long time ago. My other family members live over in Australia, so while I'm here, I'm the only person who keeps everyone here in a job. It's a lot of pressure, but…"

    "Evie looks at me and I can see a sort of determination behind her worried expression."
    show evie serious
    ei "I'll do whatever I can to keep the house running smoothly, like my parents would have wanted."

    tk base "..."

    tk happy "That's an admirable goal Evie, but don't forget to take time for yourself, too. I'm sure Theo would appreciate your company as much as he appreciates the opportunity to help you."

    "Evie looks up at me, and her worried and determined eyes seem to see right through me. She stands up straight and holds out the calling card, smiling confidently as if she were pointing and accusing me of something."
    show evie happy
    ei "Something tells me that you should be taking that advice as well."
    show evie base
    "I stare at her in silence as she places the card into my hand. She leaves to call over a few of her attendants, who quickly don their pristine white gloves and gently handle the music box, taking it away to somewhere safer."
    show evie happy
    ei "Thank you for the help, detective. I sincerely hope that Selene is caught, but in the meantime, I'll be watching my treasure like a hawk! My knight in shining armor and I will be equipped and ready!"
    hide evie happy
    tk smiley "Ah- yes! Good luck, Miss Evie!"

    "...A knight in shining armor?"
    
    "I finish up my investigation and after saying goodbye to Chief Vasquez, I exit the room and find Theo standing outside. He looked a bit tense and didn't even turn to make eye contact with me as I approached him."
    show theo base
    tk serious "Theo?"
    show theo serious
    tp "Ah- hello Detective. Are you finished with your investigation?"
    show theo base
    tk "More or less, yeah. I'll have my other subordinates report anything I might have missed when we return to the station later."
    show theo serious
    tp "Okay, and thank you again for doing this."
    show theo base
    tk happy "All in a day's work. I'd like to investigate one more thing outside if that's okay with you."
    show theo serious
    tp "Yes, I'll accompany you."

    scene manor outside morning with dissolve
    play sound park fadein 0.5
    
    "I follow the trail of footsteps outside the manor with my eyes. There weren't many heel-prints, implying that Selene is someone that is light on their feet, and the sole of the shoe had medium traction. Boots, most likely. And the prints were small, though most shoe sizes are small compared to my feet."

    "The trail leads right up to the window that I recognize as Evie's room, right underneath the window that had blood on its latch. That must have been Selene's entry point."

    "Alright, I guess I'm done here."

    tk happy "Thanks for escorting me, Theo."
    show theo serious
    tp "Of course."
    show theo base
    "I heave a heavy sigh, pinching my eyebrows. I take my journal out and scribble my findings down quickly."

    tk pensive "I think I'll go back to the office and gather my thoughts. Please keep in touch with us if you figure anything out or find any new updates."
    show theo serious
    tp "Ah, yes. Thank you."
    show theo concern
    tp "And- um- Detective?"

    tk base "Yes?"

    tp "Uh, thanks for your hard work. Take it easy."
    show theo base
    tk "..."

    tk happy "Yeah, thanks."

    "I return to the car and after a few minutes, we take off toward the office. Because of the midday traffic, it took longer for us to return than it took for us to get to the Ilhe Manor, but on the way back, I took a quick look inside my journal."

    # JOURNAL MECHANIC

    "For once, I actually seemed to be getting somewhere."

    "I bask in the warm sunlight and smile. Today was going exceptionally well."

    scene black with dissolve
    stop sound fadeout 0.5

    "Later..."

    scene evieroomnight with dissolve
    play sound night fadein 0.5
    # December 29, 1:05 PM
    show theo base at slightright
    show evie serious at slightleft
    "Evie sits in front of her vanity, brushing her hair anxiously. Theo stands at her doorway, arms crossed and leaning against the doorframe. His eyes are serious, expression unchanging."
    show theo serious
    tp "Where'd you end up putting the music box?"
    show evie serious
    ei "It's in the basement."
    show evie base
    show theo concern
    tp "You sure it'll be safe in there, right?"
    show theo base
    show evie happy
    ei "Yeah! I'll have some of the best security guarding it, after all."
    show theo concern at centerpos
    hide evie happy
    "Theo sighs."

    tp "..."

    tp "Yeah, you will."
    show theo base
    "Theo turns away from Evie, not quite leaving but not staying either. He took a deep breath and looked down at his hands. He whispered to himself, just out of Evie's hearing."
    show theo base
    tp "Let's get to work."

    #December 29, 10:00 PM

    scene manor outside night with dissolve
    play sound night fadein 0.5
    "I had just started getting ready to clock out when the station received a frantic call from Evie at around 9:15 at night, and without hesitation, I, Chief Vasquez, and a handful of officers made haste to the Ilhe Manor."
    show evie concern
    "Evie was waiting outside, pacing around. I didn't even have a moment to ask her what was wrong when she grabbed me by the hand and dragged me inside and down to her basement."

    scene safe room with dissolve
    stop sound fadeout 0.5
    show evie concern at slightleft
    "I was surprised to see a room completely encased in metal, almost as if it were a bank safe, and inside that room was Theo, who was currently pinning a hooded figure down onto the ground and wielding… a sword?"
    show theo base at slightright
    tk serious "No way… is that…"
    show theo surprise
    tp "Evie! Is that the detective?"
    show evie concern
    ei "Yeah! And the Chief and some other officers also came!"
    show theo concern
    tp "Oh, thank goodness… this thief here is speedy- I was almost bested!"
    hide evie concern
    show leonel serious at slightleft
    lv "Well, young man, I didn't expect you to guard the music box with a sword… and I'm sure Selene didn't expect it either."
    show leonel base
    show theo serious
    tp "Well, I am a fencer… and I do dabble in recreational swordfighting…"
    show theo base
    tk "If you and the music box are safe, we'll take care of the rest from here."
    hide theo base
    "I followed close behind Chief Vasquez as he approached the hooded figure. My heart was racing- I was about to find out who Selene was and lock them up for good, but… I had a bad feeling. This felt too good to be true. Too easy."

    "Chief Vasquez kneeled down and grabbed hold of the figure's hood."
    show leonel serious at centerpos
    lv "I'm getting a good look at your face before we throw you in jail, buddy."
    show leonel base
    "The hood came off and there was a clacking sound as Selene's mask hit the floor." 
    
    "My breath stopped. I came face-to-face with a familiar pair of bright blue eyes and a head of dark, messy hair that I knew all too well. Time felt like it stopped, and the only words I could choke out were..."

    scene staredown with dissolve
    hide leonel base
    tk sad "Naoya...?"

    nt "Gh-!"

    scene safe room with dissolve

    "Before I realized it, Naoya had reached for something on his person and threw what looked to be a crude, homemade device. It beeped before releasing a thick cloud of white smoke, throwing Theo off-guard and allowing Naoya to wriggle free and slip past the crowd of officers and heave the metal door shut."

    tk serious "WAIT!"
    show leonel serious
    lv "Tobias- wait! Ah- that thief snatched mask out of my hard!"
    hide leonel serious
    "Just before the door had shut completely, I slipped through the crack and chased the fleeting images of a pitch black hood through halls and stairs. I could feel my head and my heart fighting each other, weighing the option to pursue Selene or just let Naoya go."

    scene manor outside night with dissolve
    play sound night fadein 0.5

    "Naoya had come to a stop outside of the manor, as if he were waiting for me. Did he give up? Was he going to turn himself in? That might be something Naoya did, but it wasn't in Selene's nature."

    tk "I've finally found you... Selene..."

    "Naoya turned around and put his arms up in a mocking faux-surrender, a condescending smirk on his face."
    show naoya smirk
    nt "Took you long enough, detective."

    tk "It... all makes sense... the thief's reported short stature... the blood on the latch and your injury... the footprints... the mask and hood to cover your bright eyes... it all makes sense."
    show naoya contempt
    nt "Mmm... yeah, I kept you so busy, didn't I? Poor Detective Kova... slaving over my heists day and night. I almost felt bad for you."

    "He took a step forward and I tried to reach for my taser in my holster only to find that it wasn't there, but in Naoya's hands."
    
    nt "We can't be having that now, can we?"

    "He smiled and tossed the taser off to the side, out of reach for both of us."

    "We were completely alone in the driveway, and I reached for my two-way radio and paged Chief Vasquez."

    tk "Chief! Im okay! Ive got Selene in my sights!"
    
    "\"Nice wo- …tective. We'll be- over- as soon as- …eo gets thi- ..door open-!\""

    tk "Chief!? Chief Vasquez!?"
    show naoya flustered
    nt "Looks like the walls of the safe room are interfering with your connection."

    "I looked up to find Naoya standing right in front of me. It's like he teleported or something… he had his hands on his hips and looked a lot more relaxed now."
    show naoya smirk
    nt "I'll give you the chance to ask three questions. After that, I'll have to make my escape."

    tk "You're mine now, Selene. I'm not letting you go anywhere."
    show naoya contempt
    nt "Ooh... possessive, are we? Didn't peg you as the type, how cute... now, your questions?"

    "I suppose getting the chance to do this is better than nothing. Some answers would be good for my peace of mind."

    jump question_selene

label question_selene:
    menu:
        "Why are you stealing?" if q1 == False:
            play sound night
            $ q1 = True
            tk pensive "Questions, huh? Why are you stealing things anyway? It certainly couldn't have been for money because you still work a barista job."
            show naoya contempt
            nt "You're right. I don't do it for me. All those artifacts belong to their families and descendants, not rich collectors who don't know their true value. I'm just giving people what's rightfully theirs, even if they aren't rich, influential, or powerful."
            jump question_selene
        "Were you manipulating me?" if q2 == False:
            $ q2 = True
            tk pensive "Okay... were you treating me kindly because I was a detective? If you were trying to get me to lower my guard around you, it worked. I didn't suspect you at all."
            show naoya contempt
            nt "I think you just like me too much, Toby."
            tk serious "A-answer me!"
            show naoya smirk
            nt "The letter I wrote and the cake I baked for you were genuine, I assure you."
            show naoya surprise
            nt "Though, if there was something I was lying about, it would be enjoying making you that mocha. You do realize there's like 8 pumps of chocolate syrup in that thing, right?"
            tk sad "Wait... seriously?"
            nt "More chocolate than coffee and enough sugar to kill an elephant."
            tk "Huh..."
            "Wait... I'm going off-topic!"
            jump question_selene
        "How do you make people forget?" if q1 == True and q2 == True:
            play sound night fadein 0.5
            tk serious "Last question. How do you make people just... forget about you? Everyone swears they don't remember anything about your appearance and you remove any traces of your name and trace from their records."
            "Naoya goes silent for a moment, his face becoming slightly downcast. He loses his confident smirk and looks away to the side, as if contemplating something."
            show naoya surprise
            nt "I... I can't exactly put it into words… um, is there something you want?"
            tk "Something I want? Anything?"
            show naoya contempt
            nt "Yeah, anything. It's the only way I can make you understand."
            tk sad "Then..."
            "I gulp, feeling my face flush."
            tk serious "I want you to tell me how you feel about me. Not as Selene, but as plain old Naoya. Right now... please."
            "Naoya's face goes red, and he drops the whole \"Selene\" facade."
            show naoya surprise
            nt "Out of all the- right now? It's just-"
            tk sad "I'll pick something else!"
            nt "No! No. It's okay… I'll tell you if that's what you want."
            "Naoya takes a deep breath."
            show naoya flustered
            nt "Detective- no, um, Tobias. I really like you. Like a lot. Like in an \"I-wanna-go-out-with-you\" kind of way. And I've been feeling this way ever since you first walked into that cafe."
            tk "That's... that's a long time."
            nt "Yeah... um, if I could just be selfish for one second?"
            "And against my better judgement, I forget that there's a phantom thief standing right in front of me and just see Naoya Tamaki, my regular barista, looking me in the eyes."
            tk "What is it?"
            nt "Could I give you a hug? As a goodbye? I was going to ask you tomorrow, but the way things are going, I'm not sure that's going to happen."
            tk blush "Oh- right. Sure... I mean, I was going to ask you too."
            nt "Then..."
            jump fork

label fork:
    if good_end_counters >= 36:
        jump good_ending
    if good_end_counters < 36:
        jump sad_ending

label sad_ending:
    "Naoya removed both of his gloves and puts his hands in mine. His palms are a little sweaty, but I don't mind. He puts his arms around me and whispers something unintelligable."
    scene untilwemeetagain with dissolve
    "..."
    scene manor outside night with dissolve
    "The two of us pull away and it's awkward for a few seconds before Naoya looks away and sudden dizziness overcomes me."
    tk serious "What th- Naoya- what- is this-"
    show naoya contempt
    nt "You know too much. I can't risk my identity being revealed now."
    show naoya flustered
    nt "This is how I make people forget. I give you something you want in exchange for your memories of our time together. Everything. One hand and you partially forget, two hands and you forget everything about me. And... that smoke bomb I threw also has the same effect."
    "I don't even have the strength to retort back as my head hits the floor. I hear the sound of a clock tower's bells in the distance, signifying a new day."
    #December 30, 12:00 AM
    "Naoya knelt down, putting his gloves back on and patting my head. I could barely keep my eyes open, but as my consciousness faded away, I could hear Naoya say some final words."
    show naoya smirk
    nt "Happy Birthday Detective, I'll see you soon."
    hide naoya smirk
    stop sound fadeout 0.5
    scene black with dissolve

    "Two weeks later..."

    scene black with dissolve
    play music sad fadein 0.5

    "Detective Kova doesn't come around the station much anymore. All he can think about is how he let Selene get away. Julia and Romeo visit him occasionally, but other than that, no one really sees him much anymore."

    "He's been cooped up in his apartment, just thinking. Thinking about the case. Thinking about how close he was. Thinking about how he failed his father."

    "He's since handed the case over to someone else, but since then, he's felt the need to prove himself even more. If he isn't at the office archives gathering new information, he's at home reading, thinking, working. No time to rest, no time to slow down."

    "At this rate, all this work is going to send him to an early grave."

    "If only he had learned to just take it easy."

    "SAD ENDING ACHIEVED."
    stop music fadeout 0.5
    return

label good_ending:
    "Naoya removed one of his gloves and cupped my face with his hand. His palm is a little sweaty, but I don't mind. He puts his arms around me and whispers something unintelligable."
    scene untilwemeetagain with dissolve
    "..."
    scene manor outside night with dissolve
    "The two of us pull away and it's awkward for a few seconds before Naoya looks away and sudden dizziness overcomes me."
    tk serious "What th- Naoya- what- is this-"
    show naoya flustered
    nt "This is how I make people forget. I give you something you want in exchange for your memories of our time together. Everything. One hand and you partially forget, two hands and you forget everything about me. And... that smoke bomb I threw also has the same effect."
    "I don't even have the strength to retort back as my head hits the floor. I hear the sound of a clock tower's bells in the distance, signifying a new day."
    #December 30, 12:00 AM
    "Naoya knelt down, putting his gloves back on and patting my head. I could barely keep my eyes open, but as my consciousness faded away, I could hear Naoya say some final words."
    show naoya smirk
    nt "Happy Birthday Detective, I'll see you soon."
    hide naoya smirk
    scene black with dissolve
    stop sound fadeout 0.5
    play sound park fadein 0.5
    "I woke up in a hospital bed with Julia waiting for me at my bedside and a letter on my chest. It wasn't from her, she said- it had been there before she arrived." 
    
    "I picked it up and read it."

    scene seleneletter with dissolve

    "\"Dearest Detective Kova, I'm sorry I had to erase your memory last night. My work is too important for me to be arrested, but I have a feeling that we will fight on the same side one day.\""

    "\"If all goes well, I will not have erased your memory of me entirely, and when you meet me again, you won't have forgotten who I was.\""

    "\"I look forward to seeing you again, and I hope that you feel the same way. Until then, take it easy, Detective Kova.\""

    "\"Yours truly, Selene.\""

    scene black with dissolve
    stop sound fadeout 0.5
    scene cafe with dissolve
    play music home fadein 0.5
    tk smiley "Naoya!"
    show naoya concern
    nt "Ah!"
    show naoya cheeky
    nt "You remembered..."
    show naoya base
    tk pensive "Huh? Of course I'd remember to see the person who asked me out. What am I, some kind of scoundrel?."
    show naoya happy
    nt  "Of course, of course. The usual?"
    show naoya base
    tk happy "You know it."
    show naoya happy
    nt "And because it's your birthday, it's on me."
    show naoya base
    tk smiley "Aw, you didn't have to do that!"
    show naoya smiley
    nt "Any ideas on what you want to do for your birthday?"
    
    tk blush "I have ideas, but I need to tell you about the crazy thing that happened last night."
    show naoya cheeky
    nt "Oh?"

    tk happy "Is that okay? I'm not interrupting you or anything, am I?"
    show naoya smiley
    nt "Of course you aren't."

    tk "Okay, good."

    "Naoya hands me my drink, hot and fresh as usual. He rests his head in his hands, ready to listen, and I see a glint of mischief in his eyes."
    show naoya cheeky
    nt "Tell me all about it, dearest Detective Kova."

    "GOOD ENDING ACHIEVED!"
    hide naoya cheeky
    stop music fadeout 0.5
    return

#HANGOUT EVENTS
label hangout_event:
    menu:
        "Hangout with Julia!":
            jump julia_hangout
        "Hangout with Chief Vasquez!":
            jump leonel_hangout
label julia_hangout:

    play sound office

    "I decde to hang out with Julia for a bit. Maybe her good mood will rub off on me."
    "I pull out my phone and text her, asking \"You down to chat? Chief says I need a break.\" Almost instantly, I receive a very enthusiastic reply."
    "\"OMG DETECTIVE TOBIAS KOVA ASKING TO HANG OUT!? THIS IS UNHEARD OF! IS THE WORLD ABOUT TO END!?"
    "I roll my eyes, but before I have a change to reply, Julia has already run up to my desk, squealing like a little piglet."
    show julia happy
    js "Phew...! Alright, Toby, what's popping!?"
    show julia base
    tk "Please stop saying that. And don't call me Toby."
    show julia surprise
    js "Ah, saving that nickname for a certain someone, are you?"
    show julia base
    tk "That's not-"
    show julia happy
    js "I'm kidding! Actually, I know you wanted to chat, but I have a burning question that needs to be answered right now!"
    show julia base
    tk "What is it?"
    show julia surprise
    js "Why do you even like Naoya in the first place?"

    tk "Huh... that's a good question..."

    "Why do I like him anyways?"

    menu:
        "His appearance.":
            $ good_end_counters += 1
            tk "He has a cute face and very pretty blue eyes."
            show julia concern
            js "That's kinda shallow, don't you think?"
            tk "You're the one who asked."
            show julia concern
            js "True, true, but..."
        "His personality.":
            tk "He has a really sweet personality."
            show julia concern
            js "That's just his customer service personality."
            tk "What is that supposed to mean?"
            js "I mean, that's just what he's like at work. What if he's actually a sadist or something? That would be weird, unless you're into that, which- I'm not judging or anything."
            tk "You think of the most ridiculous scenarios sometimes, Julia."
            show julia base
            js "I know!"
        "The coffee he makes.":
            tk "He always makes the perfect cup of coffee."
            show julia concern
            js "That is so dumb. You're only in love with him because he makes you coffee?"
            tk "Okay, love is a bit strong-"
            show julia base
            js "Is that how you usually fall in love with people? They make you coffee and you fold? What if Chief Vasquez made you a cup of coffee from the machine here? Would you have fallen in love with him instead?"
            tk "Ew, no, he's like a father figure to me."
            show julia upset
            js "Eugh! Forget I even asked..."

    show julia base
    js "...Is that all that comes to mind?"

    tk "I guess..."
    show julia surprise
    js "Interesting. And what do you think he likes about you?"

    tk "Me? I dunno, my... persistence?"
    show julia upset
    js "Bzzt! Not that. Try again."

    tk "You talk as if you know."
    show julia concern
    js "I'm not convinced that anyone would fall in love with you because you were overworking yourself."

    tk "Is it because I'm a regular?"
    show julia base
    js "Hm... yeah, that's the best explanation for it."

    tk "So you didn't know."
    show julia surprise
    js "No, but think about it! You keep visiting in the morning, requesting Naoya to make your coffee, ordering the same thing as far as I can tell, and not only does he appreciate you paying his bills, he gets to see your face and hear your voice like, every day!"
    show julia concern
    js "..."

    js "How much money have you spent on coffee over these past few months?"

    tk "I... don't even want to think about it..."

    js "Yikes."

    tk "I know. I'm scared to even look at my bank statements."
    show julia surprise
    js "Yeah, I would be scared too."
    show julia base
    js "Anyways, I have to get to class soon. I have a calculus quiz today, ugh..."

    tk "I loved calculus."
    show julia upset
    js "Ew! Who likes math?"

    tk "It's actually really simple-"
    show julia happy
    js "Whatever! See you soon, Detective!"
    hide julia happy
    "Julia bolts out of the room again before doubling back to peek inside and wave goodbye."
    show julia base
    js "Let's chat again sometime!"

    tk "Good luck, Julia!"
    hide julia base
    "She sticks her tongue out at me before running off, and I turn to my itinerary for the day, feeling refreshed."

    tk "Alright, let's get to work."

    jump interrogating
label leonel_hangout:

    play sound office

    "I run after the chief, who surprisingly wasn't far from the office and invite him back inside for a chat."
    show leonel serious
    lv "When I said you should take a break, I didn't mean now. You are still on the clock, Kova."
    show leonel base
    tk "Just for a bit? I had a terrible headache just now and don't want to push it. Besides, I have a question."
    show leonel happy
    lv "Sure, make it quick."
    show leonel base
    "Chief Vasquez takes another sip of coffee from his mug, grimacing. I chuckle at the face he makes, attempting to disguise it behind a cough."

    menu:
        "What was my dad like?":
            $ good_end_counters += 1
            tk "I wanted to know a little more about my dad."
            show leonel worry
            "Chief Vasquez looks at me, slightly surprised, before smiling."
            lv "Your dad was the best detective on the force. When he was dispatched to a scene, he could figure out a culprit within 48 hours."
            show leonel base
            tk "Oh."
            "As soon as I am reminded of my dad's achievements, I realize that I still have far to go."
            show leonel happy
            lv "Chin up, Kova. You're still a good detective yourself, even if you don't realize it."
        "Have you ever had a case as hard as this one before?":
            tk "This Selene case is hard. The two detectives who took this case up before me were equally as stumped. Are all cases this hard?"
            show leonel serious
            lv "You'll have your fair share of ongoing investigations- cases that go on for years."
            lv "It can be frustrating, but it'll be worth it when justice is served."
            show leonel base
            "Chief Vasquez does a stupid looking superhero pose and I laugh for real this time. He smiles."
            show leonel happy
            lv "Don't be so hard on yourself, Kova. You're a great detective, even if you don't realize it."
    
    show leonel base
    tk "I am?"
    show leonel serious
    lv "Sure, you're not near your dad's level yet, but you make up for it with your persistence. If something doesn't make sense right away, you go after answers like a hungry wolf stalking its prey."
    
    lv "Though, sometimes, that persistence is a double edged sword. You don't know when to quit, which is like, the opposite of your father."
    show leonel base
    tk "Really?"
    show leonel happy
    lv "Yeah. His brain was scarily efficient that it circled back to him being lazy and putting almost no effort into solving a case."
    show leonel base
    tk "That sounds really annoying."
    show leonel serious
    lv "Right!? I was so jealous of him. It made me want to work even harder. I'm glad you didn't inherit that trait of his."

    lv "Although..."
    show leonel base
    tk "What is it?"
    show leonel happy
    lv "You look just like him. Your dad."
    show leonel base
    tk "Really?"
    show leonel happy
    lv "Yeah. Especially when you put your hand to your chin and start thinking. He used to do that too."

    lv "Though, he'd also make this stupd grumbling noise whenever he thought. Like this."
    show leonel base
    "Chief Vasquez made a noise that sounded close to a microwave, which sent me into a fit of laughter. He joined in soon after, slapping his knee loud enough to draw the attention of some passerby officers."
    show leonel happy
    lv "Yeah, your dad was great."

    tk "Thanks, Mr. Vasquez."
    show leonel serious
    lv "You're still on the clock, Kova. That's Chief Vasquez to you."
    show leonel base
    tk "R-right, sorry."
    
    "Chief Vasquez stood up and grabbed his mug, reaching out to ruffle my hair."
    show leonel happy
    lv "I'll be happy to trash talk your father any day of the week, preferably outside of work."
    show leonel base
    tk "Haha, okay. Thanks again, Chief."
    show leonel happy
    lv "See you around, Kova."
    hide leonel happy
    "Chief Vasquez walked out of the room and I turned to the rest of my itinerary for the day, feeling refreshed."

    tk "Alright, let's get to work."

    jump interrogating

#FILE 1: DANTE'S TESTIMONY
label file1:
    scene dantefile

    call screen dantefile

    screen dantefile():
        add "dantefile"
        modal True
        imagebutton auto "dante_%s.webp":
            focus_mask True
            action Jump("dante_photo")
    
        imagebutton auto "fileinfo1_%s.webp":
            focus_mask True
            action Jump ("sticky_note")

        imagebutton auto "fileinfo2_%s.webp":
            focus_mask True
            action Jump ("testimony1")

        imagebutton auto "fileinfo3_%s.webp":
            focus_mask True
            action Jump ("testimony2")

        imagebutton auto "fileinfo4_%s.webp":
            focus_mask True
            action Jump ("testimony3")

        imagebutton auto "finishbutton_%s.webp":
            focus_mask True
            if dfileread1 == True and dfileread2 == True and dfileread3 == True:
                action Jump ("continuation4")
            elif dfileread1 == False and dfileread2 == False and dfileread3 == False:
                action Jump ("unfinishedFile1")
label dante_photo:
    scene dantefile
    "This is Dante Andre del Rosaria, secretary to a famous art collector and the witness in this case."
    "He came face-to-face with Selene on his way home from work one night... sort of."
    "He doesn't look too happy in this photo."
    jump file1
label sticky_note:
    scene dantefile
    "More information about Dante."
    "26, Colombian-American, 6 feet tall, white hair with a green streak and green eyes."
    "He has been working for this art collector, Ms. Vautrin since he graduated college at the age of 22."
    "Apparently, she doesn't treat the pieces in her collection all that well. They're stuffed in some storage container to be sold for profit later instead of being hung on walls and admired."
    "Kinda sad, if you ask me."
    jump file1
label testimony1:
    scene dantefile
    $ dfileread1 = True
    "The first part of Dante's testimony. It reads..."
    "{i}I was walking home from my workplace, carrying some important transaction documents regarding an art piece Ms. Vautrin was looking to purchase.{/i}"
    "{i}The papers were in my bag, in a blue plastic folder. And it was a messeger bag, which means it was slung over my shoulder and not on my back.{/i}"
    "{i}Anyways, I was minding my own business, just walking home when that thief jumped me! Well, I wasn't hurt physically, but they did snatch my bag from me.{/i}"
    "{i}I... I didn't even see it coming...{/i}"
    jump file1
label testimony2:
    scene dantefile
    $ dfileread2 = True
    "The second part of Dante's testimony. It reads..."
    "{i}I chased after them, but every time I thought I got close, they made a quick escape...{/i}"
    "{i}They were crazy fast and really athletic. They were jumping over alleyway gates and dodging trash cans and all that stuff.{/i}"
    "{i}You'd think someone that short could be caught a lot faster, but no. They totally outran me.{/i}"
    "{i}Huh? How tall? Um.. if I had to guess... around 5 feet and 5 inches? Could be less, I can't say for sure.{/i}"
    "That seems important. Better add that to my journal."
    jump file1
label testimony3:
    scene dantefile
    $ dfileread3 = True
    "The last part of Dante's testimony. It reads..."
    "{i}I turned the corner into an alley, but it was a dead end. I looked everywhere, but it seemed like they had just vanished into thin air- like with magic or something.{/i}"
    "{i}My bag was on the ground and inside the folder where the documents once were was a calling card. Something about... something being put into deserving hands or whatever.{/i}"
    "{i}...did I catch anything about their appearance? N-no, they had a hood and gloves and- just- everything was covered, okay? I didn't see anything.{/i}"
    "{i}That's... all I can remember for now...{/i}"
    "I expected an answer like this. No one has been able to see Selene's face or even catch a piece of their hair. They either forget everything about their appearance or just never encounter their features in the first place."
    jump file1
label unfinishedFile1:
    scene dantefile
    "I'm not done reading just yet. I need to be thorough."
    jump file1

#FILE 2: KLARIKA'S NOTES FILE
label file2:

    scene klarikafile
    
    call screen kfile

    screen kfile():
        add "klarikafile"
        modal True
        imagebutton auto "notes_%s.webp":
            focus_mask True
            action Jump ("description1")

        imagebutton auto "script1_%s.webp":
            focus_mask True
            action Jump ("description2")

        imagebutton auto "script2_%s.webp":
            focus_mask True
            action Jump ("description3")

        imagebutton auto "script3_%s.webp":
            focus_mask True
            action Jump ("description4")

        imagebutton auto "finishbutton_%s.webp":
            focus_mask True
            if kfileread1 == True and kfileread2 == True and kfileread3 == True:
                action Jump ("continuation5")
            elif kfileread1 == False and kfileread2 == False and kfileread3 == False:
                action Jump ("unfinishedFile2")
label description1:
    scene klarikafile
    "A photocopied picture of Klarika's notes."
    "If I hadn't known any better, I would have assumed that this was a doctor's note of some sort."
    "For a rich lady, her handwriting is atrocious. Kudos to the handwriting analyst..."
    jump file2
label description2:
    scene klarikafile
    $ kfileread1 = True
    "This part of Klarika's notes has been redacted with what looks like a permanent marker."
    "The handwriting analyst noted that they probably would have been able to decode what was underneath the marker if they had the physical notepad."
    "...I don't think Klarika would have agreed to do such a thing. Her notes are crucial to her work, after all. And I don't think she was the one who redacted the person's name either."
    "Shame. Selene's name is probably under that marker... or they could have used an alias... or there's a chance this isn't even their paper!"
    "...No I'm definitely overthinking it..."
    "Why does this thief have to be so... crafty!"
    jump file2
label description3:
    scene klarikafile
    $ kfileread2 = True
    "This part of Klarika's notes lists Selene's measurements."
    "Chest, 86.36 centimeters. Shoulder width, 45.97 centimeters."
    "Arm length and width, leg length and width, Hips, waist- even the ankle width?"
    "I gotta hand it to Klarika- she doesn't play around when it comes to her work. But, there isn't really anything here that can point to anyone specific."
    "The force can't exactly go up to everyone they see and measure every part of their body."
    "But... based on these measurements, it seems that Dante's previous testimony was correct. Selene is probably a little on the shorter side."
    jump file2
label description4:
    scene klarikafile
    $ kfileread3 = True
    "At the very bottom of Klarika's notes are a few blurbs of information that seem a little more personal."
    "\"Fair complexion and brightly colored eyes, a more muted color palette would be better...\""
    "\"Softer features, slightly longer a-line w/ a petticoat; gives a modern princess feel.\""
    "Bright eyes and a fair complextion... that seems important. I better take note of that in my journal."
    jump file2
label unfinishedFile2:
    scene klarikafile
    "I'm not done reading just yet. I need to be thorough."
    jump file2

#FILE 3: THE PERSON WHO FORGOT
label file3:
    scene anonfile
    
    call screen afile

    screen afile():
        add "anonfile"
        modal True
        imagebutton auto "anonnote_%s.webp":
            focus_mask True
            action Jump ("desc1")
        imagebutton auto "anoninfo1_%s.webp":
            focus_mask True
            action Jump ("desc2")
        imagebutton auto "anoninfo2_%s.webp":
            focus_mask True
            action Jump ("desc3")
        imagebutton auto "anoninfo3_%s.webp":
            focus_mask True
            action Jump ("desc4")
        imagebutton auto "anoninfo4_%s.webp":
            focus_mask True
            action Jump ("desc5")
        imagebutton auto "finishbutton_%s.webp":
            focus_mask True
            if vfileread1 == True and vfileread2 == True and vfileread3 == True:
                if earlyBird == True:
                    action Jump ("earlybird")
                elif onTime == True:
                    action Jump ("continuation2")
            elif vfileread1 == False and vfileread2 == False and vfileread3 == False:
                action Jump ("unfinishedFile3")
label desc1:
    scene anonfile
    "A sticky note regarding the person in the transcript."
    "\"The person being interrogated has opted out of taking a picture.\""
    "It was signed by the person conducting the interrogation."
    "That shouldn't be a problem."
    jump file3
label desc2:
    scene anonfile
    "\"Name: Eka Santoso, Age: 21, Indonesian-American-\""
    "Oh! He's a student at the same police academy I went to!"
    "\"Five feet and five inches, brown hair, brown eyes, lean figure.\""
    "I guess this is the person being interrogated."
    jump file3
label desc3:
    scene anonfile
    $ vfileread1 = True
    "The first part of the transcript..."
    "\"My first interrogation- haha, I kinda hoped I would be the person conducting it, not the one being interrogated...\""
    "\"Well um... where do I start? I heard from a friend of a friend that the force was having a bit of trouble with the Selene cases- the detective in charge was really beating himself up over it-\""
    "... that was uncalled for... whatever..."
    "\"I thought to myself, if I try to find something out, maybe this could be my big break! If I helped solve this case, I might, I dunno, graduate early and be a detective too? But, I guess that's pretty childish.\""
    "\"Anyways, I caught wind that a potential suspect was working for a lawyer who was interested in selling a certain valuable painting, so I eagerly approached the lawyer pretending to be interested in the art.\""
    "\"He told me to meet him at his home one night so I could see the piece and discuss over some drinks, and I agreed, but when I got there, the guy was knocked out cold! Alive, but like, unconscious.\""
    "That sounds terrifying... I hope he's okay."
    jump file3
label desc4:
    scene anonfile
    $ vfileread2 = True
    "The second part of the transcript..."
    "\"I checked his vitals and stuff- like they taught as at the academy- and I went to go check on the painting.\""
    "\"When I last saw it, it was perfectly intact, still hanging on the wall by the guy's stairs, but out of the corner of my eye, I saw a shadow watching me from a dark hallway!"
    "\"I chased after the figure, obviously, because they were suspicious, and I- I jumped them! I tackled them to the ground!\""
    "\"They had all the makings of a phantom thief! Outfit and mask and all! I couldn't give you the exact details, but if you think of any phantom thief from any popular media, they probably wore similar-ish clothes.\""
    "\"I tried to reach for their hood to see their face and snatch their mask off, but they put up a fight! They seemed pretty athletic and energetic.\""
    "That seems important... better note that down in my journal..."
    jump file3
label desc5:
    scene anonfile
    $ vfileread3 = True
    "The last part of the transcript..."
    "\"We got into a real scuffle back there, and I do remember grabbing the hem of their hood and pulling it down and being met with a nice face, but...\""
    "\"I don't remember anything about what they looked like, though I'm sure that must be a known fact at this point.\""
    "\"What else do I remember? Hm... well, during the scuffle, I remember them struggling to take their gloves off with their teeth. I remember I thought it was pretty stupid because they could get their prints on the wall or something.\""
    "\"That's all I remember, unfortunately. We got into a scuffle, they took their gloves off to square up, and then I blacked out and lost my memory of them.\""
    "This is just becoming more and more supernatural. That mind erasing ability sounds terrifying, but it seems to only affect the victims' memories of Selene's identity."
    jump file3
label unfinishedFile3:
    scene anonfile
    "I'm not done reading everything yet. I need to be thorough."
    jump file3

#FILE 4: INCRIMINATING
label file4:
    scene finalfile
    
    call screen finalfile

    screen finalfile():
        add "finalfile"
        modal True
        imagebutton auto "hairphoto_%s.webp":
            focus_mask True
            action Jump ("hairphoto")
        imagebutton auto "hairinfo_%s.webp":
            focus_mask True
            action Jump ("hairinfo")
        imagebutton auto "printphoto_%s.webp":
            focus_mask True
            action Jump ("printphoto")
        imagebutton auto "finalinfo_%s.webp":
            focus_mask True
            action Jump ("finalinfo")
        imagebutton auto "finishbutton_%s.webp":
            focus_mask True
            if photo1 == True and photo2 == True and evidence1 == True and evidence2 == True:
                action Jump ("late_night")
            else:
                action Jump ("unfinishedFile4")
label hairphoto:
    scene finalfile
    $ photo1 = True
    "It's... a photo of a strand of hair from a crime scene..."
    "It's dark enough that it had to be placed on a bright background so that the camera could catch it."
    "It almost looks like... a dark blue?"
    jump file4
label hairinfo:
    scene finalfile
    $ photo2 = True
    "Information about the hair..."
    "According to analysts, there was no root on the strand to extract DNA from. Of course it would never be that easy..."
    "The strand was short and on the thinner side."
    "This strand of hair could be related to the suspect, but in taking the fingerprint into account, there are some doubts about whether or not the owner of this hair is actually Selene or someone unrealted."
    jump file4
label printphoto:
    scene finalfile
    $ evidence1 = True
    "It's a... fingerprint? Or at least, half of it."
    "...did they get an intern or student to lift this? It doesn't seem like it would be very helpful..."
    "Though I guess at this point anything is better than nothing."
    jump file4
label finalinfo:
    scene finalfile
    $ evidence2 = True
    "This is..."
    "Information from the fingerprint analyst regarding the print."
    "They were able to trace it back to a person-- an elementary school student."
    "...seriously?"
    "It begs the questions as to whether or not the owner of the piece of hair could even be considered Selene's or if it was planted or mere coincidence."
    jump file4
label unfinishedFile4:
    scene finalfile
    "I'm not done reading everything yet..."
    jump file4
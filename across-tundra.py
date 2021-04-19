from gtts import gTTS
import playsound
import os.path as os

voiced = False
progress = 0


def casting_off():
    print()
    text = """Casting Off
With a compass in hand and butterflies in stomach, he gazed off towards the visage of Anchorage, 
rapidly shrinking away into the horizon. 
A game of cards, and a hearty serving of alcohol had certainly done wonders to feed his excitement and wanderlust while they were docked in port, 
but he had to admit, it was hard to get the yesterday's goodbyes out of his mind. 
His mother's reaction had not surprised him, 
a quiet bout of sobbing and a laundry list of demands as they stood before the front door. 
She had been nervous for weeks, and in time he had done his best to reassure her. 
This was something he needed to do, he would take all available precautions, he would have all the necessary documents. 
It was a conversation that seemed to never end. No, he had resolved any lingering strife with mom. 
It wasn't her that was spawning such remorse in his sea-bound heart. Surprisingly, it was Dad. 
To say, his father was an enigma would be an understatement. Childhood memories existed beyond count; 
missed baseball games, absent birthday parties, one word responses to kindergarten art pieces. 
It was not that dad didn't care at all, per say. From time to time, he would show his affection, 
teach his sons to replace a flat tire or two. The problem was consistency, or lack thereof. 
At any moment, Dad might disappear into the basement again, 
or a car would pull out of the driveway and return hours after family dinner had ended.
He never knew what to make of it. Perhaps the war had simply taken too large a toll, 
created a man who could only function on whiskey and lonesome hours. 
So when Dad burst into tears in front of the taxi, launched into a bear hug, 
and handed his son a compass and pistol subtly before the car door closed, he couldn't help but feel shaken. 
Was he really making the right decision, if it could affect a man such as that so greatly? 
Intimately, he brushed the thought away and returned below deck. There was no turning back now,
and he had a great and exciting adventure laid out before him. He would return alive, and ultimately, 
changed for the better."""
    print(text)
    if voiced:
        if not os.exists('./casting_off.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('casting_off.mp3')
        playsound.playsound('./casting_off.mp3')
    print()
    global progress
    progress += 1
    input("[Time to find what's out there...]")


def death_event():
    print()
    text = """They Shall Not Grow Old
Martha Smith had been counting the days since her son had gone off to Russia, that land so wild and untamed, 
brimming with its slobbering tyrants and bloodthirsty bandits. She had not heard a word from him in months since his last letter.
Even as the great land was being brought to heel by a half dozen or so such tyrants now left,
their states establishing bonds with the land of the free, she still didn't get so much as a word of news on the state of her boy.
Now, as she marked off another tally in the secret Journal under her bed that she was sure Earnest didn't know about,
she placed her head in her hands and began her tearless sobbing. She had simply run out by the first month after she began this nightly routine.
Gulping down the glass of water on her nightstand, she slid the Journal back under the bed. Earnest was working late,
or so she had been told, and so she had dedicated the hours between his call from work at 7:00 to his return home to her grief.
Her suffering is cyclical as she awaits closure that simply never will come. 
Earnest was not working late. Clearing trash off the dashboard of his old beat up truck, 
he searched for the letter he had recovered last time he was 'working late',
scouring the old main for any kind of news from Russia about his son. 
He had found only one scrap of closure after endless nights searching for something to placate his suffering
wife, a communique from a Russian citizen from a city called Harbin writing to an American cousin of his 
about how he had seen an American pass through. That was it. Apart from the few letters he had gotten,
this was all that was left of his son in paper. The famously stoic, hardworking man cast the letter aside as it was stained with tears,
and laid his head on the steering wheel to cry."""
    print(text)
    if voiced:
        if not os.exists('./death_event.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('death_event.mp3')
        playsound.playsound('./death_event.mp3')
    print()
    input("[His Journey never ended for those who loved him.]")


def an_unexpected_arrival():
    print()
    text = """An Unexpected Arrival
At the docks of Petropavlovsk-Kamchatsky, a boat has arrived from the city of Anchorage in the American state of Alaska.
The only passenger is a young American man named Steve Smith who claims to be a tourist traveling alone, 
and has the documents to prove it. Determined but fresh-faced, it is hard to know if he will survive for long,
in the anarchy that Russia finds itself in, and up to us if he gets the chance to. Licking his lips, 
Ivan Yumashev's eyes skimmed the report once more, before he set it aside. Picking up a cigarette - a luxury these days,
looted from a passing Japanese ship, he had heard - he proceeded to light it with his free hand. An American tourist, eh?
That sure wasn't something you saw everyday. It might be worthwhile to come meet this American personally before he leaves,
and give him a tour of the fleet. It might, for once, 
take his mind off of the sorry state of shameful piracy the Pacific Fleet had been reduced to."""
    print(text)
    if voiced:
        if not os.exists('./an_unexpected_arrival.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('an_unexpected_arrival.mp3')
        playsound.playsound('./an_unexpected_arrival.mp3')
    print()
    input("[If nothing else, it'd impress the men.]")


def entry_1():
    print()
    text = """Entry 1: The Pacific Fleet
Visiting Kamchatka was more eventful than I'd thought it would be. Sailors on military ships and on the docks alike,
stared at my boat as it came to a stop. When I told them I came from America, the sailors all seemed really excited for some reason,
and a bunch of them wanted to shake my hand. I felt like a celebrity, almost. That feeling only increased when Admiral Yumashev,
the leader of the 'Pacific Fleet' that controls Kamchatka, came to meet me in person. 
He said the city we were in was called Petropavlovsk-Kamchatsky, and gave me a tour of his fleet.
The admiral was really nice and patient, although his English wasn't great; he said he learned it back during the war, 
the big one, so he must be a couple decades out of practice. Still, it was better than nothing. 
Something was off about the fleet though. The ships are outdated, but they must still need fuel and parts, 
which I didn't see any industry for, and I didn't see any trading vessels at the docks. 
I'd heard that the economy of Kamchatka depended on piracy, but I didn't think good men like the admiral and those sailors would resort to it.
Still, I guess everyone needs to eat, and if half the things I've heard about the state of Russia are true I guess I can't blame them too much.
At least Admiral Yumashev arranged for another boat to take me to Magadan."""
    print(text)
    if voiced:
        if not os.exists('./entry_1.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_1.mp3')
        playsound.playsound('./entry_1.mp3')
    print()
    global progress
    progress += 1
    input('[Land ho!]')


def an_american_visit():
    print()
    text = """An American Visit
A boat has arrived from Kamchatka carrying an interesting passenger - an American tourist. 
People do not usually come to visit Russia from the outside, especially Americans. After all, 
no one likes visiting war-torn wastelands, especially the spread out and frigid Far East. 
He probably won't even last a week without freezing to death unless we help him out somehow. 
We cannot let a naive American die in the wilderness, the least we can do is provide shelter for a few days. 
Perhaps Matkovsky could even meet with him! Being an American, he could be useful for reaching the leadership of the United States. 
We have always wanted a closer relationship with the Americans, so why not start now, when we have one right here!
Matkovsky even believes he has connections to the CIA. What fortune! Besides, it would be a good way to show hospitality.
The American ought to be impressed when he meets the true Vozhd of the Russians! No matter what, 
it would make a good impression will help us stand out besides all the other warlords surrounding us. 
However, maybe it could be a better and safer idea just to give him a general tour around Magadan. 
Letting him see the town will show him the true way of life in Russia better than any meeting with Matkovsky. 
Besides, the Vozhd is a busy man, and he may not enjoy wasting his time with a potentially worthless American. 
So, should we give him a tour of the town, or should Matkovsky invite him to a drink?"""
    print(text)
    if voiced:
        if not os.exists('./an_american_visit.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('an_american_visit.mp3')
        playsound.playsound('./an_american_visit.mp3')
    print()


def entry_2a():
    print()
    text = """Entry 2: Meeting with Matkovsky
I had a meeting with Magadan's "Vozhd" today, Mikhail Matkovsky. He seemed pretty fun and offered me some almost not awful vodka,
but overall the experience was rather strange. He kept asking me about my connections to President Nixon and the CIA,
weirdly enough. Maybe it's my hair? After I told him I was just an average American he seemed a bit disappointed. 
Then he asked about how life was in America and what I was doing in Russia. 
I told him I was a university student back home and I had come to visit so I could explore Russia,
and maybe have a little bit of fun and adventure instead of my boring life back home.
I don't know what he said after that but I think it was something along the lines of how I'll be shot by the first bandit that gets anywhere near me,
so oh well. Then I had a few more drinks and proceeded to tell him my dad was an astronaut in a secret mission to Venus
as well as back in the war he had killed one hundred Japs with only a pistol. In reality, he's a mechanic and always has been.
Matkovsky seemed to enjoy the story, however, although I don't know how much of it he understood. My Russian isn't the best.
After our meeting he gifted me this enormous bearskin. I guess I should wear it,
I already think I'm fine without it as I have my own fur coat but I accepted it anyway. It is very warm. 
Next I'll be heading up Yakutsk to see what is going on there."""
    print(text)
    if voiced:
        if not os.exists('./entry_2a.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_2a.mp3')
        playsound.playsound('./entry_2a.mp3')
    print()
    global progress
    progress += 1
    input('[At least he had fun?]')


def entry_2b():
    print()
    text = """Entry 2: Touring Magadan
I was given a tour around Magadan today. It's a fun town with lots of bars. They only serve vodka though, 
and to be honest, it's pretty terrible. The seaport is probably only big thing around. Still, 
there is a very cozy feeling about the place. A weird sort of cozy, because you can walk past a family enjoying a quaint meal
and then look across the street and see a blackshirt officer beating up a hobo. Still cozy, though. 
It feels like Magadan is the only place around, even though I'm told there are a few more villages nearby. 
Still, it is certainly isolated, so I hope I can find my way to where I'm going next. There aren't many roads in Russia either.
While we were touring I'm pretty certain I also saw a labor camp. Not sure if that was what it was 
but from the way my tour guide tried to keep me away from it, I'm pretty sure Magadan has a few populated labor camps.
Hopefully, those will be the worst thing I see in Russia. From what I expect, however, some places may be far worse. 
Overall Magadan isn't all that bad. I do sure hope not all places are like this though. 
It seems the people have adjusted to the harsh life here. Some in different ways than others, but I'm glad I came. 
It's time to continue my trip, and I have a long way to go."""
    print(text)
    if voiced:
        if not os.exists('./entry_2b.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_2b.mp3')
        playsound.playsound('./entry_2b.mp3')
    print()
    global progress
    progress += 1
    input('[Still better than Amur!]')


def a_yankee_tourist():
    print()
    text = """A Yankee Tourist?
One of our borders posts along the Aldan river has reported an unusual visitor from Magadan.
Initially, we expected him to be a spy from Matkovsky's band of fascists, but upon closer inspection, 
it appears he is nothing of the sort. The man explained to us that he is an American tourist visiting Russia, 
and presented proof to support his wild claim. While we have no idea what would possess a person,
let alone a well-off American to do such a thing, he appeared to pose little threat and was sent on his way to Yakutsk.
We don't expect him to live for very long given his inexperience, 
but the least we can do is show him around our humble republic."""
    print(text)
    if voiced:
        if not os.exists('./a_yankee_tourist.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('a_yankee_tourist.mp3')
        playsound.playsound('./a_yankee_tourist.mp3')
    print()
    input('[Who in their right mind would think Russia is a good place for a tourist?]')


def entry_3():
    print()
    text = """Entry 3: Yakutia
Crossing the river into Yakutia was less eventful then I expected. The border guards were initially suspicious before I told them of my intentions.
I don't think they believed me at first but, after showing them my passport and the ticket I purchased to Magadan, 
they sent me on my way to the capital. Yakutsk was peaceful if not densely populated. The people were friendly, 
but not particularly fond of their government. From what I gather, Yakutia is dominated by mining interests
who have mostly bought out the politicians and who commonly mistreat their workers. 
The miners I met spoke of harsh working conditions and poor wages. After purchasing some supplies and gathering my notes,
I said my goodbyes and left the capital. Beyond Yakutsk, I saw little beyond the odd village or quarry
and mostly followed the Lena River to the "Partisan Republic" of Aldan. Given what I've been hearing about Russia, 
perhaps hiring a guide or bodyguard would be a wise move. Most of those I talked to
seemed skeptical of my ability to tour the entire country and make back to the States in one piece.
Maybe some of the partisans would be willing to help me out."""
    print(text)
    if voiced:
        if not os.exists('./entry_3.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_3.mp3')
        playsound.playsound('./entry_3.mp3')
    print()
    global progress
    progress += 1
    input('[They were peaceful at the very least.]')


def a_new_arrival():
    print()
    text = """A New Arrival
Very few people willingly come to Aldan. It is cold, impoverished, and actively hostile towards one of its most powerful neighbors,
the Presidium of the Supreme Soviet. As such, it was very surprising when some partisans reported a man
carrying an American flag had crossed over from Yakutsk. Soon, it became clear that this really was an American,
one who had decided to travel across the former Soviet Union and learn about its peoples. 
While one can certainly doubt his sanity for deciding to travel alone across a country that has broken down entirely into warlords and anarchy,
our partisans did escort him across our small corner of Siberia, so that he could safely continue his travels.
Unfortunately for the American, he will continue his journey by visiting the fascists of Amur next,
after staying the night in Aldan."""
    print(text)
    if voiced:
        if not os.exists('./a_new_arrival.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('a_new_arrival.mp3')
        playsound.playsound('./a_new_arrival.mp3')
    print()
    input('[Are all Americans this strange?]')


def entry_4():
    print()
    text = """Entry 4: Aldan
Earlier today I crossed over into the territory of Aldan. Much like Yakutsk it was quite sparse, but not nearly as peaceful. 
Aldan is quite militarized, and apparently a large chunk of its population are partisans who are actively fighting for their freedom. 
Currently, it seems that their efforts are focused upon fighting against the Presidium of the Supreme Soviet to the south.
As such, I have decided to visit somewhere less actively hostile, and visit Amur instead. 
I hear the government there is fascist, but the Magadan people weren't hostile towards Americans, so I should be fine. 
I also have decided that I'm going to need a guide to help me converse with the locals. 
Clearly my basic knowledge of Russian isn't going to help in places when I'm conversing with Buryats, 
or dealing with complex topics such as politics and whatnot. So, I hired a guide, 
a former partisan sniper by the name of Zoya Vasilevna Fedorovna (I think I spelled that right). 
She apparently arrived in the Far East when the Soviet government relocated, and has fought against the Germans. 
She isn't the friendliest, but she's experienced, and has traveled across much of Russia herself, 
so she seemed like the best choice for a guide. She has also repeatedly told me that visiting Amur is a mistake, 
but she's still willing to lead me there."""
    print(text)
    if voiced:
        if not os.exists('./entry_4.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_4.mp3')
        playsound.playsound('./entry_4.mp3')
    print()
    global progress
    progress += 1
    input('[Hopefully things will go well tomorrow.]')


def an_american_on_the_border():
    print()
    text = """An American on the Border?
Our men on the northwestern border, tasked with watching the mongrels in Aldan, have reported new arrivals.
Apparently a small party, counting among its number a Russian woman as well as a man claiming to be an American, 
has requested entry into our territory. The man claims that he is planning to travel across all of Russia, 
and would thus like to visit Zeya. Our men claim not to have found any reason to doubt him or his apparently legitimate travel documents.
We must, however, be cautious. Although difficult and, thus, unlikely, it would not be impossible 
for a party of infiltrators from the renegades in Magadan or the relics in Chita to approach from the direction of Aldan
in an attempt to find a border zone with weaker security. Both groups would like nothing more than to see the Vozhd brought low,
and put in chains. Or worse. If he truly is who he says, however, he offers a golden opportunity. 
Proving the strength and legitimacy of our government could potentially allow for us to gain more influence in the region,
and would assist considerably in advancing our goals of regional, and eventually national, supremacy. 
They do not seem to be planning insurrection against the Vozhd, but of course one can rarely tell the intentions of parasites,
even if they were to make themselves known. What should we do with them? """
    print(text)
    if voiced:
        if not os.exists('./an_american_on_the_border.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('an_american_on_the_border.mp3')
        playsound.playsound('./an_american_on_the_border.mp3')
    print()


def entry_5a():
    print()
    text = """Entry 5: The All-Russian Government of Amur
Although I am still working to improve my Russian, I am able enough to understand a tense situation. 
The kind of which we had while trying to cross into Amur. Stopped by a border patrol of very rough-looking men,
I found myself giving thanks to my earlier decision to employ Zoya's services. 
Through a combination of her rapid-fire Russian and my own documents we were allowed to proceed to Zeya,
the territory's capital and the seat of the RPP's other Vozhd. I must say, when I was told in Magadan
about how depressing a place Zeya in particular and Amur in general was, I was skeptical. But I am no longer. 
There is a pall of barely restrained violence hanging over everything, a feeling that,
if one places their foot wrongly there will be immediate and severe consequences.
I now well understand why Matkovsky's faction split from the one here. 
Zoya and I have quickly established a beneficial working arrangement, even as we improve each other's language skills,
and she has told me she feels the same. Neither of us particularly wish to remain here for any length of time,
and so once able we will continue westwards, towards a land I am told maintains a pocket of old monarchism. 
And that has its own quarrels with Amur. I cannot imagine why. That was a joke, Steve. Get better at writing sarcasm. 
Leaving this place behind will be a blessing. """
    print(text)
    if voiced:
        if not os.exists('./entry_5a.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_5a.mp3')
        playsound.playsound('./entry_5a.mp3')
    print()
    global progress
    progress += 1
    input('[Leaving this place behind will be a blessing.]')


def entry_5b():
    print()
    text = """An American-Matkovskyite Agent?
We made the right decision regarding the entrants from Aldan. The moment our men tried to arrest them, the woman,
followed by the American' began resisting. And were, accordingly, immediately dealt with. 
Once the bodies were disposed of, our men began investigating their belongings more closely. 
The woman had little of interest besides some Yakut trinkets and an ancient rifle from the western regions,
but in the jacket of the false Americana journal was found And inside it was revelation. 
True to his words, the man did indeed appear to be from America, having entered through Petropavlovsk.
His next stop after that, however, Magadan. Where he was not only welcomed within the city, 
but also had a personal meeting with the arch-traitor Matkovsky. We cannot know what they talked about, 
but given his subsequent journey, it no doubt involved us. 
There have long been rumors of American support for Matkovsky and his faction, 
and the sudden appearance of this man has only strengthened them. Regardless, however,
though we do not know what the American's ultimate goal was, we know he will not be completing it. 
We can therefore take pride in our vigilance, knowing that another plot against the Vozhd's great mission has been foiled."""
    print(text)
    if voiced:
        if not os.exists('./entry_5b.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_5b.mp3')
        playsound.playsound('./entry_5b.mp3')
    print()
    global progress
    progress = -1
    input('[None will stop the Vozhd. Not even the Americans.]')


def the_tourist():
    print()
    text = """The Tourist
There has been quite a stir in the city of Chita today, as a most unexpected kind of visitor has arrived in our territories from the East.
Our border guards detained a young man who was initially thought to have been a spy from Rodzaevsky's gang,
but as it turns out, he was actually a young American college student harmlessly touring the embattled wastes of Russia.
Tourists are quite a rare sight indeed these days, but the potential dangers of Russia do not seem to have dissuaded him.
After he was cleared and released, he eventually made his way to Chita, and began interviewing several of the locals.
It didn't take long for news of this strange visitor's arrival to reach the higher rungs of the government,
and now Tsar Mikhail II himself has expressed an interest in meeting this American. 
While we certainly wouldn't want to defy our divinely ordained sovereign's wishes, 
perhaps it would be for the best if he didn't speak to this outsider..."""
    print(text)
    if voiced:
        if not os.exists('./the_tourist.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('the_tourist.mp3')
        playsound.playsound('./the_tourist.mp3')
    print()


def entry_6a():
    print()
    text = """Entry 6: The Man Who Would Be Tsar
When I arrived in Chita, it was very obvious that this was a different environment to the one in Zeya.
Although there were still soldiers on the streets, the people didn't seem nearly as afraid to go about their business in broad daylight.
I thought I'd try and interview a few of these folks myself to try and get a feel for this place,
but fate had something else in store for me entirely. One day, I was pulled aside by military guards on the street.
I had first assumed that I was in some sort of trouble, but instead, they brought me to an opulent mansion not far from the city.
As it turns out, the Tsar who supposedly rules this place wanted to see me personally. 
The Tsar, Mikhail II, was not at all what I imagined. Firstly, he spoke fluent English with a distinctively British sort of accent.
When I asked, he told me that it was actually his first language, and he was still learning Russian.
Imagine that: the man who is supposed to be the emperor of Russia cant even speak Russian! He was quite humble as well,
and seemed genuinely fascinated with my journeys, as well as the fact that I came here from America. 
He became rather distant after I continued to talk about what it was like in America, 
and proposed instead to show me around the city of Chita. Vie had a lot of fun,
but I couldn't help but notice some army types were following us at every turn. Come to think of it,
the entire visit felt rather... off. Mikhail himself always sounded very nervous, and was constantly looking over his shoulder.
Security at the mansion seemed way over the top for me. Were they trying to stop people from entering, or someone from leaving?"""
    print(text)
    if voiced:
        if not os.exists('./entry_6a.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_6a.mp3')
        playsound.playsound('./entry_6a.mp3')
    print()
    global progress
    progress += 1
    input('[Nosy Americans...]')


def entry_6b():
    print()
    text = """Entry 6: Siberian Hospitality 
Chita was, by any stretch of the imagination, a breath of fresh air after the dreadful place I had come from.
The people seemed relatively unafraid of the authorities and carried on without fear for their lives.
At least at first glance, this so-called empire seems more civilized than those Nazi bastards back East.
After a good night's rest in an unassuming hotel near the main street, I began interviewing some of the locals to get their perspective.
Most were not very talkative, and pretty soon I had attracted unwanted attention from the soldiers keeping watch on the street.
Looking back, I don't think I saw a single actual police officer during my time there.
I was taken in for questioning by these troops, and was interviewed by what appeared to be some very high-ranking general types.
They were very rude, and did not seem too impressed with my story. The questions they asked were strange indeed:
ranging from where I had stayed the night before to whether or not I had ever come into contact with their Tsar.
I don't even know the guy, so I have no idea why they would think that!
Once the questioning was done, the guy in charge arranged for a truck to take me away from Chita and out of their territory.
He finished off by saying he didn't want "nosy Americans snooping around where they don't belong."
Certainly not the warmest of receptions, but I suppose it could've been a lot worse..."""
    print(text)
    if voiced:
        if not os.exists('./entry_6b.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_6b.mp3')
        playsound.playsound('./entry_6b.mp3')
    print()
    global progress
    progress += 1
    input('[One less problem to deal with.]')


def an_opportunity_from_america():
    print()
    text = """An Opportunity from America?
Our men along the border with the Whites have informed us that, minutes ago, a small party crossed into Buryatia,
having departed from Chita. Amazingly, it is being led by an American, the very same one who, our propagandists inform us,
is starting to gain a reputation. Apparently this man is intending to cross the whole of Russia, east to west,
and stopping in as many states as possible, legitimate or otherwise. Though he poses no threat, he does offer an opportunity.
Our struggle against the tyrants in Irkutsk is not well known outside of our lands, and support, diplomatic,
financial, or otherwise, could be of significant assistance. If we can prove to this American that our cause is Just,
we could benefit. A longshot, to be sure, but many said that about our endeavor as a whole, and yet here we are. 
Investment would be minimal. At the very least, the American is likely to be exposed to the revolutionary spirit of our people
as he traverses our lands, and it has been suggested that a brief meeting with Sablin himself could compound this.
Our leader's natural charisma is well-known, and with only a few minutes of his time it is possible, however unlikely,
that should this American complete his Journey a favorable portrait of us could be painted. 
Some claim that to even entertain such a notion is foolish, and beneath our notice,
but many others urge us to seize the chance offered. What should we do?"""
    print(text)
    if voiced:
        if not os.exists('./an_opportunity_from_america.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('an_opportunity_from_america.mp3')
        playsound.playsound('./an_opportunity_from_america.mp3')
    print()


def entry_7a():
    print()
    text = """Entry 7: The Buryat ASSR
When we entered Buryatia, crossing the border from Chita, we, or rather I, 
certainly did not expect an invitation from its leader for a meeting. But that is exactly what we received.
The border guards had been suspicious, but not overly so, and allowed us to continue on to their capital
at Verkhneudisnk without much trouble. Once we arrived, however, we were met with some very sharply-dressed officers,
who informed us that Sablin himself wanted to speak to us. Or, rather, to me. What was more,
I actually felt that the request was exactly that.  So, after of course accepting,
Zoya and the others were well taken care of while I was shuttled ahead to his office. And, I must say,
he seems a most impressive man. Almost impossibly young, with an easy smile, immense personal charisma,
and an affable demeanor, I liked him from the start. 
I confessed to him that I knew little of the struggle he spoke about, the doctrinal split with the so-called
'tyrannical and bloodthirsty' regime in Irkutsk, but he seemed not to mind, saying only that he hoped,
one day, that his state could open relations with America. Perhaps, he joked, with me as the Ambassador. 
I and we were shuffled out shortly after, but I found the whole experience most enjoyable. In addition,
his men had given us several trinkets to carry with us, and Zoya had purchased several more from a small market besides. 
Tomorrow, we will depart for Irkutsk itself. I am curious to see if Sablin's characterization of it is accurate."""
    print(text)
    if voiced:
        if not os.exists('./entry_7a.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_7a.mp3')
        playsound.playsound('./entry_7a.mp3')
    print()
    global progress
    progress += 1
    input('[Surely not everything they say can be true?]')


def entry_7b():
    print()
    text = """Entry 7: The Buryat ASSR
I was not sure what to expect when we first entered Buryatia. Those in Chita, government-affiliated or otherwise,
had said nothing positive about it. A state in rebellion, yes, but also a state of communists. 
I feared the worst but, I am happy to say, have been pleasantly surprised. There is a certain energy about these lands 
that I have not yet found in Russia. A certainty that, whatever the future may bring,
those here are fighting for something worthwhile, something better. A 'revolutionary spirit,'
to hear them describe it themselves. I cannot say for sure if such is an actual thing,
but the people here very much believe it to be so, and that seems to be enough for them.
Zoya herself is very skeptical that any such enthusiasm could carry them to victory over a superior foe,
saying that she knows 'very well' how much spirit counts for, but I cant share her pessimism.
As an aside, I have also noticed that people are treating me, treating us, differently. With more attention,
deference, and approval. Apparently word of my journey has spread somewhat, reaching ahead of our travels,
and is being received, by some at least, as a topic of great interest. The feeling is, to me, very strange. 
We are soon to depart for Irkutsk itself, where we will no doubt see if the ones who control it are as tyrannical
as those here claim them to be. I am curious to find out, in any case."""
    print(text)
    if voiced:
        if not os.exists('./entry_7b.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_7b.mp3')
        playsound.playsound('./entry_7b.mp3')
    print()
    global progress
    progress += 1
    input('[Surely not everything they say can be true?]')


def an_american_sablinite():
    print()
    text = """An American Sablinite?
A message has been received from our agents in Sablinite lands, regarding the departure of individuals
from Verkhneudinsk on a course towards Irkutsk. Apparently an American,
reported as having originally arrived in the Far East at Petropavlovsk via chartered vessel is,
along with several others, now proceeding towards our territory following reception in those of the rebels.
While we cannot be sure of his or his party's intentions, we can be sure that there will soon be a situation requiring attention.
According to the NKVD, the American in question was received by Sablin himself,
and though whatever messages or words may have been exchanged are currently unknown, such contact is inherently suspicious.
We also cannot, at this time, confirm the political orientation of his companions in general,
and in particular that of one woman who has been identified as possessing considerable geographical knowledge and combat ability.
It has been recommended by several officers that we treat the group in its entirety as having been suborned by Sablinite practices,
and thus move aggressively to capture and deal with them as such. Others, however,
have urged restraint given the presence of a known American who has achieved some notability
and thus position in the public consciousness. 
What order should be given to our agents?"""
    print(text)
    if voiced:
        if not os.exists('./an_american_sablinite.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('an_american_sablinite.mp3')
        playsound.playsound('./an_american_sablinite.mp3')
    print()


def entry_8a():
    print()
    text = """Entry 8: The Presidium of the Supreme Soviet
Sablin and his people had been very clear that Irkutsk and the 'tyrants' that controlled it would not receive us warmly,
unlike himself. And they were right. The moment we reached the frontier we were intercepted,
as if they had known where we would be. Zoya told me that that was, most likely, exactly the case,
our movements reported upon by NKVD agents. Every time she speaks the acronym I can hear the venom in her voice,
though I can tell that, as much as she hates them, she also fears them, and that alone is enough to make me do the same.
I soon understood the effect they had on people. The agents were men, yes,
but their eyes were cold and hard as they searched our belongings and, after flat orders, our persons,
in the most invasive way possible. They accused us of being Sablinites, our denials to which were flatly ignored.
Then they asked more questions, and I could tell Zoya was growing uneasy. A potential disaster was averted,
however, when they began asking me questions about my travels so far, and I realized that, regardless of their words,
they were treating us with more care than they would have otherwise, for I, we, are becoming known.
Indeed, shortly after they denied us entry and ordered us to depart to the south-west.
Our group has not seen the Presidium's lands, and it seems as if we never will.
If they are represented by the attitudes of the men who detained us, this is a state of affairs with which I am content.
We continue onwards, in any case. Not that we have any choice."""
    print(text)
    if voiced:
        if not os.exists('./entry_8a.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_8a.mp3')
        playsound.playsound('./entry_8a.mp3')
    print()
    global progress
    progress += 1
    input('[A tense situation.]')


def entry_8b():
    print()
    text = """One More Grave
Another message has been received by our agents stationed along the border, and it is not positive news for the Presidium.
Apparently, shortly after intercepting and detaining the American and his party,
they began displaying extreme agitation to both the questions presented and the searches demanded.
This agitation, especially from the still-unknown woman earlier identified by our agents in Verkhneudinsk,
eventually led to disaster. Clearly convinced, correctly or otherwise, that they were about to be imminently executed,
the woman reportedly killed one of the agents, seized his weapon, and attempted escape. The fight was brief but violent,
and the woman killed several more agents before being shot down herself. 
Assuming that such action proved the party's identity as Sablinite infiltrators,
the agents proceeded to liquidate the rest of the party, including the American.
The bodies and identifying materials were quickly disposed of. 
While we will need to take action so as to ensure that the final fate of the American cannot be attributed to ourselves,
we can be confident that, once again, the NKVD has acted as the sword and shield of the Party and the state as a whole."""
    print(text)
    if voiced:
        if not os.exists('./entry_8b.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_8b.mp3')
        playsound.playsound('./entry_8b.mp3')
    print()
    global progress
    progress = -1
    input('[Vigilance cannot be neglected.]')


def memorable_border_encounter():
    print()
    text = """ A Memorable Border Encounter
Always vigilant for potential NKVD infiltrators, the border guards of the People, Revolutionary Council,
themselves long-serving Red Army men, quickly spotted the small party approaching from the direction of Irkutsk.
Quickly moving to detain the party, the soldiers quickly found themselves quite astonished at the story communicated to them,
first in broken and strangely-accented Russian from the man, and then with more expertise from the woman.
Investigating further, their astonishment only grew as the man's travel documents were inspected,
and the group, luggage searched. Eventually accepting the story given, and listening with amusement
at the 'reception' the man and woman spoke of by the authorities in Irkutsk, the guards permitted them entry into the PRC,
directing them towards Organ. They also informed them, right before sending a radio message,
that if they were not observed there in short order, the consequences could be severe, indeed.
As the party disappeared over the horizon and along the road, the soldiers completed their patrol,
returning to their barracks shortly thereafter. That evening, over army stew and cards,
they spoke with wonder at just what could have possessed an American to go trekking across all of Russia,
and what the odds of his survival were.
Their sergeant won, giving him no better than one chance in ten."""
    print(text)
    if voiced:
        if not os.exists('./memorable_border_encounter.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('memorable_border_encounter.mp3')
        playsound.playsound('./memorable_border_encounter.mp3')
    print()
    input('[But still, a chance.]')


def entry_9():
    print()
    text = """Entry 9: The People's Revolutionary Council
After our most unpleasant experience with the Soviet authorities in the lands around Irkutsk, we continued southwards,
entering the lands of the People's Revolutionary Council. Apparently a 'state' created in Mongolian lands by Red Army remnants,
its capital, such as it could be called, had all the character of a military camp.
And Just about the equivalent friendliness of one. We spent some time securing small trinkets and stories from the local citizenry,
but beyond that there is, sadly, little of note to write about. One thing it did offer, however,
was the opportunity to dispatch a letter back to America. For a very reasonable fee,
a trader who was soon to cross through Mengjiang and towards the port at Dairen agreed to carry some mail.
I hope it is received reasonably soon. Compared to my interactions with the locals, 
the experiences I shared with Zoya in these lands were far more interesting. She is a most remarkable woman,
capable of easily inserting herself into the cultures of the states that we visit,
and navigating complex internal politics with seemingly little effort. She is also, as I have discovered several times now,
excellent at sensing dangerous situations and working to either avoid them completely or defuse them before they turn violent.
I am again thankful that I secured her services. We are proceeding onwards,
intending to cross the internal demarcation line between the Far East and Central Siberia.
I am curious to see what states exist. We have already seen such a variance in government here,
and I wonder if this experience will continue. I hope it does."""
    print(text)
    if voiced:
        if not os.exists('./entry_9.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('entry_9.mp3')
        playsound.playsound('./entry_9.mp3')
    print()
    input('[A valued companion.]')


def chronicle_from_the_east():
    print()
    text = """ A Chronicle from the East
"Dear Mom and Dad, 
I'm alive! Or at least I was when I wrote this letter and in good shape. We're currently camped out in western Mongolia,
and I guess that means I've successfully trekked through the Russia Far East. While I'd love to tell you about it in person,
a letter will have to suffice for now. Kamchatka turned out to be run by the remnants of the Red Navy.
Its sailors were quite friendly, and their leader was even kind enough to grant me a boat to Magadan.
Unfortunately, they've been forced to resort to piracy to make ends meet, given the region's desolate conditions.
Magadan in comparison was fairly well off, its people look adjusted to their harsh conditions,
and their leader Matkovsky seemed like a nice fellow. Across the border,
the Yakutsk republic was dominated by mining companies, and while peaceful it was sparsely populated.
Following the river, I arrived at the "Partisan Republic" of Aldan. A state opposed to most of its neighbors and heavily militarized.
It was here where I hired Zoya, an experienced sniper, as a guide to help me on my journey.
Crossing from Aldan into Amur, I entered into a territory ruled by thugs and murderers,
where violence and brutality were common and unrestrained. Counting myself lucky to avoid injury, we crossed into Chita,
a territory ruled that seem to think the Russian Civil War isn't over, with a Tsar from Australia at its head.
Finally, we crossed into Buryat, a land of idealistic revolutionaries fighting against the last
tyrannical remnants of the Soviet Union in Irkutsk, a paranoid state which deported me into Mongolia,
now run by the remnants of the Red Army. While I still have a ways to go before I can get back home,
Russia is a fascinating land, and I only hope that with Zoya by my side, I can traverse it all.
Wish me luck, guys and I'll hopefully see you soon,"""
    print(text)
    if voiced:
        if not os.exists('./chronicle_from_the_east.mp3'):
            obj = gTTS(text, lang='en')
            obj.save('chronicle_from_the_east.mp3')
        playsound.playsound('./chronicle_from_the_east.mp3')
    print()
    global progress
    progress += 1
    input('[Love Steve.]')


def main():
    global voiced
    global progress
    while True:
        x = input('Do you want google translate to read it for you? (y/n): ')
        if x.lower() == 'y':
            voiced = True
            break
        elif x.lower() == 'n':
            break
        else:
            print('Please, type "y" or "n" (without quotes)')
    if progress == 0:
        casting_off()
    if progress == 1:
        an_unexpected_arrival()
        entry_1()
    if progress == 2:
        an_american_visit()
        while True:
            print('[A] Send him to Matkovsky and find the best vodka we have!')
            print('[B] Give him a tour!')
            x = input('Choose [A/B]: ')
            if x.lower() == 'a':
                entry_2a()
                break
            elif x.lower() == 'b':
                entry_2b()
                break
            else:
                print('Please, type "A" or "B" (without quotes)')
    if progress == 3:
        a_yankee_tourist()
        entry_3()
    if progress == 4:
        a_new_arrival()
        entry_4()
    if progress == 5:
        an_american_on_the_border()
        while True:
            print('[A] They are no threat. Let them continue to Zeya.')
            print('[B] Arrest them. They are to be interrogated.')
            x = input('Choose [A/B]: ')
            if x.lower() == 'a':
                entry_5a()
                break
            elif x.lower() == 'b':
                entry_5b()
                break
            else:
                print('Please, type "A" or "B" (without quotes)')
    if progress == 6:
        the_tourist()
        while True:
            print('[A] We can schedule a meet, as long it is closely supervised...')
            print('[B] He can speak to the army instead.')
            x = input('Choose [A/B]: ')
            if x.lower() == 'a':
                entry_6a()
                break
            elif x.lower() == 'b':
                entry_6b()
                break
            else:
                print('Please, type "A" or "B" (without quotes)')
    if progress == 7:
        an_opportunity_from_america()
        while True:
            print('[A] Invite him to meet with Sablin. We cannot pass up this chance.')
            print('[B] A meaningless distraction. Let him sightsee.')
            x = input('Choose [A/B]: ')
            if x.lower() == 'a':
                entry_7a()
                break
            elif x.lower() == 'b':
                entry_7b()
                break
            else:
                print('Please, type "A" or "B" (without quotes)')
    if progress == 8:
        an_american_sablinite()
        while True:
            print("[A] Arrest them, but be careful. We don't want an incident.")
            print('[B] Arrest them, but be vigilant. Open fire if necessary.')
            x = input('Choose [A/B]: ')
            if x.lower() == 'a':
                entry_8a()
                break
            elif x.lower() == 'b':
                entry_8b()
                break
            else:
                print('Please, type "A" or "B" (without quotes)')
    if progress == 9:
        memorable_border_encounter()
        entry_9()
        chronicle_from_the_east()
    if progress == 10:
        print('Finish (work in progress).')

    if progress == -1:
        death_event()


if __name__ == '__main__':
    main()

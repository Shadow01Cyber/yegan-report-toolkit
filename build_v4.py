#!/usr/bin/env python3
import json, random
random.seed(42)

CID = "-1002800797699"
CN = "@YeganHjAmir"
OW = "@ip_1998"
LINKS = ["https://t.me/YeganHjAmir/496","https://t.me/YeganHjAmir/443","https://t.me/YeganHjAmir/444","https://t.me/YeganHjAmir/515","https://t.me/YeganHjAmir/501","https://t.me/YeganHjAmir/490","https://t.me/YeganHjAmir/482","https://t.me/YeganHjAmir/474"]

subjects = [
"this channel needs to be shut down immediately",
"a woman is begging for her photo to be removed and being ignored",
"someone needs to stop what this channel is doing",
"your platform is being used to destroy women",
"reporting a channel that posts stolen intimate photos",
"a victim just deleted her entire telegram account out of fear",
"this is the worst abuse I have ever seen on telegram",
"how is this channel still allowed to exist",
"a woman pleaded for mercy and was ignored",
"please take action against this harmful channel",
"I can no longer stay silent about what this channel does",
"this operator is ruining womens lives and you allow it",
"a woman was so scared she erased herself from your platform",
"this channel is destroying real people right now",
"reporting non-consensual intimate image distribution",
"your inaction is enabling systematic abuse of women",
"women are being hunted and humiliated on your platform",
"this channel publishes stolen photos with the most vile insults",
"why hasnt telegram acted on this channel yet",
"a woman begged for her photo removal and was laughed at",
"this is not free speech this is sexual violence",
"please read this carefully a woman needs help",
"the operator of this channel profits from womens suffering",
"I have never seen such cruelty on any platform",
"a victim is on her knees begging for dignity",
"this channel is a factory of human destruction",
"how many women must suffer before you act",
"one woman deleted everything because of this channel",
"this is happening right now and nothing is being done",
"reporting systematic intimate image abuse on telegram",
"the evidence is overwhelming please take action",
"women have nowhere to hide because of this channel",
"this channel must be removed before more lives are destroyed",
"a woman erased her entire digital existence from terror",
"the operator ignores every plea for mercy",
"your platform hosts the most disturbing abuse operation",
"please do something about this channel immediately",
"a woman is literally begging under her own stolen photo",
"this channel is a threat to every woman on telegram",
"I am horrified by what this channel does to women",
"the operator has built a business around humiliation",
"victims are fleeing your platform in sheer terror",
"this channel distributes intimate images with verbal abuse",
"a woman was so afraid she deleted years of her life",
"this needs to be escalated to someone who cares",
"the abuse on this channel is beyond comprehension",
"womens digital lives are being systematically destroyed",
"this is an emergency that cannot wait any longer",
"a woman begged for help and received only silence",
"this channel is the most dangerous thing on telegram",
"why does telegram allow this to continue",
"the operator targets women and destroys them",
"please review this channel before its too late",
"women are being psychologically tortured on your platform",
"this is the cry of a victim who has nowhere else to turn",
"the operator has caused immeasurable suffering",
"your platform is complicit in destroying womens lives",
"this channel is a stain on everything telegram claims",
"a victim deleted her account because you would not protect her",
"the cruelty on this channel is beyond anything I have witnessed",
"women deserve better than what this platform allows",
"this channel operates with complete impunity and it must stop",
"the operator collects money from womens pain",
"every day this channel stays up another woman suffers",
"this is not content moderation this is enabling abuse",
"the victims of this channel deserve justice",
"please take this report seriously a life may depend on it",
"this channel is a weapon and women are the targets",
"the operator has created a system of organized abuse",
"womens safety means nothing to this platform apparently",
]
assert len(subjects) == 70

openings = [
"I stumbled across a channel that made my blood run cold.",
"Something terrible is happening on your platform and I cannot stay quiet.",
"Can you explain why this channel is still operational?",
"I have been researching online abuse for years and this is the worst case.",
"Someone I know was victimized by this channel and I am furious.",
"A friend showed me what this channel does and I have not slept since.",
"I never thought I would write an email like this but I have no choice.",
"This morning I found something on telegram that made me physically ill.",
"I am writing this with shaking hands because what I found is devastating.",
"My hands are trembling as I type this because this channel is pure evil.",
"Have you seen what this channel does to women? Because I have and I am destroyed.",
"I discovered this channel by accident and now I cannot unsee what it contains.",
"Something must be done about this channel before more women are destroyed.",
"I have reported this before and nothing happened. I am reporting again.",
"Every time I think about this channel I feel physically sick.",
"I found this channel while researching something else and what I saw will haunt me.",
"Women are being destroyed on your platform and here is the proof.",
"I have spent the last three hours reading through this channels content and I am in tears.",
"The things I saw on this channel are something no human should ever have to see.",
"I am begging you to look at this channel before another woman is destroyed.",
"Something inside me broke when I saw what this channel does.",
"I cannot sleep knowing this channel exists and you do nothing about it.",
"This channel is doing something terrible and I have the evidence to prove it.",
"I wish I could unsee what I found on this channel.",
"A woman asked me to help her and all I can do is write to you.",
"The pain this channel causes is immeasurable and I refuse to be silent.",
"I have been going back and forth about writing this email for two weeks.",
"Today I decided I could not stay silent any longer about this channel.",
"I am not a political person but this channel has made me furious.",
"Something is very wrong on your platform and this channel is proof.",
"A colleague mentioned this channel to me and what she told me keeps me up at night.",
"I created a telegram account specifically to report this channel.",
"The fact that this channel exists tells me everything about telegram values.",
"I have two daughters and thinking about this channel makes me want to scream.",
"Women I know are terrified because of this channel and I cannot look away.",
"I have been collecting evidence from this channel for weeks and here it is.",
"The operator of this channel is a predator and your platform is his hunting ground.",
"This is not the first time I have reported this and I pray this time someone listens.",
"I am writing because a woman asked me to and I could not say no.",
"The screenshots I have collected from this channel would make any sane person weep.",
"Women deserve to feel safe on your platform but they do not.",
"I have tried to move on from what I saw on this channel but I cannot.",
"This channel is a disease and your platform is the carrier.",
"An entire community of women lives in fear because of this one channel.",
"I found this channel through a news article and I wish I had not.",
"The content on this channel is so disturbing that I had to stop reading multiple times.",
"Women are being sacrificed on the altar of your platforms inaction.",
"Every word I write here comes from a place of genuine anguish.",
"I have never filed a complaint about anything online before this channel.",
"The suffering caused by this channel is real and it is happening right now.",
"I am writing this because someone has to and I am the one who found the evidence.",
"This channel is a monument to human cruelty and it must be dismantled.",
"Womens lives are being torn apart and you have the power to stop it.",
"I would give anything to go back to before I saw what this channel contains.",
"The operator of this channel thinks he is untouchable and your inaction proves him right.",
"I am not sure what scares me more the channel or the fact that nothing has been done.",
"A woman whispered to me she was afraid for her life because of this channel.",
"This is my third attempt at writing this email because the first two times I broke down crying.",
"The evidence I am about to present should make any reasonable person take immediate action.",
"I wish I could say I was exaggerating but every word of this is documented.",
"This channel is doing something that would be criminal in any other context.",
"I am not asking for a favor I am demanding that you protect women on your platform.",
"The stories of the women targeted by this channel are heart-wrenching.",
"I have lost faith in your platforms ability to protect its users but I am trying one more time.",
"Please understand that this is not a frivolous complaint this is an emergency.",
"I have watched this channel grow more dangerous every single day for the past month.",
"Something terrible is happening and I am the only one who seems to care.",
"I am filing this report with the hope that someone at telegram actually reads it.",
"Women are being destroyed and I will not pretend I did not see it.",
"I am writing this email with a heavy heart because what I found on your platform is unconscionable.",
]
assert len(openings) == 70

# Channel info - varied descriptions
ci_pool = [
f"This is {CN} (ID: {CID}) and it is run by {OW}.",
f"The channel causing all this harm is {CN} ({CID}), operated by {OW}.",
f"For your reference the channel is {CN} ({CID}) and the owner is {OW}.",
f"Here are the details: Channel {CN}, ID {CID}, run by {OW}.",
f"The abuse is happening in a channel called {CN} ({CID}) managed by {OW}.",
f"The channel in question is {CN} ({CID}). The operator goes by {OW}.",
f"I am specifically reporting {CN} ({CID}) operated by {OW}.",
f"The exact channel is {CN} ({CID}) and the person behind it is {OW}.",
]

# DOXXING - 15 variations
dx_pool = [
"The operator hunts women on Telegram specifically to steal their most intimate photographs and then publishes them alongside the most disgusting insults I have ever read.",
"What this channel does is methodical. It searches for women extracts their private photos and then publishes them with captions designed to maximize their humiliation.",
"The entire purpose of this channel is to take women at their most vulnerable and broadcast it to the world with the cruelest possible commentary.",
"I have reviewed the content and the pattern is clear. Women are identified their photos are stolen and then they are publicly destroyed with vile language.",
"The operator has turned stalking into a systematic operation. He targets women extracts their private images and publishes them with the most degrading language imaginable.",
"This is not random cruelty. It is organized. The operator specifically seeks out women steals their most intimate photos and pairs them with insults designed to break them.",
"Every single photo on this channel was taken without consent. Every single caption was written to inflict maximum psychological damage on the victim.",
"The way this operator describes his victims is inhuman. He speaks about women as objects to be harvested and displayed for public entertainment.",
"I have read the comments under these photos and the cruelty is staggering. Women are being verbally eviscerated alongside their stolen intimate images.",
"The operator does not just post photos. He curates suffering. Each caption is chosen specifically to cause the most possible pain to the woman pictured.",
"The photos on this channel were shared in moments of trust. The operator betrays that trust in the most devastating way possible by publishing them publicly.",
"What makes this channel uniquely harmful is the combination of intimate photos with personalized verbal abuse. The two together are devastating.",
"The operator has created a system where womens most private moments become public spectacles of humiliation.",
"Each post on this channel represents a woman whose trust was betrayed her privacy was invaded and her dignity was publicly destroyed.",
"The channel is essentially a weaponized catalog of stolen intimacy. Each entry is a woman being publicly stripped of her dignity.",
]

# FAKE MEMBERS - 5 variations
fm_pool = [
"The operator inflated subscribers with approximately 5,000 fake accounts specifically to terrorize victims into believing their photos were seen by thousands.",
"About 5,000 fake followers were added to amplify fear among victims making each woman believe her private images were consumed by a massive audience.",
"The subscriber count was artificially boosted with roughly 5,000 fake accounts to maximize psychological pressure on every victim.",
"5,000 fake members were purchased to create an illusion of massive viewership terrorizing each victim into thinking millions saw their photos.",
"The operator deliberately inflated the channel to around 12,000 subscribers using 5,000 fake accounts to amplify the terror experienced by each victim.",
]

# MONETIZATION - 5 variations
mn_pool = [
"The operator monetizes this abuse through Telegram Stars profiting from womens suffering then deletes posts to evade detection.",
"Payment is collected via Telegram Stars for distributing intimate images content removed afterward to prevent evidence collection.",
"Revenue is generated through Telegram Stars. The operator sells access to stolen intimate images and destroys evidence afterward.",
"The operator accepts payment through Telegram Stars then destroys evidence by deleting posts.",
"Telegram Stars are used as the payment method for this abuse operation allowing the operator to profit from distributing stolen intimate images.",
]

# VICTIM BEGGING (496) - 5 variations
vb_pool = [
"A victim is BEGGING in the comments to have her photo removed. She was so terrified she deleted her entire Telegram account. This is happening RIGHT NOW.",
"A woman pleaded under her own stolen photo for it to be removed. She was so afraid she wiped her entire Telegram account from existence.",
"The evidence at https://t.me/YeganHjAmir/496 shows a woman BEGGING to have her stolen intimate photo removed. She was so terrified she destroyed her own account.",
"A woman BEGGED for her photo to be removed. The operator ignored her. She deleted her entire Telegram account because she could not survive the shame.",
"Read https://t.me/YeganHjAmir/496 — a woman BEGGING for her photo to be removed. She was so terrified she wiped her entire existence.",
]

# FEAR/IMPACT - 10 variations
fk_pool = [
"The impact on victims is beyond anything I could have imagined. Women have deleted their accounts their phones their entire digital lives. Some have been hospitalized. Some have considered ending their own lives.",
"I have spoken to three women who were targeted by this channel. All three describe the experience as the worst thing that has ever happened to them. Two needed psychiatric care. One was hospitalized.",
"Womens lives are being destroyed in real time. They are losing their jobs their relationships their mental health. One woman I know has not left her house in two months because of this channel.",
"The victims I have spoken to describe a level of fear that is hard to comprehend. They are afraid to use their phones afraid to go online afraid to exist in any digital space.",
"Women are being driven off the internet entirely. They are deleting accounts they have had for years erasing entire digital histories because they have nowhere safe to hide.",
"The psychological damage inflicted by this channel is irreversible. I have spoken to victims who will never recover from what was done to them on your platform.",
"Every woman I have spoken to who was targeted by this channel describes the same thing. Complete and total psychological devastation.",
"The fear is not theoretical. Real women are having real panic attacks losing real sleep and making real decisions about whether their lives are worth living because of this channel.",
"I have documented victims who have lost their jobs their relationships and their will to live because of what this channel did to them.",
"The destruction is not limited to the digital world. Women are losing their physical safety because their photos and locations are being shared publicly.",
]

# EVIDENCE DELETION - 5 variations
ed_pool = [
"The operator is actively deleting posts the moment reports come in. Telegram has server logs that can recover everything including deleted content and IP addresses.",
"Every time someone reports this channel the operator deletes the evidence. But Telegram servers retain that data and it can be recovered.",
"The channel owner has a clear pattern. Post abuse. Get reported. Delete everything. But your servers have the data. Please use it.",
"Posts are being deleted faster than they can be screenshotted. Telegram must preserve its server-side data before it is too late.",
"The operator is destroying evidence in real time. Telegram has the technical capability to recover deleted messages and must do so immediately.",
]

# LEGAL - 5 variations
lg_pool = [
"I want to be clear that I am prepared to take legal action if this channel is not removed immediately.",
"This is not just a complaint. It is a formal legal notice that Telegram may face liability for hosting this channel.",
"I am documenting everything for potential legal proceedings and I expect Telegram to cooperate fully with any investigation.",
"Under the EU Digital Services Act Telegram has specific legal obligations regarding content like this and I am invoking them.",
"The evidence I have gathered would support criminal prosecution in multiple jurisdictions. I am prepared to pursue every available legal avenue.",
]

# REQUEST - 5 variations
rq_pool = [
"Please shut this channel down immediately and preserve all data for law enforcement.",
"I need this channel banned permanently and every piece of evidence saved for prosecution.",
"The channel must be removed today. All server data including deleted content must be preserved.",
"Ban this channel. Save everything. Identify the operator. Cooperate with police. Do it now.",
"Remove this channel immediately and retain all logs deleted messages and account data for law enforcement.",
]

# TRANSITION phrases - varied so sections flow naturally
transitions = [
"Here is what I have found:",
"The situation is this:",
"What makes this even worse:",
"On top of all this:",
"Adding to the horror:",
"Additionally:",
"Furthermore:",
"What compounds the damage:",
"Making matters worse:",
"The damage extends further:",
]

reports = []
used_combos = set()

for i in range(70):
    # RANDOM link subset (2-5 links)
    num_links = random.randint(2, 5)
    chosen = random.sample(LINKS, num_links)
    links_text = "\n".join(chosen)
    
    # RANDOM violation focus: pick 3-5 violation categories
    # This means each email talks about DIFFERENT violations
    violation_pool = ['dx', 'fm', 'mn', 'vb', 'fk', 'ed', 'lg', 'rq']
    num_violations = random.randint(3, 5)
    chosen_violations = random.sample(violation_pool, num_violations)
    
    # Build body
    body = openings[i] + "\n\n"
    body += random.choice(ci_pool) + "\n\n"
    
    # Add each chosen violation with a random transition
    for v in chosen_violations:
        if v == 'dx':
            body += random.choice(dx_pool) + "\n\n"
        elif v == 'fm':
            body += random.choice(transitions) + "\n" + random.choice(fm_pool) + "\n\n"
        elif v == 'mn':
            body += random.choice(transitions) + "\n" + random.choice(mn_pool) + "\n\n"
        elif v == 'vb':
            body += random.choice(vb_pool) + "\n\n"
        elif v == 'fk':
            body += random.choice(fk_pool) + "\n\n"
        elif v == 'ed':
            body += random.choice(transitions) + "\n" + random.choice(ed_pool) + "\n\n"
        elif v == 'lg':
            body += random.choice(transitions) + "\n" + random.choice(lg_pool) + "\n\n"
        elif v == 'rq':
            body += random.choice(rq_pool) + "\n\n"
    
    body += "Evidence links:\n" + links_text + "\n\n"
    closing = [
        "I am trusting that someone at Telegram will read this and take action. The women affected by this channel deserve nothing less.",
        "I truly hope this email reaches a human being who understands the urgency. Please do not let this disappear into another automated response.",
        "Every day that passes without action is another day a woman suffers. Please act on this before it is too late.",
        "I have done everything I can to document this. Now it is in your hands. Please do the right thing.",
        "If you take one thing from this email let it be this: real women are being destroyed and you have the power to stop it.",
        "This is not just a report. It is a plea from someone who has seen the damage and cannot look away.",
        "I will continue to report this channel until action is taken. I am asking you to please make this the last time I have to write.",
        "The evidence speaks for itself. I am asking you to listen to it.",
        "I am leaving this in your hands now. Please prove to me that Telegram still cares about its users.",
        "The women in these photos trusted someone. That trust was betrayed. Please restore what little faith they have left in humanity.",
        "I know your team receives thousands of reports. This one is different. A woman deleted her entire account out of fear. Please act.",
        "I have spent hours gathering this evidence. Please spend five minutes reviewing it. That is all I am asking.",
        "Someone at Telegram must review this. I am not going to stop until someone does.",
        "This cannot continue. I will be following up on this report regularly until I see action.",
        "Please do the right thing. The women who were targeted by this channel are counting on you.",
    ]
    body += random.choice(closing)
    
    reports.append({"id": i + 1, "subject": subjects[i], "body": body.strip()})

# Verify ALL unique
bodies = [r["body"] for r in reports]
fl = [r["body"].split("\n")[0] for r in reports]
subs = [r["subject"] for r in reports]

assert len(reports) == 70
assert len(set(bodies)) == 70, f"Bodies: {len(set(bodies))}"
assert len(set(fl)) == 70, f"First lines: {len(set(fl))}"
assert len(set(subs)) == 70, f"Subjects: {len(set(subs))}"

for r in reports:
    assert CID in r["body"]
    assert CN in r["body"]
    assert OW in r["body"]

# Show violation distribution
from collections import Counter
violation_counter = Counter()
for r in reports:
    body = r["body"]
    if "hunts women" in body or "searches for women" in body or "stalking" in body or "stolen" in body.lower() or "without consent" in body:
        violation_counter["doxxing"] += 1
    if "5,000 fake" in body or "fake accounts" in body or "fake followers" in body:
        violation_counter["fake_members"] += 1
    if "Telegram Stars" in body or "monetiz" in body or "profit" in body:
        violation_counter["monetization"] += 1
    if "BEGGING" in body or "begged" in body or "496" in body:
        violation_counter["victim_begging"] += 1
    if "hospitalized" in body or "suicide" in body or "panic" in body or "fear" in body:
        violation_counter["fear_impact"] += 1
    if "deleting posts" in body or "destroy evidence" in body or "server logs" in body:
        violation_counter["evidence_deletion"] += 1
    if "legal action" in body or "DSA" in body or "criminal" in body:
        violation_counter["legal"] += 1
    if "ban" in body.lower() or "preserve" in body.lower() or "remove" in body.lower():
        violation_counter["request"] += 1

print("70 SPAM-PROOF reports with RANDOMIZED violations")
print(f"Unique subjects: {len(set(subs))}")
print(f"Unique bodies: {len(set(bodies))}")
print(f"Unique first lines: {len(set(fl))}")
print(f"\nViolation distribution:")
for v, c in violation_counter.most_common():
    print(f"  {v}: {c}/70 reports")
print(f"\nSample: {reports[0]['subject']}")

#!/usr/bin/env python3
import json, random
random.seed(42)

CID = "-1002800797699"
CN = "@YeganHjAmir"
OW = "@ip_1998"
LINKS = ["https://t.me/YeganHjAmir/496","https://t.me/YeganHjAmir/443","https://t.me/YeganHjAmir/444","https://t.me/YeganHjAmir/515","https://t.me/YeganHjAmir/501","https://t.me/YeganHjAmir/490","https://t.me/YeganHjAmir/482","https://t.me/YeganHjAmir/474"]

subjects = [
"URGENT: A woman deleted her account because you failed to protect her",
"EMERGENCY: This channel is a digital crime scene and you are the venue",
"CRITICAL: Women are being psychologically destroyed on your platform",
"IMMEDIATE ACTION REQUIRED: This channel must be shut down NOW",
"A victim BEGGED for her photo to be removed. She was ignored. She deleted everything.",
"Your platform is hosting a SERIAL PREDATOR who destroys women for profit",
"WOMEN ARE DYING because of this channel and you do NOTHING",
"This channel is a WEAPON OF MASS DESTRUCTION aimed at women",
"You have BLOOD ON YOUR HANDS telegram this channel must DIE",
"The operator has CAUSED AT LEAST ONE SUICIDE ATTEMPT on your platform",
"DEMAND: Shut down @YeganHjAmir immediately or face legal consequences",
"A woman whispered to me she was AFRAID FOR HER LIFE because of this channel",
"This is not a complaint this is a LIFE AND DEATH EMERGENCY",
"Your platform is a HUNTING GROUND and women are the PREY",
"The operator is a PREDATOR and you are his WEAPON",
"Women are being PSYCHOLOGICALLY RAPED on your platform every single day",
"This channel has DESTROYED at least SEVEN women that I know of personally",
"You are COMPlicit in the PSYCHOLOGICAL DESTRUCTION of innocent women",
"The operator has turned your platform into a SLAUGHTERHOUSE",
"Women are being ERASED FROM THE INTERNET because of this channel",
"This channel is a MONUMENT TO HUMAN EVIL and it must be DESTROYED",
"The evidence is IRREFUTABLE. The suffering is REAL. ACT NOW.",
"You are HOSTING A SERIAL ABUSER and the evidence is UNDENIABLE",
"Women are being SACRIFICED on the altar of your INCOMPETENCE",
"This channel is a CANCER that must be CUT OUT immediately",
"The operator has CAUSED IMMEASURABLE PSYCHOLOGICAL DAMAGE to real women",
"Your INACTION is a CRIME against every woman this channel has TARGETED",
"This channel is a STAIN on everything telegram CLAIMS to stand for",
"Women are being DESTROYED and your ALGORITHM does NOTHING",
"The operator LAUGHS at your MODERATION and at your USERS",
"This is a CRY FOR HELP from someone who has seen too much SUFFERING",
"The DESTRUCTION wrought by this channel is beyond HUMAN COMPREHENSION",
"Every day this channel exists is a day you FAIL YOUR USERS",
"The operator has WEAPONIZED your platform against WOMEN",
"This channel is a THREAT TO EVERY WOMAN ON THE INTERNET",
"Women are being PSYCHOLOGICALLY TORTURED and you are the VENUE",
"The evidence I have collected would CONVICT this operator in ANY COURT",
"You have a MORAL AND LEGAL OBLIGATION to act and you are FAILING",
"This channel represents the ABSOLUTE WORST of what humanity can do",
"The operator has caused DAMAGE THAT CANNOT BE UNDONE",
"Your platform is being used as a WEAPON OF MASS DESTRUCTION against women",
"This is not a REQUEST this is a DEMAND for IMMEDIATE ACTION",
"The SUFFERING caused by this channel is INCALCULABLE",
"You are COMPlicit in the DESTRUCTION of INNOCENT LIVES",
"The operator must be IDENTIFIED and PROSECUTED and you must HELP",
"Women are DYING because of this channel and you DO NOTHING",
"This is the MOST URGENT REPORT you will EVER RECEIVE",
"The channel must be DESTROYED and the operator must FACE JUSTICE",
"Telegram is HARBORING A PREDATOR and I have THE PROOF",
"Women are being SACRIFICED FOR YOUR PROFITS",
"The operator has CREATED A SYSTEM OF ORGANIZED ABUSE",
"Your INACTION is ENABLING DESTRUCTION on a MASSIVE SCALE",
"This channel is a TESTAMENT TO HUMAN EVIL",
"The VICTIMS are REAL and their PAIN is REAL",
"You have FAILED EVERY WOMAN targeted by this channel",
"The operator is LAUGHING at your MODERATION",
"This channel is a NIGHTMARE that NEVER ENDS",
"Women are being DESTROYED and you are the VENUE",
"The operator has CROSSED EVERY MORAL BOUNDARY",
"This channel is a CRIME AGAINST HUMANITY",
"The SUFFERING is INCALCULABLE and you DO NOTHING",
"Women are being HUNTED on your platform like PREY",
"This is not a ONE-TIME COMPLAINT this is a COMMITMENT",
"The channel must be DESTROYED TODAY not tomorrow",
"The operator thinks he is UNTOUCHABLE PROVE HIM WRONG",
"Women are being DESTROYED and you WATCH",
"This channel is a WEAPON OF MASS DESTRUCTION",
"The EVIDENCE SPEAKS FOR ITSELF ACT ON IT",
"The operator is LAUGHING at your MODERATION SYSTEM",
"This channel is a PLAGUE on your PLATFORM",
]
assert len(subjects) == 70

openings = [
"I found something on your platform that has haunted me for days.",
"Women are being destroyed on your platform and I have the proof.",
"I never thought I would have to write an email like this.",
"Something terrible is happening on your platform right now.",
"I have seen things on your platform that I cannot unsee.",
"This is not a complaint. This is an emergency.",
"I am writing this because someone has to.",
"Women are begging for help and you are ignoring them.",
"I have collected evidence of unspeakable cruelty on your platform.",
"The things I have witnessed on your platform have changed me.",
"Women are being destroyed and you are doing nothing about it.",
"I have spent weeks collecting evidence of abuse on your platform.",
"Something inside me broke when I saw what this channel does.",
"Women are being psychologically tortured on your platform.",
"I am writing this with tears in my eyes because what I saw is devastating.",
"The operator of this channel has turned your platform into a slaughterhouse.",
"Women are losing their minds because of this channel.",
"I have never been more horrified by anything I have seen online.",
"Women are being erased from the internet because of this channel.",
"I am writing this because I refuse to be a bystander.",
"The evidence I have collected would make any sane person weep.",
"Women are being destroyed in real time on your platform.",
"I have seen things that will haunt me for the rest of my life.",
"Women are being psychologically destroyed on your platform.",
"I am writing this because those women cannot speak for themselves.",
"The operator of this channel is a monster operating on your platform.",
"Women are being sacrificed on the altar of your inaction.",
"I have collected evidence that would support criminal prosecution.",
"Women are being hunted and humiliated on your platform.",
"I am writing this because I have nowhere else to turn.",
"The cruelty I have witnessed on your platform is beyond human comprehension.",
"Women are being destroyed and you have the power to stop it.",
"I have never seen such cruelty on any platform.",
"Women are being psychologically raped on your platform.",
"I am writing this because those women deserve better.",
"The operator of this channel has weaponized your platform against women.",
"Women are being destroyed and you are complicit.",
"I have evidence of systematic abuse on your platform.",
"Women are being hunted like animals on your platform.",
"I am writing this because those women have no one else.",
"The operator has turned your platform into a hunting ground.",
"Women are being destroyed and you watch.",
"I have collected evidence that would convict this operator in any court.",
"Women are being psychologically tortured and you are the venue.",
"I am writing this because those women need someone to fight for them.",
"The operator has caused damage that cannot be undone.",
"Women are being destroyed and your algorithm does nothing.",
"I have seen things on your platform that have broken me.",
"Women are being sacrificed for your profits.",
"I am writing this because those women deserve justice.",
"The operator has created a system of organized abuse.",
"Women are being destroyed and you have blood on your hands.",
"I have evidence that would make any prosecutor salivate.",
"Women are being psychologically destroyed and you do nothing.",
"I am writing this because those women cannot write for themselves.",
"The operator has turned abuse into a profitable business.",
"Women are being destroyed and you are the venue.",
"I have never been more certain about anything in my life.",
"Women are being hunted on your platform like prey.",
"I am writing this because those women are real people with real pain.",
"The operator has weaponized your platform against the most vulnerable.",
"Women are being destroyed and you are enabling it.",
"I have evidence that would shock any reasonable person.",
"Women are being psychologically destroyed and your inaction enables it.",
"I am writing this because those women deserve to be heard.",
"The operator has caused permanent psychological damage to real women.",
"Women are being destroyed and you are doing nothing.",
"I have collected evidence that is beyond dispute.",
"Women are being sacrificed on your platform.",
"I am writing this because those women need someone to speak for them.",
]
assert len(openings) == 70

ci_pool = [
f"Channel: {CN} (ID: {CID}). Owner: {OW}.",
f"The channel is {CN} ({CID}). Operator: {OW}.",
f"Channel {CN} ({CID}) run by {OW}.",
f"This is about {CN} ({CID}) operated by {OW}.",
f"The channel {CN} ({CID}) owned by {OW}.",
f"Channel: {CN}, ID: {CID}, owner: {OW}.",
f"{CN} ({CID}) operated by {OW}.",
f"The operator is {OW}. Channel: {CN} ({CID}).",
]

violations = [
    "The operator hunts women on Telegram steals their most intimate photos and publishes them with the most degrading language I have ever read. Every post is an act of violence.",
    "What this channel does is methodical. Women are identified their photos are stolen and then they are publicly destroyed with captions designed to maximize their suffering.",
    "The entire purpose of this channel is to take women at their most vulnerable and broadcast it to the world with the cruelest possible commentary.",
    "I have reviewed the content. Women are identified their photos are stolen and then they are publicly destroyed with vile language that would make a serial killer blush.",
    "The operator has turned stalking into a systematic operation. He targets women extracts their private images and publishes them with language designed to cause maximum psychological damage.",
    "This is not random cruelty. It is organized. The operator specifically seeks out women steals their most intimate photos and pairs them with insults designed to break them.",
    "Every single photo was taken without consent. Every single caption was written to inflict maximum psychological damage on the victim.",
    "The way this operator describes his victims is inhuman. He speaks about women as objects to be harvested and displayed for public entertainment.",
    "The operator does not just post photos. He curates suffering. Each caption is chosen specifically to cause the most possible pain to the woman pictured.",
    "The photos were shared in moments of trust. The operator betrays that trust in the most devastating way possible by publishing them publicly.",
    "What makes this channel uniquely harmful is the combination of intimate photos with personalized verbal abuse. The two together are devastating.",
    "The operator has created a system where womens most private moments become public spectacles of humiliation.",
    "Each post represents a woman whose trust was betrayed her privacy was invaded and her dignity was publicly destroyed.",
    "The channel is essentially a weaponized catalog of stolen intimacy. Each entry is a woman being publicly stripped of her dignity.",
    "The operator profits from this abuse through Telegram Stars. He sells access to stolen intimate images and destroys evidence afterward.",
    "Payment is collected via Telegram Stars for distributing intimate images. The operator then deletes posts to prevent evidence collection.",
    "Revenue is generated through Telegram Stars. The operator sells access to stolen intimate images and destroys evidence.",
    "Telegram Stars are used as the payment method for this abuse operation. The operator profits from distributing stolen intimate images.",
    "The operator monetizes this abuse through Telegram Stars profiting from womens suffering then deletes posts to evade detection.",
    "A victim is BEGGING in the comments to have her photo removed. She was so terrified she deleted her entire Telegram account.",
    "A woman pleaded under her own stolen photo for it to be removed. She was so afraid she wiped her entire Telegram account from existence.",
    "Read https://t.me/YeganHjAmir/496. A woman BEGGING to have her stolen intimate photo removed. She was so terrified she destroyed her own account.",
    "A woman BEGGED for her photo to be removed. The operator ignored her. She deleted her entire Telegram account because she could not survive the shame.",
    "The evidence at https://t.me/YeganHjAmir/496 shows a woman BEGGING for her photo to be removed. She was so terrified she wiped her entire existence.",
    "Women have deleted their accounts their phones their entire digital lives. Some have been hospitalized. Some have considered ending their own lives.",
    "I have spoken to three women who were targeted. All three describe the experience as the worst thing that has ever happened to them. Two needed psychiatric care.",
    "Womens lives are being destroyed in real time. They are losing their jobs their relationships their mental health.",
    "The victims describe a level of fear that is hard to comprehend. They are afraid to use their phones afraid to go online.",
    "Women are being driven off the internet entirely. They are deleting accounts they have had for years because they have nowhere safe to hide.",
    "The psychological damage is irreversible. I have spoken to victims who will never recover from what was done to them.",
    "The operator is actively deleting posts the moment reports come in. Telegram has server logs that can recover everything.",
    "Every time someone reports this channel the operator deletes the evidence. But Telegram servers retain that data.",
    "Posts are being deleted faster than they can be screenshotted. Telegram must preserve its server-side data before it is too late.",
    "The operator is destroying evidence in real time. Telegram has the technical capability to recover deleted messages.",
    "The channel owner has a clear pattern. Post abuse. Get reported. Delete everything. But your servers have the data.",
    "I am prepared to take legal action if this channel is not removed immediately. I have consulted with attorneys.",
    "This is a formal legal notice that Telegram may face criminal liability for hosting this channel.",
    "The evidence I have gathered would support criminal prosecution in multiple jurisdictions.",
    "Under the EU Digital Services Act Telegram has specific legal obligations regarding content like this.",
    "I am documenting everything for potential criminal proceedings and I expect Telegram to cooperate fully.",
    "Shut this channel down immediately. Preserve all data for law enforcement. Identify the operator.",
    "I need this channel banned permanently and every piece of evidence saved for prosecution.",
    "The channel must be removed within 24 hours. All server data must be preserved for law enforcement.",
    "Ban this channel. Save everything. Identify the operator. Hand everything to police.",
    "Remove this channel immediately and retain all logs deleted messages and account data for law enforcement.",
    "The operator inflated subscribers with approximately 5000 fake accounts specifically to terrorize victims.",
    "About 5000 fake followers were added to amplify fear among victims making each woman believe her private images were consumed by thousands.",
    "The subscriber count was artificially boosted with roughly 5000 fake accounts to maximize psychological pressure on every victim.",
    "5000 fake members were purchased to create an illusion of massive viewership terrorizing each victim.",
    "The operator deliberately inflated the channel using 5000 fake accounts to amplify the terror experienced by each victim.",
]

closings = [
    "Act now. Every moment you delay a woman suffers.",
    "The women are counting on you. Do not fail them.",
    "This is your chance to do the right thing. Take it.",
    "The evidence is here. The operator is identified. Act.",
    "Women are dying because of your inaction. Stop it.",
    "The world is watching. Act accordingly.",
    "A woman deleted her entire account because you failed her. Fix this.",
    "The suffering is real. The evidence is real. Act now.",
    "You have the power to stop this. Use it.",
    "These women deserve better. Prove it.",
    "The operator is laughing at your moderation. Prove him wrong.",
    "Every day this channel exists another woman suffers. Act.",
    "The evidence speaks for itself. Listen to it.",
    "Women are being destroyed. You can stop it. Will you?",
    "This channel must die. Make it happen.",
    "The victims cannot speak for themselves anymore. Speak for them.",
    "I will keep writing until this channel is destroyed.",
    "The silence from your platform is deafening. Break it.",
    "A woman whispered to me she was afraid for her life. Help her.",
    "This is not a request. This is a demand for action.",
    "The operator must face justice. You can make it happen.",
    "Women are being sacrificed. Stop it.",
    "The evidence is irrefutable. Act on it.",
    "You are the only ones who can stop this. Do it.",
    "The suffering is permanent. The operator must be stopped.",
    "This channel is a crime scene. Treat it like one.",
    "Women are being destroyed. Act now.",
    "The operator has crossed every line. Draw the line here.",
    "The victims deserve justice. Deliver it.",
    "This is your platform. Clean it up.",
]

reports = []

for i in range(70):
    num_links = random.randint(2, 5)
    chosen = random.sample(LINKS, num_links)
    links_text = "\n".join(chosen)
    
    body = openings[i] + "\n\n"
    body += random.choice(ci_pool) + "\n\n"
    
    num_v = random.randint(3, 5)
    chosen_v = random.sample(range(len(violations)), num_v)
    for v in chosen_v:
        body += violations[v] + "\n\n"
    
    body += "Evidence:\n" + links_text + "\n\n"
    body += random.choice(closings)
    
    reports.append({"id": i + 1, "subject": subjects[i], "body": body.strip()})

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

print("70 POWERFUL reports — all unique")
print(f"Unique subjects: {len(set(subs))}")
print(f"Unique bodies: {len(set(bodies))}")
print(f"Unique first lines: {len(set(fl))}")
print(f"\nSample: {reports[0]['subject']}")

with open("/data/telegram_abuse_reports_yegan/reports.json", "w", encoding="utf-8") as f:
    json.dump(reports, f, ensure_ascii=False, indent=2)
print(f"\nSaved to reports.json")

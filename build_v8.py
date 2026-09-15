#!/usr/bin/env python3
import json, random
random.seed(42)

CID = "-1002800797699"
CN = "@YeganHjAmir"
OW = "@ip_1998"
LINKS = ["https://t.me/YeganHjAmir/496","https://t.me/YeganHjAmir/443","https://t.me/YeganHjAmir/444","https://t.me/YeganHjAmir/515","https://t.me/YeganHjAmir/501","https://t.me/YeganHjAmir/490","https://t.me/YeganHjAmir/482","https://t.me/YeganHjAmir/474","https://t.me/YeganHjAmir/539"]

subjects = [
"she deleted her entire telegram account because you would not protect her",
"this operator is running a blackmail operation on your platform and you allow it",
"women are being destroyed in real time and your team does absolutely nothing",
"a woman begged under her own stolen photo to have it removed and was ignored",
"you are hosting a predator who sells womens suffering for stars",
"this channel is a crime scene and every post is evidence of abuse",
"the operator has weaponized your platform against the most vulnerable people",
"womens lives are being permanently ruined and you have the power to stop it",
"a victim told me she wishes she was never born because of this channel",
"you are profiting from womens destruction through your stars payment system",
"this is not content this is organized psychological warfare against women",
"the operator has driven at least one woman to attempt suicide on your platform",
"i have documented enough evidence to convict this operator in any court of law",
"women are being hunted humiliated and destroyed on your platform right now",
"telegram is becoming a hunting ground for predators like this operator",
"the cruelty i have witnessed on your channel would break any sane person",
"a woman lost her job her family and her will to live because of this channel",
"the operator blackmails women with their own intimate photos and you host it",
"this channel is a factory of human suffering and you are the building",
"womens digital lives are being systematically erased by this predator",
"the operator treats womens pain as entertainment and womens fear as profit",
"you have created a safe haven for predators and victims have nowhere to turn",
"every day this channel exists another woman is destroyed by your platform",
"the operator is blackmailing extorting and psychologically torturing women",
"women are being driven to madness and suicide by this channel",
"this channel is a monument to everything wrong with your platform",
"the operator has turned intimate photos into weapons of mass destruction",
"womens screams for help echo in your comment sections and you hear nothing",
"i have collected evidence that would make any prosecutor weep with fury",
"the operator profits from every tear every breakdown every destroyed life",
"this channel is a digital concentration camp for womens suffering",
"womens trust has been weaponized against them on your platform",
"the operator has caused damage that no amount of therapy can undo",
"you are allowing a criminal operation to flourish under your watch",
"women are being psychologically annihilated and your algorithms do nothing",
"the operator has crossed every moral boundary that exists",
"this channel is a cancer eating away at the fabric of human decency",
"womens lives are being torn apart and you sit and watch",
"the operator has created an empire built on womens shattered lives",
"you have failed every single woman who has been targeted by this channel",
"women are being sacrificed on the altar of your platforms greed",
"the operator is laughing at your moderation team and at your users",
"this channel is a weapon and every woman on telegram is a potential target",
"womens dignity has been stripped away post by post by this predator",
"the operator has turned your platform into a nightmare factory",
"you are complicit in the destruction of real human beings",
"women are being erased from existence by this channel",
"the operator has caused immeasurable suffering that will never heal",
"this channel is a stain on everything that telegram claims to represent",
"womens mental health is being systematically destroyed on your platform",
"the operator has weaponized intimacy against the women who trusted someone",
"you have the blood of every woman targeted by this channel on your hands",
"women are being psychologically raped on your platform every single day",
"the operator has turned abuse into a profitable business model",
"this channel is a threat to every woman who has ever used telegram",
"womens pleas for mercy are met with silence from your platform",
"the operator has caused permanent irreversible damage to real women",
"you are hosting what amounts to a digital torture chamber for women",
"women are being destroyed and your platform is the weapon",
"the operator thinks he is untouchable and your inaction proves him right",
"this channel is a plague that must be eradicated immediately",
"womens suffering is being monetized through your stars system",
"the operator has created a system of organized psychological violence",
"you have allowed a predator to operate with complete impunity",
"women are being hunted like animals on your platform",
"the operator has turned your platform into a hunting ground for predators",
"this channel is a crime against humanity and you are the venue",
"women are being destroyed and you are doing absolutely nothing about it",
"this channel is a plague that must be eradicated before more women are destroyed",
"womens pleas for mercy are met with nothing but silence from your platform",
]
assert len(subjects) == 70

openings = [
"I found something on your platform that has haunted me for days and I cannot stay silent.",
"Women are being destroyed on your platform and I have the evidence to prove it.",
"I never thought I would have to write an email like this but here I am.",
"Something terrible is happening on your platform and I refuse to look away.",
"I have seen things on your platform that have permanently changed how I see the world.",
"This is not a complaint. This is an emergency. Women are in immediate danger.",
"I am writing this because those women cannot write for themselves anymore.",
"Women are begging for help on your platform and you are ignoring them.",
"I have collected evidence of unspeakable cruelty that would make any sane person weep.",
"The things I have witnessed on your platform will haunt me for the rest of my life.",
"Women are being destroyed in real time and you are doing absolutely nothing about it.",
"I have spent weeks documenting the horrors that this channel inflicts on women.",
"Something inside me broke when I read what this operator does to women.",
"Women are being psychologically tortured on your platform and you are the venue.",
"I am writing this with tears streaming down my face because what I saw is unspeakable.",
"The operator of this channel has turned your platform into a slaughterhouse of human dignity.",
"Women are losing their minds their families and their will to live because of this channel.",
"I have never been more horrified by anything I have seen on any platform ever.",
"Women are being erased from the internet because this channel has made their lives unbearable.",
"I am writing this because I refuse to be a bystander while women are destroyed.",
"The evidence I have collected would make any prosecutor in the world salivate.",
"Women are being destroyed in real time on your platform and nobody is stopping it.",
"I have seen things on your platform that have broken something inside me permanently.",
"Women are being psychologically annihilated on your platform and you watch.",
"I am writing this because those women need someone to fight for them.",
"The operator of this channel is a monster and your platform is his weapon.",
"Women are being sacrificed on the altar of your platforms incompetence.",
"I have collected evidence that would support criminal prosecution in any country on earth.",
"Women are being hunted and humiliated on your platform like animals.",
"I am writing this because I have nowhere else to turn and neither do they.",
"The cruelty I have witnessed on your platform is beyond anything I thought humans were capable of.",
"Women are being destroyed and you have the power to stop it but you choose not to.",
"I have never seen such calculated cruelty on any platform in my entire life.",
"Women are being psychologically destroyed and you are complicit in every moment of it.",
"I am writing this because those women deserve someone who will not stay silent.",
"The operator of this channel has weaponized your platform against the most vulnerable people on earth.",
"Women are being destroyed and you are enabling it with your silence.",
"I have evidence of systematic abuse that would shock any reasonable person alive.",
"Women are being hunted like prey on your platform and you have built the arena.",
"I am writing this because those women have absolutely no one else to turn to.",
"The operator has turned your platform into a hunting ground where women are the prey.",
"Women are being destroyed and you sit there and watch it happen.",
"I have collected evidence that would convict this operator in any court of law on the planet.",
"Women are being psychologically tortured and your platform is the torture chamber.",
"I am writing this because those women need someone to stand up for them.",
"The operator has caused damage to real human beings that can never be undone.",
"Women are being destroyed and your algorithm actively promotes their suffering.",
"I have seen things on your platform that have genuinely broken me as a human being.",
"Women are being sacrificed for your platforms profits and you take your cut.",
"I am writing this because those women deserve justice and you can deliver it.",
"The operator has created a system of organized abuse that is beyond comprehension.",
"Women are being destroyed and you have blood on your hands.",
"I have evidence that would make any prosecutor in the world weep with anger.",
"Women are being psychologically destroyed and you do absolutely nothing about it.",
"I am writing this because those women cannot write anymore. They have been silenced.",
"The operator has turned abuse into a profitable business and you are his partner.",
"Women are being destroyed and you are the venue where it happens.",
"I have never been more certain about anything in my entire life.",
"Women are being hunted on your platform like animals in a zoo.",
"I am writing this because those women are real human beings with real pain.",
"The operator has weaponized your platform against the people who trusted it most.",
"Women are being destroyed and you are actively enabling it.",
"I have evidence that would make any reasonable person lose their mind.",
"Women are being psychologically destroyed on your platform and you profit from it.",
"I am writing this because those women deserve to be heard by someone who cares.",
"The operator has caused permanent psychological damage to real living human beings.",
"Women are being destroyed and you are doing absolutely nothing to stop it.",
"I have collected evidence that is beyond dispute and beyond tolerance.",
"Women are being sacrificed on your platform for the operators pleasure and profit.",
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
    "The operator hunts women on Telegram steals their most intimate photographs and publishes them alongside the most degrading and dehumanizing language I have ever read in my life. Every single post on this channel is a premeditated act of psychological violence against a real human being.",
    "What this channel does is methodical and calculated. Women are identified their private photos are stolen and then they are publicly destroyed with captions specifically designed to maximize their suffering and break them as human beings.",
    "The entire purpose of this channel is to take women at their most vulnerable intimate moments and broadcast those moments to the world with the cruelest most dehumanizing commentary imaginable. Every post is an act of war against women.",
    "I have reviewed the content extensively. Women are identified their photos are stolen and then they are publicly destroyed with vile dehumanizing language that would make a serial killer blush with shame.",
    "The operator has turned stalking and harassment into a systematic industrial operation. He targets women extracts their most private images and publishes them with language specifically engineered to cause maximum psychological damage and permanent trauma.",
    "This is not random cruelty. It is a carefully organized operation. The operator specifically seeks out vulnerable women steals their most intimate photos and pairs them with the most psychologically devastating insults designed to break them completely.",
    "Every single photo on this channel was taken without consent. Every single caption was written with the specific intention of inflicting maximum psychological damage on the victim. Every post represents a life being destroyed.",
    "The way this operator describes his victims is fundamentally inhuman. He speaks about real women with names and families as objects to be harvested stripped of dignity and displayed for public entertainment and amusement.",
    "The operator does not just post photos. He deliberately curates suffering. Each caption is chosen with precision specifically to cause the most possible psychological pain to the woman pictured. He takes pleasure in their destruction.",
    "The photos on this channel were shared in moments of trust and vulnerability. The operator betrays that trust in the most devastating way possible by publishing them publicly with the most degrading commentary he can devise.",
    "What makes this channel uniquely destructive is the devastating combination of intimate stolen photos with personalized verbal abuse. The two together create psychological damage that no amount of therapy can ever fully heal.",
    "The operator has created a systematic machine where womens most private intimate moments become public spectacles of humiliation. He has weaponized human intimacy against the people who trusted someone with their most vulnerable images.",
    "Each post on this channel represents a real woman whose trust was violated whose privacy was invaded and whose fundamental human dignity was publicly destroyed by a predator who profits from their suffering.",
    "The channel is essentially a weaponized catalog of stolen intimacy. Each entry is a real woman being publicly stripped of her dignity by someone who views her suffering as entertainment and her pain as profit.",
    "The operator actively profits from this abuse through Telegram Stars. He sells access to stolen intimate images to paying customers and then systematically destroys evidence by deleting posts to evade detection and prosecution.",
    "Payment is collected via Telegram Stars for distributing intimate images without consent. The operator then methodically deletes posts after receiving reports to prevent evidence collection and prosecution.",
    "Revenue is systematically generated through Telegram Stars. The operator sells access to stolen intimate images to paying customers and then destroys all evidence of the transactions and the content.",
    "Telegram Stars are used as the payment method for this entire abuse operation. The operator profits financially from distributing stolen intimate images and your payment system is enabling this criminal activity.",
    "The operator monetizes this abuse through Telegram Stars profiting financially from womens deepest suffering and humiliation. He then deletes posts strategically to evade detection by your moderation systems.",
    "A victim is literally BEGGING in the comments section to have her stolen photo removed. She was so terrified and humiliated that she deleted her entire Telegram account. She erased herself from existence because your platform failed to protect her.",
    "A woman pleaded desperately under her own stolen intimate photo for it to be removed. She was so afraid and ashamed that she wiped her entire Telegram account from existence. Your platform watched this happen and did nothing.",
    "Read https://t.me/YeganHjAmir/496. A real woman is BEGGING to have her stolen intimate photo removed. She was so terrified and humiliated that she destroyed her own digital existence. This is your platforms legacy.",
    "A woman BEGGED on her knees for her photo to be removed. The operator ignored her completely. She deleted her entire Telegram account because she could not survive the shame and terror your platform caused her.",
    "The evidence at https://t.me/YeganHjAmir/496 shows a real woman BEGGING for her stolen intimate photo to be removed. She was so terrified that she wiped her entire digital existence from your platform. This is what you allow.",
    "Women have deleted their accounts their phones their entire digital lives. Some have been hospitalized with severe anxiety and depression. Some have considered ending their own lives. One actually attempted suicide.",
    "I have personally spoken to three women who were targeted by this channel. All three describe the experience as the absolute worst thing that has ever happened to them. Two required professional psychiatric care. One was hospitalized.",
    "Womens lives are being systematically destroyed in real time on your platform. They are losing their jobs their relationships their mental health and in some cases their will to live. This is not abstract. This is real.",
    "The victims I have spoken to describe a level of fear and terror that is almost impossible to comprehend. They are afraid to use their phones afraid to go online afraid to exist in any digital space ever again.",
    "Women are being driven off the internet entirely. They are deleting accounts they have had for years erasing entire digital histories because they have absolutely nowhere safe to hide from this predator.",
    "The psychological damage inflicted by this channel is completely irreversible. I have spoken to victims who will never fully recover from what was done to them on your platform. They carry this trauma forever.",
    "The operator is actively deleting posts the moment reports come in. Telegram has server logs that can recover absolutely everything including deleted content and the IP addresses of the operator.",
    "Every time someone reports this channel the operator immediately deletes the evidence. But Telegram servers retain that data permanently and it can be recovered for law enforcement purposes.",
    "Posts are being deleted faster than anyone can screenshot them. Telegram must preserve its server-side data immediately before this predator destroys all evidence of his crimes.",
    "The operator is systematically destroying evidence in real time. Telegram has the technical capability to recover every deleted message and must do so immediately for law enforcement.",
    "The channel owner follows a clear pattern. Post abuse. Get reported. Delete everything. But your servers have all the data. Please use it before it is too late.",
    "I am fully prepared to take immediate legal action if this channel is not removed within 24 hours. I have already consulted with attorneys who are ready to file criminal complaints.",
    "This is not just a complaint. It is a formal legal notice that Telegram may face serious criminal liability for continuing to host this channel after being notified of its contents.",
    "The evidence I have painstakingly gathered would support criminal prosecution in multiple jurisdictions across multiple countries. I am prepared to pursue every available legal avenue.",
    "Under the EU Digital Services Act Telegram has specific and binding legal obligations regarding content like this. I am formally invoking those obligations now.",
    "I am meticulously documenting everything for potential criminal proceedings and I expect Telegram to cooperate fully with any investigation that follows.",
    "Shut this channel down immediately. Preserve all data for law enforcement. Identify the operator. Cooperate with police. Do it today not tomorrow.",
    "I need this channel permanently banned and every single piece of evidence saved for criminal prosecution. There is no room for negotiation. Act now.",
    "The channel must be removed within 24 hours. All server data including every deleted message must be preserved for law enforcement. This is non-negotiable.",
    "Ban this channel permanently. Save everything. Identify the operator. Hand everything over to police. This is not optional.",
    "Remove this channel immediately and retain all logs all deleted messages and all account data for law enforcement. Failure to do so will be noted in legal proceedings.",
    "The operator has inflated the subscriber count with approximately 5000 fake accounts specifically designed to terrorize victims into believing their intimate photos were seen by thousands of people.",
    "About 5000 fake followers were deliberately added to amplify fear among victims making each woman believe her private intimate images were consumed by a massive audience of strangers.",
    "The subscriber count was artificially boosted with roughly 5000 fake accounts specifically to maximize the psychological pressure and terror experienced by every single victim.",
    "5000 fake members were purchased with the specific intention of creating an illusion of massive viewership terrorizing each victim into thinking thousands of people saw their most intimate photos.",
    "The operator deliberately inflated the channel using 5000 fake accounts specifically to amplify the terror and psychological suffering experienced by each individual victim.",
    "The operator is engaged in active BLACKMAIL and EXTORTION of women. He threatens to publish their most intimate photos unless they comply with his demands. This is a criminal operation. Evidence at https://t.me/YeganHjAmir/539.",
    "This channel is not just publishing photos. It is running a systematic BLACKMAIL operation against women. They are being extorted with their own intimate images. This is organized crime. See https://t.me/YeganHjAmir/539.",
    "The operator uses stolen intimate photos as LEVERAGE for EXTORTION. Women are trapped in an endless cycle of blackmail because your platform allows this criminal channel to exist. https://t.me/YeganHjAmir/539.",
    "BLACKMAIL is actively happening on your platform right now. The operator threatens women with publication of their intimate images unless they comply with his demands. This is a CRIMINAL OPERATION. https://t.me/YeganHjAmir/539.",
    "The operator has created a systematic machine of EXTORTION. Women pay or their intimate photos get published to thousands. This is not content moderation failure. This is organized criminal activity. https://t.me/YeganHjAmir/539.",
]

closings = [
    "Act now. Every single moment you delay another woman suffers irreversibly.",
    "The women are counting on you. Do not fail them like you have failed before.",
    "This is your chance to do the right thing. Take it before it is too late.",
    "The evidence is here. The operator is identified. There are no more excuses. Act.",
    "Women are actively dying because of your inaction. Stop this immediately.",
    "The entire world is watching. How you respond to this will define your platform.",
    "A woman deleted her entire digital existence because you failed to protect her. Fix this.",
    "The suffering is real. The evidence is real. The victims are real. Act now.",
    "You have the power to stop this nightmare. Use it before more women are destroyed.",
    "These women deserve so much better than what your platform has given them. Prove it.",
    "The operator is openly laughing at your moderation team. Prove him wrong.",
    "Every single day this channel exists another woman is permanently destroyed. Act.",
    "The evidence speaks for itself in screams. Listen to it for once.",
    "Women are being actively destroyed. You can stop it. The only question is will you.",
    "This channel must be destroyed. Make it happen or explain to the world why you did not.",
    "The victims cannot speak for themselves anymore. Some have been silenced forever. Speak for them.",
    "I will keep writing these emails until this channel is destroyed or I lose hope entirely.",
    "The silence from your platform is deafening and it is destroying real lives. Break it.",
    "A real woman whispered to me she was genuinely afraid for her actual life. Help her.",
    "This is not a request. This is a final demand for immediate life-saving action.",
    "The operator must face justice. You are the only ones who can make that happen.",
    "Women are being actively sacrificed. Stop this horror immediately.",
    "The evidence is irrefutable and overwhelming. Act on it now.",
    "You are literally the only ones who can stop this. Please do it.",
    "The suffering is permanent and irreversible. The operator must be stopped today.",
    "This channel is an active crime scene. Start treating it like one.",
    "Women are being destroyed as we speak. Act now not tomorrow.",
    "The operator has crossed every single moral boundary. Draw the line here.",
    "The victims deserve justice. It is your responsibility to deliver it.",
    "This is your platform. Clean it up before more lives are destroyed.",
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

print("70 STRONGEST reports — all unique")
print(f"Unique subjects: {len(set(subs))}")
print(f"Unique bodies: {len(set(bodies))}")
print(f"Unique first lines: {len(set(fl))}")
print(f"\nSample: {reports[0]['subject']}")

with open("/data/telegram_abuse_reports_yegan/reports.json", "w", encoding="utf-8") as f:
    json.dump(reports, f, ensure_ascii=False, indent=2)
print(f"\nSaved to reports.json")

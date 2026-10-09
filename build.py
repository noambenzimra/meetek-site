"""Generates public/index.html (Hebrew) and public/en/index.html (English).

Apple-style variant. Edit the HE / EN text dictionaries below, then run:  python3 build.py
Styles live in public/styles.css, behaviour in public/site.js.
"""
import os
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

ICONS = {
 "calc": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2M8 18h8"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "link": '<circle cx="6" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><path d="M9 6h6a3 3 0 0 1 3 3v6M15 18H9a3 3 0 0 1-3-3V9"/>',
 "checkbox": '<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>',
 "grid": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 14h3M8 17h6"/>',
 "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
}
def ic(name, size=22, sw=1.8):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

LOGO = '<svg width="30" height="21" viewBox="0 0 30 22" aria-hidden="true"><circle class="c1" cx="10" cy="11" r="8.6" fill="none" stroke-width="2.4"/><circle class="c2" cx="20" cy="11" r="8.6" fill="none" stroke-width="2.4"/></svg>'

HE = dict(
 lang="he", dir="rtl", base="", other="en/", other_label="EN",
 title="Meetek | הטמעת AI בחברות הנדסה, ביצוע ותשתיות",
 desc="Meetek מציבה בחברה שלכם סטודנט מצטיין להנדסה מהטכניון, 3 ימים בשבוע, שמוצא איפה הולכות השעות ובונה את הכלים שמחזירים לכם אותן.",
 og_title="כמה שעות בשבוע הולכות אצלכם על עבודה ידנית?",
 og_desc="סטודנט מצטיין מהטכניון יושב אצלכם 3 ימים בשבוע ומטמיע בינה מלאכותית בעבודה האמיתית. פגישת היכרות ללא עלות.",
 og_locale="he_IL", url="https://meetek.ai/", alt_href="https://meetek.ai/en/", alt_lang="en",
 skip="דילוג לתוכן", home="Meetek, לראש העמוד", nav_label="ניווט ראשי",
 nav=[("#compare","לפני ואחרי"),("#work","על מה עובדים"),("#how","איך זה עובד"),("#students","הסטודנטים"),("#faq","שאלות")],
 theme_label="מצב כהה או בהיר", cta_nav="קביעת פגישה",
 h1a="AI שעובד אצלכם במשרד.", h1b="לא רק במצגת.",
 lead="סטודנט מצטיין להנדסה מהטכניון יושב אצלכם <b>3 ימים בשבוע</b>, לומד איך העבודה נעשית היום, ובונה את הכלים שמחזירים לכם את השעות.",
 cta1="לפגישת היכרות", cta2="איך זה עובד",
 facts=[("1:10","רק אחד מכל עשרה מועמדים מתקבל"),("3","ימים בשבוע, אצלכם במשרד"),("0","התחייבות להעסקה")],
 cmp_eyebrow="לפני ואחרי", cmp_h2a="מכרז אחד.", cmp_h2b="שתי דרכים לעבוד.",
 cmp_lead="ככה נראית הכנה של הצעה למכרז, היום ועם סטודנט של Meetek.",
 tab_before="היום", tab_after="עם Meetek",
 before=[("קוראים 200 עמודים של מסמכי מכרז","שעות"),("בודקים תנאי סף ידנית, סעיף אחרי סעיף","שעות"),("מחפשים אישורים ומסמכים בתיקיות ובמיילים","חצי יום"),("מגלים ערב לפני ההגשה שחסר אישור בתוקף","לחץ")],
 after=[("כל מכרז מגיע מסוכם בעמוד אחד","דקות"),("תנאי הסף נבדקים מול הנתונים שלכם","אוטומטי"),("רשימת מסמכים שמתעדכנת לבד","תמיד מעודכן"),("תזכורת שבוע מראש על כל מה שחסר","בזמן")],
 cmp_foot="המחשה של תהליך טיפוסי. כל חברה מתחילה מהתהליך שהכי כואב לה.",
 p_eyebrow="הבעיה", p_h2a="כולם מדברים על AI.", p_h2b="מעט באמת משתמשים בו.",
 pains=[("ניסיתם ChatGPT, וזה נשאר בטאב בדפדפן.","העבודה עצמה נשארה אותו דבר: אקסל, מסמכים והעתק-הדבק."),
        ("אף אחד בחברה לא יודע מאיפה להתחיל.","לכולם יש עבודה שוטפת, ואין למי לתת את הפרויקט הזה."),
        ("יועצים נותנים מצגת, אבל לא בונים.","ההמלצות נשארות על הנייר, והתהליכים לא משתנים.")],
 statement_a="אנחנו לא נותנים לכם מפת דרכים.", statement_b="אנחנו יושבים אצלכם ובונים.",
 s_eyebrow="על מה הסטודנט עובד", s_h2a="התהליכים שאוכלים", s_h2b="לכם את השבוע.",
 feature_eyebrow="מכרזים", feature_h="מ-200 עמודים לעמוד אחד.",
 feature_p="הסטודנט בונה לכם מערכת שמסכמת כל מכרז, בודקת תנאי סף ומראה מה חסר, לפני שמחליטים לגשת.",
 sample_title="סיכום מכרז", sample_auto="נוצר אוטומטית",
 sample_rows=[("מזמין","רשות מקומית"),("עבודה","שיקום תשתיות, שלב א'"),("הגשה","עוד 12 ימים"),("סיווג","ג3 ומעלה")],
 sample_checks=[("ok","✓","עומדים בתנאי הסף"),("ok","✓","9 מתוך 13 מסמכים קיימים"),("warn","!","חסר: אישור ניהול ספרים בתוקף"),("warn","!","סעיף פיצוי מוסכם חריג")],
 sample_foot="המחשה בלבד.",
 services=[("calc","w3","כתבי כמויות וחשבונות חלקיים","חשבון חלקי שיוצא מתוך כתב הכמויות, בלי להקליד הכול מחדש בכל חודש."),
           ("chart","w3","טפסים, דוחות ויומני עבודה","מסמכים שנוצרים מהנתונים שכבר יש לכם, במקום למלא אותם ביד."),
           ("link","w2","חיבור בין מערכות","Priority, חשבשבת, אקסל ומייל שמדברים אחד עם השני."),
           ("checkbox","w2","התאמת חשבוניות","חשבוניות ספקים מול הזמנות, וחריגות נתפסות לפני התשלום."),
           ("grid","w2","כלים פנימיים","רווחיות לכל פרויקט ומעקב ציוד, במקום עשרה קבצי אקסל.")],
 h_eyebrow="איך זה עובד", h_h2a="מפגישה אחת", h_h2b="לסטודנט שעובד אצלכם.",
 flow=[("01","פגישת היכרות","מבינים איך אתם עובדים היום ואיפה הולך הזמן.","30 דקות, ללא עלות"),
       ("02","התאמת סטודנט","בוחרים את מי שמתאים לתחום ולאנשים שלכם.","מתוך מי שעבר ראיונות"),
       ("03","החודש הראשון","ממפים תהליכים ומתחילים מזה שיגרום לכם להרוויח הכי הרבה.","תוצאה כבר בהתחלה"),
       ("04","ליווי שוטף","אנחנו מלווים את הסטודנט, ואם צריך, מחליפים.","3 ימים בשבוע")],
 q_eyebrow="למה הקמנו את Meetek",
 quote=["\"מצאתי מהנדסים מצוינים שעובדים כמו בשנות ה-90. בניתי להם מערכת, ותהליכים שלקחו ימים לוקחים היום דקות.",
        "<span class=\"dim\">יש מאות חברות כאלה. ויש סטודנטים מצוינים בטכניון שמחפשים בדיוק את האתגר הזה.\"</span>"],
 who="נועם בן זמרה", role="מנכ\"ל ומייסד שותף",
 su_eyebrow="הסטודנטים", su_h2a="לא כל סטודנט.", su_h2b="הסטודנט הנכון.",
 dots_label="מתוך עשרה מועמדים, אחד מתקבל", dots_b="1 מכל 10", dots_t="מועמדים עובר את הראיונות שלנו ומתקבל.",
 su_who_h="מי הם", su_who="סטודנטים להנדסה ולמדעי המחשב בטכניון: יכולת טכנית גבוהה, סבלנות להבין איך עסק עובד באמת, ויכולת לדבר עם אנשים שלא באים מעולם ההייטק.",
 su_you_h="מה זה אומר בשבילכם", su_you=["הסטודנט מועסק על ידי Meetek. אין גיוס ואין התחייבות להעסקה.","הוא יושב אצלכם 3 ימים בשבוע ומכיר את המערכות מבפנים.","אנחנו מלווים אותו מקצועית לאורך כל הדרך.","אם ההתאמה לא עובדת, מחליפים."],
 c_eyebrow="השוואה", c_h2a="למה לא פשוט לגייס,", c_h2b="או להביא יועץ?",
 c_head=["קריטריון","גיוס עובד","יועץ חיצוני","Meetek"],
 c_rows=[("התחייבות","חוזה העסקה","פרויקט סגור, יקר לשעה","לפי שעות, בלי התחייבות ארוכה"),
         ("נמצא אצלכם","כן","לרוב לא","3 ימים בשבוע, במשרד"),
         ("מה מקבלים","תלוי במי שגייסתם","המלצות ומצגת","כלים שנבנים ומוטמעים"),
         ("אם זה לא מתאים","תהליך פיטורים","סוף הפרויקט","מחליפים סטודנט")],
 f_eyebrow="שאלות נפוצות", f_h2a="מה ששואלים אותנו", f_h2b="בפגישה הראשונה.",
 faq=[("כמה זה עולה?","משלמים לפי שעות עבודה בפועל, בלי דמי הצטרפות ובלי התחייבות ארוכה. נפרט את המחיר המדויק בפגישת ההיכרות."),
      ("ניסינו AI וזה לא עבד. למה שהפעם זה יהיה אחרת?","כי הפעם יש מישהו שיושב אצלכם. כלי AI לבד לא יודעים איך נראה כתב הכמויות שלכם או מי צריך לאשר מה. הסטודנט לומד את זה מבפנים ובונה סביב העבודה האמיתית."),
      ("למה סטודנט ולא מהנדס בכיר?","כי צריך מישהו חד, סקרן וזמין, שיושב אצלכם שלושה ימים בשבוע ולומד את העסק. רק אחד מכל עשרה מתקבל, ואנחנו מלווים אותו לאורך כל הדרך."),
      ("מה לגבי סודיות המידע שלנו?","לפני תחילת העבודה חותמים על הסכם סודיות. הסטודנט עובד רק על המערכות והמסמכים שתאשרו לו."),
      ("צריך מחלקת IT או מערכות חדשות?","לא. הסטודנט עובד מעל מה שכבר יש לכם: אקסל, Priority, חשבשבת, מייל ותיקיות משותפות."),
      ("מה קורה אם הסטודנט לא מתאים?","מחליפים. ההתאמה היא באחריות שלנו.")],
 k_h2a="חצי שעה,", k_h2b="ותדעו איפה הולך לכם הזמן.",
 k_lead="פגישת היכרות ללא עלות, אצלכם במשרד או בטלפון.",
 k_call="058-4001054", k_wa="וואטסאפ", k_wa_text="היי נועם, אשמח לשמוע על Meetek", k_mail="noam@meetek.ai", k_mail_subj="פגישת היכרות עם Meetek",
 j_t="סטודנטים בטכניון? מחפשים עבודה עם השפעה אמיתית.", j_btn="שלחו קורות חיים", j_subj="מועמדות ל-Meetek",
 foot="הטמעת AI בחברות הנדסה, ביצוע ותשתיות", foot_other="English",
)

EN = dict(
 lang="en", dir="ltr", base="../", other="../", other_label="עב",
 title="Meetek | AI implementation for engineering, construction and infrastructure firms",
 desc="Meetek places a top Technion engineering student in your company, 3 days a week, to find where the hours go and build the tools that give them back.",
 og_title="How many hours a week go to manual work?",
 og_desc="A top Technion engineering student sits in your office 3 days a week and puts AI to work in your real processes. Free intro meeting.",
 og_locale="en_US", url="https://meetek.ai/en/", alt_href="https://meetek.ai/", alt_lang="he",
 skip="Skip to content", home="Meetek, back to top", nav_label="Main",
 nav=[("#compare","Before and after"),("#work","What we do"),("#how","How it works"),("#students","Students"),("#faq","FAQ")],
 theme_label="Toggle dark or light mode", cta_nav="Book a meeting",
 h1a="AI that works in your office.", h1b="Not just in a slide deck.",
 lead="A top Technion engineering student sits in your office <b>3 days a week</b>, learns how the work gets done today, and builds the tools that give you the hours back.",
 cta1="Book an intro", cta2="How it works",
 facts=[("1:10","only one in ten candidates is accepted"),("3","days a week, in your office"),("0","hiring commitment")],
 cmp_eyebrow="Before and after", cmp_h2a="One tender.", cmp_h2b="Two ways to work.",
 cmp_lead="This is what preparing a tender bid looks like, today and with a Meetek student.",
 tab_before="Today", tab_after="With Meetek",
 before=[("Reading 200 pages of tender documents","Hours"),("Checking threshold conditions by hand, clause by clause","Hours"),("Hunting for certificates in folders and email","Half a day"),("Finding out the night before that a certificate expired","Stress")],
 after=[("Every tender arrives summarized on one page","Minutes"),("Threshold conditions checked against your data","Automatic"),("A document checklist that updates itself","Always current"),("A reminder a week ahead about anything missing","On time")],
 cmp_foot="Illustration of a typical process. Every company starts with whatever hurts the most.",
 p_eyebrow="The problem", p_h2a="Everyone talks about AI.", p_h2b="Few actually use it.",
 pains=[("You tried ChatGPT, and it stayed in a browser tab.","The work itself stayed the same: spreadsheets, documents and copy-paste."),
        ("Nobody in the company knows where to start.","Everyone is busy with day-to-day work, and there's no one to own this."),
        ("Consultants give you a deck, but don't build.","The recommendations stay on paper, and the processes don't change.")],
 statement_a="We don't hand you a roadmap.", statement_b="We sit in your office and build.",
 s_eyebrow="What the student works on", s_h2a="The processes that", s_h2b="eat up your week.",
 feature_eyebrow="Tenders", feature_h="From 200 pages to one.",
 feature_p="The student builds you a system that summarizes every tender, checks threshold conditions and shows what's missing, before you decide to bid.",
 sample_title="Tender summary", sample_auto="Generated automatically",
 sample_rows=[("Client","Local municipality"),("Scope","Infrastructure renewal, phase A"),("Deadline","In 12 days"),("Class","C3 or higher")],
 sample_checks=[("ok","✓","Meets threshold conditions"),("ok","✓","9 of 13 documents on file"),("warn","!","Missing: valid bookkeeping certificate"),("warn","!","Unusual liquidated damages clause")],
 sample_foot="Illustration only.",
 services=[("calc","w3","Bills of quantities and progress billing","Progress invoices generated from the bill of quantities, without retyping everything each month."),
           ("chart","w3","Forms, reports and site logs","Documents generated from data you already have, instead of being filled in by hand."),
           ("link","w2","Connecting your systems","ERP, accounting, spreadsheets and email that talk to each other."),
           ("checkbox","w2","Invoice reconciliation","Supplier invoices matched to orders, with anomalies caught before you pay."),
           ("grid","w2","Internal tools","Profitability per project and equipment tracking, instead of ten spreadsheets.")],
 h_eyebrow="How it works", h_h2a="From one meeting", h_h2b="to a student in your office.",
 flow=[("01","Intro meeting","We learn how you work today and where the time goes.","30 minutes, free"),
       ("02","Student match","We pick the student who fits your field and your people.","From those who passed interviews"),
       ("03","The first month","We map your processes and start with the one that will make you the most money.","Results early on"),
       ("04","Ongoing support","We mentor the student, and replace them if needed.","3 days a week")],
 q_eyebrow="Why we started Meetek",
 quote=["\"I found excellent engineers working like it was the 90s. I built them a system, and processes that took days now take minutes.",
        "<span class=\"dim\">There are hundreds of companies like this. And there are brilliant Technion students looking for exactly this challenge.\"</span>"],
 who="Noam Ben Zimra", role="CEO and co-founder",
 su_eyebrow="Our students", su_h2a="Not just any student.", su_h2b="The right one.",
 dots_label="Out of ten candidates, one is accepted", dots_b="1 in 10", dots_t="candidates passes our interviews and is accepted.",
 su_who_h="Who they are", su_who="Engineering and computer science students at the Technion: strong technical ability, the patience to understand how a business really works, and the ability to talk with people outside tech.",
 su_you_h="What this means for you", su_you=["The student is employed by Meetek. No recruiting, no hiring commitment.","They sit in your office 3 days a week and learn your systems from the inside.","We mentor them professionally throughout.","If the fit isn't right, we replace them."],
 c_eyebrow="Comparison", c_h2a="Why not just hire,", c_h2b="or bring in a consultant?",
 c_head=["Criteria","Hiring an employee","External consultant","Meetek"],
 c_rows=[("Commitment","Employment contract","Fixed project, high hourly rate","Hourly, no long-term commitment"),
         ("On site","Yes","Usually not","3 days a week, in your office"),
         ("What you get","Depends on who you hired","Recommendations and a deck","Tools built and deployed"),
         ("If it doesn't fit","A termination process","End of project","We replace the student")],
 f_eyebrow="FAQ", f_h2a="What people ask us", f_h2b="in the first meeting.",
 faq=[("How much does it cost?","You pay for actual hours worked, with no setup fee and no long-term commitment. We'll give you the exact price in the intro meeting."),
      ("We tried AI and it didn't work. Why would this be different?","Because this time someone sits in your office. AI tools on their own don't know what your bill of quantities looks like or who signs off on what. The student learns that from the inside and builds around your real work."),
      ("Why a student and not a senior engineer?","Because you need someone sharp, curious and available, who sits with you three days a week and learns the business. Only one in ten is accepted, and we mentor them all the way."),
      ("What about the confidentiality of our data?","We sign a non-disclosure agreement before work begins. The student only works on the systems and documents you approve."),
      ("Do we need an IT department or new systems?","No. The student works on top of what you already use: spreadsheets, your ERP and accounting software, email and shared folders."),
      ("What if the student isn't a good fit?","We replace them. Getting the match right is our responsibility.")],
 k_h2a="30 minutes,", k_h2b="and you'll know where your time goes.",
 k_lead="A free intro meeting, at your office or by phone.",
 k_call="+972 58-400-1054", k_wa="WhatsApp", k_wa_text="Hi Noam, I'd like to hear about Meetek", k_mail="noam@meetek.ai", k_mail_subj="Intro meeting with Meetek",
 j_t="Technion student? Looking for work with real impact.", j_btn="Send your CV", j_subj="Application to Meetek",
 foot="AI implementation for engineering, construction and infrastructure firms", foot_other="עברית",
)

def q(s): return quote(s, safe="")

def page(t):
    b = t["base"]
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in t["nav"])
    facts = "".join(f'<div class="fact"><b>{n}</b><span>{s}</span></div>' for n, s in t["facts"])
    before = "".join(f'<li><span class="mark" aria-hidden="true">!</span><span>{x}</span><span class="t">{tm}</span></li>' for x, tm in t["before"])
    after = "".join(f'<li><span class="mark" aria-hidden="true">✓</span><span>{x}</span><span class="t">{tm}</span></li>' for x, tm in t["after"])
    pains = "".join(f'<article class="tile reveal"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></article>' for i, (h, p) in enumerate(t["pains"]))
    srows = "".join(f'<dt>{a}</dt><dd>{v}</dd>' for a, v in t["sample_rows"])
    schecks = "".join(f'<li><span class="{c}" aria-hidden="true">{m}</span>{x}</li>' for c, m, x in t["sample_checks"])
    services = "".join(f'<article class="b {w} reveal"><div class="ic">{ic(i)}</div><h3>{h}</h3><p>{p}</p></article>' for i, w, h, p in t["services"])
    flow = "".join(f'<li class="reveal"><span class="n">{n}</span><h3>{h}</h3><p>{p}</p><span class="meta">{m}</span></li>' for n, h, p, m in t["flow"])
    quote_html = "".join(f"<p>{x}</p>" for x in t["quote"])
    dots = "".join('<span class="dot%s"></span>' % (" on" if k == 9 else "") for k in range(10))
    you = "".join(f"<li>{x}</li>" for x in t["su_you"])
    ch = t["c_head"]
    thead = f'<tr><th scope="col"><span class="sr-only">{ch[0]}</span></th><th scope="col">{ch[1]}</th><th scope="col">{ch[2]}</th><th scope="col" class="us">{ch[3]}</th></tr>'
    trows = "".join(f'<tr><td>{a}</td><td>{x}</td><td>{y}</td><td class="us">{z}</td></tr>' for a, x, y, z in t["c_rows"])
    faq = "".join(f'<details><summary>{qq}<span class="plus">{ic("plus",16,2.2)}</span></summary><p>{a}</p></details>' for qq, a in t["faq"])
    wa = "https://wa.me/972584001054?text=" + q(t["k_wa_text"])
    mail = "mailto:noam@meetek.ai?subject=" + q(t["k_mail_subj"])
    jmail = "mailto:noam@meetek.ai?subject=" + q(t["j_subj"])
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta property="og:title" content="{t["og_title"]}">
<meta property="og:description" content="{t["og_desc"]}">
<meta name="twitter:title" content="{t["og_title"]}">
<meta name="twitter:description" content="{t["og_desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{t["url"]}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta property="og:site_name" content="Meetek">
<meta property="og:image" content="https://meetek.ai/og.png">
<meta property="og:image:secure_url" content="https://meetek.ai/og.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Meetek">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://meetek.ai/og.png">
<meta name="theme-color" content="#000000">
<link rel="alternate" hreflang="{t["alt_lang"]}" href="{t["alt_href"]}">
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{b}apple-touch-icon.png">
<link rel="stylesheet" href="{b}styles.css">
<script>try{{if(localStorage.getItem('meetek-theme')==='light')document.documentElement.removeAttribute('data-theme')}}catch(e){{}}</script>
</head>
<body class="no-js">
<a class="skip" href="#main">{t["skip"]}</a>

<header class="nav" id="top">
  <div class="wrap nav-in">
    <a class="brand" href="#top" aria-label="{t["home"]}">{LOGO}Meetek</a>
    <nav class="nav-links" aria-label="{t["nav_label"]}">{nav}</nav>
    <div class="nav-end">
      <a class="icon-btn" href="{t["other"]}" hreflang="{t["alt_lang"]}">{t["other_label"]}</a>
      <button class="icon-btn theme" type="button" aria-label="{t["theme_label"]}"><span class="moon">{ic("moon",18)}</span><span class="sun">{ic("sun",18)}</span></button>
      <a class="btn btn-primary" href="#contact">{t["cta_nav"]}</a>
    </div>
  </div>
</header>

<main id="main">

<section class="hero">
  <div class="wrap">
    <div class="reveal">
      <h1 class="display">{t["h1a"]}<br><span class="second">{t["h1b"]}</span></h1>
      <p class="lede">{t["lead"]}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#contact">{t["cta1"]}</a>
        <a class="link" href="#how">{t["cta2"]}<span class="chev" aria-hidden="true">›</span></a>
      </div>
    </div>
    <div class="facts reveal">{facts}</div>
  </div>
</section>

<section class="alt" id="compare">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["cmp_eyebrow"]}</span>
      <h2 class="title">{t["cmp_h2a"]}<br><span class="second">{t["cmp_h2b"]}</span></h2>
      <p class="lede">{t["cmp_lead"]}</p>
    </div>
    <div class="seg-wrap reveal">
      <div class="seg" role="tablist" data-state="before">
        <span class="thumb" aria-hidden="true"></span>
        <button type="button" role="tab" id="tab-before" aria-controls="p-before" aria-selected="true" data-state="before">{t["tab_before"]}</button>
        <button type="button" role="tab" id="tab-after" aria-controls="p-after" aria-selected="false" tabindex="-1" data-state="after">{t["tab_after"]}</button>
      </div>
    </div>
    <div class="compare-card reveal">
      <div class="panel panel-before" id="p-before" role="tabpanel" aria-labelledby="tab-before"><ul class="steps-list">{before}</ul></div>
      <div class="panel panel-after" id="p-after" role="tabpanel" aria-labelledby="tab-after" hidden><ul class="steps-list">{after}</ul></div>
    </div>
    <p class="compare-foot">{t["cmp_foot"]}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["p_eyebrow"]}</span>
      <h2 class="title">{t["p_h2a"]}<br><span class="second">{t["p_h2b"]}</span></h2>
    </div>
    <div class="trio">{pains}</div>
    <p class="statement title reveal" style="font-size:clamp(1.6rem,3.2vw,2.5rem)">{t["statement_a"]}<br><span style="color:var(--accent-ink)">{t["statement_b"]}</span></p>
  </div>
</section>

<section class="alt" id="work">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["s_eyebrow"]}</span>
      <h2 class="title">{t["s_h2a"]}<br><span class="second">{t["s_h2b"]}</span></h2>
    </div>
    <div class="bento">
      <article class="b w6 b-feature reveal">
        <div>
          <span class="eyebrow">{t["feature_eyebrow"]}</span>
          <h3 class="title">{t["feature_h"]}</h3>
          <p class="lede">{t["feature_p"]}</p>
        </div>
        <div class="doc" aria-label="{t["sample_title"]}">
          <div class="doc-head"><strong>{t["sample_title"]}</strong><span>{t["sample_auto"]}</span></div>
          <dl>{srows}</dl>
          <ul>{schecks}</ul>
          <p class="doc-foot">{t["sample_foot"]}</p>
        </div>
      </article>
      {services}
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["h_eyebrow"]}</span>
      <h2 class="title">{t["h_h2a"]}<br><span class="second">{t["h_h2b"]}</span></h2>
    </div>
    <ol class="flow">{flow}</ol>
  </div>
</section>

<section class="alt">
  <div class="wrap quote reveal">
    <span class="eyebrow">{t["q_eyebrow"]}</span>
    <blockquote>{quote_html}</blockquote>
    <cite><b>{t["who"]}</b> · {t["role"]}, Meetek</cite>
  </div>
</section>

<section id="students">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["su_eyebrow"]}</span>
      <h2 class="title">{t["su_h2a"]}<br><span class="second">{t["su_h2b"]}</span></h2>
    </div>
    <div class="reveal">
      <div class="dots" role="img" aria-label="{t["dots_label"]}">{dots}</div>
      <p class="dots-cap"><b>{t["dots_b"]}</b> {t["dots_t"]}</p>
    </div>
    <div class="duo">
      <div class="tile reveal"><h3>{t["su_who_h"]}</h3><p style="margin-top:1rem;color:var(--ink-2)">{t["su_who"]}</p></div>
      <div class="tile reveal"><h3>{t["su_you_h"]}</h3><ul>{you}</ul></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["c_eyebrow"]}</span>
      <h2 class="title">{t["c_h2a"]}<br><span class="second">{t["c_h2b"]}</span></h2>
    </div>
    <div class="table-wrap reveal"><table><thead>{thead}</thead><tbody>{trows}</tbody></table></div>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="head center reveal">
      <span class="eyebrow">{t["f_eyebrow"]}</span>
      <h2 class="title">{t["f_h2a"]}<br><span class="second">{t["f_h2b"]}</span></h2>
    </div>
    <div class="faq reveal">{faq}</div>
  </div>
</section>

<section class="alt cta" id="contact">
  <div class="wrap reveal">
    <h2 class="display" style="font-size:clamp(2.3rem,6vw,4.5rem)">{t["k_h2a"]}<br><span class="second">{t["k_h2b"]}</span></h2>
    <p class="lede">{t["k_lead"]}</p>
    <div class="contact-row">
      <a class="btn btn-primary" href="tel:+972584001054"><span class="ltr">{t["k_call"]}</span></a>
      <a class="btn btn-quiet" href="{wa}" target="_blank" rel="noopener">{t["k_wa"]}</a>
      <a class="btn btn-quiet" href="{mail}"><span class="ltr">{t["k_mail"]}</span></a>
    </div>
    <p class="join">{t["j_t"]} <a href="{jmail}">{t["j_btn"]}<span class="chev" aria-hidden="true">›</span></a></p>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <span>© <span id="y">2026</span> Meetek · {t["foot"]}</span>
    <span><a href="mailto:noam@meetek.ai">noam@meetek.ai</a> · <a href="{t["other"]}" hreflang="{t["alt_lang"]}">{t["foot_other"]}</a></span>
  </div>
</footer>

<script src="{b}site.js"></script>
</body>
</html>
'''

os.makedirs(OUT + "/en", exist_ok=True)
open(OUT + "/index.html", "w").write(page(HE))
open(OUT + "/en/index.html", "w").write(page(EN))
print("ok")

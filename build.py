"""Generates public/index.html (Hebrew) and public/en/index.html (English).

Edit the HE / EN text dictionaries below, then run:  python3 build.py
Styles live in public/styles.css, behaviour in public/site.js.
"""
import os
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

ICONS = {
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h4"/>',
 "calc": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2M8 18h8"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "link": '<circle cx="6" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><path d="M9 6h6a3 3 0 0 1 3 3v6M15 18H9a3 3 0 0 1-3-3V9"/>',
 "checkbox": '<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>',
 "grid": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 14h3M8 17h6"/>',
 "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
 "x": '<path d="M7 7l10 10M17 7L7 17"/>',
 "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 4.5a3 3 0 0 1 0 6M18 14a5.5 5.5 0 0 1 3 6"/>',
 "coins": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "chat": '<path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "brain": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a3 3 0 0 0-3-1z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
 "rocket": '<path d="M5 15c-1 1-1.5 4-1.5 4s3-.5 4-1.5"/><path d="M9 15l-3-3c1-4 5-9 12-9 0 7-5 11-9 12z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 "handshake": '<path d="M3 11l4-4 5 2 5-2 4 4"/><path d="M7 7v6l5 5 5-5V7"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}
def ic(name, size=22, sw=1.9):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

LOGO = '<svg width="34" height="24" viewBox="0 0 30 22" aria-hidden="true"><circle class="c1" cx="10" cy="11" r="8.6" fill="none" stroke-width="2.6"/><circle class="c2" cx="20" cy="11" r="8.6" fill="none" stroke-width="2.6"/></svg>'

HE = dict(
 lang="he", dir="rtl", base="", other="en/", other_label="EN", other_lang="en",
 title="Meetek | הטמעת AI בחברות הנדסה, ביצוע ותשתיות",
 desc="Meetek מציבה בחברה שלכם סטודנט מצטיין להנדסה מהטכניון, 3 ימים בשבוע, שמוצא איפה הולכות השעות ובונה את הכלים שמחזירים לכם אותן.",
 og_title="Meetek | AI שעובד אצלכם במשרד", og_locale="he_IL", url="https://meetek.ai/", alt_href="https://meetek.ai/en/", alt_lang="en",
 skip="דילוג לתוכן", home="Meetek, לראש העמוד", nav_label="ניווט ראשי",
 nav=[("#work","על מה עובדים"),("#how","איך זה עובד"),("#students","הסטודנטים"),("#faq","שאלות נפוצות")],
 theme_label="מצב כהה או בהיר", cta_nav="לתיאום פגישה",
 badge="סטודנטים מצטיינים מהטכניון, רק 1 מכל 10 מתקבל",
 h1a="AI שעובד אצלכם במשרד.", h1b="לא רק במצגת.",
 lead="Meetek מציבה בחברה שלכם סטודנט מצטיין להנדסה מהטכניון, 3 ימים בשבוע. הוא לומד איך העבודה נעשית היום, מוצא איפה הולכות השעות, ובונה את הכלים שמחזירים לכם אותן.",
 cta1="לפגישת היכרות של חצי שעה", cta2="איך זה עובד",
 stats=[("users","1:10","רק אחד מכל עשרה מועמדים מתקבל"),("clock","3","ימים בשבוע אצלכם במשרד"),("shield","0","התחייבות להעסקה")],
 p_badge="הבעיה", p_h2a="AI הוא בדרך כלל", p_h2b="רק דיבורים",
 p_lead="כולם מדברים על בינה מלאכותית. מעט חברות באמת משתמשות בה בעבודה היומיומית.",
 pains=[("r","clock","ניסיתם ChatGPT, וזה נשאר בטאב בדפדפן","העבודה עצמה נשארה אותו דבר: אקסל, מסמכים והעתק-הדבק."),
        ("o","users","אף אחד בחברה לא יודע מאיפה להתחיל","לכולם יש עבודה שוטפת, ואין למי לתת את הפרויקט הזה."),
        ("p","coins","יועצים נותנים מצגת, אבל לא בונים","ההמלצות נשארות על הנייר, והתהליכים לא משתנים.")],
 callout_a="אנחנו לא נותנים לכם מפת דרכים.", callout_b="אנחנו יושבים אצלכם ובונים.",
 s_badge="על מה הסטודנט עובד", s_h2a="התהליכים שאוכלים", s_h2b="לכם את השבוע",
 s_lead="הסטודנט מתחיל מהתהליך שהכי כואב לכם, ומשם ממשיך לבא בתור.",
 services=[("doc","מכרזים","איתור מכרזים רלוונטיים, סיכום של כל מכרז לעמוד אחד, בדיקת תנאי סף ורשימת מסמכים שנבדקת אוטומטית."),
           ("calc","כתבי כמויות וחשבונות חלקיים","הפקת חשבון חלקי מתוך כתב הכמויות והמדידות, בלי להקליד הכול מחדש בכל חודש."),
           ("chart","טפסים, דוחות ויומני עבודה","טפסי רגולציה, דוחות למזמין ויומני עבודה שנוצרים מהנתונים שכבר יש לכם."),
           ("link","חיבור בין מערכות","Priority, חשבשבת, אקסל ומייל שמדברים אחד עם השני, במקום העתק-הדבק ידני."),
           ("checkbox","התאמות וחשבוניות","התאמת חשבוניות ספקים להזמנות ולתעודות משלוח, ואיתור חריגות לפני שמשלמים."),
           ("grid","כלים פנימיים","דשבורד רווחיות לכל פרויקט, מעקב ציוד בשטח, וכל מה שהיום מפוזר בעשרה קבצי אקסל.")],
 x_badge="דוגמה מהשטח", x_h2a="ככה נראית", x_h2b="עבודה של הסטודנט",
 x_lead="קחו לדוגמה מכרזים. במקום שמישהו יקרא 200 עמודים, כל מכרז מגיע מסוכם בעמוד אחד:",
 x_points=["מה העבודה, מי המזמין ומתי ההגשה","האם אתם עומדים בתנאי הסף","אילו מסמכים כבר יש לכם ומה חסר","אילו סעיפים כדאי לבדוק לפני שניגשים"],
 sample_tag="דוגמה לתוצר", sample_title="סיכום מכרז בעמוד אחד", sample_auto="נוצר אוטומטית",
 sample_rows=[("מזמין","רשות מקומית"),("עבודה","שיקום תשתיות ופיתוח, שלב א'"),("הגשה","עוד 12 ימים"),("סיווג נדרש","ג3 ומעלה")],
 sample_checks=[("ok","✓","עומדים בתנאי הסף: סיווג וניסיון קודם"),("ok","✓","9 מתוך 13 מסמכים כבר קיימים אצלכם"),("warn","!","חסר: אישור ניהול ספרים בתוקף וערבות הגשה"),("warn","!","סעיף פיצוי מוסכם חריג: כדאי לבדוק")],
 sample_foot="המחשה בלבד. כך נראה תוצר טיפוסי של סטודנט שמטפל אצלכם במכרזים.",
 h_badge="איך זה עובד", h_h2a="מפגישה אחת", h_h2b="לסטודנט שעובד אצלכם",
 steps=[("search","שלב 1","פגישת היכרות","מבינים איך אתם עובדים היום ואיפה הולך הזמן.","30 דקות, ללא עלות"),
        ("handshake","שלב 2","התאמת סטודנט","בוחרים את הסטודנט שמתאים לתחום ולאנשים שלכם.","מתוך מי שעבר ראיונות"),
        ("bolt","שלב 3","החודש הראשון","ממפים תהליכים ומתחילים מזה שיחסוך הכי הרבה.","תוצאה כבר בהתחלה"),
        ("rocket","שלב 4","ליווי שוטף","אנחנו מלווים את הסטודנט, ואם צריך, מחליפים.","3 ימים בשבוע")],
 st_badge="למה הקמנו את Meetek", st_h2a="התחלנו", st_h2b="מבעיה אמיתית",
 quote=["\"התחלתי לעבוד בחברת תשתיות ומצאתי מהנדסים מצוינים שעובדים כמו בשנות ה-90: דף, עט, וכמה סבבים בין אנשים עד שמסמך אחד יוצא. בניתי להם מערכת, ותהליך שלקח ימים לוקח היום דקות.",
        "אז הבנתי שיש מאות חברות כאלה. ומהצד השני יש סטודנטים מצוינים בטכניון שמחפשים בדיוק אתגר כזה. Meetek מחברת בין השניים.\""],
 avatar="נ", who="נועם בן זמרה", role="מנכ\"ל ומייסד שותף, Meetek",
 su_badge="הסטודנטים", su_h2a="לא כל סטודנט.", su_h2b="הסטודנט הנכון.",
 su_who_h="מי הם", su_who="סטודנטים להנדסה ולמדעי המחשב בטכניון. אנחנו מחפשים שילוב נדיר: יכולת טכנית גבוהה, סבלנות להבין איך עסק עובד באמת, ויכולת לדבר עם אנשים שלא באים מעולם ההייטק.",
 pick_label="מתוך עשרה מועמדים, אחד מתקבל", pick_cap_b="1 מכל 10", pick_cap="מועמדים עובר את הראיונות שלנו ומתקבל",
 su_you_h="מה זה אומר בשבילכם", su_you=["הסטודנט מועסק על ידי Meetek. אין גיוס, אין קליטה ואין התחייבות להעסקה.","הוא יושב אצלכם 3 ימים בשבוע ומכיר את האנשים ואת המערכות מבפנים.","אנחנו מלווים אותו מקצועית לאורך כל הדרך.","אם ההתאמה לא עובדת, מחליפים."],
 c_badge="השוואה", c_h2a="למה לא פשוט לגייס,", c_h2b="או להביא יועץ?",
 c_head=["קריטריון","גיוס עובד","יועץ חיצוני","Meetek"],
 c_rows=[("התחייבות","חוזה העסקה","פרויקט סגור, תשלום גבוה לשעה","תשלום לפי שעות, בלי התחייבות ארוכה"),
         ("נמצא אצלכם","כן","לרוב לא","3 ימים בשבוע, במשרד"),
         ("מה מקבלים","תלוי במי שגייסתם","המלצות ומצגת","כלים שנבנים ומוטמעים בפועל"),
         ("אם זה לא מתאים","תהליך פיטורים","סוף הפרויקט","מחליפים סטודנט")],
 f_badge="שאלות נפוצות", f_h2a="מה ששואלים אותנו", f_h2b="בפגישה הראשונה",
 faq=[("כמה זה עולה?","משלמים לפי שעות עבודה בפועל, בלי דמי הצטרפות ובלי התחייבות ארוכה. נפרט את המחיר המדויק בפגישת ההיכרות, אחרי שנבין מה אתם צריכים."),
      ("ניסינו AI וזה לא עבד. למה שהפעם זה יהיה אחרת?","כי הפעם יש מישהו שיושב אצלכם. כלי AI לבד לא יודעים איך נראה כתב הכמויות שלכם, איפה נשמרים המסמכים, או מי צריך לאשר מה. הסטודנט לומד את זה מבפנים, ובונה את הכלים סביב העבודה האמיתית שלכם."),
      ("למה סטודנט ולא מהנדס בכיר?","כי מה שצריך כאן הוא מישהו חד, סקרן וזמין, שיושב אצלכם שלושה ימים בשבוע ולומד את העסק. הסטודנטים שלנו עוברים ראיונות, רק אחד מכל עשרה מתקבל, ואנחנו מלווים אותם לאורך כל הדרך."),
      ("מה לגבי סודיות המידע שלנו?","לפני תחילת העבודה חותמים על הסכם סודיות. הסטודנט עובד רק על המערכות והמסמכים שתאשרו לו."),
      ("צריך מחלקת IT או מערכות חדשות?","לא. הסטודנט עובד מעל מה שכבר יש לכם: אקסל, Priority, חשבשבת, מייל ותיקיות משותפות."),
      ("מה קורה אם הסטודנט לא מתאים?","מחליפים. ההתאמה בין הסטודנט לחברה היא באחריות שלנו.")],
 k_badge="בואו נדבר", k_h2="חצי שעה, ותדעו איפה הולך לכם הזמן",
 k_lead="פגישת היכרות ללא עלות, אצלכם במשרד או בטלפון. נבין איך אתם עובדים היום, ונגיד לכם איפה אפשר לחסוך הכי הרבה.",
 k_phone="טלפון", k_phone_v="058-4001054", k_wa="וואטסאפ", k_wa_v="שלחו הודעה", k_wa_text="היי נועם, אשמח לשמוע על Meetek",
 k_mail="מייל", k_mail_subj="פגישת היכרות עם Meetek",
 j_b="סטודנטים בטכניון?", j_t="מחפשים עבודה אמיתית עם השפעה, בחברות שבאמת צריכות אתכם? שלחו לנו קורות חיים.", j_btn="להגשת מועמדות", j_subj="מועמדות ל-Meetek",
 foot="הטמעת AI בחברות הנדסה, ביצוע ותשתיות", foot_other="English",
)

EN = dict(
 lang="en", dir="ltr", base="../", other="../", other_label="עב", other_lang="he",
 title="Meetek | AI implementation for engineering, construction and infrastructure firms",
 desc="Meetek places a top Technion engineering student in your company, 3 days a week, to find where the hours go and build the tools that give them back.",
 og_title="Meetek | AI that works in your office", og_locale="en_US", url="https://meetek.ai/en/", alt_href="https://meetek.ai/", alt_lang="he",
 skip="Skip to content", home="Meetek, back to top", nav_label="Main",
 nav=[("#work","What we do"),("#how","How it works"),("#students","Our students"),("#faq","FAQ")],
 theme_label="Toggle dark or light mode", cta_nav="Book a meeting",
 badge="Top Technion students, only 1 in 10 accepted",
 h1a="AI that works in your office.", h1b="Not just in a slide deck.",
 lead="Meetek places a top engineering student from the Technion in your company, 3 days a week. They learn how the work gets done today, find where the hours go, and build the tools that give those hours back.",
 cta1="Book a 30-minute intro", cta2="How it works",
 stats=[("users","1:10","only one in ten candidates is accepted"),("clock","3","days a week in your office"),("shield","0","hiring commitment")],
 p_badge="The problem", p_h2a="AI is often just", p_h2b="talk",
 p_lead="Everyone talks about artificial intelligence. Few companies actually use it in their day-to-day work.",
 pains=[("r","clock","You tried ChatGPT, and it stayed in a browser tab","The work itself stayed the same: spreadsheets, documents and copy-paste."),
        ("o","users","Nobody in the company knows where to start","Everyone is busy with day-to-day work, and there's no one to own this."),
        ("p","coins","Consultants give you a deck, but don't build","The recommendations stay on paper, and the processes don't change.")],
 callout_a="We don't hand you a roadmap.", callout_b="We sit in your office and build.",
 s_badge="What the student works on", s_h2a="The processes that", s_h2b="eat up your week",
 s_lead="The student starts with whatever hurts the most, and moves on from there.",
 services=[("doc","Tenders","Finding relevant tenders, summarizing each on a single page, checking threshold conditions and keeping an automatic document checklist."),
           ("calc","Bills of quantities and progress billing","Producing progress invoices straight from the bill of quantities and site measurements, without retyping everything each month."),
           ("chart","Forms, reports and site logs","Regulatory forms, client reports and daily site logs generated from data you already have."),
           ("link","Connecting your systems","ERP, accounting software, spreadsheets and email that talk to each other, instead of manual copy-paste."),
           ("checkbox","Reconciliation and invoices","Matching supplier invoices to orders and delivery notes, and catching anomalies before you pay."),
           ("grid","Internal tools","A profitability dashboard for every project, equipment tracking on site, and everything now scattered across ten spreadsheets.")],
 x_badge="A real-world example", x_h2a="This is what", x_h2b="a student's work looks like",
 x_lead="Take tenders. Instead of someone reading 200 pages, every tender arrives summarized on one page:",
 x_points=["What the job is, who the client is and when it's due","Whether you meet the threshold conditions","Which documents you already have and what's missing","Which clauses to review before you bid"],
 sample_tag="Example output", sample_title="One-page tender summary", sample_auto="Generated automatically",
 sample_rows=[("Client","Local municipality"),("Scope","Infrastructure renewal, phase A"),("Deadline","In 12 days"),("Required class","C3 or higher")],
 sample_checks=[("ok","✓","Meets threshold: classification and track record"),("ok","✓","9 of 13 documents already on file"),("warn","!","Missing: valid bookkeeping certificate and bid bond"),("warn","!","Unusual liquidated damages clause: worth a review")],
 sample_foot="Illustration only. This is what a typical output looks like when one of our students handles your tenders.",
 h_badge="How it works", h_h2a="From one meeting", h_h2b="to a student in your office",
 steps=[("search","Step 1","Intro meeting","We learn how you work today and where the time goes.","30 minutes, free"),
        ("handshake","Step 2","Student match","We pick the student who fits your field and your people.","From those who passed interviews"),
        ("bolt","Step 3","The first month","We map your processes and start with the one that saves the most.","Results early on"),
        ("rocket","Step 4","Ongoing support","We mentor the student, and replace them if needed.","3 days a week")],
 st_badge="Why we started Meetek", st_h2a="It started with", st_h2b="a real problem",
 quote=["\"I started working at an infrastructure company and found excellent engineers working like it was the 90s: paper, pen, and several rounds between people before a single document goes out. I built them a system, and a process that used to take days now takes minutes.",
        "That's when I realized there are hundreds of companies like this. And on the other side, there are brilliant Technion students looking for exactly this kind of challenge. Meetek connects the two.\""],
 avatar="N", who="Noam Ben Zimra", role="CEO and co-founder, Meetek",
 su_badge="Our students", su_h2a="Not just any student.", su_h2b="The right one.",
 su_who_h="Who they are", su_who="Engineering and computer science students at the Technion. We look for a rare combination: strong technical ability, the patience to understand how a business really works, and the ability to talk with people who don't come from tech.",
 pick_label="Out of ten candidates, one is accepted", pick_cap_b="1 in 10", pick_cap="candidates passes our interviews and is accepted",
 su_you_h="What this means for you", su_you=["The student is employed by Meetek. No recruiting, no onboarding paperwork, no hiring commitment.","They sit in your office 3 days a week and get to know your people and systems from the inside.","We mentor them professionally throughout.","If the fit isn't right, we replace them."],
 c_badge="Comparison", c_h2a="Why not just hire,", c_h2b="or bring in a consultant?",
 c_head=["Criteria","Hiring an employee","External consultant","Meetek"],
 c_rows=[("Commitment","Employment contract","Fixed project, high hourly rate","Pay by the hour, no long-term commitment"),
         ("On site","Yes","Usually not","3 days a week, in your office"),
         ("What you get","Depends on who you hired","Recommendations and a deck","Tools actually built and deployed"),
         ("If it doesn't fit","A termination process","End of project","We replace the student")],
 f_badge="FAQ", f_h2a="What people ask us", f_h2b="in the first meeting",
 faq=[("How much does it cost?","You pay for actual hours worked, with no setup fee and no long-term commitment. We'll give you the exact price in the intro meeting, once we understand what you need."),
      ("We tried AI and it didn't work. Why would this be different?","Because this time someone sits in your office. AI tools on their own don't know what your bill of quantities looks like, where documents are stored, or who signs off on what. The student learns all of that from the inside and builds the tools around your real work."),
      ("Why a student and not a senior engineer?","Because what you need here is someone sharp, curious and available, who sits with you three days a week and learns the business. Our students go through interviews, only one in ten is accepted, and we mentor them all the way."),
      ("What about the confidentiality of our data?","We sign a non-disclosure agreement before work begins. The student only works on the systems and documents you approve."),
      ("Do we need an IT department or new systems?","No. The student works on top of what you already use: spreadsheets, your ERP and accounting software, email and shared folders."),
      ("What if the student isn't a good fit?","We replace them. Getting the match right is our responsibility.")],
 k_badge="Let's talk", k_h2="30 minutes, and you'll know where your time goes",
 k_lead="A free intro meeting, at your office or by phone. We'll learn how you work today and tell you where you can save the most.",
 k_phone="Phone", k_phone_v="+972 58-400-1054", k_wa="WhatsApp", k_wa_v="Send a message", k_wa_text="Hi Noam, I'd like to hear about Meetek",
 k_mail="Email", k_mail_subj="Intro meeting with Meetek",
 j_b="Technion student?", j_t="Looking for real work with real impact, at companies that truly need you? Send us your CV.", j_btn="Apply", j_subj="Application to Meetek",
 foot="AI implementation for engineering, construction and infrastructure firms", foot_other="עברית",
)

def page(t):
    b = t["base"]
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in t["nav"])
    stats = "".join(f'<div class="stat reveal"><div class="ic">{ic(i)}</div><b>{n}</b><span>{s}</span></div>' for i, n, s in t["stats"])
    pains = "".join(f'<article class="pain {c} reveal"><div class="pi"><span>{ic("x",18,2.2)}</span><span>{ic(i,18)}</span></div><h3>{h}</h3><p>{p}</p></article>' for c, i, h, p in t["pains"])
    services = "".join(f'<article class="card reveal"><div class="ic">{ic(i)}</div><h3>{h}</h3><p>{p}</p></article>' for i, h, p in t["services"])
    points = "".join(f'<li><span class="tick">{ic("check",14,2.6)}</span>{p}</li>' for p in t["x_points"])
    srows = "".join(f'<dt>{a}</dt><dd>{v}</dd>' for a, v in t["sample_rows"])
    schecks = "".join(f'<li><span class="dot {c}" aria-hidden="true">{m}</span>{x}</li>' for c, m, x in t["sample_checks"])
    steps = "".join(f'<li class="step reveal"><div class="ic">{ic(i)}</div><small>{s}</small><h3>{h}</h3><p>{p}</p><span class="pill">{pl}</span></li>' for i, s, h, p, pl in t["steps"])
    quote = "".join(f"<p>{q}</p>" for q in t["quote"])
    dots = "".join('<span class="pd%s"></span>' % (" on" if k == 9 else "") for k in range(10))
    you = "".join(f'<li><span class="tick">{ic("check",14,2.6)}</span>{x}</li>' for x in t["su_you"])
    ch = t["c_head"]
    thead = f'<tr><th scope="col"><span class="sr-only">{ch[0]}</span></th><th scope="col">{ch[1]}</th><th scope="col">{ch[2]}</th><th scope="col" class="us">{ch[3]}</th></tr>'
    trows = "".join(f'<tr><td>{a}</td><td>{x}</td><td>{y}</td><td class="us">{z}</td></tr>' for a, x, y, z in t["c_rows"])
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t["faq"])
    wa = "https://wa.me/972584001054?text=" + quote_(t["k_wa_text"])
    mail = "mailto:noam@meetek.ai?subject=" + quote_(t["k_mail_subj"])
    jmail = "mailto:noam@meetek.ai?subject=" + quote_(t["j_subj"])
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta property="og:title" content="{t["og_title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{t["url"]}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta name="theme-color" content="#0A1020">
<link rel="alternate" hreflang="{t["alt_lang"]}" href="{t["alt_href"]}">
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}styles.css">
<script>try{{if(localStorage.getItem('meetek-theme')==='light')document.documentElement.removeAttribute('data-theme')}}catch(e){{}}</script>
</head>
<body class="no-js">
<div class="page-bg" aria-hidden="true"></div>
<a class="skip" href="#main">{t["skip"]}</a>

<header class="site" id="top">
  <div class="nav">
    <a class="brand" href="#top" aria-label="{t["home"]}">{LOGO}Meetek</a>
    <nav class="nav-links" aria-label="{t["nav_label"]}">{nav}</nav>
    <div class="nav-end">
      <a class="icon-btn" href="{t["other"]}" lang="{t["other_lang"]}" hreflang="{t["other_lang"]}">{t["other_label"]}</a>
      <button class="icon-btn theme" type="button" aria-label="{t["theme_label"]}"><span class="moon">{ic("moon",18)}</span><span class="sun">{ic("sun",18)}</span></button>
      <a class="btn btn-primary" href="#contact">{t["cta_nav"]}</a>
    </div>
  </div>
</header>

<main id="main">

<section class="hero">
  <span class="float-ic a">{ic("brain",34,1.6)}</span>
  <span class="float-ic b">{ic("rocket",30,1.6)}</span>
  <span class="float-ic c">{ic("sparkle",28,1.6)}</span>
  <div class="wrap center">
    <div class="reveal">
      <span class="badge">{ic("sparkle",16)}{t["badge"]}</span>
      <h1>{t["h1a"]}<br><span class="grad-text">{t["h1b"]}</span></h1>
      <p class="lead">{t["lead"]}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#contact">{t["cta1"]}<span class="arrow">{ic("arrow",18,2.2)}</span></a>
        <a class="btn btn-ghost" href="#how">{t["cta2"]}</a>
      </div>
    </div>
    <div class="stats">{stats}</div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("x",16,2.2)}{t["p_badge"]}</span>
      <h2>{t["p_h2a"]} <span class="grad-text">{t["p_h2b"]}</span></h2>
      <p class="lead">{t["p_lead"]}</p>
    </div>
    <div class="pains">{pains}</div>
    <p class="callout reveal">{t["callout_a"]} <b>{t["callout_b"]}</b></p>
  </div>
</section>

<section class="block" id="work" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("sparkle",16)}{t["s_badge"]}</span>
      <h2>{t["s_h2a"]} <span class="grad-text">{t["s_h2b"]}</span></h2>
      <p class="lead">{t["s_lead"]}</p>
    </div>
    <div class="cards">{services}</div>
  </div>
</section>

<section class="block" style="padding-top:0">
  <div class="wrap showcase">
    <div class="head reveal">
      <span class="badge">{ic("doc",16)}{t["x_badge"]}</span>
      <h2>{t["x_h2a"]} <span class="grad-text">{t["x_h2b"]}</span></h2>
      <p class="lead">{t["x_lead"]}</p>
      <ul>{points}</ul>
    </div>
    <aside class="sample reveal" aria-label="{t["sample_title"]}">
      <span class="sample-tag">{t["sample_tag"]}</span>
      <div class="sample-head"><strong>{t["sample_title"]}</strong><span>{t["sample_auto"]}</span></div>
      <dl>{srows}</dl>
      <ul class="checks">{schecks}</ul>
      <p class="sample-foot">{t["sample_foot"]}</p>
    </aside>
  </div>
</section>

<section class="block" id="how" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("bolt",16)}{t["h_badge"]}</span>
      <h2>{t["h_h2a"]} <span class="grad-text">{t["h_h2b"]}</span></h2>
    </div>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section class="block" style="padding-top:0">
  <div class="wrap">
    <div class="story reveal">
      <div class="head">
        <span class="badge">{ic("sparkle",16)}{t["st_badge"]}</span>
        <h2>{t["st_h2a"]} <span class="grad-text">{t["st_h2b"]}</span></h2>
      </div>
      <div>
        <blockquote>{quote}</blockquote>
        <cite><span class="avatar" aria-hidden="true">{t["avatar"]}</span><span><b>{t["who"]}</b>{t["role"]}</span></cite>
      </div>
    </div>
  </div>
</section>

<section class="block" id="students" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("users",16)}{t["su_badge"]}</span>
      <h2>{t["su_h2a"]} <span class="grad-text">{t["su_h2b"]}</span></h2>
    </div>
    <div class="students">
      <div class="panel reveal">
        <h3>{t["su_who_h"]}</h3>
        <p>{t["su_who"]}</p>
        <div class="pick" role="img" aria-label="{t["pick_label"]}">{dots}</div>
        <p class="pick-cap"><b>{t["pick_cap_b"]}</b> {t["pick_cap"]}</p>
      </div>
      <div class="panel reveal">
        <h3>{t["su_you_h"]}</h3>
        <ul>{you}</ul>
      </div>
    </div>
  </div>
</section>

<section class="block" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("chart",16)}{t["c_badge"]}</span>
      <h2>{t["c_h2a"]} <span class="grad-text">{t["c_h2b"]}</span></h2>
    </div>
    <div class="table-wrap reveal"><table><thead>{thead}</thead><tbody>{trows}</tbody></table></div>
  </div>
</section>

<section class="block" id="faq" style="padding-top:0">
  <div class="wrap">
    <div class="head reveal">
      <span class="badge">{ic("chat",16)}{t["f_badge"]}</span>
      <h2>{t["f_h2a"]} <span class="grad-text">{t["f_h2b"]}</span></h2>
    </div>
    <div class="faq reveal">{faq}</div>
  </div>
</section>

<section class="block" style="padding-top:0">
  <div class="wrap">
    <div class="contact reveal" id="contact">
      <div>
        <span class="badge">{ic("chat",16)}{t["k_badge"]}</span>
        <h2>{t["k_h2"]}</h2>
        <p class="lead">{t["k_lead"]}</p>
      </div>
      <div class="contact-list">
        <a href="tel:+972584001054"><span><small>{t["k_phone"]}</small><strong>{t["k_phone_v"]}</strong></span><span class="ic">{ic("phone",20)}</span></a>
        <a href="{wa}" target="_blank" rel="noopener"><span><small>{t["k_wa"]}</small><strong>{t["k_wa_v"]}</strong></span><span class="ic">{ic("chat",20)}</span></a>
        <a href="{mail}"><span><small>{t["k_mail"]}</small><strong>noam@meetek.ai</strong></span><span class="ic">{ic("mail",20)}</span></a>
      </div>
    </div>
    <div class="join reveal">
      <p><b>{t["j_b"]}</b> {t["j_t"]}</p>
      <a class="btn btn-ghost" href="{jmail}">{t["j_btn"]}</a>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <a class="brand" href="#top" aria-label="Meetek">{LOGO}Meetek</a>
    <span>{t["foot"]} · <a href="mailto:noam@meetek.ai">noam@meetek.ai</a></span>
    <span>© <span id="y">2026</span> Meetek · <a href="{t["other"]}" lang="{t["other_lang"]}">{t["foot_other"]}</a></span>
  </div>
</footer>

<script src="{b}site.js"></script>
</body>
</html>
'''

def quote_(s):
    return quote(s, safe="")

os.makedirs(OUT + "/en", exist_ok=True)
open(OUT + "/index.html", "w").write(page(HE))
open(OUT + "/en/index.html", "w").write(page(EN))
print("ok")

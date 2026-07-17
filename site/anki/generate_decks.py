#!/usr/bin/env python3
"""Generate Anki decks for Development & Aging lectures."""

from pathlib import Path
import genanki
import random

OUT = Path(__file__).resolve().parent

MODEL = genanki.Model(
    1607392319,
    "BRS Basic",
    fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Source"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "<div style='font-family: Georgia, serif; font-size: 22px;'>{{Question}}</div>",
            "afmt": "{{FrontSide}}<hr id='answer'><div style='font-family: Georgia, serif; font-size: 20px;'>{{Answer}}</div>"
            "<div style='margin-top:12px;font-size:12px;color:#666;font-family:sans-serif;'>{{Source}}</div>",
        }
    ],
    css="""
    .card { background: #f2f6f8; color: #0c1f2e; text-align: left; padding: 1.2em; }
    """,
)


def deck(deck_id: int, name: str, cards: list[tuple[str, str]], source: str) -> genanki.Deck:
    d = genanki.Deck(deck_id, name)
    for q, a in cards:
        note = genanki.Note(model=MODEL, fields=[q, a, source])
        d.add_note(note)
    return d


# ---------------------------------------------------------------------------
# 1.1–1.2 Disorders of Pregnancy & Parturition
# ---------------------------------------------------------------------------
cards_112 = [
    ("What is histiotrophic nutrition?", "Early embryo nutrition: feeding on tissue — breaks down endometrium and uses uterine gland secretions via syncytiotrophoblast."),
    ("Why is early nutrition called “histiotrophic”?", "Histio = tissue; trophic = feeding."),
    ("What nutritional switch occurs from 1st to 2nd trimester, and why?", "Histiotrophism → haemotrophism, because histiotrophic nutrition cannot sustain the growing fetus."),
    ("Through what structure is haemotrophism achieved?", "A haemochorial-type placenta."),
    ("What is a haemochorial placenta?", "A placenta where maternal blood is in direct contact with fetal membranes."),
    ("What placental adaptation enables fetal–maternal exchange?", "Chorionic villi — finger-like chorion protrusions contacting maternal circulation."),
    ("How does the fetus cope with rising O₂/nutrient demand?", "Increasing branching of chorionic villi → greater exchange surface area."),
    ("Difference between cytotrophoblast and syncytiotrophoblast?", "Cytotrophoblast = source population; syncytiotrophoblast = invasive cells that invade endometrium for implantation."),
    ("What two populations form from the inner cell mass peri-implantation?", "Epiblast and hypoblast."),
    ("Epiblast vs hypoblast roles?", "Epiblast → fetal tissues; hypoblast → some extra-embryonic cells (yolk sac) for early gas/nutrient support."),
    ("When does bilaminar disc formation occur?", "Around day 12; creates amniotic cavity, ready for gastrulation."),
    ("What are intervillous spaces (lacunae)?", "Maternal placental regions around chorionic villi enabling mother–fetus exchange."),
    ("Role of spiral artery remodelling?", "De-spiralise/broaden arteries, ↓ resistance, supply lacunae to meet fetal demand."),
    ("What is the chorion?", "Surrounding cell layer of the early conceptus/embryo."),
    ("Stages of chorionic villus formation?", "Primary: cytotrophoblast outgrowth/branching. Secondary: fetal mesoderm grows in. Tertiary: umbilical artery/vein invade mesoderm."),
    ("How do villi change from early to late pregnancy?", "Early: ~150–200 µm diameter, ~10 µm trophoblast thickness. Late: villi thin to ~40 µm; vessels leave only 1–2 µm separation from maternal blood."),
    ("Which cells coat villi and remodel spiral arteries?", "Extra-villous trophoblast (EVT) cells."),
    ("How does spiral artery conversion work?", "EVT invade arteries → endovascular EVT; endothelium & smooth muscle broken down; EVT coat lumen → low-pressure, high-capacity conduit; ECM replaced with fibrinoid."),
    ("EVT vs endovascular EVT?", "EVT originate in cytotrophoblast then invade; once inside the artery coating the lumen they are endovascular EVT."),
    ("Features of failed spiral artery conversion?", "Retained smooth muscle; immune cells embedded in wall; RBC occlusion; intimal hyperplasia; atherosis; hypoxia; inefficient substrate delivery."),
    ("Define pre-eclampsia.", "New-onset hypertension after 20 weeks in previously normotensive woman: BP ≥140 systolic and/or ≥90 diastolic."),
    ("What is eclampsia?", "Onset of seizures in a woman with pre-eclampsia."),
    ("Early vs late-onset pre-eclampsia?", "Early (before 34 weeks): fetal+maternal symptoms, placental changes. Late (after 34 weeks, ~90%): mostly maternal, fetus usually OK, less placental change."),
    ("Clinical features of pre-eclampsia?", "↓ Fetal movement ± amniotic fluid (~30%); proteinuria; oedema (non-discriminatory); headache (~40% severe); abdominal pain (~15%); visual disturbance/seizures/breathlessness in severe PE."),
    ("What is HELLP syndrome?", "Life-threatening PE variant: Haemolysis, Elevated Liver enzymes, Low Platelets."),
    ("Maternal risks of PE?", "Damage to kidneys/liver/brain; eclampsia; HELLP; placental abruption."),
    ("Fetal risks of PE?", "Preterm birth; IUGR; pregnancy loss/stillbirth."),
    ("What is wrong with spiral artery conversion in PE?", "EVT invasion limited to decidual/endometrial layer — not deep enough into myometrium → restricted perfusion → placental ischaemia."),
    ("Decidua vs endometrium?", "Decidua is a specialised temporary lining formed from the endometrium."),
    ("What is PlGF?", "Placental growth factor — VEGF-family pro-angiogenic factor released in large amounts by the placenta."),
    ("What is sFlt1 (soluble VEGFR1)?", "Soluble receptor that binds VEGF-like factors (e.g. PlGF), limiting their bioavailability."),
    ("How is sFlt1/PlGF altered in PE?", "↓ PlGF, ↑ sFlt1 → ↑ sFlt1/PlGF ratio → endothelial dysfunction."),
    ("Healthy vs PE placenta regarding PlGF/VEGF?", "Healthy releases PlGF/VEGF that bind endothelial receptors (vasodilation, healthy endothelium). PE releases sFlt1 that mops up PlGF/VEGF → endothelial dysfunction."),
    ("What are extracellular vesicles?", "Nano-scale lipid-bilayer vesicles (exosomes, microvesicles, etc.) carrying mRNA, miRNA, proteins, lipids; released especially when cells are stressed/dying."),
    ("EV changes in PE?", "Overall ↑ EVs; ↑ endothelial-derived EVs; ↓ placenta-derived EVs (cargo may still be harmful)."),
    ("Main source of placenta-derived EVs?", "Syncytiotrophoblasts (SDEVs)."),
    ("Proposed EV mechanism in PE?", "Placental ischaemia → trophoblast apoptosis → EVs enter maternal circulation → endothelial dysfunction, inflammation, hypercoagulation."),
    ("Effect of severe PE EVs on vessels?", "Inhibit vasorelaxation of mouse aorta; inhibit endothelial eNOS (needed for NO-mediated dilation)."),
    ("Theory for late-onset PE?", "Little reduced spiral conversion; maternal genetic predisposition to CVD unmasked by pregnancy as a cardiovascular “stress test”."),
    ("Consequences of placental ischaemia leading to systemic PE signs?", "↑ sFlt1 and sEng → systemic vascular dysfunction → proteinuria, hypertension, visual/headache/seizures, HELLP/coagulopathy."),
]

# ---------------------------------------------------------------------------
# 1.3 Early Environmental Impacts
# ---------------------------------------------------------------------------
cards_13 = [
    ("What are early life impacts?", "Profound lasting effects of childhood (and prenatal) experiences on lifelong physical, mental, and emotional wellbeing."),
    ("List in-utero challenges that can affect lifelong health.", "Fetal infection; maternal under/overnutrition; maternal illness, stress, medication; environmental exposures."),
    ("What is the DOHaD hypothesis (Barker pattern)?", "Link between early growth and later coronary risk: small at birth, thin at 2 years, then rapid weight gain; risk related more to rate of childhood BMI change than BMI at any age."),
    ("Pathway from fetal undernutrition to CV risk?", "Undernutrition in utero → overnutrition in childhood → metabolic syndrome → ↑ cardiovascular events."),
    ("What is metabolic syndrome?", "Cluster of HTN, hyperglycaemia, central obesity, dyslipidaemia increasing risk of heart disease, stroke, and T2DM."),
    ("What is fetal programming?", "Programming the fetus by environmental stimuli in the womb in preparation for particular later-life conditions."),
    ("What are predictive adaptive responses (PARs)?", "Developmental adaptations anticipating a future environment; they don’t benefit the fetus immediately."),
    ("How can PAR mismatch cause later disease?", "If postnatal environment differs from that predicted (e.g. scarcity programmed then nutrient-rich childhood), the organism is maladapted → higher disease risk."),
    ("Example of PAR mismatch?", "Maternal malnutrition → SGA + PARs for nutrient-poor world → child in nutrient-rich environment → overweight."),
    ("Factors that may negatively impact fetal developmental responses?", "Maternal health/environment; nutrient demand > supply; endocrine environment; placental vascular supply."),
    ("Fetal developmental responses to in-utero environment?", "Altered endocrinology/metabolism; changes in bone/lean/fat mass; altered blood flow/vascular loading; altered immune responses."),
    ("Three main mechanisms of fetal programming?", "Hormonal effects (esp. glucocorticoids); epigenetic modifications; irreversible changes in organ size/structure."),
    ("What enzyme regulates fetal glucocorticoid exposure?", "11β-hydroxysteroid dehydrogenase 2 (11β-HSD2)."),
    ("How does 11β-HSD2 protect the fetus?", "Converts cortisol → inactive cortisone."),
    ("Effect of reduced 11β-HSD2 or increased maternal GCs?", "Greater fetal GC exposure → programmes growth, development, metabolism; HPA dysregulation; altered GC receptor expression."),
    ("What is an epigenetic change?", "Modification of gene expression without changing DNA sequence."),
    ("Three types of epigenetic change?", "DNA methylation; post-translational histone modification; non-coding RNAs."),
    ("Can epigenetic changes be passed down?", "Yes — acquired epigenetic changes can be transmitted across generations."),
    ("Downstream effects of fetal epigenomic changes?", "FGR; ↑ energy storage → obesity; metabolic adaptations → DM; fewer terminally differentiated cardiomyocytes (HTN/CVD) or neurons (stroke, schizophrenia, depression, cognitive dysfunction)."),
    ("Key vulnerable epigenetic windows?", "Gametogenesis; early development (erasure/re-patterning); organogenesis & fetal growth; also postnatal/adulthood/ageing."),
    ("Fetal hypoxia → adult disease pathway?", "↓ Nephron number → ↑ risk of hypertension/renal disease in adulthood."),
    ("Fetal undernutrition → adult metabolic disease pathway?", "↓ β-cell mass / altered muscle insulin sensitivity → impaired glucose control in adulthood."),
    ("What are primordial germ cells (PGCs)?", "Embryonic precursors of oocytes and spermatozoa."),
    ("How can PGC changes affect the next generation?", "PGCs undergo epigenetic reprogramming and give rise to gametes that transmit marks to offspring; sensitive to diet/pharmaceuticals."),
]

# ---------------------------------------------------------------------------
# 1.4 Postnatal & Child Development
# ---------------------------------------------------------------------------
cards_14 = [
    ("Role of fetal vs maternal genetics in prenatal growth?", "Fetal genetics minor; maternal factors (esp. maternal size) dominate birth size; paternal genetics little effect on birth."),
    ("Role of genetics postnatal?", "Largely determine final adult height; sex chromosomes — XY boys taller than XX girls on average."),
    ("Prenatal vs postnatal genetic influence summary?", "Prenatally maternal genetics dominate; postnatally fetal genetics play the largest role."),
    ("Most important hormone for embryonic growth?", "IGF-2."),
    ("Most important hormone for later fetal/infant growth?", "IGF-1."),
    ("Most important hormone for postnatal growth?", "Human growth hormone (hGH)."),
    ("Endocrine switch prenatal → postnatal?", "IGF-2 → IGF-1 → hGH."),
    ("Most common cause of IUGR?", "Placental insufficiency."),
    ("Placental function vs uterine capacity for fetal growth?", "Placental function is more influential than uterine capacity."),
    ("Effects of postnatal nutrition extremes?", "Poor nutrition may delay puberty; starvation limits growth potential; malabsorption → reduced growth; excess → obesity."),
    ("Head:body proportion at birth vs adulthood?", "Head ~1/3 of body length at birth vs ~1/7 in adulthood."),
    ("When do cranial sutures open and close?", "Open at birth; close by ~18 months."),
    ("Four recognised phases of growth?", "Fetal; infantile; childhood; pubertal."),
    ("Which growth phase is fastest and what % of adult height?", "Fetal — ~30% of eventual height; driven mainly by hyperplasia (~42 cell-division cycles before birth vs ~5 more after)."),
    ("Infantile phase timing, % height, key stats?", "0–18 months; ~15% height; length ↑50%, head circ ↑30%, weight triples; largely nutrition-dependent."),
    ("Childhood phase timing and growth rates?", "18 months–12 years; ~40% height; ~5–6 cm/year height, ~3–3.5 kg/year weight."),
    ("Pubertal phase contribution and drivers?", "~15% height; sex hormones boost hGH; ~25 cm boys / ~20 cm girls spurt; sex hormones also fuse growth plates → adult height."),
    ("What is mini-puberty?", "Transient postnatal HPG reactivation after release from placental hormone restraint; lasts ~6 months."),
    ("Why is mini-puberty important in males?", "Elevated sex steroids support testicular tissue and penile development; may contribute to higher early male growth velocity."),
    ("Pathway thought to drive puberty onset?", "KNDy neurons → kisspeptin → GnRH neurons → pulsatile GnRH; KISS1R mutations alter puberty timing."),
    ("What is consonance in puberty?", "Compliance with the predictable sequence of pubertal developmental events."),
    ("What is menarche and how has its age changed?", "First menstruation; age fell ~4 years 1850–1960, then ~3 months per decade 1977–2013."),
    ("Four major developmental domains?", "Gross motor; fine motor; speech/language/hearing; social/behavioural."),
    ("Gross motor: sits without support?", "6–8 months."),
    ("Gross motor: walks steadily?", "15 months."),
    ("Fine motor: mature pincer grip?", "10 months."),
    ("Fine motor: when can a child draw a circle / square / triangle?", "Circle ~3 y; square ~4 y; triangle ~5 y."),
    ("Language: 2–3 words other than dada/mama?", "Around 12 months."),
    ("Language: 3–4 word sentences constantly?", "Around 2.5–3 years."),
]


def main():
    decks = [
        (1607392320, "BRS::Development & Aging::1.1-1.2 Disorders of Pregnancy", cards_112,
         "1.1-1.2 Disorders of Pregnancy & Parturition I-II",
         "1.1-1.2-disorders-of-pregnancy.apkg"),
        (1607392321, "BRS::Development & Aging::1.3 Early Environmental Impacts", cards_13,
         "1.3 Early Environmental & Biological Impacts on Lifelong Health",
         "1.3-early-environmental-impacts.apkg"),
        (1607392322, "BRS::Development & Aging::1.4 Postnatal & Child Development", cards_14,
         "1.4 Postnatal & Child Development",
         "1.4-postnatal-child-development.apkg"),
    ]

    for deck_id, name, cards, source, filename in decks:
        # stable note IDs via seeded shuffle not needed; genanki handles GUIDs from fields
        d = deck(deck_id, name, cards, source)
        path = OUT / filename
        genanki.Package(d).write_to_file(path)
        print(f"{filename}: {len(cards)} cards → {path}")


if __name__ == "__main__":
    main()

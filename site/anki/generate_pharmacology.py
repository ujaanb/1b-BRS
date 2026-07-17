#!/usr/bin/env python3
"""Build Pharmacology & Therapeutics note pages + Anki decks.

Anki decks are named by the disease the drugs treat (per curator request),
while site lecture pages keep the full lecture title.
"""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import html
import genanki

SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
TOPIC = "pharmacology-and-therapeutics"
TOPIC_NAME = "Pharmacology & Therapeutics"
TOPIC_DIR = SITE / "topics" / TOPIC
ANKI_DIR = SITE / "anki"
TOPIC_DIR.mkdir(parents=True, exist_ok=True)

MODEL = genanki.Model(
    1607392319,
    "BRS Basic",
    fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Source"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "<div style='font-family: Georgia, serif; font-size: 22px;'>{{Question}}</div>",
        "afmt": "{{FrontSide}}<hr id='answer'><div style='font-family: Georgia, serif; font-size: 20px;'>{{Answer}}</div>"
                "<div style='margin-top:12px;font-size:12px;color:#666;font-family:sans-serif;'>{{Source}}</div>",
    }],
    css=".card { background: #f2f6f8; color: #0c1f2e; text-align: left; padding: 1.2em; }",
)

# Each lecture: full lecture id/title, disease deck name, deck file/id, and
# sections of (heading, [(question, answer_html), ...]).
LECTURES = [
    {
        "id": "1.2",
        "title": "1.2 Pharmacology of Diabetes",
        "slug": "pharmacology-of-diabetes",
        "disease": "Diabetes",
        "deck_file": "diabetes.apkg",
        "deck_id": 1607392710,
        "sections": [
            ("Metformin", [
                ("Recall four drugs used in the management of diabetes.", "<ul><li>Metformin</li><li>DPP-4 inhibitors</li><li>Sulphonylureas</li><li>SGLT-2 inhibitors</li></ul>"),
                ("Describe the primary mechanism of action of metformin.", "<ul><li>Activates AMPK in hepatocyte mitochondria.</li><li>Inhibits ATP production, blocking gluconeogenesis and glucose output.</li><li>Also blocks adenylate cyclase, promoting fat oxidation. Both effects help restore insulin sensitivity.</li></ul>"),
                ("What is the drug target for metformin?", "5'-AMP-activated protein kinase (AMPK) in hepatocyte mitochondria."),
                ("Describe the main side effects of metformin.", "<ul><li>GI side effects in 20–30% of patients (abdominal pain, decreased appetite, diarrhoea, vomiting).</li><li>Particularly evident at very high doses.</li></ul>"),
                ("How can the side effects of metformin be reduced?", "A slow increase in dose may improve tolerability."),
                ("Describe the polarity of metformin and how it accesses tissues.", "Metformin is highly polar, so it requires organic cation transporter-1 (OCT-1) to access tissues."),
                ("Why is metformin's transport mechanism significant?", "Because it depends on OCT-1 to enter tissues, it accumulates in the liver (therapeutic effect) and the GI tract (side effects)."),
                ("When is metformin most effective?", "In the presence of endogenous insulin, so it works best with some residual functioning pancreatic islet cells."),
            ]),
            ("DPP-4 inhibitors", [
                ("What is the role of dipeptidyl-peptidase 4 (DPP-4)?", "An enzyme in vascular endothelium that metabolises incretins in the plasma."),
                ("What is an incretin?", "A hormone that increases insulin secretion when glucose is taken orally versus intravenously (the \"incretin effect\"). Incretins are released from the small intestine after eating."),
                ("What is the role of incretins such as GLP-1?", "Secreted by enteroendocrine cells; stimulate insulin production when needed (after eating), reduce hepatic glucagon production when not needed, slow digestion, and decrease appetite."),
                ("Recall an example of a DPP-4 inhibitor.", "Sitagliptin."),
                ("Describe the mechanism of action of DPP-4 inhibitors.", "They inhibit the action of DPP-4. The primary site of action is the vascular endothelium."),
                ("What is the drug target of DPP-4 inhibitors?", "DPP-4 (at the vascular endothelium)."),
                ("Describe the main side effects of DPP-4 inhibitors.", "<ul><li>Upper respiratory tract infections (~5% of patients).</li><li>Flu-like symptoms (headache, runny nose, sore throat).</li></ul>"),
                ("Describe the less common but serious side effects of DPP-4 inhibitors.", "Serious allergic reactions; avoid in patients with pancreatitis."),
                ("What is an advantage of DPP-4 inhibitors over other anti-diabetic drugs?", "Compared with other anti-diabetic drugs (though not metformin), they do not appear to cause weight gain."),
                ("What condition must generally be met for DPP-4 inhibitors to work?", "They augment insulin secretion, so they are effective only when some residual pancreatic beta-cell activity is present."),
            ]),
            ("Sulphonylureas", [
                ("Recall an example of a sulphonylurea.", "Gliclazide."),
                ("Describe the primary mechanism of action of sulphonylureas.", "<ul><li>Inhibit the ATP-sensitive potassium (K_ATP) channel on the pancreatic beta cell.</li><li>Channel closure prevents K+ efflux, depolarising the membrane.</li><li>Depolarisation triggers Ca2+ influx and insulin vesicle exocytosis.</li></ul>"),
                ("What is the drug target of sulphonylureas?", "The ATP-sensitive potassium channel."),
                ("Describe the main side effects of sulphonylureas.", "<ul><li>Weight gain (likely).</li><li>Hypoglycaemia (2nd most common).</li></ul>"),
                ("What condition must generally be met for sulphonylureas to work?", "They augment insulin secretion, so they are effective only when some residual pancreatic beta-cell activity is present."),
                ("How can weight gain caused by sulphonylureas be mitigated?", "By concurrent administration with metformin."),
            ]),
            ("SGLT-2 inhibitors", [
                ("Recall an example of an SGLT-2 inhibitor.", "Dapagliflozin."),
                ("Describe the mechanism of action of SGLT-2 inhibitors.", "Reversibly inhibit SGLT-2 in the renal proximal convoluted tubule, reducing glucose reabsorption and increasing urinary glucose excretion."),
                ("What is the drug target of SGLT-2 inhibitors?", "The SGLT-2 co-transporter in the proximal convoluted tubule."),
                ("Describe the main side effects of SGLT-2 inhibitors.", "<ul><li>Urogenital infections due to increased glucose load (~5% of patients).</li><li>Slight decrease in bone formation.</li><li>Can worsen diabetic ketoacidosis (stop immediately).</li></ul>"),
                ("Describe another effect of SGLT-2 inhibitors.", "They cause weight loss and a reduction in blood pressure."),
                ("What condition must generally be met for SGLT-2 inhibitors to work?", "Their action depends on normal renal function, so they are less effective in renal impairment."),
            ]),
        ],
    },
    {
        "id": "1.4",
        "title": "1.4 Pharmacology of Parkinson's Disease",
        "slug": "pharmacology-of-parkinsons-disease",
        "disease": "Parkinson's Disease",
        "deck_file": "parkinsons-disease.apkg",
        "deck_id": 1607392711,
        "sections": [
            ("Overview", [
                ("What is Parkinson's disease?", "A progressive brain condition that causes movement problems, mental health issues, and other health concerns."),
                ("What happens to the brain in Parkinson's disease?", "Degeneration of the dopaminergic neurons originating in the substantia nigra and projecting to the striatum."),
                ("Recall four drug classes used to treat Parkinson's disease.", "<ul><li>Dopamine precursors</li><li>Dopa decarboxylase inhibitors</li><li>Dopamine receptor agonists</li><li>Local anaesthetics</li></ul>"),
            ]),
            ("Dopamine precursors", [
                ("Recall two examples of dopamine precursors.", "Levodopa and fos-levodopa."),
                ("Describe the mechanism of action of dopamine precursors.", "<ul><li>Levodopa is taken up at the terminals of nigrostriatal neurones.</li><li>It is decarboxylated to dopamine by dopa decarboxylase.</li><li>This compensates for the loss of endogenous dopamine in nigrostriatal neurones.</li></ul>"),
                ("How else can levodopa be thought of?", "As a prodrug for dopamine."),
                ("What is the drug target for levodopa?", "No classical target; once converted to dopamine, the targets are the dopamine receptors."),
                ("Recall the side effects of levodopa.", "Nausea and vomiting, dizziness, headache, GI discomfort, somnolence, dyskinesias."),
                ("How can somnolence present with levodopa?", "Onset can be rapid and without warning, so caution is needed while driving."),
                ("What is fos-levodopa?", "A phosphate pro-drug of levodopa."),
                ("What is the advantage of fos-levodopa?", "It is more water soluble than levodopa, making it more suitable for constant subcutaneous infusion."),
                ("What are the effects of rapid withdrawal of levodopa?", "It can lead to neuroleptic malignant syndrome."),
                ("What is neuroleptic malignant syndrome?", "A rare, potentially life-threatening reaction to dopamine-blocking drugs (or dopamine-agonist withdrawal), with high fever, muscle rigidity, altered mental status, and autonomic instability."),
            ]),
            ("Dopa decarboxylase inhibitors", [
                ("What does dopa decarboxylase do?", "Catalyses dopa → dopamine."),
                ("Recall two dopa decarboxylase inhibitors.", "Carbidopa and benserazide."),
                ("Describe the mechanism of action of dopa decarboxylase inhibitors.", "<ul><li>Block the dopa decarboxylase enzyme, preventing conversion of dopa to dopamine.</li><li>They cannot enter the brain, acting only peripherally, so they reduce peripheral dopamine side effects such as nausea.</li></ul>"),
                ("What is the drug target of dopa decarboxylase inhibitors?", "The dopa decarboxylase enzyme."),
                ("Recall the main side effects of dopa decarboxylase inhibitors.", "Dyskinesias (facial twitching, head bobbing), vitamin deficiencies (B3 & B6), peripheral monoamine depletion."),
                ("What is the maximum dose of carbidopa?", "200 mg."),
                ("Why is it hard to identify adverse effects specific to carbidopa?", "Carbidopa is rarely given alone, making it difficult to attribute specific adverse effects to it."),
            ]),
            ("Dopamine receptor agonists", [
                ("Recall two dopamine receptor agonists.", "Ropinirole and rotigotine."),
                ("Describe the mechanism of action of dopamine receptor agonists.", "They bind post-synaptic dopamine receptors independently of dopaminergic neurone activation."),
                ("What is the drug target of dopamine receptor agonists?", "Dopamine receptors (D2/D3 receptors are key targets in Parkinson's disease)."),
                ("Recall the side effects of dopamine receptor agonists.", "Nausea and vomiting, dizziness, headache, GI discomfort, somnolence, hallucinations, dyskinesias."),
                ("How are dopamine receptor agonists administered?", "Usually as add-on therapy with levodopa; as add-ons they are not within the top 250 most prescribed drugs."),
                ("What is special about newer dopamine receptor agonists?", "They are more selective for D2/D3 receptors."),
                ("What is the significance of D3 receptor stimulation?", "D3 receptors mediate drug-seeking behaviour, so these drugs are more associated with impulsivity and compulsive gambling."),
                ("Describe the use of anti-Parkinson's drugs in the NHS.", "They are not usually prescribed in primary care, so they are less commonly prescribed than other drugs."),
            ]),
            ("Local anaesthetics", [
                ("Describe the mechanism of action of local anaesthetics.", "The uncharged form diffuses through the neurone and binds the sodium channel from the inside, locking it open and preventing depolarisation."),
                ("Recall an example of a local anaesthetic.", "Lidocaine."),
                ("What is the drug target of local anaesthetics?", "Voltage-gated sodium channels."),
                ("Recall the side effects of local anaesthetics.", "Mild: redness/swelling at injection site, numbness. Severe toxicity (uncommon): fear/anxiety, anaphylaxis."),
                ("What reduces the efficacy of lidocaine, and why?", "Inflammation: the lower pH keeps basic lidocaine in a more charged state, so less can diffuse across neurones."),
                ("What is an alternative function of lidocaine?", "It is a class Ib anti-arrhythmic, slowing cardiac conduction by decreasing sodium-channel permeability to sodium."),
            ]),
        ],
    },
    {
        "id": "1.6",
        "title": "1.6 Pharmacology of Depression",
        "slug": "pharmacology-of-depression",
        "disease": "Depression",
        "deck_file": "depression.apkg",
        "deck_id": 1607392712,
        "sections": [
            ("Overview", [
                ("Recall five drugs used to treat depression.", "Sertraline, citalopram, fluoxetine, venlafaxine, mirtazapine."),
                ("Describe the effects of serotonin.", "In the CNS, serotonin helps regulate mood, personality, and wakefulness."),
            ]),
            ("SSRIs (sertraline, citalopram, fluoxetine)", [
                ("Describe the primary mechanism of action of sertraline.", "Inhibits serotonin reuptake, causing serotonin accumulation (serotonin regulates mood, personality, and wakefulness)."),
                ("What is the drug target of sertraline?", "The serotonin transporter."),
                ("Recall the main side effects of sertraline.", "GI effects (nausea, diarrhoea), sexual dysfunction, anxiety, insomnia."),
                ("Describe an additional function of sertraline.", "Mild inhibition of the dopamine transporter."),
                ("What consideration is needed for patients on sertraline?", "Taper gradually on discontinuation; partial CYP2D6 inhibition at high doses (150 mg)."),
                ("Describe the primary mechanism of action of citalopram.", "Inhibits serotonin reuptake, causing serotonin accumulation."),
                ("What is the drug target of citalopram?", "The serotonin transporter."),
                ("Recall the main side effects of citalopram.", "GI effects (nausea, diarrhoea), sexual dysfunction, anxiety, insomnia."),
                ("Describe an additional function of citalopram.", "Mild antagonism of muscarinic and histamine (H1) receptors."),
                ("What consideration is needed for patients on citalopram?", "Taper gradually on discontinuation; metabolised by CYP2C19."),
                ("Describe the primary mechanism of action of fluoxetine.", "Inhibits serotonin reuptake, causing serotonin accumulation."),
                ("What is the drug target of fluoxetine?", "The serotonin transporter."),
                ("Recall the main side effects of fluoxetine.", "GI effects (nausea, diarrhoea), sexual dysfunction, anxiety, insomnia."),
                ("Describe an additional function of fluoxetine.", "Mild antagonism of 5-HT2A and 5-HT2C receptors."),
                ("What consideration is needed for patients on fluoxetine?", "Complete CYP2D6 inhibition and significant CYP2C19 inhibition (caution with warfarin)."),
            ]),
            ("Venlafaxine (SNRI)", [
                ("Describe the primary mechanism of action of venlafaxine.", "A more potent inhibitor of serotonin than noradrenaline reuptake, but it inhibits both; noradrenaline in the CNS regulates emotions and cognition."),
                ("What is the drug target of venlafaxine?", "The serotonin transporter and the noradrenaline transporter."),
                ("Recall the main side effects of venlafaxine.", "GI effects (nausea, diarrhoea), sexual dysfunction, anxiety, insomnia, and hypertension at higher doses."),
                ("What consideration is needed for patients on venlafaxine?", "Taper gradually on discontinuation."),
            ]),
            ("Mirtazapine", [
                ("Describe the primary mechanism of action of mirtazapine.", "<ul><li>Antagonises central presynaptic alpha-2 adrenergic receptors, increasing serotonin and noradrenaline release.</li><li>Antagonises central 5-HT2 receptors, leaving 5-HT1 unopposed for antidepressant effects.</li></ul>"),
                ("What is the drug target of mirtazapine?", "The alpha-2 receptor and the 5-HT2 receptor."),
                ("What does the alpha-2 receptor do?", "Mainly inhibits noradrenaline release, reducing sympathetic outflow and causing sedation, hypotension, and analgesia, especially in the CNS."),
                ("What does the 5-HT2 receptor do?", "It is a serotonin receptor that modulates mood, perception, vascular tone, and appetite."),
                ("Recall the main side effects of mirtazapine.", "Weight gain and sedation."),
                ("Describe additional facts about mirtazapine.", "Low probability of sexual dysfunction; may exacerbate REM sleep behaviour disorder."),
                ("Which antidepressants need to be gradually decreased on discontinuation?", "Sertraline, citalopram, fluoxetine, and venlafaxine."),
            ]),
        ],
    },
    {
        "id": "1.8",
        "title": "1.8 Pharmacology of Hypertension",
        "slug": "pharmacology-of-hypertension",
        "disease": "Hypertension",
        "deck_file": "hypertension.apkg",
        "deck_id": 1607392713,
        "sections": [
            ("ACE inhibitors", [
                ("Recall four drug classes used to treat hypertension.", "<ul><li>ACE inhibitors</li><li>Calcium channel blockers</li><li>Thiazide/thiazide-like diuretics</li><li>Angiotensin receptor blockers (ARBs)</li></ul>"),
                ("Recall two ACE inhibitors.", "Ramipril and lisinopril (also perindopril)."),
                ("Describe the primary mechanism of action of ACE inhibitors.", "Inhibit the angiotensin-converting enzyme, preventing conversion of angiotensin I to angiotensin II."),
                ("What is the drug target of ACE inhibitors?", "Angiotensin-converting enzyme (ACE)."),
                ("Recall the main side effects of ACE inhibitors.", "Cough, hypotension, hyperkalaemia (care with K+ supplements/K+-sparing diuretics), fetal injury (avoid in pregnancy), renal failure (in renal artery stenosis), urticaria/angioedema."),
                ("Describe two additional facts about ACE inhibitors.", "Most (not lisinopril) are pro-drugs needing hepatic activation; eGFR and serum potassium must be monitored regularly."),
            ]),
            ("Calcium channel blockers", [
                ("Describe the primary mechanism of action of calcium channel blockers.", "<ul><li>Block L-type calcium channels, predominantly on vascular smooth muscle.</li><li>Reduced Ca2+ influx inhibits myosin light chain kinase and prevents cross-bridge formation.</li><li>Resulting vasodilation reduces peripheral resistance.</li></ul>"),
                ("Recall two calcium channel blockers.", "Amlodipine and felodipine."),
                ("What is the drug target of calcium channel blockers?", "The L-type calcium channel."),
                ("Recall the main side effects of calcium channel blockers.", "Ankle oedema, constipation, palpitations, flushing/headaches."),
                ("Describe an additional fact about calcium channel blockers.", "Dihydropyridine-type CCBs show higher vascular selectivity; amlodipine was the 2nd most commonly prescribed drug in West London in 2020."),
            ]),
            ("Thiazide / thiazide-like diuretics", [
                ("Describe the primary mechanism of action of thiazide/thiazide-like diuretics.", "<ul><li>Block the Na+/Cl- co-transporter in the early distal convoluted tubule.</li><li>Na+ and Cl- reabsorption is inhibited.</li><li>Raised tubular osmolarity reduces the osmotic gradient for water reabsorption in the collecting duct.</li></ul>"),
                ("Recall two thiazide/thiazide-like diuretics.", "Bendroflumethiazide (thiazide) and indapamide (thiazide-like)."),
                ("What is the drug target of thiazide/thiazide-like diuretics?", "The sodium/chloride co-transporter."),
                ("Recall the main side effects of thiazide/thiazide-like diuretics.", "Hypokalaemia, hyponatraemia, metabolic alkalosis, hypercalcaemia, hyperglycaemia, hyperuricaemia."),
                ("Describe an additional fact about thiazide/thiazide-like diuretics.", "The diuretic effect is lost within 1–2 weeks; continuing antihypertensive action is due to vasodilation (more pronounced with thiazide-like diuretics)."),
            ]),
            ("Angiotensin receptor blockers (ARBs)", [
                ("Describe the primary mechanism of action of ARBs.", "Act as insurmountable (non-competitive) antagonists at the AT1 (angiotensin II type 1) receptor on the kidneys and vasculature."),
                ("Recall two ARBs.", "Losartan and irbesartan (also candesartan)."),
                ("What is the drug target of ARBs?", "The angiotensin receptor."),
                ("Recall the main side effects of ARBs.", "Hypotension, hyperkalaemia, fetal injury (avoid in pregnancy), renal failure (in renal artery stenosis)."),
                ("Recall a contraindication of ARBs.", "Avoid in pregnant women."),
                ("Describe additional facts about ARBs.", "Most trials suggest ARBs are less effective antihypertensives than ACE inhibitors; losartan and candesartan are pro-drugs needing hepatic activation."),
            ]),
        ],
    },
    {
        "id": "1.10",
        "title": "1.10 Pharmacology of Asthma",
        "slug": "pharmacology-of-asthma",
        "disease": "Asthma",
        "deck_file": "asthma.apkg",
        "deck_id": 1607392714,
        "sections": [
            ("Salbutamol (SABA)", [
                ("Recall four drugs used to treat asthma.", "Salbutamol, fluticasone, mometasone, budesonide."),
                ("Describe the primary mechanism of action of salbutamol.", "Agonist at the beta-2 receptor on airway smooth muscle; activation reduces Ca2+ entry, preventing smooth muscle contraction."),
                ("What is the drug target of salbutamol?", "The beta-2 (β2) adrenergic receptor on airway smooth muscle cells."),
                ("Recall the main side effects of salbutamol.", "Palpitations/agitation, tachycardia/arrhythmias, hypokalaemia (at higher doses)."),
                ("Describe additional facts about salbutamol.", "<ul><li>A short-acting beta agonist (SABA) with a half-life of 2.5–5 hours.</li><li>Beta-2 selectivity is not absolute, so cardiac (beta-1) effects can occur.</li><li>Hypokalaemia is via Na+/K+ ATPase and can be worsened by co-administered corticosteroids.</li></ul>"),
                ("Describe the difference between beta-1 and beta-2 receptors.", "Beta-1 = heart; beta-2 = airways."),
            ]),
            ("Inhaled corticosteroids (fluticasone, mometasone, budesonide)", [
                ("Describe the primary mechanism of action of fluticasone.", "A very powerful drug with multiple actions across cell types; it directly decreases inflammatory cells (eosinophils, monocytes, mast cells, macrophages, dendritic cells) and the cytokines they produce."),
                ("What is the drug target of fluticasone (and other inhaled corticosteroids)?", "The glucocorticoid receptor."),
                ("Recall the main side effects of inhaled corticosteroids.", "Local: sore throat, hoarse voice, opportunistic oral infections. Systemic: growth retardation in children, hyperglycaemia, decreased bone mineral density, immunosuppression, effects on mood."),
                ("Describe an additional fact about fluticasone.", "Greater affinity for the glucocorticoid receptor than cortisol; oral bioavailability <1%, so systemic delivery is mainly via the pulmonary vasculature after inhalation."),
                ("Describe the mechanism of action of mometasone.", "Like fluticasone: a powerful glucocorticoid with multiple actions, directly decreasing inflammatory cells and their cytokines."),
                ("Describe an additional fact about mometasone.", "Greater affinity for the glucocorticoid receptor than cortisol; oral bioavailability <1%, so systemic delivery is mainly via the pulmonary vasculature."),
                ("What is meant by oral bioavailability?", "The fraction of an oral drug dose that reaches the therapeutic site of action; important because much of an oral drug may be metabolised and eliminated before reaching the systemic circulation."),
                ("Describe the mechanism of action of budesonide.", "Like fluticasone: a powerful glucocorticoid acting on many cell types to reduce inflammatory cells and their cytokines."),
                ("Describe an additional fact about budesonide.", "Oral bioavailability >10%, so inhaled budesonide still causes some systemic absorption via the GI tract."),
                ("Compare budesonide with fluticasone and mometasone.", "Budesonide is less potent than fluticasone and mometasone."),
            ]),
            ("Montelukast", [
                ("Describe the primary mechanism of action of montelukast.", "Antagonism of the CysLT1 leukotriene receptor on eosinophils, mast cells, and airway smooth muscle decreases eosinophil migration, bronchoconstriction, and inflammation-induced oedema."),
                ("What is the drug target of montelukast?", "The CysLT1 leukotriene receptor."),
                ("Recall the main side effects of montelukast.", "Mild: diarrhoea, fever, headaches, nausea/vomiting. Serious: mood changes, anaphylaxis."),
                ("Describe an additional fact about montelukast.", "For prophylaxis of exercise-induced bronchoconstriction, give at least 2 hours before exercise."),
            ]),
        ],
    },
    {
        "id": "1.12",
        "title": "1.12 Pharmacology of GORD / Peptic Ulcer Disease",
        "slug": "pharmacology-of-gord-peptic-ulcer-disease",
        "disease": "GORD & Peptic Ulcer Disease",
        "deck_file": "gord-peptic-ulcer-disease.apkg",
        "deck_id": 1607392715,
        "sections": [
            ("NSAIDs", [
                ("Recall four drugs used to treat GORD/peptic ulcer disease.", "NSAIDs, proton pump inhibitors (PPIs), histamine (H2) receptor antagonists, paracetamol (acetaminophen)."),
                ("Describe the primary mechanism of action of NSAIDs.", "<ul><li>Inhibit cyclo-oxygenase (COX), the rate-limiting step for producing all prostanoids (prostaglandins & thromboxanes) from arachidonic acid.</li><li>Anti-inflammatory and most analgesic/antipyretic actions relate to COX-2 inhibition; unwanted effects largely relate to COX-1 inhibition.</li></ul>"),
                ("Recall three NSAIDs.", "Paracetamol, naproxen, diclofenac."),
                ("What is the drug target of NSAIDs?", "The cyclo-oxygenase (COX) enzyme."),
                ("Recall the main side effects of NSAIDs.", "Gastric irritation, ulceration, bleeding and (extreme) perforation; reduced creatinine clearance and possible nephritis; bronchoconstriction (contraindicated in asthma); rashes/allergies, dizziness, tinnitus; adverse CV effects with prolonged use; chronic renal failure with long-term abuse; aspirin linked to Reye's syndrome in children."),
                ("Describe the main uses of NSAIDs.", "Analgesics for mild-to-moderate pain (musculoskeletal pain, headache, dysmenorrhoea); antipyretics; anti-inflammatories (e.g. gout); and aspirin as an anti-aggregatory agent to reduce stroke/MI risk."),
            ]),
            ("Proton pump inhibitors (PPIs)", [
                ("Describe the primary mechanism of action of PPIs.", "Irreversible inhibitors of H+/K+ ATPase in gastric parietal cells; weak bases that accumulate in the acidic canaliculi, concentrating and prolonging their action. Omeprazole's half-life is ~1 h but a single daily dose affects acid secretion for 2–3 days, inhibiting acid secretion by >90%."),
                ("Recall two PPIs.", "Omeprazole and lansoprazole."),
                ("What is the drug target of PPIs?", "H+/K+ ATPase (the 'proton pump')."),
                ("Recall the main side effects of PPIs.", "Uncommon: headache, diarrhoea, bloating, abdominal pain, rashes; may mask gastric cancer symptoms; omeprazole inhibits CYP2C19 and can reduce clopidogrel activity."),
                ("Describe additional facts about PPIs.", "Pro-drugs converted at low pH into reactive species that react with sulphydryl groups of H+/K+ ATPase; given as enteric-coated granules because they degrade at low pH; omeprazole was the 5th most prescribed drug in West London in 2020."),
            ]),
            ("Histamine (H2) receptor antagonists", [
                ("Describe the primary mechanism of action of H2 receptor antagonists.", "Competitive antagonists of H2 histamine receptors (structural analogues of histamine); inhibit the stimulatory action of histamine from ECL cells on parietal cells, reducing gastric acid secretion by ~60%."),
                ("Recall a histamine (H2) receptor antagonist.", "Ranitidine."),
                ("What is the effect of H2 receptor antagonists on acid secretion?", "They inhibit gastric acid secretion by approximately 60%."),
                ("Recall the main side effects of H2 receptor antagonists.", "Incidence is low; diarrhoea, dizziness, muscle pains, transient rashes. Cimetidine (but not others) inhibits cytochrome P450 and can potentiate drugs such as oral anticoagulants and TCAs."),
                ("Describe additional facts about H2 receptor antagonists.", "Ranitidine half-life ~2–3 h; twice-daily dosing is effective; undergo first-pass metabolism; ~50% bioavailability; low-dose OTC formulations available."),
                ("What is first-pass metabolism?", "The initial breakdown of a drug by the liver (and sometimes gut wall) before it reaches the systemic circulation."),
            ]),
            ("Paracetamol", [
                ("Recall another name for paracetamol.", "Acetaminophen."),
                ("Suggest three possible mechanisms of action for paracetamol.", "<ul><li>May inhibit a peripheral peroxidase involved in converting arachidonic acid to prostaglandins.</li><li>Activation of descending serotonergic pathways, possibly via 5-HT3 receptors.</li><li>Inhibits reuptake of endogenous endocannabinoids, increasing cannabinoid receptor activation.</li></ul>"),
                ("When may the mechanism of paracetamol be impaired?", "Its peroxidase inhibition can be blocked when excessive peroxide builds up, as in inflammation."),
                ("What is the drug target for paracetamol?", "Unclear — possibly 5-HT3 receptors, cannabinoid reuptake proteins, or peroxidase."),
                ("Recall the side effects of paracetamol.", "A relatively safe drug with few common side effects; effects arise from overdose."),
                ("Describe the effects of paracetamol overdose.", "Liver damage and, less often, renal damage; early nausea and vomiting (settle in 24 h); right subcostal pain after 24 h indicates hepatic necrosis."),
                ("Describe the uses of paracetamol.", "Analgesic and antipyretic; does NOT have anti-inflammatory activity; many products contain paracetamol, so care is needed to avoid accidental overdose."),
            ]),
        ],
    },
    {
        "id": "1.14",
        "title": "1.14 Pharmacology of CKD",
        "slug": "pharmacology-of-ckd",
        "disease": "CKD",
        "deck_file": "ckd.apkg",
        "deck_id": 1607392716,
        "sections": [
            ("Overview", [
                ("Recall nine drugs used in the management of CKD.", "Statins, aspirin, trimethoprim, gentamicin, ACE inhibitors, ARBs, calcium channel blockers, dapagliflozin, NSAIDs."),
            ]),
            ("Statins", [
                ("Recall two statins.", "Atorvastatin and simvastatin."),
                ("Describe the primary mechanism of action of statins.", "<ul><li>Selective, competitive inhibitors of HMG-CoA reductase, the rate-limiting enzyme converting HMG-CoA to mevalonate in cholesterol synthesis.</li><li>Reduced hepatic cholesterol synthesis upregulates LDL receptors and increases hepatic LDL-cholesterol uptake.</li></ul>"),
                ("What is the drug target for statins?", "HMG-CoA reductase."),
                ("Recall the main side effects of statins.", "Muscle toxicity (increases with higher doses and in at-risk patients); constipation/diarrhoea and other GI symptoms."),
                ("Describe additional facts about statins.", "Effective at reducing adverse cardiac events; monitor for hyperkalaemia and acute renal failure; potent CYP3A4 inhibitors raise statin levels; atorvastatin was the most prescribed drug in West London in 2020."),
            ]),
            ("Aspirin", [
                ("Describe the primary mechanism of action of aspirin.", "<ul><li>Irreversibly inactivates COX, preventing oxidation of arachidonic acid to prostaglandins.</li><li>Reducing platelet thromboxane A2 reduces aggregation.</li><li>Reducing PGE2 lessens pain at sensory neurones and fever in the brain.</li></ul>"),
                ("What is the drug target for aspirin?", "Cyclo-oxygenase (COX)."),
                ("Recall the main side effects of aspirin.", "Dyspepsia (indigestion) and haemorrhage."),
                ("Describe the uses of aspirin.", "Low-dose aspirin is the most cost-effective medicine for secondary prevention of thrombotic events; COX-1 blockade in gastric mucosa reduces mucus/bicarbonate, exposing the lining to acid."),
                ("Describe the physiological roles of COX-1 versus COX-2.", "COX-1 is constitutive: protects the stomach lining, supports platelet aggregation (thromboxane A2), and maintains kidney function/blood flow. COX-2 is inducible: upregulated during inflammation, injury, and infection."),
                ("Which COX isoform links to therapeutic versus unwanted NSAID effects?", "Anti-inflammatory and most analgesic/antipyretic actions relate to COX-2 inhibition; unwanted effects (dyspepsia, haemorrhage) relate to COX-1 inhibition."),
                ("Describe an important consideration for aspirin use in the elderly.", "Avoid doses greater than 160 mg daily (increased bleeding risk) and co-administer a PPI if there is a history of peptic ulcer."),
            ]),
            ("Trimethoprim", [
                ("Describe the primary mechanism of action of trimethoprim.", "A direct competitor of dihydrofolate reductase, inhibiting reduction of dihydrofolic acid to tetrahydrofolic acid (needed for purine synthesis). It has much higher affinity for bacterial than human DHFR, making it selectively toxic to bacteria."),
                ("What is the drug target for trimethoprim?", "Dihydrofolate reductase."),
                ("Recall the main side effects of trimethoprim.", "Diarrhoea and skin reactions."),
                ("Describe the use of trimethoprim.", "Often given with sulfamethoxazole (co-trimoxazole), blocking two steps of bacterial nucleic acid/protein synthesis."),
                ("Describe an additional fact about trimethoprim.", "Monitor blood counts with long-term use or folate-deficiency risk, and monitor serum electrolytes where hyperkalaemia risk exists."),
            ]),
            ("Gentamicin", [
                ("Describe the primary mechanism of action of gentamicin.", "Binds the bacterial 30S ribosomal subunit, disrupting mRNA translation and producing dysfunctional proteins."),
                ("What is the drug target for gentamicin?", "The bacterial 30S ribosomal subunit."),
                ("Recall the main side effects of gentamicin.", "Ototoxicity and nephrotoxicity."),
                ("Describe the use of gentamicin.", "An aminoglycoside that crosses the gram-negative membrane in an oxygen-dependent manner (ineffective against anaerobes); usually given IV for endocarditis, septicaemia, meningitis, pneumonia, or surgical prophylaxis."),
                ("What type of drugs are trimethoprim and gentamicin?", "Antibiotics."),
                ("Which CKD drugs are covered in earlier lectures as cross-references?", "Calcium channel blockers, ACE inhibitors, ARBs, and SGLT-2 inhibitors (dapagliflozin) — see the Hypertension and Diabetes lectures for mechanisms, targets, side effects, and additional facts."),
            ]),
        ],
    },
    {
        "id": "1.16",
        "title": "1.16 Pharmacology of Pain",
        "slug": "pharmacology-of-pain",
        "disease": "Pain",
        "deck_file": "pain.apkg",
        "deck_id": 1607392717,
        "sections": [
            ("Paracetamol", [
                ("Recall four drugs used to treat pain.", "Paracetamol, opioids, co-amoxiclav, lactulose."),
                ("Recall another name for paracetamol.", "Acetaminophen."),
                ("Suggest three possible mechanisms of action for paracetamol.", "<ul><li>May inhibit a peripheral peroxidase involved in converting arachidonic acid to prostaglandins.</li><li>Activation of descending serotonergic pathways, possibly via 5-HT3 receptors.</li><li>Inhibits reuptake of endogenous endocannabinoids, increasing cannabinoid receptor activation.</li></ul>"),
                ("When may the mechanism of paracetamol be impaired?", "Its peroxidase inhibition can be blocked when excessive peroxide builds up, as in inflammation."),
                ("What is an endocannabinoid?", "A naturally occurring lipid-based molecule that interacts with cannabinoid receptors; this system regulates mood, pain, and appetite."),
                ("What is the drug target for paracetamol?", "Unclear — possibly 5-HT3 receptors, cannabinoid reuptake proteins, or peroxidase."),
                ("Recall the side effects of paracetamol.", "A relatively safe drug with few common side effects; effects arise from overdose."),
                ("Describe the effects of paracetamol overdose.", "Liver damage and, less often, renal damage; early nausea and vomiting (settle in 24 h); right subcostal pain after 24 h indicates hepatic necrosis."),
                ("Describe the uses of paracetamol.", "Analgesic and antipyretic; does NOT have anti-inflammatory activity; care is needed to avoid accidental overdose from combination products."),
            ]),
            ("Opioids", [
                ("Recall the two classes of opioids with examples.", "Weak: codeine, tramadol. Strong: morphine, fentanyl."),
                ("Describe the primary mechanism of action of opioids.", "<ul><li>Overall a depressant effect on cellular activity.</li><li>Act at multiple sites in the pain pathway; opioid receptor activation decreases perception of, or increases tolerance to, pain.</li><li>Anti-tussive effect from decreased activation of afferent cough nerves.</li></ul>"),
                ("What is the drug target for opioids?", "The opioid receptor."),
                ("Recall the main side effects of opioids.", "Constipation (common; opioid receptors reduce gut motility); nausea and vomiting (chemoreceptor trigger zone)."),
                ("Describe the effects of opioid overdose.", "Respiratory depression via direct and indirect inhibition of the respiratory control centre."),
                ("Describe how opioid prescribing is changing in the UK.", "Prescriptions have more than doubled in 20 years; in 2020 several weak opioid or opioid/paracetamol combinations were among the most prescribed drugs in West London (e.g. co-codamol)."),
            ]),
            ("Co-amoxiclav", [
                ("What is co-amoxiclav?", "An antibiotic consisting of amoxicillin and clavulanic acid."),
                ("Describe the mechanism of action of co-amoxiclav.", "<ul><li>Amoxicillin binds bacterial penicillin-binding proteins (PBPs), preventing transpeptidation (cross-linking) in cell-wall synthesis.</li><li>Clavulanate inhibits beta-lactamase, the bacterial enzyme that degrades beta-lactam antibiotics and confers resistance.</li></ul>"),
                ("What is the drug target for co-amoxiclav?", "Amoxicillin targets penicillin-binding proteins; clavulanate targets beta-lactamase."),
                ("Recall the side effects of co-amoxiclav.", "Amoxicillin is well tolerated; commonest effects are nausea and diarrhoea; penicillin hypersensitivity is relatively common (rash, occasionally anaphylaxis)."),
                ("What does amoxicillin work against?", "A semisynthetic antibiotic with broad-spectrum bactericidal activity against many gram-positive and gram-negative organisms."),
                ("How is co-amoxiclav commonly used in the NHS?", "It is a commonly prescribed antibiotic in hospital settings."),
            ]),
            ("Lactulose", [
                ("What is lactulose?", "A non-absorbable disaccharide."),
                ("Describe the primary mechanism of action of lactulose.", "It reaches the large bowel unchanged, drawing in water by osmosis for an easier-to-pass stool; colonic bacteria metabolise it, adding a further laxative effect."),
                ("What is the drug target for lactulose?", "No drug target."),
                ("Recall the side effects of lactulose.", "Abdominal pain, diarrhoea, flatulence, nausea."),
                ("Describe the efficacy of lactulose.", "Begins working within 8–12 hours but may take up to 2 days to improve constipation."),
            ]),
        ],
    },
]


def common_head(title: str) -> str:
    return (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8"/>'
        '<meta name="viewport" content="width=device-width,initial-scale=1"/>\n'
        f'<title>{html.escape(title)} — BRS</title>'
        '  <link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        '  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,650;9..144,700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet" />'
        '<link rel="stylesheet" href="../../css/styles.css"/>'
    )


def all_cards(lecture):
    return [(q, a) for _, cards in lecture["sections"] for q, a in cards]


def main():
    hub_links = []
    lecture_cards_html = []
    for lecture in LECTURES:
        cards = all_cards(lecture)
        deck_name = f"BRS::{TOPIC_NAME}::{lecture['disease']}"
        deck = genanki.Deck(lecture["deck_id"], deck_name)
        for q, a in cards:
            deck.add_note(genanki.Note(model=MODEL, fields=[q, a, f"7 (P&T) {lecture['id']} — {lecture['disease']}"]))
        genanki.Package(deck).write_to_file(ANKI_DIR / lecture["deck_file"])

        toc = "".join(
            f'<li><a href="#s{i}">{html.escape(section)}</a></li>'
            for i, (section, _) in enumerate(lecture["sections"])
        )
        section_html = []
        for i, (section, section_cards) in enumerate(lecture["sections"]):
            qa = "".join(
                f'<div class="qa"><h3>{html.escape(q)}</h3><div>{a}</div></div>'
                for q, a in section_cards
            )
            section_html.append(f'<section class="panel" id="s{i}"><h2>{html.escape(section)}</h2>{qa}</section>')

        page = common_head(lecture["title"]) + (
            "\n<style>.qa{padding:.9rem 0;border-bottom:1px solid var(--line)}.qa:last-child{border-bottom:none}\n"
            ".qa h3{font-family:var(--font-ui);font-size:1rem;font-weight:700;margin:0 0 .45rem;line-height:1.35}\n"
            ".qa p,.qa li,.qa div{font-size:.98rem;color:var(--ink-soft)}.qa ul,.qa ol{margin:.25rem 0 0;padding-left:1.2rem}.qa li+li{margin-top:.3rem}</style>\n"
            "</head><body>\n"
            '<header class="site-header"><a class="brand" href="../../index.html"><span class="brand-mark">BRS</span><span class="brand-sub">Phase 1B · Imperial</span></a>\n'
            '<nav class="nav-links"><a href="index.html">Pharmacology</a><a href="../../index.html">Home</a></nav></header>\n'
            '<main class="wrap page">\n'
            f'<p class="crumb"><a href="../../index.html">Home</a> / <a href="index.html">Pharmacology &amp; Therapeutics</a> / {html.escape(lecture["id"])}</p>\n'
            f'<h1 class="page-title">{html.escape(lecture["title"])}</h1>\n'
            f'<p class="page-lead">Complete notes from the source PDF (every Q&amp;A and explanatory block). {len(cards)} Anki cards.</p>\n'
            f'<div class="anki-bar"><span>{len(cards)} flashcards</span> <a class="anki-all" href="../../anki/bundles/all-decks-pharmacology-and-therapeutics.zip" download>ALL DECKS — Pharmacology</a><span style="opacity:0.75;font-size:0.82rem">{len(LECTURES)} decks</span><a href="../../anki/{lecture["deck_file"]}">Download “{html.escape(lecture["disease"])}” deck</a></div>\n'
            f'<div class="notes-layout"><aside class="toc"><strong>Sections</strong><ol>{toc}</ol></aside><div class="notes">{"".join(section_html)}</div></div>\n'
            '</main><footer class="site-footer">Source: <code>raw/pdfs/pharmacology-and-therapeutics/'
            f'{lecture["id"]} Pharmacology of {html.escape(lecture["disease"])} - Core Drugs.pdf</code></footer></body></html>'
        )
        (TOPIC_DIR / f"{lecture['slug']}.html").write_text(page, encoding="utf-8")

        hub_links.append(f'<a href="../../anki/{lecture["deck_file"]}">{html.escape(lecture["disease"])}</a>')
        lecture_cards_html.append(
            f'<li><a class="lecture-card" href="{lecture["slug"]}.html"><span class="lecture-id">{html.escape(lecture["id"])}</span>'
            f'<div><h3>{html.escape(lecture["title"])}</h3><p>Deck: {html.escape(lecture["disease"])}</p></div>'
            f'<span class="lecture-meta">{len(cards)} cards</span></a></li>'
        )
        print(f"{lecture['title']}: {len(cards)} cards -> {lecture['deck_file']}")

    hub = common_head(TOPIC_NAME) + (
        "</head><body>\n"
        '<header class="site-header"><a class="brand" href="../../index.html"><span class="brand-mark">BRS</span><span class="brand-sub">Phase 1B · Imperial</span></a>\n'
        '<nav class="nav-links"><a href="../../index.html">Home</a></nav></header>\n'
        '<main class="wrap page"><p class="crumb"><a href="../../index.html">Home</a> / Pharmacology &amp; Therapeutics</p>\n'
        '<h1 class="page-title">Pharmacology &amp; Therapeutics</h1>\n'
        '<p class="page-lead">Core-drug lectures with full PDF coverage. Anki decks are named by the disease each drug set treats.</p>\n'
        f'<div class="anki-bar"><span>Anki decks</span> <a class="anki-all" href="../../anki/bundles/all-decks-pharmacology-and-therapeutics.zip" download>ALL DECKS — Pharmacology</a><span style="opacity:0.75;font-size:0.82rem">{len(LECTURES)} decks</span>{"".join(hub_links)}</div>\n'
        f'<ul class="lecture-list">{"".join(lecture_cards_html)}</ul></main>\n'
        '<footer class="site-footer">Phase 1B BRS · Imperial College London</footer></body></html>'
    )
    (TOPIC_DIR / "index.html").write_text(hub, encoding="utf-8")

    bundle = ANKI_DIR / "bundles" / "all-decks-pharmacology-and-therapeutics.zip"
    with ZipFile(bundle, "w", ZIP_DEFLATED) as archive:
        for lecture in LECTURES:
            archive.write(ANKI_DIR / lecture["deck_file"], arcname=lecture["deck_file"])
    print(f"Hub -> {TOPIC_DIR / 'index.html'}")
    print(f"Bundle -> {bundle}")


if __name__ == "__main__":
    main()

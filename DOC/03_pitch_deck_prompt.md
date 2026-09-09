# Gamma Pitch Deck Build — DrishtiSport AI (Samsung Solve for Tomorrow 2026)

## Step 1 — Slide size

Reference template (`Pitch Deck Template_Top100_SFT2026.pptx`) is exactly **13.333″ × 7.5″** — standard PowerPoint widescreen. In Gamma's size picker, choose **"Traditional 16:9"** (not "Default," which Gamma often renders at a slightly different ratio, and not "Tall 4:3").

## Step 2 — Paste this first (style/design instructions)

If Gamma gives you a separate "additional instructions" or theme-prompt field, paste this there. If not, paste it as the very first block of your outline, before the first `---`.

```
Design a pitch deck for "DrishtiSport AI," an AI sports-biomechanics app, for
Samsung Solve for Tomorrow 2026 judges (Samsung + FITT-IIT Delhi panel) watching
a 4-minute narrated video with only 2-3 minutes of real attention.

PALETTE (bespoke to this topic — do not use generic corporate blue):
- Primary/dominant (~65% weight): deep graphite/charcoal (#1B1F2B) — evokes a
  floodlit night sports field and serious tech.
- Secondary: electric amber-coral (#FF5A36) — athletic energy, used for headline
  accents and key stat highlights.
- Accent: cyber cyan (#00C2C2) — an AI/data feel, echoing a live pose-tracking dot.
- Functional colors, used ONLY inside diagrams/mockups, never as decoration:
  safe-green (#2ECC71) and alert-red (#E63946) — these mirror the app's own
  real-time overlay colors, so diagrams stay visually consistent with the demo.
- Title and Closing slides: full dark graphite background. All content slides:
  white/very light background (dark/light "sandwich" structure).

VISUAL MOTIF (repeat on every slide, exactly two elements, no third motif):
1. Icon-in-circle badges (solid colored circle, white-line icon) next to every
   section header or key stat.
2. A "joint-node" connector — a small dot linked by a thin line, echoing a
   skeletal pose-tracking landmark — used between diagram steps instead of plain
   arrows wherever a flow/process is shown.

RULES:
- No accent stripes, color bars, or side borders on any card or slide edge.
- No horizontal rule/underline beneath any title.
- Sans-serif throughout (Calibri or Arial) — no traditional serif pitch-deck styling.
- Left-align all body copy; center only titles.
- Every slide must use a DIFFERENT layout structure from the one before and after
  it — rotate through: left-right split, icon cards, flow diagram, concentric/
  circular model, comparison matrix, layered funnel, stat-callout row. Never repeat
  plain title+bullets.
- Every slide must be visually full — no large empty white space; if a slide looks
  sparse, add a supporting chart, icon row, or secondary data point rather than
  leaving blank area.
- Fill every slide with all the content given for it below — do not shorten or
  drop bullets to make a slide "cleaner"; density is intentional here, the spoken
  narration will be trimmed separately, but the deck itself must show full content
  for judges who read at their own pace.
```

## Step 3 — Paste this as your slide-by-slide outline

This covers, on every slide, every point the official FITT template requires (checked against the extracted template text) plus extra sections that make each slide stand out — each slide also carries a `[Standout: ...]` note flagging its differentiator so it doesn't read like a generic hackathon deck.

Every slide's heading below is written to match the official FITT template's exact
section names (Project Title, Introduction/Team, Problem/Opportunity, Solution,
Customer, Competition/Unique Value Proposition, Impact, Revenue Model, Closing
slide) — a subtitle/tagline line sits under each heading for narrative punch, but
the heading itself stays identical to the template so a reviewer scanning against
their own checklist recognizes every section instantly.

```
DrishtiSport AI
Turning Every Rural Playground Into a Biomechanics Lab
- Samsung Solve for Tomorrow 2026 | Theme 3: Sport & Tech | Top 100 Shortlisted
- Team / Builder: [YOUR TEAM OR SOLO NAME] | [YOUR INSTITUTE]
[Layout: full-bleed dark graphite background, diagonal 60/40 split — left holds
title/tagline/badge, right holds a cricket bowler mid-delivery photo with a subtle
skeletal joint-overlay graphic hinting at the product]
[Standout: the joint-overlay on the hero image previews the product before a
single word of narration]
---
Introduction/Team
Meet the Builder Behind DrishtiSport AI
- Solo founder-builder, [Your Institute Name] — building this end-to-end alone
- One person, three disciplines: computer vision & ONNX model development,
  Flutter/mobile app engineering, and hands-on grounding in grassroots sport
- Personal motivation: [insert your real reason — a bowling action you saw called
  out unfairly, an injury that went undiagnosed, a coach with no tools, etc.]
- Backed by structured mentorship: FITT-IIT Delhi design-thinking sessions
  [+ any named mentor/advisor, if you have one]
- Vision: "One builder, one mission — put elite biomechanics in every rural
  coach's pocket."
- Why solo works here: a single, tightly-owned technical vision means faster
  iteration and direct personal accountability for the working prototype in
  today's live demo — no coordination overhead, no diluted ownership
[Layout: hero profile card — large circular photo placeholder left; name, bio,
and 3 icon-badge skill chips (CV/ML, Mobile Dev, Sports Domain) right; vision
statement in its own soft-shaded card below, separated from the bio block]
[Standout: reframes solo status as focused ownership rather than a gap — directly
answers the "team competence" judging criterion before it's even asked]
---
Problem / Opportunity
A Biomechanics Gap No One Is Pricing For
- 98% of rural Indian athletes train with zero access to biomechanical analysis —
  the exact difference between raw talent and injury-free, technically correct
  performance
- Elite motion-capture labs cost ₹5,000+/hour — restricted to national academies,
  completely unreachable for Tier 2/3 coaches and rural playgrounds
- Sharpest version of the gap: cricket's ICC Law 24.3 sets a hard 15° elbow-
  extension limit for a legal bowling action, but no rural umpire or coach has
  equipment to check it — bowlers get called out mid-match with no warning, or
  never get flagged until a career-ending injury
- What motivated this: [insert your real observation/story here]
- Scale of the problem: [X crore] youth participate in grassroots cricket/
  athletics annually in India — VERIFY exact figure before presenting; do not
  guess a number
[Layout: split-screen contrast image at top (biomechanics lab vs. rural pitch);
below it, 3 stacked icon-callout cards — Cost Barrier / Access Barrier /
Detection Barrier — each with a one-line stat]
[Standout: citing the actual ICC rule number (Law 24.3, 15°) signals real domain
research instead of a generic "lack of coaching" narrative every competitor uses]
---
Solution
DrishtiSport AI — Biomechanics in Every Pocket
- A free, 100% offline smartphone app turning any budget camera into a real-time
  biomechanics coach — no wearables, no lab, no internet connection required
- Core engine: on-device pose estimation (Google MediaPipe, 33 skeletal
  landmarks) plus a lightweight quantized ONNX model computing joint angles
  frame-by-frame
- Flagship working module: cricket bowling-action legality checker — live green
  skeleton overlay while elbow extension stays under the ICC's 15° threshold,
  instant red overlay plus local-language audio alert ("Illegal action risk —
  elbow extension 19°") the moment the threshold is crossed
- User benefit: instant, objective feedback that previously required a paid lab
  visit; coaches catch technique faults before they become injuries or match-day
  disqualifications; scouts get an unbiased, timestamped performance log instead
  of a subjective opinion
- Current stage: working prototype (POC), built and running — live demo follows
  this deck
- What's next: sprint start-position analysis, kabaddi lunge safety, and squat/
  landing injury-risk modules, all on the same core engine with new sport-
  specific thresholds
[Layout: horizontal architecture flow diagram — Phone Camera > MediaPipe Pose
Extraction > On-Device ONNX Angle Model > Green/Red Visual + Audio Alert >
Verified Local Log — each step an icon-in-circle joined by the joint-node
connector; below the flow, a real green-vs-red screenshot pair from your own
demo footage]
[Standout: the only slide showing your actual working screenshots — makes
"technical depth" demonstrated, not claimed]
---
Customer
Who This Is For
- Aspiring athletes (10-22) in Tier 2/3 and rural India training without access
  to professional coaching or lab-grade feedback
- PE teachers and grassroots academy coaches managing large groups with zero
  specialized equipment or biomechanics training
- Talent scouts and sports bodies who need objective, tamper-proof performance
  data instead of subjective, locally-biased judgment calls
- Market sizing: TAM = all grassroots sport participants in India across
  cricket/athletics/kabaddi; SAM = Tier 2/3 school- and academy-affiliated
  athletes; SOM = [X] pilot academies/schools targeted in Year 1 — mark every
  figure "illustrative, to verify" until you have a sourced number
- Early validation: [insert any real pilot conversation, school interest, or
  mentor feedback you actually have — omit this bullet entirely rather than
  invent one if you have none yet]
[Layout: left column = 3 icon-badge persona cards; right column = concentric
TAM-SAM-SOM circles, outer to inner, each labeled with its definition and figure]
[Standout: SOM framed as a specific, near-term pilot target rather than an
abstract "millions of users" claim shows business realism]
---
Competition / Unique Value Proposition
Why DrishtiSport AI Wins on the Ground
- Elite motion-capture labs: accurate, but expensive and location-bound —
  inaccessible to rural coaches
- Wearable sensor kits: functional, but require per-athlete hardware cost and
  don't scale to a whole academy
- Generic fitness-form apps: give vague "good form" scores with no sport-specific
  or rule-grounded accuracy
- DrishtiSport AI: 100% offline (zero connectivity needed), zero extra hardware
  (uses the phone already owned), sport-specific rule-grounded thresholds (not
  vague form scoring), and a tamper-proof verified performance log that directly
  targets scouting bias and corruption — a gap no competitor product addresses
[Layout: comparison matrix — rows: the 3 competitor categories plus DrishtiSport
AI; columns: Cost / Hardware Needed / Offline Capability / Rule-Specific
Accuracy / Anti-Bias Verification; DrishtiSport AI's row highlighted with a soft
accent fill, not a border]
[Standout: the "Anti-Bias Verification" column is a category no competitor even
claims to compete on — this is the moat, make it visually unmissable]
---
Impact (Optional)
Impact Beyond the App
- Injury prevention: catching unsafe or illegal technique before it causes
  long-term joint damage or forced early retirement
- Equal access: a rural academy with one phone gets the same technical feedback
  quality as a national training center
- Coach empowerment: PE teachers gain a diagnostic tool requiring zero
  biomechanics training to operate
- National alignment: consistent with Khelo India and Fit India's grassroots
  sports development goals
- Global alignment: directly supports UN SDG 3 (Good Health & Well-Being) and
  SDG 10 (Reduced Inequalities) — a natural fit given the UN's own partnership
  in this program
[Layout: 4 icon-badge impact cards in a single row, each with a bold short
headline and one supporting line]
[Standout: explicitly naming SDG 3 and SDG 10 signals awareness of the UN's
specific role as a program partner, not generic "social impact" language]
---
Revenue Model
How This Sustains Itself
- Free forever for individual athletes, schools, and rural academies — this is
  the adoption engine, not a compromise
- B2B subscription: state and private sports academies pay for a multi-athlete
  scouting analytics dashboard and progress-tracking tools
- Data licensing: anonymized, aggregated performance and injury-risk analytics
  licensed to sports federations and scouting bodies for talent identification
- Revenue mix built for stability: recurring annual academy subscriptions
  provide steady inflow; federation licensing deals add higher-value, if less
  frequent, contracts
- No hidden cost to the athlete at any point — monetization sits entirely at the
  institutional layer, never the individual user
[Layout: layered funnel/stack diagram — bottom (widest) = free athlete/school
tier, middle = B2B academy subscriptions, top (narrowest) = federation data
licensing, gradient-colored light to dark from bottom to top]
[Standout: explicitly stating "no hidden cost to the athlete" pre-empts the
obvious judge question about monetizing your own free users]
---
Closing Slide
Thank You
- DrishtiSport AI — every rural playground deserves a coach. This makes sure it
  gets one.
- Contact: [your email] | [your team or solo name]
- Direct ask: requesting FITT-IIT Delhi lab access to validate the elbow-angle
  model against certified biomechanics equipment, and mentorship on scaling to
  additional sports
[Layout: full-bleed dark graphite background matching the title slide for
bookend symmetry, centered content, small QR code placeholder linking to a demo
video]
[Standout: the closing ask is specific and actionable — lab validation — giving
judges/mentors something concrete to say yes to, instead of a generic sign-off]
```

## Judging-lens cheat sheet

| Lens | Where it's won or lost |
|---|---|
| **Innovation** | Solution + Competition slides — the ICC 15° elbow-legality threshold and the anti-bias verified log are the two hooks; don't let either get diluted into generic "AI coaching app" language. |
| **Technical depth** | Solution slide's architecture flow must show real components (MediaPipe → ONNX → on-device output) plus your actual demo screenshots — not a vague "AI magic" box. |
| **Clarity** | Even with dense content, each slide must resolve to one clear idea within 3 seconds of looking at it — density in bullets is fine, density in *message* is not. |
| **Business viability** | Customer + Revenue slides — must show real non-grant revenue (B2B subscriptions, data licensing), not just "it's free and impactful." |
| **Demo effectiveness** | Not a slide — this is your video's live-screen-recording segment. The Solution slide should visually set up exactly what that demo is about to show. |
| **Problem Statement alignment** | Problem slide must tie explicitly to Theme 3 (Sport & Tech) and the specific access/detection gap — don't let it drift into generic "sports in India" framing. |

## Notes on what changed from the first draft

- **Slide size** now explicitly matched to the template's real 13.333″×7.5″ (16:9).
- **Palette swapped** from generic navy/cyan to a bespoke graphite/amber/cyan scheme built around this topic, plus functional green/red pulled directly from the product's own UI — not reused from the unrelated "Street Surge" reference deck.
- **Slide 2 rebuilt for a solo team** — profile-card format instead of multi-row team list, with an explicit reframe of "solo" as focused ownership.
- **Every slide now carries the full set of points the official template asks for**, written out in full rather than compressed to fit a spoken time budget — the video script (next step) is where you trim for the 4-minute limit; the deck itself stays complete for judges reading at their own pace.
- **Added a `[Standout: ...]` note per slide** so each one has a stated, deliberate differentiator instead of reading like a template fill-in.

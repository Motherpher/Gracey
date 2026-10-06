# WP01 — Grace Graphic Profile / Personalised CareerHub Surface

**Repository:** `Motherpher/Gracey`  
**System authority:** `Motherpher/CareerHubZero`  
**WP type:** Profile-specific presentation / UX  
**Status:** `READY_FOR_EXECUTION`  
**Target state:** `STRUCTURE_READY → IMPLEMENTATION_READY → PERSONALISATION_LOCK`  
**Date:** 2026-10-06

---

## 1. Purpose

Build Grace's CareerHub as a genuinely person-specific professional workspace inside the CareerHubZero personalisation contract.

The goal is **not** to create a separate Grace runtime or to skin the shared CareerHub with another colour. The goal is to use the central CareerHub body and compose it into a Grace-specific experience whose hierarchy, language, visual grammar and interaction rhythm are materially different because Grace needs a different user experience.

The intended experience is:

> **quiet luxury service** — calm, curated, mature, welcoming and prepared.

The earlier Prada / Gucci comparison is treated as a **service and experience metaphor**, not as permission to reproduce either brand's trade dress, logos, typography, store architecture or other proprietary visual identity.

The user should feel that the workspace has already been prepared for her. The interface offers the next useful step instead of exposing system machinery.

---

## 2. CareerHubZero authority

WP01 follows the canonical CareerHubZero non-generic profile formula:

```text
NGH(person) = CH-Core
            + Identity Signature
            + Work-Logic Signature
            + Information-Need Signature
            + Career-Surface Signature
            + Voice Signature
            + Visual-Grammar Signature
            + Interaction Signature
            + Reference Provenance
```

CareerHubZero remains authoritative for:

- runtime and reusable components,
- accessibility behaviour,
- profile/search/analyse/apply/track contracts,
- schemas,
- evidence firewall,
- HRDM,
- application state,
- central web shell.

Grace's repository owns only the evidence-derived composition and profile-specific presentation files.

**No Grace-local fork of shared UI components is permitted.**

---

## 3. Evidence boundary for WP01

Graphic personalisation may use only permitted non-sensitive sources:

1. verified career evidence,
2. explicit design and workflow decisions made for Grace,
3. non-sensitive usability / interaction preferences from the working process,
4. supplied visual references that have actually been inspected,
5. observed usability feedback.

WP01 must not use private-life or sensitive information as a visual signal, career signal or matching signal.

The screened interview may inform **interaction design** where the material supports practical usability preferences — for example the value of clear, concrete steps and practice-oriented explanation — but it may not be converted into unsupported candidate claims.

### Current career-evidence state

The current active profile contains one verified professional source, Grace's LinkedIn profile, with two promoted source-bound facts: professional connection to Region Skåne and professional geographic context in Greater Malmö. Those facts do not yet justify a narrow occupational brand or a role-title-based visual identity.

Therefore WP01 deliberately avoids branding Grace as a specific profession before stronger verified career material is available.

---

# 4. The Grace design proposition

## Working concept

### **GRACE — QUIET FORWARD MOTION**

Swedish experiential translation:

### **Lugn styrka · varm service · tydlig riktning**

The graphic profile should communicate four things at the same time:

- **maturity** — this is not an entry-level career portal,
- **care** — the interface feels prepared, considered and human,
- **direction** — every surface leads somewhere clear,
- **possibility** — the future is open without becoming motivational advertising.

### Core line

> **Erfarenheten följer med. Riktningen kan förändras.**

This is product framing, not a factual career claim.

---

# 5. Eight-vector Grace signature

## V1 — Identity Signature

### Decision

Grace is the visible identity. CareerHub, GitHub, repository names and Motor terminology remain secondary or invisible on normal user surfaces.

### Presentation

- Display name: **Grace**
- No unverified professional title in the masthead.
- Identity is prominent but restrained.
- Product line: **Erfarenheten följer med. Riktningen kan förändras.**
- The first screen should feel addressed to Grace, not written about Grace.

### Rule

Use **du** in all user-facing prose. Grace's name belongs in identity/title contexts, not in third-person sentences such as “Grace behöver…”.

**Provenance:** `EXPLICIT_USER` + CareerHubZero site-identity rule.

---

## V2 — Work-Logic Signature

### Decision

Grace's surface is organised around **clear movement through a practical career process**, not around analytical architecture.

The interface should answer:

1. What is ready for me now?
2. What looks interesting?
3. What is the next action?

### Information grouping

Priority order:

1. next useful action,
2. current opportunities,
3. application progress,
4. prepared documents / outputs,
5. profile state and evidence status.

Technical profile-health information is available but visually subordinate.

### Design consequence

Do not lead with system state, evidence counters, HRDM terminology or configuration controls. The Motor can remain rigorous without making its internal vocabulary the product experience.

**Provenance:** `EXPLICIT_USER` + `CHAT_PATTERN` + CHZero human-facing simplicity rule.

---

## V3 — Information-Need Signature

### Decision

Grace receives **high guidance with low cognitive clutter**.

This means:

- airy rather than dense,
- short sections,
- one primary action per visual block,
- progressive disclosure,
- direct explanations in ordinary Swedish,
- no walls of system text,
- advanced/audit material behind secondary navigation,
- a clear visual difference between “ready”, “next”, and “for reference”.

### UX rule

High guidance does **not** mean more text. It means better sequencing.

**Provenance:** `EXPLICIT_USER` + non-sensitive usability signals from the working process.

---

## V4 — Career-Surface Signature

### Decision

Grace has **one professional CareerHub surface** at this stage.

Do not manufacture multiple “rooms”, portfolios or professional identities simply to create visual variety. Current verified evidence does not support materially separate professional surfaces.

### Consequence

- `profile.shell.yaml` should **not** be enabled merely for aesthetics.
- The central CareerOverview / task journey should carry the personalisation.
- Additional professional surfaces may be introduced later only when verified career evidence supports clearly different readings of the same profile.

**Provenance:** `VERIFIED_CAREER` + CHZero V4 Career-Surface rule.

---

## V5 — Voice Signature

### Posture

**Warm, adult, self-assured, discreetly service-oriented.**

### Preferred language patterns

- “När du vill …”
- “När något känns intressant …”
- “Vi har förberett nästa steg.”
- “Du väljer tempot.”
- “Vi håller ihop resten.”
- “Vill du titta närmare på det här jobbet?”

### Avoid

- third-person references to Grace in running text,
- system vocabulary,
- HR boilerplate,
- motivational clichés,
- startup enthusiasm,
- gamification,
- officialese,
- exaggerated claims,
- “du måste” unless required for a genuine validation/error state.

### Microcopy principle

**Service before instruction.**

Bad:
> Complete the Search Profile and run the configured lane.

Good:
> När du vill se nya möjligheter kan du söka direkt. Vill du lägga till ett särskilt önskemål gör du det i samma ruta.

**Provenance:** `EXPLICIT_USER` + `CHAT_PATTERN`.

---

## V6 — Visual-Grammar Signature

## Character

**Editorial quiet luxury, not corporate SaaS.**

The visual system should resemble a well-composed editorial service environment rather than a dashboard product.

### Typography

- Display: serif character with fashion/editorial restraint.
- Body: clean contemporary sans serif.
- Large typographic hierarchy.
- Short lines and generous leading.
- Headlines carry atmosphere; body copy carries clarity.

Schema-valid stack:

```text
Display: Iowan Old Style, Baskerville, Georgia, ui-serif, serif
Body: Inter, Aptos, ui-sans-serif, system-ui, sans-serif
Scale: large
```

No font files are bundled into the repo.

### Colour hierarchy

#### Core UI colours

| Function | Colour | Hex |
|---|---|---|
| Main background | Ivory | `#F7F1E3` |
| Main text | Charcoal | `#1B2220` |
| Secondary text | Soft olive | `#7F7A5B` |
| Primary action | Deep petrol | `#063A3D` |
| Text on primary action | White | `#FFFFFF` |

Deep petrol is the interaction colour because it provides strong readable contrast with white.

#### Secondary expressive colours

These belong to illustrations, dividers, botanical marks, editorial highlights and occasional non-text decoration — not primary button backgrounds:

- Warm cream: `#F4D59B`
- Saffron: `#F2A000`
- Hibiscus / coral: `#D94A3A`

This protects accessibility while retaining the warmer Grace palette.

### Geometry

- soft radius,
- quiet borders,
- restrained shadow,
- no pill-everything UI,
- no dense card mosaic,
- no decorative glassmorphism.

### Surfaces

- editorial treatment,
- large negative space,
- strong typographic starts,
- selective use of full-width or two-column editorial blocks,
- quiet surface separation rather than heavy boxes.

### Imagery

Initial mode: **graphic / muted**.

Use:

- abstract botanical or petal-like forms,
- linework,
- restrained organic geometry,
- tactile editorial texture.

Do not use:

- generic stock-office photography,
- generic smiling corporate people,
- pseudo-luxury product imagery,
- a portrait of Grace unless she intentionally supplies and approves one.

### Motion

Subtle only:

- small elevation / underline changes,
- restrained entrance transitions,
- no bouncing, counters, celebratory animations or gamified progress.

**Provenance:** `EXPLICIT_USER` + current Grace visual direction. Prada/Gucci references are service metaphors, not `VISUAL_HARVEST` records.

---

## V7 — Interaction Signature

### Landing emphasis

Grace should arrive at **what is ready and what she can do next**, not at configuration.

### Primary interaction journey

Visible journey:

```text
Hitta jobb → Analysera? → Sök → Följ
```

The deeper CareerHub contract remains:

```text
Profile → Search → Analyse → Apply → Track
```

The two are compatible: the first is the service-facing simplification, the second is the canonical information architecture.

### Search

Normal search presents:

1. saved search scope in plain Swedish,
2. one optional field: **Specifika önskemål eller behov**,
3. primary action: **Sök jobb**.

Technical lane selection must not be required from Grace.

### Analyse

Primary decision:

> **Vill du analysera det här jobbet?**

CTA:

> **JA — Analysera**

### Apply

Application material is prepared, never auto-submitted.

### Track

Timeline should read as a service journey, not a database state machine.

**Provenance:** `EXPLICIT_USER` + existing Grace workflow + CHZero interaction contract.

---

## V8 — Reference Provenance

Every material design deviation must remain explainable.

Canonical provenance map for WP01:

| Decision | Provenance state |
|---|---|
| Always address user as “du” | `EXPLICIT_USER` |
| “När du vill” service language | `EXPLICIT_USER` / `CHAT_PATTERN` |
| Quiet-luxury service posture | `EXPLICIT_USER` |
| Airy layout / high guidance | `EXPLICIT_USER` + usability signal |
| Ivory/petrol/cream/saffron/coral palette | `EXPLICIT_USER` |
| Serif editorial display direction | `EXPLICIT_USER` / design synthesis |
| One professional surface for now | `VERIFIED_CAREER` + CHZero contract |
| No unverified title in hero | `VERIFIED_CAREER` boundary |
| No technical CareerHub vocabulary in primary UX | CHZero canonical UX + `EXPLICIT_USER` |
| No portrait without supplied/approved image | evidence / asset boundary |

No sensitive/private-life attribute is an admissible provenance source.

---

# 6. Canonical configuration target

## 6.1 `personalisation/hub.profile.yaml`

Target:

```yaml
schema_version: "1.0"

identity:
  display_name: "Grace"
  strapline: "Erfarenheten följer med. Riktningen kan förändras."
  language: "sv"

experience:
  mode: "editorial"
  density: "airy"
  guidance: "high"
  motion: "subtle"

home:
  headline: "Välkommen, Grace. Nästa steg är redan framlagt."
  intro: "Se möjligheter, välj vad du vill titta närmare på och gå vidare när det känns rätt. Vi håller ihop analys, underlag och uppföljning."
  slots:
    - identity
    - next_action
    - opportunities
    - pipeline
    - artifacts
    - profile_health

navigation:
  primary:
    - home
    - find
    - analyse
    - apply
    - track
    - profile
    - library
  labels:
    home: "Översikt"
    find: "Hitta jobb"
    analyse: "Analysera"
    apply: "Sök"
    track: "Följ"
    profile: "Min profil"
    library: "Mina underlag"

modules:
  portfolio: false
  analytics: true
  profile_health: true
  geography: true
  hrdm_explainer: false

visibility:
  show_verified_sources: false
  show_match_scores: true
  show_hrdm_trace: false
  show_application_history: true
```

### Why this differs from the current file

The current profile leads with “build the profile / configure search” and system verification language. WP01 changes the first impression from **setup state** to **prepared service** while preserving the evidence boundary underneath.

---

## 6.2 `personalisation/theme.tokens.json`

Target must validate against the current CareerHubZero theme schema.

```json
{
  "schema_version": "1.0",
  "typography": {
    "display": "Iowan Old Style, Baskerville, Georgia, ui-serif, serif",
    "body": "Inter, Aptos, ui-sans-serif, system-ui, sans-serif",
    "scale": "large"
  },
  "shape": {
    "radius": "soft",
    "border": "quiet"
  },
  "surface": {
    "treatment": "editorial",
    "shadow": "subtle"
  },
  "palette": {
    "background": "#F7F1E3",
    "foreground": "#1B2220",
    "muted": "#7F7A5B",
    "accent": "#063A3D",
    "accent_foreground": "#FFFFFF"
  },
  "imagery": {
    "mode": "graphic",
    "treatment": "muted"
  }
}
```

### Current defect to remove

The present Grace token file uses values such as:

- `scale: balanced`
- `radius: 10px`
- CSS declaration as `border`
- `surface.treatment: soft`

Those are not valid values in the current CHZero theme-token schema and must be replaced rather than patched around.

---

## 6.3 `personalisation/voice.yaml`

Target:

```yaml
schema_version: "1.0"
voice:
  posture: "varm, vuxen, självsäker, diskret serviceorienterad"
  person: "second"
  verbosity: "compact"
  avoid:
    - "tredjeperson om Grace i löpande text"
    - "teknisk CareerHub-terminologi på användarytor"
    - "generiska karriärklyschor"
    - "myndighets- eller HR-språk"
    - "startup-ton och gamifiering"
    - "överdrivna eller obelagda styrkepåståenden"
  prefer:
    - "när du vill"
    - "när något känns intressant"
    - "vi har förberett nästa steg"
    - "en tydlig nästa handling åt gången"
    - "kort och evidensbunden förklaring"
    - "service före instruktion"
```

The current Grace `voice.yaml` uses a legacy shape and must be normalized to the current central voice contract.

---

# 7. Required new provenance files

WP01 creates the missing canonical personalisation records:

```text
CareerHub/personalisation/
  hub.profile.yaml
  theme.tokens.json
  voice.yaml
  derivation.yaml        ← new
  references.yaml        ← new
  visual-harvest.yaml    ← new
```

## `derivation.yaml`

Records:

- eight-vector signature,
- every material person-specific decision,
- source class,
- confidence / lock state,
- what is deliberately unchanged from CH-Core.

## `references.yaml`

Registers only references that are permitted to influence presentation.

The Prada / Gucci metaphor is recorded as an **explicit service brief**, not as harvested brand design.

## `visual-harvest.yaml`

Records actual observed visual characteristics only.

For WP01 initial execution:

```text
state: STRUCTURE_READY
external_visual_reference_state: REFERENCE_PENDING
```

unless a nominated external visual reference is later supplied and actually inspected.

---

# 8. Central CareerHubZero dependency

WP01 identifies one central blocker that must be solved centrally rather than in Grace:

**CareerOverview still contains hard-coded English user-facing microcopy.**

Examples include actions and labels equivalent to:

- “See current profile”
- “Search with my settings”
- “Current direction”
- “Profile state”
- “Next useful move”

### Required central correction

CareerHubZero must make this copy either:

1. language-aware from `identity.language`, or
2. configurable through the protected personalisation contract.

### Rule

Do **not** create a Grace-specific local copy of `CareerOverview.tsx`.

That would violate the unified-body architecture.

---

# 9. WP01 implementation sequence

## G-WP1.1 — Contract repair

- replace invalid `theme.tokens.json` values with schema-valid tokens,
- normalize `voice.yaml` to the central shape,
- validate `hub.profile.yaml` against the current personalised-hub schema.

**Exit:** all three files validate against central schemas/contracts.

---

## G-WP1.2 — Grace derivation package

Create:

- `derivation.yaml`
- `references.yaml`
- `visual-harvest.yaml`

Populate provenance for all eight vectors.

**Exit:** every non-default decision has a traceable source class.

---

## G-WP1.3 — Information hierarchy inversion

From:

```text
profile setup → verification state → configuration → opportunity
```

To:

```text
welcome → next action → opportunities → progress → prepared material → profile status
```

**Exit:** normal landing page is useful without knowledge of evidence mechanics.

---

## G-WP1.4 — Swedish service-language pass

Audit all normal Grace surfaces:

- Home
- Profile
- Hitta jobb
- Analysera
- Sök
- Följ
- Mina underlag
- Wish / improvement surface

Rules:

- second person,
- service-oriented,
- no system jargon,
- no third-person Grace prose,
- no mixed English/Swedish normal UI,
- errors remain precise and actionable.

**Exit:** normal user path is Swedish end-to-end.

---

## G-WP1.5 — Central localisation dependency

Implement the required generic localisation/configuration change in CareerHubZero.

Then sync through the central web-shell path into Grace.

**Exit:** no Grace-local component fork exists.

---

## G-WP1.6 — Editorial visual implementation

Apply the canonical Grace theme through shared CSS variables and reusable CHZero components.

Required visual behaviour:

- ivory field,
- petrol primary actions,
- serif editorial display hierarchy,
- high whitespace,
- quiet borders,
- restrained shadows,
- botanical / organic graphic accent capability,
- no dense SaaS card-wall as primary composition.

Secondary saffron/coral accents must not create low-contrast text states.

**Exit:** the hub reads visually as one coherent Grace environment across pages.

---

## G-WP1.7 — Responsive and accessibility gate

Check:

- keyboard navigation,
- focus visibility,
- semantic heading order,
- normal text contrast,
- CTA contrast,
- zoom/reflow,
- reduced-motion behaviour,
- mobile legibility,
- no colour-only state communication.

**Exit:** no unresolved accessibility failure.

---

## G-WP1.8 — Anti-generic audit

Audit the eight material dimensions:

| Dimension | Grace-specific target |
|---|---|
| Information hierarchy | changed |
| Module ordering | changed |
| Career surfaces | intentionally unchanged / one surface |
| Voice | changed |
| Density | changed |
| Visual grammar | changed |
| Interaction defaults | changed |
| Content framing | changed |

Target nominal genericity distance:

```text
G = 7 / 8 = 0.875
```

This is only a guardrail. Provenance and usability still determine validity.

**Exit:** anti-generic audit PASS with at least five material source-backed differences and at least four active vectors beyond identity.

---

## G-WP1.9 — Grace preview

Produce a rendered desktop and mobile preview.

Review questions:

1. Does this feel like it is made for you?
2. Do you immediately know what you can do next?
3. Is anything too technical?
4. Is anything too wordy?
5. Does it feel calm, adult and welcoming?
6. Does the visual identity feel distinctive without feeling theatrical?

**Exit:** reviewer feedback recorded.

---

## G-WP1.10 — Personalisation lock

WP01 reaches `PERSONALISATION_LOCK` only when:

- profile/theme/voice contracts validate,
- provenance package is complete,
- central localisation dependency is resolved,
- Swedish UX pass is complete,
- accessibility gate passes,
- anti-generic audit passes,
- rendered preview has been reviewed,
- no unsupported candidate claim has entered presentation.

---

# 10. Must replace / must not create

## Replace

- current invalid Grace theme tokens,
- legacy voice-file shape,
- setup-led homepage language,
- system-centred information order,
- English central microcopy on normal Grace surfaces.

## Do not create

- Grace-specific runtime,
- Grace-local fork of central React components,
- duplicate design system,
- a second evidence truth,
- a speculative professional title,
- a fake portfolio surface,
- sensitive/private personalisation signals,
- copied Prada/Gucci trade dress.

---

# 11. Final acceptance state

WP01 is complete when Grace's hub can be described accurately as:

> **A Swedish, editorial, high-service CareerHub with quiet-luxury visual grammar, an airy guided interaction model and a clear evidence boundary — materially personalised to Grace while still running entirely on the shared CareerHubZero body.**

User-facing principle:

> **Du väljer riktning och tempo. CareerHub förbereder nästa steg och håller ihop resten.**

---

# 12. WP status

```yaml
wp_id: G-WP01
name: Grace Graphic Profile
state: READY_FOR_EXECUTION
central_body: Motherpher/CareerHubZero
profile_node: Motherpher/Gracey
personalisation_lock: false
structure_ready: true
implementation_ready: true
blocking_dependency:
  - central CareerOverview localisation/configurable microcopy
next_action:
  - execute G-WP1.1 through G-WP1.10
```

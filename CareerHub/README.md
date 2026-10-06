# Grace · CareerHub

Grace är ett aktivt profilerat CareerHub-node under den centrala CareerHubZero-motorn.

- Repository: `Motherpher/Gracey`
- Central motor: `Motherpher/CareerHubZero`
- Current central release: `0.2.9-alpha`
- Runtime model: **unified body / thin profile node**
- Local authoritative motor: **none**
- Profile contract: [`careerhub.yaml`](careerhub.yaml)

## Evidence boundary

Den matchningsbara kandidatprofilen får endast genereras från **verifierade karriärkällor**.

Tillåtna källtyper är CV, professionell profil, dokumenterad anställning, utbildning/examen, certifiering, portfolio/arbetsprov, arbetsgivarreferens och verifierat projektrecord.

Privatliv, modellminne, samtalsintryck, lösa biografiska uppgifter och icke verifierade påståenden har ingen väg in i kandidatprofilen.

## Search-only raster

Grace kan vid sökning skriva **specifika önskemål eller behov**. Detta lagras och behandlas som `user_input / search_only`.

Det får påverka:

- sourcing,
- filtrering,
- ranking,
- presentationsordning.

Det får inte påverka:

- kandidatfakta,
- CV-påståenden,
- HRDM proof points,
- ansökningspåståenden.

## Current state

- Verified career sources: **0**
- Verified candidate evidence: **0**
- Current profile-matched jobs: **0 until verified sources are added or a one-search raster is supplied**
- Historical job vault: **preserved**
- Historical Region Stockholm application artifact: **retired from external use**
- Web shell: **centrally managed**
- Central runtime cutover: **complete**

## Canonical journey

**Profile → Search → Analyse → Apply → Track**

1. Add and verify career sources.
2. Build or review source-bound evidence.
3. Search from the verified profile, optionally with a temporary wishes/needs raster.
4. Run HRDM-R on selected roles.
5. Generate application material only from verified evidence and a valid analysis.
6. Track application state and outcomes separately from the candidate profile.

**[Open Grace CareerHub →](CONTROL_ROOM.md)**

Migration and alignment record: [`MIGRATION_STATUS.md`](MIGRATION_STATUS.md)

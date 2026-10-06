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

## Verified professional source

Grace LinkedIn-profil är nu registrerad som den första verifierade professionella källan:

https://www.linkedin.com/in/grace-assabil-b304b340/

Den offentliga indexeringen stödjer två kandidatfakta:

- professionell anknytning till **Region Skåne**,
- professionell geografisk kontext: **Greater Malmö Metropolitan Area**.

Övriga arbetsrelaterade teman från intervjumaterial ligger kvar i verifieringskö tills de styrks av CV eller annan godkänd karriärkälla.

## Search-only raster

Vid sökning kan du skriva **specifika önskemål eller behov**. Detta behandlas som `user_input / search_only`.

Det får påverka sourcing, filtrering, ranking och presentationsordning, men inte kandidatfakta, CV-påståenden, HRDM proof points eller ansökningspåståenden.

## Current state

- Verified career sources: **1**
- Verified candidate evidence: **2**
- Next primary verification source: **current CV**
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

Profile source register: [`profile/SOURCE_REGISTER.md`](profile/SOURCE_REGISTER.md)  
Migration and alignment record: [`MIGRATION_STATUS.md`](MIGRATION_STATUS.md)

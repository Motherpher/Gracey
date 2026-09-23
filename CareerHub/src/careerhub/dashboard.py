from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from dateutil import parser as dtparser

from .models import Job
from .state import STATUS_LABELS, TERMINAL_STATUSES, case_counts, rank_label


REPO = "Hybrismannen/Gracey"
PALETTE = {
    "paper": "#F4D59B",
    "ink": "#1B2220",
    "cobalt": "#063A3D",
    "blue": "#063A3D",
    "pale": "#F7F1E3",
    "coral": "#D94A3A",
    "sun": "#F2A000",
    "white": "#F7F1E3",
}


def save_public_jobs(path: Path, jobs: list[Job]):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(jobs),
        "jobs": [j.public_dict() for j in jobs],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def priority_label(index: int) -> str:
    if index < 4:
        return "Stark träff"
    if index < 8:
        return "Bra möjlighet"
    return "Utforska"


def deadline_info(value: str) -> tuple[str, int | None]:
    if not value:
        return "No deadline shown", None
    try:
        d = dtparser.parse(str(value))
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        days = (d.date() - datetime.now(timezone.utc).date()).days
        label = d.strftime("%d %b")
        if days < 0:
            return f"{label} · closed", days
        if days == 0:
            return f"{label} · today", days
        if days == 1:
            return f"{label} · 1 day", days
        return f"{label} · {days} days", days
    except Exception:
        return str(value), None


def why_short(job: Job) -> str:
    reasons = []
    blob = job.search_blob
    if job.work_mode:
        reasons.append(job.work_mode)
    elif "remote" in blob or "distans" in blob:
        reasons.append("remote")
    if any(x in blob for x in ["part time", "part-time", "deltid"]):
        reasons.append("part-time")
    if job.matched_query:
        reasons.append(f"matches {job.matched_query}")
    return " · ".join(reasons[:2]) or "matched search profile"


def choose_link(job: Job, default_priority: int = 3) -> str:
    title = f"[CareerHub Job] {job.company or 'Employer'} — {job.title}"
    body = (
        "### Job URL\n"
        f"{job.url}\n\n"
        "### Job ID\n"
        f"{job.id}\n\n"
        "### Role\n"
        f"{job.title}\n\n"
        "### Employer\n"
        f"{job.company}\n\n"
        "### Lane\n"
        f"{job.lane}\n\n"
        "### Priority 1–5\n"
        f"{default_priority}\n\n"
        "### Deadline\n"
        f"{job.deadline or ''}\n\n"
        "### Job text (optional)\n"
        "_Leave blank unless the site blocks automated retrieval._"
    )
    return f"https://github.com/{REPO}/issues/new?title={quote(title)}&body={quote(body)}"


def choose_any_link() -> str:
    return f"https://github.com/{REPO}/issues/new?template=careerhub-choose-job.yml"


def status_update_link(case: dict, status: str) -> str:
    issue = int(case.get("issue_number") or 0)
    label = STATUS_LABELS.get(status, status)
    title = f"[CareerHub Update] #{issue} — {label}"
    body = (
        "### Grace · Karriärhubben case issue\n"
        f"{issue}\n\n"
        "### New status\n"
        f"{status}\n\n"
        "### Date\n"
        f"{datetime.now(timezone.utc).date().isoformat()}\n\n"
        "### Next action (optional)\n\n"
        "### Next action date (optional)\n"
    )
    return f"https://github.com/{REPO}/issues/new?title={quote(title)}&body={quote(body)}"


def lane_title(lane: str) -> tuple[str, str]:
    return {
        "core": ("Huvudspår", "Handledande, samordnande, utbildande och relationsnära roller där Grace befintliga erfarenhet kommer till tydlig användning."),
        "adjacent": ("Närliggande möjligheter", "Närliggande roller där handledning, samordning, stöd och tryggt ledarskap kan överföras till en ny miljö."),
        "bridge": ("Flexibelt / extra", "Deltid, tidsbegränsade roller och andra arbeten som kan fungera som en trygg bro till nästa steg."),
    }.get(lane, (lane.title(), ""))


def render_visual(path: Path, jobs: list[Job], cases_data: dict, vault: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    counts = case_counts(cases_data)
    active_deadlines = 0
    for job in jobs:
        _, days = deadline_info(job.deadline)
        if days is not None and 0 <= days <= 7:
            active_deadlines += 1

    found = len(jobs)
    chosen = counts["chosen"]
    applied = counts["applied"]
    total_seen = int(vault.get("total_jobs_ever_seen") or found)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560">
<rect width="1200" height="560" fill="{PALETTE["paper"]}"/>
<path d="M-80 90 C160 40 250 230 420 175 C585 122 565 390 730 328 C880 272 930 120 1280 220"
      fill="none" stroke="{PALETTE["cobalt"]}" stroke-width="92" stroke-linecap="round"/>
<text x="68" y="68" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="{PALETTE["ink"]}" letter-spacing="2">GRACE · KARRIÄRHUBBEN</text>
<text x="68" y="480" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="{PALETTE["ink"]}">Tre steg till nästa jobb</text>
<g transform="translate(110 122)">
  <circle cx="0" cy="0" r="70" fill="{PALETTE["paper"]}" stroke="{PALETTE["cobalt"]}" stroke-width="5"/>
  <text x="0" y="-12" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{PALETTE["ink"]}">1 · HITTA</text>
  <text x="0" y="21" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="800" fill="{PALETTE["cobalt"]}">{found}</text>
  <text x="0" y="46" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="{PALETTE["ink"]}">aktuella jobb</text>
</g>
<g transform="translate(518 290)">
  <circle cx="0" cy="0" r="78" fill="{PALETTE["pale"]}" stroke="{PALETTE["blue"]}" stroke-width="5"/>
  <text x="0" y="-16" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{PALETTE["ink"]}">2 · VÄLJ</text>
  <text x="0" y="23" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="800" fill="{PALETTE["blue"]}">{chosen}</text>
  <text x="0" y="49" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="{PALETTE["ink"]}">valda jobb</text>
</g>
<g transform="translate(940 208)">
  <circle cx="0" cy="0" r="78" fill="{PALETTE["sun"]}" stroke="{PALETTE["ink"]}" stroke-width="4"/>
  <text x="0" y="-16" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{PALETTE["ink"]}">3 · SÖK</text>
  <text x="0" y="23" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="800" fill="{PALETTE["ink"]}">{applied}</text>
  <text x="0" y="49" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="{PALETTE["ink"]}">pågående</text>
</g>
<g transform="translate(770 430)">
  <rect x="0" y="0" rx="25" width="350" height="74" fill="{PALETTE["coral"]}"/>
  <text x="24" y="31" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="700" fill="{PALETTE["ink"]}">{active_deadlines} sista datum inom 7 dagar</text>
  <text x="24" y="54" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="{PALETTE["ink"]}">{total_seen} jobb sparade i historiken</text>
</g>
</svg>'''
    path.write_text(svg, encoding="utf-8")


def render_job_vault(path: Path, vault: dict, cases_data: dict):
    cases_by_job = {c.get("job_id"): c for c in cases_data.get("cases", []) if c.get("job_id")}
    records = vault.get("jobs", [])
    active = [r for r in records if r.get("in_latest_scan")]
    historic = [r for r in records if not r.get("in_latest_scan")]
    lines = [
        "# Job Vault", "",
        f"**{len(records)} jobs preserved** · {len(active)} in the latest scan · {len(historic)} historical", "",
        "Nothing disappears when a new sourcing run replaces the shortlist. The full machine-readable history is in CareerHub/data/job_vault.json.", "",
        "## Current / recently sourced", "",
        "| Rank | Role | Employer | Deadline | First seen | Last seen | State | Action |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in active[:100]:
        case = cases_by_job.get(r.get("id"))
        rank = rank_label(case.get("priority")) if case else "—"
        deadline, _ = deadline_info(r.get("deadline", ""))
        title = str(r.get("title") or "").replace("|", "\\|")
        company = str(r.get("company") or "").replace("|", "\\|")
        url = r.get("url") or "#"
        if case:
            action = f"[case #{case.get('issue_number')}]({case.get('issue_url')})"
        else:
            action = f"**[Välj →]({choose_link(Job.from_dict(r), 3)})**"
        lines.append(f"| {rank} | [{title}]({url}) | {company} | {deadline} | {str(r.get('first_seen',''))[:10]} | {str(r.get('last_seen',''))[:10]} | active | {action} |")
    lines += ["", "## Historical / no longer in the latest shortlist", "", "| Role | Employer | Deadline | Last seen | State | Action |", "|---|---|---|---|---|---|"]
    for r in historic[:180]:
        deadline, _ = deadline_info(r.get("deadline", ""))
        title = str(r.get("title") or "").replace("|", "\\|")
        company = str(r.get("company") or "").replace("|", "\\|")
        url = r.get("url") or "#"
        case = cases_by_job.get(r.get("id"))
        if case:
            action = f"[case #{case.get('issue_number')}]({case.get('issue_url')})"
        else:
            action = f"**[Välj →]({choose_link(Job.from_dict(r), 2)})**"
        lines.append(f"| [{title}]({url}) | {company} | {deadline} | {str(r.get('last_seen',''))[:10]} | {r.get('deadline_state') or 'historic'} | {action} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_applications(path: Path, cases_data: dict):
    cases = cases_data.get("cases", [])
    active = [c for c in cases if c.get("status") not in TERMINAL_STATUSES]
    closed = [c for c in cases if c.get("status") in TERMINAL_STATUSES]
    active.sort(key=lambda c: (-int(c.get("priority") or 3), c.get("deadline") or "9999"))
    lines = [
        "# Applications & Follow-up", "",
        "One chosen job becomes one CareerHub case. This is the process monitor after the job has left the sourcing board.", "",
        "## Active cases", "",
        "| Priority | Role | Employer | Status | Deadline | Next action | Next date | Case |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for c in active:
        deadline, _ = deadline_info(c.get("deadline", ""))
        title = str(c.get("title") or "").replace("|", "\\|")
        company = str(c.get("company") or "").replace("|", "\\|")
        issue = c.get("issue_number")
        issue_url = c.get("issue_url") or f"https://github.com/{REPO}/issues/{issue}"
        next_action = str(c.get("next_action") or "—").replace("|", "\\|")
        next_date = str(c.get("next_action_date") or "—")[:10]
        lines.append(f"| **{rank_label(c.get('priority'))}** | [{title}]({c.get('url') or issue_url}) | {company} | **{STATUS_LABELS.get(c.get('status'), c.get('status'))}** | {deadline} | {next_action} | {next_date} | [#{issue}]({issue_url}) |")
    lines += ["", "## Closed cases", "", "| Role | Employer | Outcome | Updated |", "|---|---|---|---|"]
    for c in closed[-60:]:
        lines.append(f"| {str(c.get('title') or '').replace('|','\\|')} | {str(c.get('company') or '').replace('|','\\|')} | {STATUS_LABELS.get(c.get('status'), c.get('status'))} | {str(c.get('status_updated_at') or '')[:10]} |")
    lines += ["", "## Så följs en ansökan", "", "Valt → Förbereds → Redo att söka → Ansökan skickad → Kontakt → Arbetsprov/Test → Intervju/Möte 1–5 → Erbjudande / Avslutad / Avstår"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def case_actions(case: dict) -> str:
    status = case.get("status")
    if status in TERMINAL_STATUSES:
        return "—"
    actions = []
    if status in {"saved", "preparing", "ready"}:
        actions.append(f"[Mark applied]({status_update_link(case, 'applied')})")
    if status == "applied":
        actions.append(f"[Contacted]({status_update_link(case, 'contacted')})")
        actions.append(f"[Denied]({status_update_link(case, 'denied')})")
    if status in {"contacted", "portfolio"}:
        actions.append(f"[Interview 1]({status_update_link(case, 'interview_1')})")
        actions.append(f"[Meeting 1]({status_update_link(case, 'meeting_1')})")
        actions.append(f"[Portfolio/Test]({status_update_link(case, 'portfolio')})")
    if str(status).startswith("interview_"):
        n = int(str(status).split("_")[1])
        if n < 5:
            actions.append(f"[Interview {n+1}]({status_update_link(case, f'interview_{n+1}')})")
        actions.append(f"[Offer]({status_update_link(case, 'offer')})")
        actions.append(f"[Denied]({status_update_link(case, 'denied')})")
    if str(status).startswith("meeting_"):
        n = int(str(status).split("_")[1])
        if n < 5:
            actions.append(f"[Meeting {n+1}]({status_update_link(case, f'meeting_{n+1}')})")
        actions.append(f"[Interview 1]({status_update_link(case, 'interview_1')})")
        actions.append(f"[Offer]({status_update_link(case, 'offer')})")
    return " · ".join(actions[:3]) or f"[Update status](https://github.com/{REPO}/issues/new?template=careerhub-update-status.yml)"


def render_lane(lines: list[str], lane: str, jobs: list[Job], cases_by_job: dict):
    title, explanation = lane_title(lane)
    lines += [f"### {title}", "", explanation, ""]
    visible = jobs[:8]
    if not visible:
        lines += ["No current leads in this group.", ""]
        return
    lines += ["| Prioritet | Roll | Arbetsgivare | Sista dag | Varför | Välj |", "|---|---|---|---|---|---|"]
    for index, job in enumerate(visible):
        deadline, days = deadline_info(job.deadline)
        if days is not None and 0 <= days <= 3:
            deadline = f"**{deadline}**"
        title_txt = job.title.replace("|", "\\|")
        company = (job.company or "—").replace("|", "\\|")
        source_link = f"[{title_txt}]({job.url})" if job.url else title_txt
        if job.id in cases_by_job:
            c = cases_by_job[job.id]
            choose = f"Valt · [jobbsida #{c.get('issue_number')}]({c.get('issue_url')})"
        else:
            default_priority = 5 if index < 2 else 4 if index < 5 else 3
            choose = f"**[Välj →]({choose_link(job, default_priority)})**"
        lines.append(f"| {priority_label(index)} | {source_link} | {company} | {deadline} | {why_short(job).replace('|','\\|')} | {choose} |")
    lines += ["", f"_Showing the top {len(visible)} of {len(jobs)} current leads in this group._", ""]


def render_control_room(path: Path, jobs: list[Job], lane: str, cases_data: dict, vault: dict):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    by_lane = {"core": [j for j in jobs if j.lane == "core"], "adjacent": [j for j in jobs if j.lane == "adjacent"], "bridge": [j for j in jobs if j.lane == "bridge"]}
    cases = cases_data.get("cases", [])
    cases_by_job = {c.get("job_id"): c for c in cases if c.get("job_id")}
    active_cases = [c for c in cases if c.get("status") not in TERMINAL_STATUSES]
    active_cases.sort(key=lambda c: (-int(c.get("priority") or 3), c.get("deadline") or "9999"))
    lines = [
        "![CareerHub journey](visuals/careerhub-journey.svg)", "",
        "# Grace · Karriärhubben", "",
        "## 1 · HITTA JOBB → 2 · VÄLJ JOBB → 3 · SÖK", "",
        "Allt annat sköts i bakgrunden. Grace behöver bara följa de tre stegen.", "",
        "---", "",
        "## 1 · Hitta jobb", "",
        f"**Senast uppdaterad:** {now} · **{len(jobs)} live leads** · **{vault.get('total_jobs_ever_seen', len(jobs))} jobs in the historic vault**", "",
        "**När du trycker på Uppdatera jobb:** nya jobb brukar synas här efter ungefär **30–90 sekunder**. Sidan uppdateras när sökningen är klar.", "",
        f"**[Uppdatera jobb →](https://github.com/{REPO}/actions/workflows/careerhub-scan.yml)** · **[Öppna jobbhistoriken →](JOB_VAULT.md)** · **[Jag hittade ett jobb själv →]({choose_any_link()})**", "",
    ]
    for lane_name in ["core", "adjacent", "bridge"]:
        if lane == "all" or lane == lane_name:
            render_lane(lines, lane_name, by_lane[lane_name], cases_by_job)
    lines += [
        "---", "", "## 2 · Välj jobb", "",
        "Välj bara de jobb som känns värda din tid. **Välj →** öppnar en färdig jobbsida. Du behöver normalt inte ändra något – tryck bara på **Skapa jobbsida**.", "",
        "Karriärhubben prioriterar jobbet, går igenom hur väl det passar Grace och förbereder ett ansökningsunderlag.", "",
        "Prioritet: **5 Sök · 4 Mycket intressant · 3 Intressant · 2 Svagare träff · 1 Avvakta**", "",
    ]
    if active_cases:
        lines += ["| Nivå | Jobb | Läge | Sista dag | Nästa steg |", "|---|---|---|---|---|"]
        for c in active_cases[:12]:
            deadline, days = deadline_info(c.get("deadline", ""))
            if days is not None and 0 <= days <= 3:
                deadline = f"**{deadline}**"
            issue_url = c.get("issue_url") or f"https://github.com/{REPO}/issues/{c.get('issue_number')}"
            title = str(c.get("title") or "").replace("|", "\\|")
            company = str(c.get("company") or "").replace("|", "\\|")
            lines.append(f"| **{c.get('priority',3)} / 5 · {rank_label(c.get('priority'))}** | [{title} — {company}]({issue_url}) | **{STATUS_LABELS.get(c.get('status'), c.get('status'))}** | {deadline} | {case_actions(c)} |")
    else:
        lines += ["Inga jobb är valda ännu. Tryck **Välj →** på ett jobb ovan.", ""]
    lines += [
        "", f"**[Öppna ansökningsöversikten →](APPLICATIONS.md)**", "",
        "---", "", "## 3 · Sök", "",
        "För varje valt jobb förbereder hubben en tydlig matchning, en kort arbetsgivarbild och ett redigerbart ansökningsutkast.", "",
        "1. Öppna jobbsidan.",
        "2. Ladda ner och justera ansökningsunderlaget.",
        "3. Skicka ansökan till arbetsgivaren.",
        "4. Markera **Ansökan skickad**.",
        "5. Följ sedan processen: kontakt, arbetsprov/test, intervju eller möte 1–5, erbjudande eller avslut.", "",
        "### Påminnelser", "",
        "Valda jobb kan få automatiska påminnelser före sista ansökningsdag. Påminnelser på jobbsidan kräver inget extra. E-post och sms kan kopplas på senare utan att kontaktuppgifter behöver ligga i vanliga filer.", "",
        "**[Ställ in påminnelser →](SETUP.md#deadline-reminders)**", "",
        "---", "",
        "<details>", "<summary><strong>Profil, integritet och inställningar</strong></summary>", "",
        "- [Se vad karriärhubben vet om Grace](profile/PROFILE_REVIEW.md)",
        "- [Integritet och privat arbetssätt](PRIVACY.md)",
        "- [Inställningar och påminnelser](SETUP.md)",
        "- [Jobbkällor](docs/SOURCE_MATRIX.md)",
        "- [Fördjupad matchningslogik](hrdm/HRDM_R_v6.3.md)", "",
        "</details>",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

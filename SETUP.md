# GitHub Profile Setup — Samiuzzaman Sahil

This folder contains everything needed for a professional GitHub profile README, styled to match your résumé (charcoal + copper, clean typography).

```
github-profile/
├─ README.md                 ← the profile README
├─ assets/
│  ├─ banner-dark.png        ← banner for GitHub dark mode
│  └─ banner-light.png       ← banner for GitHub light mode
├─ make_banner.py            ← regenerates the banners if details change
└─ SETUP.md                  ← this guide
```

---

## 1. Publish the profile README

GitHub shows a special README on your profile when you own a **public** repository whose name matches your username exactly: **`SamiSahil`**.

### Option A — GitHub website (easiest)

1. Open <https://github.com/new>.
2. **Repository name:** `SamiSahil` (exact spelling and capitalisation).
3. Set visibility to **Public**.
4. Do **not** add a README, .gitignore or licence — the repository must start empty.
5. Click **Create repository**.
6. On the empty repository page, click **uploading an existing file**.
7. Drag in `README.md` and the whole `assets` folder (keep the folder name `assets`).
8. Commit with the message `Add professional GitHub profile`.

### Option B — Git (already prepared)

This folder is already a Git repository with one commit and the remote configured. Run:

```powershell
cd C:\Users\Sahil\Documents\github-profile
git push -u origin main
```

Git Credential Manager will open a browser window to sign in the first time. Create the empty `SamiSahil` repository on GitHub first (steps 1–5 above), then push.

If you copy these files to another machine instead, initialize the repository yourself:

```powershell
git init
git add README.md SETUP.md make_banner.py assets
git commit -m "Add professional GitHub profile"
git branch -M main
git remote add origin https://github.com/SamiSahil/SamiSahil.git
git push -u origin main
```

### Verify

Visit <https://github.com/SamiSahil>. The banner and README should appear above your pinned repositories. If images look stale, press **Ctrl + F5**.

> The banner switches automatically between dark and light artwork using GitHub's theme preference. If your browser does not support that, the light banner is used.

---

## 2. Update your GitHub profile fields

Go to <https://github.com/settings/profile> and use these values:

| Field | Value |
| --- | --- |
| **Name** | `Samiuzzaman Sahil` |
| **Bio** | `Full-Stack Developer · CSE student at Uttara University · React, Node.js, Express & PostgreSQL.` |
| **Company** | `Uttara University` |
| **Location** | `Dhaka, Bangladesh` |
| **Website** | `https://samisahil.github.io/portfolio/` |
| **Social links** | `https://www.linkedin.com/in/samiuzzaman-sahil-11a833385/` and `https://samisahil.github.io/portfolio/` |
| **Pronouns** | Optional |

Your current bio — *"Passionate About Exploring Something New…"* — is friendly but says nothing searchable. Recruiters and collaborators scan for role, stack and university, so the version above is more useful.

---

## 3. Pin the right repositories

On your profile, click **Customize your pins** and pin these four (drag to order):

1. `edusysv1` — EduSysPro school management system
2. `aicinventory` — AIC Inventory dashboard
3. `attendance` — Student attendance system
4. `samiprofile` — Personal portfolio

Add `PYTHON`, `My-First-Web` or another project only if it has a clear README.

---

## 4. Polish the repositories (the part that matters most)

A polished README gets attention; empty repository descriptions undo it. For each pinned repo, click the gear icon next to **About** and set:

| Repository | Description | Website |
| --- | --- | --- |
| `edusysv1` | Full-stack school management system with role-based portals for students, teachers, accountants and staff. | - |
| `aicinventory` | Inventory dashboard for stock levels, orders, profitability and delivery tracking — React + Google OAuth. | `https://SamiSahil.github.io/aicinventory` |
| `attendance` | Student attendance tracker with monthly reports — React + Vite. | `https://SamiSahil.github.io/attendance` |
| `samiprofile` | Personal portfolio with animated sections and a typewriter intro — React + Framer Motion. | `https://samisahil.github.io/portfolio/` |

Suggested **topics** (comma-separated): `react`, `vite`, `tailwindcss`, `nodejs`, `express`, `mongodb`, `full-stack`, `portfolio`.

Other quick wins:

- **Fix `Password-Generator`** — its description currently says *"Config files for my GitHub profile"*, which is incorrect and confusing. Replace it with an accurate one-liner.
- **Add descriptions** to `school`, `edu`, `restos`, `rsos`, `youware` — or archive the ones that are only practice work. An empty or unexplained repo adds no signal.
- **Add a README to each pinned project** with: one-line summary, screenshot or GIF, features, tech stack, setup steps, and the live link. Screenshots make the biggest difference.
- **Add a licence** (MIT is fine for portfolio projects) so others know how they may use the code.
- **Optional rename:** `edusysv1` → `edusyspro` looks more finished. GitHub redirects the old URL, but update the two links in `README.md` if you rename it.
- **Optional:** enable *Include private contributions on my profile* under contribution settings if you want a fuller activity graph.

---

## 5. Privacy note

I deliberately left your phone number off the public README. Email, portfolio and GitHub are enough for first contact; share the phone number only when needed.

---

## 6. If you want changes

- Edit `README.md` directly and commit.
- To change the banner wording (name, tagline, tech line, location), edit the `CONTENT` block at the top of `make_banner.py`, then run:

```powershell
python make_banner.py
```

- LinkedIn: `https://www.linkedin.com/in/samiuzzaman-sahil-11a833385/` (badge added to the README)
- The stats cards are served by `github-readme-stats.vercel.app`. If they ever fail to load, it is usually temporary rate limiting — wait a few minutes or self-host the service.

### Two small notes

- I used **samisahil186@gmail.com** from your résumé. Your local Git config uses `samisahil498@gmail.com`; if the second one is your current address, change it in `README.md`, the email badge and section 2.
- The **Dhaka, Bangladesh** location and the **"Open to internship or junior full-stack role"** sentence are reasonable based on your résumé. Adjust them if they are not accurate.


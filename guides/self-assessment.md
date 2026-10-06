# Self assessment: a guide for employees

Use this guide to rate yourself against the skills for your role. It works best before a development conversation or an appraisal with your manager.

The reference profiles are illustrative. They are not your job description. Where your actual job description or objectives differ, they take priority.

## 1. Find your role

1. Open the [role index](../docs/index.md) and choose the family closest to your work.
2. Open the role that best matches what you do. If none matches well, use the [ESCO occupation index](../docs/esco.md) or the [UK GDaD PCF index](../docs/pcf.md) to search by another name.
3. Choose the level that matches your current band. You can also look at the level above, to see what progression looks like.

It's fine if no role fits exactly. Many jobs mix two roles, so pick the main one, and add a few skills from the other if you need to.

## 2. Get your self-assessment file

Each role level has a file in [`exports/self-assessment/`](../exports/self-assessment/), named `<role>--band-<band>--<level>.tsv`. Open it in any spreadsheet program. TSV files open in Excel, LibreOffice, Numbers, and Google Sheets.

Each row is one skill, with:

- **expected_level**: the level the role expects (Awareness, Working, Practitioner, or Expert)
- **expected_level_description**: what that level means, in "You can …" statements
- empty columns for **self_rating**, **manager_rating**, **gap**, **evidence**, and **development_action**

## 3. Rate yourself

For each skill, read the level descriptions in the [skills catalogue](../docs/skills.md) and choose the level that best describes what you do now:

| Rating | Level | Meaning |
| --- | --- | --- |
| 0 | Not yet | You have not used this skill yet |
| 1 | Awareness | You know about it and can explain it |
| 2 | Working | You apply it, with some supervision |
| 3 | Practitioner | You apply it independently, and guide others |
| 4 | Expert | You lead others, set standards, and are seen as an authority |

Tips:

- **Rate what you do regularly**, not what you did once or might do.
- **Write evidence** for each rating: a short, specific example, such as "Designed the FHIR integration for the referrals service; reviewed by the lead architect".
- **Be honest.** A gap is not a failing. It is where development is most useful.
- **Don't aim to be Expert in everything.** Most people meet the expected level in most skills and are above or below it in a few.

## 4. Work out your gaps

Gap = expected level minus your rating. For example, if Practitioner (3) is expected and you rate yourself Working (2), the gap is 1.

- **Gap of 1 or more**: a development need for your current role.
- **Gap of 0**: you meet the expectation.
- **Negative gap**: a strength. It may also be evidence that you are ready for the next level.

## 5. Plan development

For your two or three most important gaps, write a **development_action**. Examples include a course, shadowing a colleague, a stretch task, a community of practice, or mentoring. Agree these actions with your manager.

Also look at the ESCO skills on your role page. They are a useful checklist of the wider skills and knowledge employers ask for in your occupation.

## 6. Review

Bring the file to your appraisal or one-to-one. Your manager may add a **manager_rating**, and together you agree the final ratings and actions. Repeat every six to twelve months.

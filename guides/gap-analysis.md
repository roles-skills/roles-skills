# Team skills gap analysis: a guide for team leads

Use completed self assessments to see a team's skills strengths and gaps, then plan training, recruitment, and development.

## 1. Collect self assessments

1. Ask each team member to complete the [self assessment](self-assessment.md) file for their role level, and agree it with their manager.
2. Save each completed file under the person's name or an anonymous code, for example `alex.tsv` or `person-01.tsv`.
3. Agree with the team how the results will be used and who will see them. If individual results will be shared, anonymise them.

## 2. Run the analysis

```sh
python3 scripts/gap_analysis.py results/ alex.tsv sam.tsv person-03.tsv
```

The script uses the manager rating where there is one, and the self rating otherwise. Ratings can be numbers (0 to 4) or level names (Awareness, Working, Practitioner, Expert). It writes three files to `results/`:

| File | What it shows |
| --- | --- |
| `gap-by-person.tsv` | Every person and skill, with expected level, assessed level, and gap |
| `gap-by-skill.tsv` | For each skill: how many people were assessed, how many are below the expected level, and the average gap. The biggest gaps are listed first. |
| `gap-matrix.tsv` | A grid of skills against people, with the gap in each cell. Open it in a spreadsheet and add colour scales to make a heatmap. |

Gaps are counted only where someone is below the expected level. Being above it counts as zero.

## 3. Read the results

- **Many people below the expected level on the same skill** points to a team-wide need, which is a good case for training or a community of practice.
- **One person below the expected level** is an individual development need. Handle it in that person's development plan.
- **A skill with no one at Practitioner or above** is a single point of weakness. Consider recruiting, coaching, or sharing expertise with another team.
- **Several people above the expected level** shows strengths. Use these people to coach others, and consider whether they are ready to progress.

## 4. Plan

Turn the top gaps into a team development plan. For each gap, agree an action, an owner, a date, and how you will know it has improved. Re-run the analysis after six to twelve months.

## Comparing across teams

Every skill in the self-assessment files carries the same name across roles, and links to UK GDaD PCF and ESCO references. So you can combine results across teams, or compare them with training catalogues and job adverts that use ESCO skills.

from app.models import Job, AIAnalysis


def score_job(job: Job, analysis: AIAnalysis):
    score = 0
    reasons = []

    # Creative freedom - very important
    creative_points = analysis.creative_freedom * 0.25
    score += creative_points
    reasons.append(
        f"+{creative_points:.1f} creative freedom"
    )

    # Lower complexity is better
    complexity_points = (100 - analysis.complexity) * 0.15
    score += complexity_points
    reasons.append(
        f"+{complexity_points:.1f} low complexity"
    )

    # Lower micromanagement is better
    micromanagement_points = (100 - analysis.micromanagement) * 0.15
    score += micromanagement_points
    reasons.append(
        f"+{micromanagement_points:.1f} low micromanagement"
    )

    # Clear client / clear brief
    clarity_points = analysis.client_clarity * 0.10
    score += clarity_points
    reasons.append(
        f"+{clarity_points:.1f} client clarity"
    )

    # Long-term work matters a lot
    long_term_points = analysis.long_term_potential * 0.20
    score += long_term_points
    reasons.append(
        f"+{long_term_points:.1f} long-term potential"
    )

    # How well the job matches short-form editing
    short_form_points = analysis.short_form_fit * 0.15
    score += short_form_points
    reasons.append(
        f"+{short_form_points:.1f} short-form fit"
    )

    final_score = round(score)

    # Safety: score can never go below 0 or above 100
    final_score = max(0, min(final_score, 100))

    return final_score, reasons
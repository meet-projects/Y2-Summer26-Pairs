from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(title, content):
    safe_title = (
        title.replace(" ", "_")
             .replace(":", "")
             .replace("/", "")
             .replace("\\", "")
    )

    filename = f"{safe_title}_summary.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(title, styles["Heading1"])
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(story)

    return filename
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green


def create_simple_form():
    c = canvas.Canvas("personal_information.pdf")

    c.setFont("Courier", 20)
    c.drawCentredString(250, 700, "Personal Information")
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, "First Name:")
    form.textfield(
        name="first_name",
        tooltip="First Name",
        x=110,
        y=635,
        borderStyle="inset",
        width=300,
        textColor=blue,
    )

    c.drawString(10, 600, "Last Name:")
    form.textfield(
        name="last_name",
        tooltip="Last Name",
        x=110,
        y=585,
        borderStyle="inset",
        width=300,
        textColor=blue,
    )

    c.drawString(10, 550, "Age:")
    form.textfield(
        name="age",
        tooltip="age",
        x=110,
        y=535,
        borderStyle="inset",
        forceBorder=True,
        width=50,
    )

    c.drawString(250, 550, "Sex:")
    options = [("Male", "male"), ("Female", "female"), ("Others", "others")]
    form.choice(
        name="choice2",
        tooltip="Field choice2",
        value="others",
        options=options,
        x=350,
        y=540,
        width=65,
        height=25,
        borderStyle="solid",
        borderWidth=1,
        forceBorder=True,
    )

    c.drawString(10, 500, "Phone No.:")
    form.textfield(
        name="address",
        tooltip="Address",
        x=110,
        y=485,
        borderStyle="inset",
        width=300,
        forceBorder=True,
    )

    c.drawString(10, 450, "Location:")
    form.textfield(
        name="location",
        tooltip="location",
        x=110,
        y=435,
        borderStyle="inset",
        width=300,
        forceBorder=True,
    )

    c.save()


if __name__ == "__main__":
    create_simple_form()
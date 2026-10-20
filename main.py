
from pyscript import document

club_members = ["Andrei Viray","Lebron James","Steph Curry","Rene Baterbonia","Luisito Balajadia"]

def verify_candidate(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    result = document.getElementById("result")

    result.innerHTML = (
        f"Congratulations {full_name}! You are now part of the ICT club."
        * is_member
        + f"Sorry {full_name}, your name is not on the list."
        * (not is_member)
    )

    result.className = (
        "mt-4 text-center fw-bold "
        + ("text-success" * is_member)
        + ("text-danger" * (not is_member))
    )

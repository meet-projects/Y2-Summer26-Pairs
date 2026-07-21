from app1 import run_agent as run_damian
from app2 import run_agent as run_heather

damian_history = []

while True:

    print("\n========== THEATER ASSISTANT ==========")
    print("1 - Damian,your personal theater assistant")
    print("2 - Heather,your event coordinator. links you to tickets based on your conversation with Damian")
    print("3 - Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        print("\n--- Damian Selected ---")

        user = input("You: ")

        response = run_damian(user)

        damian_history.append(f"User: {user}")
        damian_history.append(f"Damian: {response}")

        print("\nDamian:\n")
        print(response)

    elif choice == "2":

        print("\n--- Heather Selected ---")

        if not damian_history:
            print("Please talk to Damian first!")
            continue

        user = input("What tickets are you looking for? ")

        conversation = "\n".join(damian_history)

        response = run_heather(user, conversation)

        print("\nHeather:\n")
        print(response)

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid option.")
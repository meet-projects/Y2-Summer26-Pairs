try:
    from app1 import run_weather_agent  # Ido's Weather Agent
except ImportError:
    
from app2 import run_strategy_agent  
    print("=========================================")
    print("      🏎️  MCLAREN AI PIT WALL SYSTEM  🏎️      ")
    print("=========================================")
    
    while True:
        print("\nWhich agent do you want to use?")
        print("1. Agent 1 — Weather & Environmental Conditions")
        print("2. Agent 2 — Race Strategy & Telemetry Analyst")
        print("3. Exit Program")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            run_weather_agent()
        elif choice == "2":
            run_strategy_agent()
        elif choice == "3":
            print("\nShutting down pit wall systems. Goodbye.")
            break
        else:
           
            print("\n[!] Invalid input. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()
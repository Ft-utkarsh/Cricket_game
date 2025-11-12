import mysql.connector
from prettytable import PrettyTable

try:
    # Connect to database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='7321755631',
        database='cricket_db'
    )
    mycursor = mydb.cursor()
    
    print("\n" + "="*70)
    print("           CRICKET GAME - MATCH HISTORY DATA")
    print("="*70 + "\n")
    
    # Fetch all match data
    mycursor.execute("SELECT * FROM cricket ORDER BY sno DESC")
    results = mycursor.fetchall()
    
    if results:
        # Create table
        table = PrettyTable()
        table.field_names = ["Match#", "Date", "Player Name", "Runs", "Result"]
        
        for row in results:
            table.add_row(row)
        
        print(table)
        print(f"\nTotal matches played: {len(results)}")
        
        # Statistics
        wins = sum(1 for row in results if row[4] == 'Win')
        losses = sum(1 for row in results if row[4] == 'Loss')
        ties = sum(1 for row in results if row[4] == 'Tie')
        total_runs = sum(row[3] for row in results)
        
        print(f"\n--- Statistics ---")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Ties: {ties}")
        print(f"Total Runs: {total_runs}")
        print(f"Average Runs: {total_runs/len(results):.2f}")
        
    else:
        print("No match data found. Play some games first!")
    
    mycursor.close()
    mydb.close()
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    print("\nMake sure MySQL server is running!")
    print("Run: net start MySQL80")

input("\nPress Enter to exit...")

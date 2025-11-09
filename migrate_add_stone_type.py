"""
Migration script to add calculated_stone_type fields to Episode model
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('lithiase.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE episodes ADD COLUMN calculated_stone_type VARCHAR(100)")
        print("✅ Added calculated_stone_type column")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⏭️ calculated_stone_type column already exists")
        else:
            raise
    
    try:
        cursor.execute("ALTER TABLE episodes ADD COLUMN calculated_stone_type_data TEXT")
        print("✅ Added calculated_stone_type_data column")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⏭️ calculated_stone_type_data column already exists")
        else:
            raise
    
    try:
        cursor.execute("ALTER TABLE episodes ADD COLUMN calculated_at DATETIME")
        print("✅ Added calculated_at column")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⏭️ calculated_at column already exists")
        else:
            raise
    
    conn.commit()
    conn.close()
    print("\n🎉 Migration completed successfully!")

if __name__ == '__main__':
    migrate()

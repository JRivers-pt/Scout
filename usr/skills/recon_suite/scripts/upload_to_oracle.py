import sys
import json
import oracledb
import datetime

def upload_findings(client_name, host_ip, findings_json_path, ai_summary_path, security_score):
    dsn = "(description=(retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.eu-marseille-1.oraclecloud.com))(connect_data=(service_name=ged174997fea84b_kb27kccn5au6wcjo_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
    
    try:
        # Read the files the AI generated
        with open(findings_json_path, 'r') as f:
            findings = f.read()
            
        with open(ai_summary_path, 'r') as f:
            summary = f.read()

        print(f"Connecting to Oracle DB to upload data for {client_name} ({host_ip})...")
        connection = oracledb.connect(
            user="ADMIN",
            password="JDmr1986@1986",
            dsn=dsn,
            config_dir="/home/ubuntu/wallet",
            wallet_location="/home/ubuntu/wallet",
            wallet_password="JDmr1986@1986" 
        )
        
        cursor = connection.cursor()
        
        # Insert the data into the vault
        # Note: In a real implementation, the embedding would be calculated here via an LLM API 
        # before insertion. For this stub, we create a dummy vector since we don't have an embedding key.
        sql = """
            INSERT INTO client_vault 
            (client_name, host_ip, findings_json, ai_summary, security_score, embedding)
            VALUES 
            (:1, :2, :3, :4, :5, TO_VECTOR('[0.1, 0.2, 0.3' || RPAD(',0.0', 384*5 - 15, ',0.0') || ']', 384, FLOAT32))
        """
        
        cursor.execute(sql, [client_name, host_ip, findings, summary, float(security_score)])
        connection.commit()
        
        print(f"Successfully vaulted findings for {client_name}.")
        
    except Exception as e:
        print(f"Database Error: {e}")
        sys.exit(1)
    finally:
        if "connection" in locals() and connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 upload_to_oracle.py <client_name> <host_ip> <findings_json_path> <ai_summary_path> <security_score>")
        sys.exit(1)
        
    upload_findings(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

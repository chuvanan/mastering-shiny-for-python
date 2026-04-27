

# Start docker container for SQL Server

```bash
sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=1q2w3e&R" -p 1433:1433 --name sql5 -d mcr.microsoft.com/mssql/server:latest
```